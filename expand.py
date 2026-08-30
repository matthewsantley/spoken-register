#!/usr/bin/env python3
"""
expand.py — one-off batch addition of well-known objects to the register.

Constellations are not typed in by hand. Each host star's coordinates are run
through astropy, which uses the official IAU boundary definitions, so the stem
of every name is derived rather than guessed.

Existing entries are never touched. Anything already in the register is skipped,
which keeps the "issued once, never recomputed" rule intact.
"""

import importlib.util
from astropy.coordinates import SkyCoord, get_constellation

spec = importlib.util.spec_from_file_location("iss", "issue.py")
iss = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iss)

# host, RA, Dec, [(planet letter, class, existing proper name or None), ...]
SYSTEMS = [
    # --- nearby and naked-eye systems -------------------------------------
    ("Proxima Centauri", "14h29m43s", "-62d40m46s",
     [("c", "cold super-Earth", None)]),
    ("Barnard's Star", "17h57m48s", "+04d41m36s",
     [("b", "sub-Earth", None)]),
    ("Lalande 21185", "11h03m20s", "+35d58m12s",
     [("b", "warm super-Earth", None), ("c", "temperate world", None)]),
    ("Tau Ceti", "01h44m04s", "-15d56m15s",
     [("f", "candidate world", None)]),
    ("Epsilon Eridani", "03h32m56s", "-09d27m30s", []),
    ("61 Virginis", "13h18m24s", "-18d18m40s",
     [("b", "super-Earth", None)]),
    ("Gliese 876", "22h53m17s", "-14d15m49s",
     [("c", "giant", None), ("d", "hot super-Earth", None),
      ("e", "cold Neptune", None)]),
    ("Gliese 581", "15h19m26s", "-07d43m20s",
     [("b", "warm Neptune", None), ("c", "super-Earth", None),
      ("e", "small warm world", None)]),
    ("Gliese 667 C", "17h18m57s", "-34d59m23s",
     [("b", "warm super-Earth", None)]),
    ("Gliese 486", "12h47m56s", "+09d45m05s",
     [("b", "hot rocky world", None)]),
    ("Gliese 12", "00h15m49s", "-16d08m00s",
     [("b", "temperate world", None)]),
    ("Gliese 357", "09h36m01s", "-21d39m39s",
     [("b", "hot rocky world", None), ("c", "warm super-Earth", None)]),
    ("Gliese 3512", "08h41m20s", "+59d29m50s",
     [("b", "unlikely giant", None)]),
    ("GJ 1002", "00h06m43s", "-07d32m22s",
     [("b", "temperate world", None), ("c", "temperate world", None)]),
    ("GJ 887", "23h05m52s", "-35d51m11s",
     [("b", "warm super-Earth", None), ("c", "warm super-Earth", None)]),
    ("GJ 9827", "23h27m05s", "-01d17m11s",
     [("b", "dense hot world", None), ("d", "steam world", None)]),
    ("Teegarden's Star", "02h53m00s", "+16d52m53s",
     [("c", "temperate world", None)]),
    ("YZ Ceti", "01h12m30s", "-16d59m56s",
     [("c", "hot sub-Earth", None), ("d", "warm sub-Earth", None)]),
    ("LHS 1140", "00h44m59s", "-15d16m18s",
     [("c", "hot rocky world", None)]),
    ("LTT 1445 A", "03h01m51s", "-16d35m36s",
     [("c", "hot rocky world", None)]),
    ("Wolf 1061", "16h30m18s", "-12d39m45s",
     [("b", "hot super-Earth", None), ("d", "cold super-Earth", None)]),
    ("HD 219134", "23h13m17s", "+57d10m06s",
     [("b", "lava world", None), ("c", "dense warm world", None)]),
    ("HD 20794", "03h19m55s", "-43d04m11s",
     [("d", "temperate super-Earth", None)]),
    ("HD 85512", "09h51m07s", "-43d30m10s",
     [("b", "warm super-Earth", None)]),
    ("HD 69830", "08h18m24s", "-12d37m56s",
     [("b", "hot Neptune", None), ("d", "temperate Neptune", None)]),
    ("Gliese 163", "04h09m16s", "-53d22m23s",
     [("c", "warm super-Earth", None)]),
    ("AU Microscopii", "20h45m10s", "-31d20m27s",
     [("b", "young puffy world", None), ("c", "young Neptune", None)]),

    # --- famous named systems ---------------------------------------------
    ("55 Cancri", "08h52m36s", "+28d19m51s",
     [("b", "hot giant", "Galileo"), ("c", "warm giant", "Brahe"),
      ("f", "temperate giant", "Harriot")]),
    ("Upsilon Andromedae", "01h36m48s", "+41d24m20s",
     [("c", "giant", "Samh"), ("d", "cold giant", "Majriti")]),
    ("Mu Arae", "17h44m09s", "-51d50m03s",
     [("c", "hot Neptune", "Dulcinea"), ("d", "warm giant", "Rocinante"),
      ("e", "cold giant", "Sancho")]),
    ("PSR B1257+12", "13h00m03s", "+12d40m57s",
     [("d", "pulsar world", "Phobetor")]),
    ("PSR B1620-26", "16h23m38s", "-26d31m33s",
     [("b", "ancient giant", "Methuselah")]),
    ("HD 149026", "16h30m30s", "+38d20m50s",
     [("b", "dense hot giant", "Smertrios")]),
    ("Fomalhaut", "22h57m39s", "-29d37m20s", []),
    ("Pi Mensae", "05h37m09s", "-80d28m09s",
     [("b", "cold heavy giant", None), ("c", "hot super-Earth", None)]),
    ("Nu2 Lupi", "15h21m48s", "-48d19m03s",
     [("b", "hot super-Earth", None), ("c", "warm Neptune", None),
      ("d", "temperate Neptune", None)]),

    # --- directly imaged ---------------------------------------------------
    ("HR 8799", "23h07m28s", "+21d08m03s",
     [("c", "imaged giant", None), ("d", "imaged giant", None)]),
    ("Beta Pictoris", "05h47m17s", "-51d03m59s",
     [("b", "young imaged giant", None), ("c", "young imaged giant", None)]),
    ("51 Eridani", "04h37m36s", "-02d28m25s",
     [("b", "young imaged giant", None)]),
    ("HIP 65426", "13h24m36s", "-51d30m12s",
     [("b", "imaged giant", None)]),
    ("GJ 504", "13h16m47s", "+09d25m27s",
     [("b", "cool imaged giant", None)]),
    ("HD 95086", "10h57m03s", "-68d40m02s",
     [("b", "imaged giant", None)]),
    ("PDS 70", "14h08m10s", "-41d23m53s",
     [("b", "forming world", None), ("c", "forming world", None)]),
    ("2M1207", "12h07m33s", "-39d32m54s",
     [("b", "imaged giant", None)]),

    # --- transiting workhorses --------------------------------------------
    ("WASP-19", "09h53m40s", "-45d39m33s", [("b", "ultra-hot giant", None)]),
    ("WASP-43", "10h19m38s", "-09d48m23s", [("b", "hot giant", None)]),
    ("WASP-18", "01h37m25s", "-45d40m40s", [("b", "heavy hot giant", None)]),
    ("WASP-107", "12h33m33s", "-10d08m46s", [("b", "puffy warm world", None)]),
    ("WASP-127", "10h42m15s", "-03d50m06s", [("b", "very low-density giant", None)]),
    ("WASP-17", "15h59m51s", "-28d03m42s", []),
    ("WASP-47", "22h04m49s", "-12d01m08s",
     [("b", "hot giant", None), ("d", "warm Neptune", None),
      ("e", "lava world", None)]),
    ("HAT-P-11", "19h50m50s", "+48d04m51s", [("b", "warm Neptune", None)]),
    ("HAT-P-1", "22h57m47s", "+38d40m30s", [("b", "puffy hot giant", None)]),
    ("HD 97658", "11h14m33s", "+25d42m37s", [("b", "warm super-Earth", None)]),
    ("HD 106315", "12h14m20s", "-00d39m53s",
     [("b", "hot super-Earth", None), ("c", "warm Neptune", None)]),
    ("HD 3167", "00h34m58s", "+04d22m53s",
     [("b", "lava world", None), ("c", "warm Neptune", None)]),
    ("GJ 3470", "07h59m06s", "+15d23m30s", [("b", "warm Neptune", None)]),
    ("K2-3", "11h29m21s", "-01d27m17s",
     [("b", "warm super-Earth", None), ("d", "temperate world", None)]),
    ("K2-141", "23h23m40s", "-01d11m22s", [("b", "lava world", None)]),
    ("K2-33", "16h10m14s", "-19d19m09s", [("b", "infant world", None)]),
    ("L 98-59", "08h18m07s", "-68d18m47s",
     [("b", "sub-Earth", None), ("c", "hot rocky world", None),
      ("d", "warm rocky world", None)]),
    ("LHS 3844", "22h41m59s", "-69d10m08s", [("b", "bare rock world", None)]),
    ("WD 1856+534", "18h57m40s", "+53d30m33s",
     [("b", "giant orbiting a dead star", None)]),

    # --- TRAPPIST and TESS -------------------------------------------------
    ("TRAPPIST-1", "23h06m29s", "-05d02m29s",
     [("b", "scorched rocky world", None), ("c", "hot rocky world", None),
      ("g", "rocky world", None), ("h", "cold rocky world", None)]),
    ("TOI-700", "06h28m23s", "-65d34m43s",
     [("b", "hot rocky world", None), ("c", "warm Neptune", None)]),
    ("TOI-1338", "06h08m32s", "-59d32m28s", [("b", "circumbinary world", None)]),

    # --- Kepler field ------------------------------------------------------
    ("Kepler-10", "19h02m43s", "+50d14m29s",
     [("b", "lava world", None), ("c", "dense warm world", None)]),
    ("Kepler-20", "19h10m48s", "+42d20m19s",
     [("b", "hot rocky world", None), ("e", "hot rocky world", None)]),
    ("Kepler-36", "19h25m00s", "+49d13m55s",
     [("b", "dense hot world", None), ("c", "puffy hot world", None)]),
    ("Kepler-138", "19h21m32s", "+43d17m35s",
     [("c", "water world", None), ("d", "water world", None)]),
    ("Kepler-444", "19h19m01s", "+41d38m05s",
     [("d", "ancient rocky world", None), ("e", "ancient rocky world", None)]),
    ("Kepler-7", "19h14m20s", "+41d05m23s", [("b", "cloudy hot giant", None)]),
    ("Kepler-9", "19h08m51s", "+38d24m03s", [("b", "warm giant", None)]),
    ("Kepler-78", "19h34m58s", "+44d26m54s", [("b", "lava world", None)]),
    ("Kepler-70", "19h45m26s", "+41d05m34s", [("b", "scorched remnant", None)]),
    ("Kepler-1625", "19h41m43s", "+39d53m12s", [("b", "possible moon host", None)]),
    ("Kepler-34", "19h45m55s", "+44d38m12s", [("b", "circumbinary giant", None)]),
    ("Kepler-35", "19h37m59s", "+46d41m27s", [("b", "circumbinary giant", None)]),
    ("Kepler-1647", "19h52m52s", "+40d40m10s", [("b", "circumbinary giant", None)]),
    ("Kepler-186", "19h54m37s", "+43d57m18s", []),
    ("Kepler-62", "18h52m51s", "+45d20m59s", [("e", "candidate ocean world", None)]),

    # --- hot Jupiters and oddities ----------------------------------------
    ("HD 80606", "09h22m37s", "+50d36m13s", []),
    ("HD 189733", "20h00m44s", "+22d42m39s", []),
    ("HD 209458", "22h03m11s", "+18d53m04s", []),
    ("HD 100546", "11h33m25s", "-70d11m41s", [("b", "forming giant", None)]),
    ("CoRoT-7", "06h43m49s", "-01d03m46s", [("c", "hot Neptune", None)]),
    ("HD 40307", "05h54m04s", "-60d01m24s",
     [("b", "hot super-Earth", None), ("c", "warm super-Earth", None),
      ("d", "warm super-Earth", None)]),
]


def main():
    data = iss.load()
    existing = {e["id"].lower() for e in data["register"]}
    added = skipped = 0
    stems = {}

    for host, ra, dec, planets in SYSTEMS:
        stem = get_constellation(SkyCoord(f"{ra} {dec}"), short_name=True)
        if stem not in iss.CONSTELLATIONS:
            print(f"  ?? unknown stem {stem} for {host}")
            continue
        stems[host] = stem
        for letter, cls, proper in planets:
            cid = f"{host} {letter}"
            if cid.lower() in existing:
                skipped += 1
                continue
            if proper:
                data["register"].append({
                    "id": cid, "stem": stem, "name": proper, "core": None,
                    "language": None, "meaning": None, "suffix": None,
                    "class": cls, "existing_name": True})
            else:
                chosen, name, suffix = iss.issue_name(
                    cid, stem, data["pool"], iss.taken_pairs(data["register"]))
                data["register"].append({
                    "id": cid, "stem": stem, "name": name,
                    "core": chosen["word"], "language": chosen["language"],
                    "meaning": chosen["meaning"], "suffix": suffix,
                    "class": cls, "existing_name": False})
            existing.add(cid.lower())
            added += 1

    iss.save(data)
    print(f"added {added}, skipped {skipped} already present")
    print(f"register now holds {len(data['register'])} entries "
          f"across {len(set(e['stem'] for e in data['register']))} constellations")


if __name__ == "__main__":
    main()
