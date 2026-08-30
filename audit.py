#!/usr/bin/env python3
"""
audit.py — check every entry in the register against the sky.

The first batch of objects had their constellations typed in by hand, before
coordinates were being used. This checks all of them: each host star's position
is run through astropy, which uses the official IAU boundary definitions, and
the result is compared with what the register says.

Also flags systems that appear twice under different catalogue names, and
identifiers whose planet letter has not parsed cleanly.

    ./audit.py          report only
    ./audit.py --fix    correct the stems and reissue affected names
"""

import importlib.util
import json
import re
import sys

from astropy.coordinates import SkyCoord, get_constellation

spec = importlib.util.spec_from_file_location("iss", "issue.py")
iss = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iss)

# host system -> J2000 position
COORDS = {
    "2M1207": ("12h07m33s", "-39d32m54s"),
    "51 Eridani": ("04h37m36s", "-02d28m25s"),
    "51 Pegasi": ("22h57m28s", "+20d46m08s"),
    "55 Cancri": ("08h52m36s", "+28d19m51s"),
    "61 Virginis": ("13h18m24s", "-18d18m40s"),
    "AU Microscopii": ("20h45m10s", "-31d20m27s"),
    "Barnard's Star": ("17h57m48s", "+04d41m36s"),
    "Beta Pictoris": ("05h47m17s", "-51d03m59s"),
    "CoRoT-7": ("06h43m49s", "-01d03m46s"),
    "Epsilon Eridani": ("03h32m56s", "-09d27m30s"),
    "Fomalhaut": ("22h57m39s", "-29d37m20s"),
    "GJ 1002": ("00h06m43s", "-07d32m22s"),
    "GJ 1214": ("17h15m19s", "+04d57m50s"),
    "GJ 273": ("07h27m24s", "+05d13m33s"),
    "GJ 3470": ("07h59m06s", "+15d23m30s"),
    "GJ 357": ("09h36m01s", "-21d39m39s"),
    "GJ 504": ("13h16m47s", "+09d25m27s"),
    "GJ 887": ("23h05m52s", "-35d51m11s"),
    "GJ 9827": ("23h27m05s", "-01d17m11s"),
    "Gliese 12": ("00h15m49s", "-16d08m00s"),
    "Gliese 163": ("04h09m16s", "-53d22m23s"),
    "Gliese 3512": ("08h41m20s", "+59d29m50s"),
    "Gliese 357": ("09h36m01s", "-21d39m39s"),
    "Gliese 436": ("11h42m11s", "+26d42m23s"),
    "Gliese 486": ("12h47m56s", "+09d45m05s"),
    "Gliese 581": ("15h19m26s", "-07d43m20s"),
    "Gliese 667 C": ("17h18m57s", "-34d59m23s"),
    "Gliese 667 Cc": ("17h18m57s", "-34d59m23s"),
    "Gliese 876": ("22h53m17s", "-14d15m49s"),
    "HAT-P-1": ("22h57m47s", "+38d40m30s"),
    "HAT-P-11": ("19h50m50s", "+48d04m51s"),
    "HAT-P-7": ("19h28m59s", "+47d58m10s"),
    "HD 100546": ("11h33m25s", "-70d11m41s"),
    "HD 106315": ("12h14m20s", "-00d39m53s"),
    "HD 149026": ("16h30m30s", "+38d20m50s"),
    "HD 189733": ("20h00m44s", "+22d42m39s"),
    "HD 20794": ("03h19m55s", "-43d04m11s"),
    "HD 209458": ("22h03m11s", "+18d53m04s"),
    "HD 219134": ("23h13m17s", "+57d10m06s"),
    "HD 3167": ("00h34m58s", "+04d22m53s"),
    "HD 40307": ("05h54m04s", "-60d01m24s"),
    "HD 69830": ("08h18m24s", "-12d37m56s"),
    "HD 80606": ("09h22m37s", "+50d36m13s"),
    "HD 85512": ("09h51m07s", "-43d30m10s"),
    "HD 95086": ("10h57m03s", "-68d40m02s"),
    "HD 97658": ("11h14m33s", "+25d42m37s"),
    "HIP 65426": ("13h24m36s", "-51d30m12s"),
    "HR 8799": ("23h07m28s", "+21d08m03s"),
    "K2-141": ("23h23m40s", "-01d11m22s"),
    "K2-18": ("11h30m14s", "+07d35m18s"),
    "K2-3": ("11h29m21s", "-01d27m17s"),
    "K2-33": ("16h10m14s", "-19d19m09s"),
    "KELT-9": ("20h31m26s", "+39d56m20s"),
    "Kepler-10": ("19h02m43s", "+50d14m29s"),
    "Kepler-11": ("19h48m28s", "+41d54m33s"),
    "Kepler-138": ("19h21m32s", "+43d17m35s"),
    "Kepler-16": ("19h16m18s", "+51d45m27s"),
    "Kepler-1625": ("19h41m43s", "+39d53m12s"),
    "Kepler-1647": ("19h52m52s", "+40d40m10s"),
    "Kepler-1649": ("19h30m01s", "+41d49m49s"),
    "Kepler-186": ("19h54m37s", "+43d57m18s"),
    "Kepler-20": ("19h10m48s", "+42d20m19s"),
    "Kepler-22": ("19h16m52s", "+47d53m04s"),
    "Kepler-34": ("19h45m55s", "+44d38m12s"),
    "Kepler-35": ("19h37m59s", "+46d41m27s"),
    "Kepler-36": ("19h25m00s", "+49d13m55s"),
    "Kepler-442": ("19h01m47s", "+39d16m34s"),
    "Kepler-444": ("19h19m01s", "+41d38m05s"),
    "Kepler-452": ("19h44m01s", "+44d16m39s"),
    "Kepler-62": ("18h52m51s", "+45d20m59s"),
    "Kepler-7": ("19h14m20s", "+41d05m23s"),
    "Kepler-70": ("19h45m26s", "+41d05m34s"),
    "Kepler-78": ("19h34m58s", "+44d26m54s"),
    "Kepler-9": ("19h08m51s", "+38d24m03s"),
    "Kepler-90": ("18h57m44s", "+49d18m19s"),
    "L 98-59": ("08h18m07s", "-68d18m47s"),
    "LHS 1140": ("00h44m59s", "-15d16m18s"),
    "LHS 3844": ("22h41m59s", "-69d10m08s"),
    "LTT 1445 A": ("03h01m51s", "-16d35m36s"),
    "Lalande 21185": ("11h03m20s", "+35d58m12s"),
    "Mu Arae": ("17h44m09s", "-51d50m03s"),
    "Nu2 Lupi": ("15h21m48s", "-48d19m03s"),
    "OGLE-2005-BLG-390L": ("17h54m19s", "-30d22m38s"),
    "PDS 70": ("14h08m10s", "-41d23m53s"),
    "PSR B1257+12": ("13h00m03s", "+12d40m57s"),
    "PSR B1620-26": ("16h23m38s", "-26d31m33s"),
    "Pi Mensae": ("05h37m09s", "-80d28m09s"),
    "Proxima Centauri": ("14h29m43s", "-62d40m46s"),
    "Ross 128": ("11h47m44s", "+00d48m16s"),
    "TOI-1338": ("06h08m32s", "-59d32m28s"),
    "TOI-2109": ("16h05m14s", "+16d34m32s"),
    "TOI-700": ("06h28m23s", "-65d34m43s"),
    "TRAPPIST-1": ("23h06m29s", "-05d02m29s"),
    "Tau Ceti": ("01h44m04s", "-15d56m15s"),
    "Teegarden's Star": ("02h53m00s", "+16d52m53s"),
    "Upsilon Andromedae": ("01h36m48s", "+41d24m20s"),
    "WASP-107": ("12h33m33s", "-10d08m46s"),
    "WASP-12": ("06h30m33s", "+29d40m20s"),
    "WASP-121": ("07h10m24s", "-39d05m51s"),
    "WASP-127": ("10h42m15s", "-03d50m06s"),
    "WASP-17": ("15h59m51s", "-28d03m42s"),
    "WASP-18": ("01h37m25s", "-45d40m40s"),
    "WASP-19": ("09h53m40s", "-45d39m33s"),
    "WASP-33": ("02h26m51s", "+37d33m02s"),
    "WASP-39": ("14h29m19s", "-03d26m40s"),
    "WASP-43": ("10h19m38s", "-09d48m23s"),
    "WASP-47": ("22h04m49s", "-12d01m08s"),
    "WASP-76": ("01h46m32s", "+02d42m02s"),
    "WASP-96": ("00h04m12s", "-47d21m38s"),
    "WD 1856+534": ("18h57m40s", "+53d30m33s"),
    "Wolf 1061": ("16h30m18s", "-12d39m45s"),
    "YZ Ceti": ("01h12m30s", "-16d59m56s"),
}

# same star, two catalogue names — the second is the one to keep
ALIASES = {"Gliese 357": "GJ 357"}


def main(fix=False):
    data = iss.load()
    wrong, missing, dupes = [], [], []

    hosts = {}
    for e in data["register"]:
        hosts.setdefault(iss.host_of(e["id"]), []).append(e)

    for host, entries in sorted(hosts.items()):
        if host not in COORDS:
            missing.append(host)
            continue
        real = get_constellation(SkyCoord(f"{COORDS[host][0]} {COORDS[host][1]}"),
                                 short_name=True)
        for e in entries:
            if e["stem"] != real:
                wrong.append((e, real))

    # systems that are really the same star under two names
    seen = {}
    for host in hosts:
        if host in COORDS:
            key = COORDS[host]
            if key in seen and seen[key] != host:
                dupes.append((seen[key], host))
            seen.setdefault(key, host)

    # identifiers whose planet letter did not parse into a single letter
    odd = [e["id"] for e in data["register"]
           if not re.search(r"\s[b-z]$", e["id"].strip())]

    print(f"{len(hosts)} host systems, {len(data['register'])} entries\n")
    if wrong:
        print(f"WRONG CONSTELLATION ({len(set(e['id'] for e, _ in wrong))} entries):")
        for e, real in wrong:
            print(f"   {e['id']:<24} register says {e['stem']}, sky says {real}")
    else:
        print("constellations: all correct")
    if missing:
        print(f"\nNO COORDINATES ON FILE ({len(missing)}): {', '.join(missing)}")
    if dupes:
        print("\nSAME STAR UNDER TWO NAMES:")
        for a, b in dupes:
            print(f"   {a}  ==  {b}")
    if odd:
        print(f"\nIDENTIFIER DID NOT PARSE ({len(odd)}): {', '.join(odd)}")

    if not fix:
        if wrong or dupes or odd:
            print("\nrun  ./audit.py --fix  to correct")
        return

    if not wrong:
        print("\nnothing to fix")
        return

    for e, real in wrong:
        old = e["name"]
        e["stem"] = real
        if e["existing_name"]:
            print(f"   {e['id']}: stem {old} -> {real} (proper name unchanged)")
            continue
        chosen, name, suffix = iss.issue_name(
            e["id"], real, data["pool"], iss.taken_pairs(data["register"]),
            iss.system_map([x for x in data["register"] if x is not e]))
        e.update(name=name, core=chosen["word"], language=chosen["language"],
                 meaning=chosen["meaning"], suffix=suffix)
        print(f"   {e['id']}: {old} -> {name}")

    iss.save(data)
    print("\nregister corrected")


if __name__ == "__main__":
    main("--fix" in sys.argv)
