#!/usr/bin/env python3
"""
issue.py — the register tool for the Spoken Register.

The register file (register.json) is the record. Names are hashed once, at
issue, and then stored. Nothing recomputes them afterwards.

Usage
  ./issue.py init                          build register.json from the seed list
  ./issue.py add "TOI-2109 b" Cyg "ultra-hot giant"
                                           issue a name for a new object
  ./issue.py word "Tähti" Finnish star     propose a word for the pool
  ./issue.py vouch "Tähti" "A. Virtanen"   mark a word as vetted by a speaker
  ./issue.py sync                          refresh the snapshot inside skyname.html
  ./issue.py check                         verify the register is internally consistent

Author: Matthew John Santley <mattsantley@hotmail.com>
Licence: MIT
"""

import json
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTER = os.path.join(HERE, "register.json")
PAGE = os.path.join(HERE, "index.html")

VOWEL = {"b": "a", "c": "e", "d": "i", "e": "o", "f": "u", "g": "ae", "h": "ea"}

CONSTELLATIONS = {
    "And": "Andromeda", "Ant": "Antlia", "Aps": "Apus", "Aqr": "Aquarius",
    "Aql": "Aquila", "Ara": "Ara", "Ari": "Aries", "Aur": "Auriga",
    "Boo": "Boötes", "Cae": "Caelum", "Cam": "Camelopardalis", "Cnc": "Cancer",
    "CVn": "Canes Venatici", "CMa": "Canis Major", "CMi": "Canis Minor",
    "Cap": "Capricornus", "Car": "Carina", "Cas": "Cassiopeia",
    "Cen": "Centaurus", "Cep": "Cepheus", "Cet": "Cetus", "Cha": "Chamaeleon",
    "Cir": "Circinus", "Col": "Columba", "Com": "Coma Berenices",
    "CrA": "Corona Australis", "CrB": "Corona Borealis", "Crv": "Corvus",
    "Crt": "Crater", "Cru": "Crux", "Cyg": "Cygnus", "Del": "Delphinus",
    "Dor": "Dorado", "Dra": "Draco", "Equ": "Equuleus", "Eri": "Eridanus",
    "For": "Fornax", "Gem": "Gemini", "Gru": "Grus", "Her": "Hercules",
    "Hor": "Horologium", "Hya": "Hydra", "Hyi": "Hydrus", "Ind": "Indus",
    "Lac": "Lacerta", "Leo": "Leo", "LMi": "Leo Minor", "Lep": "Lepus",
    "Lib": "Libra", "Lup": "Lupus", "Lyn": "Lynx", "Lyr": "Lyra",
    "Men": "Mensa", "Mic": "Microscopium", "Mon": "Monoceros", "Mus": "Musca",
    "Nor": "Norma", "Oct": "Octans", "Oph": "Ophiuchus", "Ori": "Orion",
    "Pav": "Pavo", "Peg": "Pegasus", "Per": "Perseus", "Phe": "Phoenix",
    "Pic": "Pictor", "Psc": "Pisces", "PsA": "Piscis Austrinus",
    "Pup": "Puppis", "Pyx": "Pyxis", "Ret": "Reticulum", "Sge": "Sagitta",
    "Sgr": "Sagittarius", "Sco": "Scorpius", "Scl": "Sculptor",
    "Sct": "Scutum", "Ser": "Serpens", "Sex": "Sextans", "Tau": "Taurus",
    "Tel": "Telescopium", "Tri": "Triangulum", "TrA": "Triangulum Australe",
    "Tuc": "Tucana", "UMa": "Ursa Major", "UMi": "Ursa Minor", "Vel": "Vela",
    "Vir": "Virgo", "Vol": "Volans", "Vul": "Vulpecula",
}

SEED_POOL = [
    ("Nyota", "Swahili", "star"), ("Irawo", "Yoruba", "star"),
    ("Bituin", "Tagalog", "star"), ("Quyllur", "Quechua", "star"),
    ("Seren", "Welsh", "star"), ("Whetu", "Māori", "star"),
    ("Tara", "Hindi", "star"), ("Hoshi", "Japanese", "star"),
    ("Byeol", "Korean", "star"), ("Tahti", "Finnish", "star"),
    ("Yildiz", "Turkish", "star"), ("Citlali", "Nahuatl", "star"),
    ("Ulloriaq", "Inuktitut", "star"), ("Realta", "Irish", "star"),
    ("Stjarna", "Icelandic", "star"), ("Kokeb", "Amharic", "star"),
    ("Najm", "Arabic", "star"), ("Hoku", "Hawaiian", "star"),
    ("Kanyezi", "Zulu", "star"), ("Sao", "Vietnamese", "star"),
    ("Dao", "Thai", "star"), ("Bintang", "Malay", "star"),
    ("Nasti", "Northern Sami", "star"), ("Izar", "Basque", "star"),
    ("Csillag", "Hungarian", "star"), ("Noquisi", "Cherokee", "star"),
    ("Mbyja", "Guarani", "star"), ("Fetu", "Samoan", "star"),
    ("Kalokalo", "Fijian", "star"), ("Xiddig", "Somali", "star"),
    ("Setareh", "Persian", "star"), ("Zvezda", "Russian", "star"),
    ("Estrela", "Portuguese", "star"), ("Kintana", "Malagasy", "star"),
    ("Nyenyezi", "Chichewa", "star"), ("Tauraro", "Hausa", "star"),
    ("Biddew", "Wolof", "star"), ("Gwiazda", "Polish", "star"),
    ("Fetuu", "Tongan", "star"), ("Aku", "Greenlandic", "star"),
    ("Tsuki", "Japanese", "moon"), ("Marama", "Māori", "moon"),
    ("Killa", "Quechua", "moon"), ("Mahina", "Hawaiian", "moon"),
    ("Qamar", "Arabic", "moon"), ("Bulan", "Malay", "moon"),
    ("Dal", "Korean", "moon"), ("Gealach", "Irish", "moon"),
    ("Anga", "Swahili", "sky"), ("Langit", "Tagalog", "sky"),
    ("Rangi", "Māori", "sky"), ("Sora", "Japanese", "sky"),
    ("Haneul", "Korean", "sky"), ("Zeru", "Basque", "sky"),
    ("Awyr", "Welsh", "sky"), ("Speir", "Irish", "sky"),
    ("Taivas", "Finnish", "sky"), ("Ilhuica", "Nahuatl", "sky"),
    ("Izulu", "Zulu", "sky"), ("Tenger", "Mongolian", "sky"),
    ("Akash", "Bengali", "sky"), ("Vaanam", "Tamil", "sky"),
    ("Trakas", "Lithuanian", "sky"), ("Nebo", "Russian", "sky"),
    ("Himinn", "Icelandic", "sky"), ("Sama", "Arabic", "sky"),
]

SEED_OBJECTS = [
    ("Kepler-452 b", "Cyg", "super-Earth", None),
    ("Kepler-186 f", "Cyg", "rocky world", None),
    ("Kepler-16 b", "Cyg", "circumbinary giant", None),
    ("Kepler-22 b", "Cyg", "temperate world", None),
    ("Kepler-1649 c", "Cyg", "rocky world", None),
    ("Kepler-11 f", "Cyg", "low-density world", None),
    ("KELT-9 b", "Cyg", "ultra-hot giant", None),
    ("HAT-P-7 b", "Cyg", "hot giant", None),
    ("Kepler-62 f", "Lyr", "rocky world", None),
    ("Kepler-442 b", "Lyr", "rocky world", None),
    ("Kepler-90 i", "Dra", "hot rocky world", None),
    ("HD 209458 b", "Peg", "evaporating giant", None),
    ("51 Pegasi b", "Peg", "hot giant", "Dimidium"),
    ("HR 8799 b", "Peg", "imaged giant", None),
    ("HR 8799 e", "Peg", "imaged giant", None),
    ("TRAPPIST-1 d", "Aqr", "rocky world", None),
    ("TRAPPIST-1 e", "Aqr", "rocky world", None),
    ("TRAPPIST-1 f", "Aqr", "rocky world", None),
    ("Gliese 876 b", "Aqr", "giant", None),
    ("Proxima Centauri b", "Cen", "nearest world", None),
    ("Proxima Centauri d", "Cen", "sub-Earth", None),
    ("WASP-12 b", "Aur", "doomed giant", None),
    ("WASP-121 b", "Pup", "ultra-hot giant", None),
    ("WASP-76 b", "Psc", "ultra-hot giant", None),
    ("WASP-33 b", "And", "hot giant", None),
    ("WASP-39 b", "Vir", "puffy giant", None),
    ("WASP-96 b", "Phe", "hazy giant", None),
    ("WASP-17 b", "Sco", "retrograde giant", None),
    ("K2-18 b", "Leo", "steam world", None),
    ("Gliese 436 b", "Leo", "warm Neptune", None),
    ("TOI-700 d", "Dor", "rocky world", None),
    ("TOI-700 e", "Dor", "rocky world", None),
    ("LHS 1140 b", "Cet", "dense world", None),
    ("Tau Ceti e", "Cet", "candidate world", None),
    ("YZ Ceti b", "Cet", "sub-Earth", None),
    ("55 Cancri e", "Cnc", "lava world", "Janssen"),
    ("GJ 1214 b", "Oph", "mini-Neptune", None),
    ("Wolf 1061 c", "Oph", "temperate world", None),
    ("GJ 357 d", "Hya", "cold super-Earth", None),
    ("PSR B1257+12 b", "Vir", "pulsar world", "Draugr"),
    ("PSR B1257+12 c", "Vir", "pulsar world", "Poltergeist"),
    ("Ross 128 b", "Vir", "temperate world", None),
    ("Fomalhaut b", "PsA", "debris object", "Dagon"),
    ("Epsilon Eridani b", "Eri", "cold giant", "AEgir"),
    ("LTT 1445 A b", "Eri", "rocky world", None),
    ("Upsilon Andromedae b", "And", "hot giant", "Saffar"),
    ("Mu Arae b", "Ara", "giant", "Quijote"),
    ("Beta Pictoris b", "Pic", "young imaged giant", None),
    ("HD 40307 g", "Pic", "super-Earth", None),
    ("HD 189733 b", "Vul", "blue giant", None),
    ("HD 80606 b", "UMa", "eccentric giant", None),
    ("CoRoT-7 b", "Mon", "lava world", None),
    ("Gliese 667 Cc", "Sco", "temperate world", None),
    ("Teegarden's Star b", "Ari", "rocky world", None),
    ("GJ 273 b", "CMi", "temperate world", "Luyten b"),
    ("OGLE-2005-BLG-390L b", "Sgr", "cold super-Earth", None),
]


def fnv1a(text):
    """32-bit FNV-1a. Chosen because it is trivial to reimplement in any
    language, so the reference implementation is not the only one possible."""
    h = 2166136261
    for ch in text:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return h


def planet_letter(catalogue_id):
    tail = catalogue_id.strip().replace("-", " ").split()[-1]
    return tail.lower() if len(tail) == 1 and tail.isalpha() else "b"


def issue_name(catalogue_id, stem, pool, taken):
    """Pick a core word. Deterministic by hash, probing forward on collision
    so no language accumulates within one constellation."""
    index = fnv1a(catalogue_id) % len(pool)
    for _ in range(len(pool)):
        word = pool[index]["word"]
        if (stem, word) not in taken:
            break
        index = (index + 1) % len(pool)
    else:
        raise SystemExit(f"pool exhausted for {stem}; add words before issuing")
    suffix = VOWEL.get(planet_letter(catalogue_id), "a")
    return pool[index], f"{stem} {pool[index]['word']}-{suffix}", suffix


def load():
    with open(REGISTER, encoding="utf-8") as fh:
        return json.load(fh)


def save(data):
    data["updated"] = date.today().isoformat()
    with open(REGISTER, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def taken_pairs(entries):
    return {(e["stem"], e["core"]) for e in entries if e.get("core")}


def cmd_init():
    pool = [{"word": w, "language": l, "meaning": m, "vouched_by": None}
            for w, l, m in SEED_POOL]
    entries, taken = [], set()
    for cid, stem, cls, proper in SEED_OBJECTS:
        if proper:
            entries.append({"id": cid, "stem": stem, "name": proper,
                            "core": None, "language": None, "meaning": None,
                            "suffix": None, "class": cls, "existing_name": True})
            continue
        chosen, name, suffix = issue_name(cid, stem, pool, taken)
        taken.add((stem, chosen["word"]))
        entries.append({"id": cid, "stem": stem, "name": name,
                        "core": chosen["word"], "language": chosen["language"],
                        "meaning": chosen["meaning"], "suffix": suffix,
                        "class": cls, "existing_name": False})
    save({"version": "0.1", "updated": None,
          "author": "Matthew John Santley",
          "contact": "mattsantley@hotmail.com",
          "licence": "MIT",
          "note": "Names are issued once and stored. Never regenerate this file "
                  "from catalogue IDs; append to it.",
          "pool": pool, "register": entries})
    print(f"initialised: {len(entries)} entries, {len(pool)} words")


def cmd_add(cid, stem, cls=""):
    data = load()
    if stem not in CONSTELLATIONS:
        raise SystemExit(f"unknown constellation abbreviation: {stem}")
    if any(e["id"].lower() == cid.lower() for e in data["register"]):
        raise SystemExit(f"already in the register: {cid}")
    chosen, name, suffix = issue_name(cid, stem, data["pool"],
                                      taken_pairs(data["register"]))
    data["register"].append({"id": cid, "stem": stem, "name": name,
                             "core": chosen["word"], "language": chosen["language"],
                             "meaning": chosen["meaning"], "suffix": suffix,
                             "class": cls, "existing_name": False})
    save(data)
    print(f"issued: {name}  ({chosen['meaning']} in {chosen['language']})")


def cmd_word(word, language, meaning):
    data = load()
    if meaning not in ("star", "sky", "moon"):
        raise SystemExit("meaning must be star, sky or moon")
    if any(w["word"].lower() == word.lower() for w in data["pool"]):
        raise SystemExit(f"already in the pool: {word}")
    data["pool"].append({"word": word, "language": language,
                         "meaning": meaning, "vouched_by": None})
    save(data)
    print(f"added: {word} ({language}) — unvouched, needs a speaker")


def cmd_vouch(word, who):
    data = load()
    for w in data["pool"]:
        if w["word"].lower() == word.lower():
            w["vouched_by"] = who
            save(data)
            print(f"vouched: {word} by {who}")
            return
    raise SystemExit(f"not in the pool: {word}")


def cmd_check():
    data = load()
    problems = []
    seen_ids, seen_pairs = set(), set()
    for e in data["register"]:
        if e["id"] in seen_ids:
            problems.append(f"duplicate identifier: {e['id']}")
        seen_ids.add(e["id"])
        if e["stem"] not in CONSTELLATIONS:
            problems.append(f"unknown constellation {e['stem']} on {e['id']}")
        if e.get("core"):
            pair = (e["stem"], e["core"])
            if pair in seen_pairs:
                problems.append(f"collision: {e['stem']} {e['core']}")
            seen_pairs.add(pair)
    words = [w["word"].lower() for w in data["pool"]]
    if len(words) != len(set(words)):
        problems.append("duplicate word in the pool")
    vouched = sum(1 for w in data["pool"] if w["vouched_by"])
    for p in problems:
        print("PROBLEM:", p)
    print(f"{len(data['register'])} entries, {len(data['pool'])} words, "
          f"{vouched} vouched, "
          f"{len(set(w['language'] for w in data['pool']))} languages")
    print("register is consistent" if not problems else "FAILED")
    return 1 if problems else 0


def cmd_sync():
    """Refresh the offline snapshot embedded in skyname.html. The page always
    prefers the live register.json; the snapshot only covers file:// use."""
    data = load()
    with open(PAGE, encoding="utf-8") as fh:
        page = fh.read()
    start, end = "/*SNAPSHOT_START*/", "/*SNAPSHOT_END*/"
    if start not in page:
        raise SystemExit("no snapshot markers in skyname.html")
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    head, rest = page.split(start, 1)
    _, tail = rest.split(end, 1)
    with open(PAGE, "w", encoding="utf-8") as fh:
        fh.write(f"{head}{start}\nconst SNAPSHOT={blob};\n{end}{tail}")
    print(f"snapshot synced: {len(data['register'])} entries")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)
    cmd, rest = args[0], args[1:]
    if cmd == "init":
        cmd_init()
    elif cmd == "add":
        cmd_add(*rest)
    elif cmd == "word":
        cmd_word(*rest)
    elif cmd == "vouch":
        cmd_vouch(*rest)
    elif cmd == "check":
        sys.exit(cmd_check())
    elif cmd == "sync":
        cmd_sync()
    else:
        raise SystemExit(f"unknown command: {cmd}")
