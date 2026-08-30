#!/usr/bin/env python3
"""
poolwork.py — two jobs, run once.

1. Withdraw two words that were wrong. "Trakas" was recorded as Lithuanian for
   "sky" and "Aku" as Greenlandic for "star". Neither is real. Lithuanian for
   sky is dangus; Greenlandic for star is ulloriaq. Both had already been used
   in issued names, so the withdrawal is recorded openly rather than erased.

2. Expand the pool so that busy constellations do not run out of words, and so
   far more languages are represented.

Every word added here is UNVOUCHED. The two withdrawals above are exactly why
that field exists.
"""

import importlib.util

spec = importlib.util.spec_from_file_location("iss", "issue.py")
iss = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iss)

WITHDRAW = {
    "Trakas": "not a Lithuanian word; Lithuanian for sky is dangus",
    "Aku": "not a Greenlandic word; Greenlandic for star is ulloriaq",
}

# word, language, meaning
NEW_WORDS = [
    # --- Africa ---------------------------------------------------------
    ("Nyanga", "Zulu", "moon"), ("Kwenkwezi", "Xhosa", "star"),
    ("Mwezi", "Chichewa", "moon"), ("Wata", "Hausa", "moon"),
    ("Weer", "Wolof", "moon"), ("Dayax", "Somali", "moon"),
    ("Chereka", "Amharic", "moon"), ("Semay", "Amharic", "sky"),
    ("Volana", "Malagasy", "moon"), ("Lanitra", "Malagasy", "sky"),
    ("Nyeredzi", "Shona", "star"), ("Mwedzi", "Shona", "moon"),
    ("Njata", "Kikuyu", "star"), ("Munyenye", "Luganda", "star"),
    ("Naledi", "Setswana", "star"), ("Kpakpando", "Igbo", "star"),
    ("Onwa", "Igbo", "moon"), ("Igwe", "Igbo", "sky"),
    ("Nsoromma", "Twi", "star"), ("Osram", "Twi", "moon"),
    ("Hoodere", "Fula", "star"), ("Lewru", "Fula", "moon"),
    ("Dolo", "Bambara", "star"), ("Kalo", "Bambara", "moon"),
    ("Inyenyeri", "Kinyarwanda", "star"), ("Monzoto", "Lingala", "star"),
    ("Sanza", "Lingala", "moon"), ("Kokob", "Tigrinya", "star"),
    ("Urjii", "Oromo", "star"), ("Itri", "Tamazight", "star"),
    ("Ayyur", "Tamazight", "moon"), ("Ster", "Afrikaans", "star"),
    ("Maan", "Afrikaans", "moon"), ("Osupa", "Yoruba", "moon"),
    ("Mwedzi2", "SKIP", "skip"),

    # --- Americas -------------------------------------------------------
    ("Warawara", "Aymara", "star"), ("Phaxsi", "Aymara", "moon"),
    ("Jasy", "Guarani", "moon"), ("Metztli", "Nahuatl", "moon"),
    ("Kaan", "Yucatec Maya", "sky"), ("Galvladi", "Cherokee", "sky"),
    ("Wicahpi", "Lakota", "star"), ("Hanwi", "Lakota", "moon"),
    ("Mahpiya", "Lakota", "sky"), ("Taqqiq", "Inuktitut", "moon"),
    ("Qilak", "Inuktitut", "sky"), ("Qaammat", "Greenlandic", "moon"),
    ("Wangulen", "Mapudungun", "star"), ("Kuyen", "Mapudungun", "moon"),
    ("Anang", "Ojibwe", "star"), ("Giizhig", "Ojibwe", "sky"),
    ("Acahkos", "Cree", "star"), ("Zetwal", "Haitian Creole", "star"),
    ("Lalin", "Haitian Creole", "moon"), ("Syel", "Haitian Creole", "sky"),

    # --- Europe ---------------------------------------------------------
    ("Lleuad", "Welsh", "moon"), ("Reul", "Scottish Gaelic", "star"),
    ("Rollage", "Manx", "star"), ("Steren", "Cornish", "star"),
    ("Steredenn", "Breton", "star"), ("Loar", "Breton", "moon"),
    ("Ilargi", "Basque", "moon"), ("Tungl", "Icelandic", "moon"),
    ("Stjerne", "Norwegian", "star"), ("Himmel", "Norwegian", "sky"),
    ("Kuu", "Finnish", "moon"), ("Taht", "Estonian", "star"),
    ("Taevas", "Estonian", "sky"), ("Manu", "Northern Sami", "moon"),
    ("Albmi", "Northern Sami", "sky"), ("Hold", "Hungarian", "moon"),
    ("Zvaigzde", "Lithuanian", "star"), ("Dangus", "Lithuanian", "sky"),
    ("Menulis", "Lithuanian", "moon"), ("Zvaigzne", "Latvian", "star"),
    ("Debess", "Latvian", "sky"), ("Meness", "Latvian", "moon"),
    ("Luna", "Russian", "moon"), ("Zorya", "Ukrainian", "star"),
    ("Misyats", "Ukrainian", "moon"), ("Niebo", "Polish", "sky"),
    ("Ksiezyc", "Polish", "moon"), ("Hvezda", "Czech", "star"),
    ("Mesic", "Czech", "moon"), ("Hviezda", "Slovak", "star"),
    ("Zvijezda", "Croatian", "star"), ("Mjesec", "Croatian", "moon"),
    ("Stea", "Romanian", "star"), ("Cer", "Romanian", "sky"),
    ("Asteri", "Greek", "star"), ("Ouranos", "Greek", "sky"),
    ("Selini", "Greek", "moon"), ("Yll", "Albanian", "star"),
    ("Hena", "Albanian", "moon"), ("Qiell", "Albanian", "sky"),
    ("Kewkba", "Maltese", "star"), ("Estrella", "Spanish", "star"),
    ("Cielo", "Spanish", "sky"), ("Estel", "Catalan", "star"),
    ("Stella", "Italian", "star"), ("Etoile", "French", "star"),
    ("Ciel", "French", "sky"), ("Lune", "French", "moon"),
    ("Estela", "Occitan", "star"), ("Stern", "German", "star"),
    ("Mond", "German", "moon"), ("Hemel", "Dutch", "sky"),
    ("Shtern", "Yiddish", "star"), ("Stjer", "Frisian", "star"),

    # --- Asia -----------------------------------------------------------
    ("Xingxing", "Mandarin", "star"), ("Tian", "Mandarin", "sky"),
    ("Yueliang", "Mandarin", "moon"), ("Troi", "Vietnamese", "sky"),
    ("Trang", "Vietnamese", "moon"), ("Chan", "Thai", "moon"),
    ("Phkay", "Khmer", "star"), ("Khae", "Khmer", "moon"),
    ("Lintang", "Javanese", "star"), ("Rembulan", "Javanese", "moon"),
    ("Bentang", "Sundanese", "star"), ("Buwan", "Tagalog", "moon"),
    ("Bitoon", "Cebuano", "star"), ("Chand", "Hindi", "moon"),
    ("Natchathiram", "Tamil", "star"), ("Nila", "Tamil", "moon"),
    ("Chukka", "Telugu", "star"), ("Nakshatra", "Kannada", "star"),
    ("Ambaram", "Malayalam", "sky"), ("Chandra", "Marathi", "moon"),
    ("Sitara", "Urdu", "star"), ("Chann", "Punjabi", "moon"),
    ("Jun", "Nepali", "moon"), ("Taruwa", "Sinhala", "star"),
    ("Handa", "Sinhala", "moon"), ("Aseman", "Persian", "sky"),
    ("Mah", "Persian", "moon"), ("Storay", "Pashto", "star"),
    ("Spogmai", "Pashto", "moon"), ("Stere", "Kurdish", "star"),
    ("Hiv", "Kurdish", "moon"), ("Gokyuzu", "Turkish", "sky"),
    ("Ulduz", "Azerbaijani", "star"), ("Zhuldyz", "Kazakh", "star"),
    ("Aspan", "Kazakh", "sky"), ("Yulduz", "Uzbek", "star"),
    ("Osmon", "Uzbek", "sky"), ("Sar", "Mongolian", "moon"),
    ("Karma", "Tibetan", "star"), ("Dawa", "Tibetan", "moon"),
    ("Namkha", "Tibetan", "sky"), ("Varskvlavi", "Georgian", "star"),
    ("Mtvare", "Georgian", "moon"), ("Astgh", "Armenian", "star"),
    ("Lusin", "Armenian", "moon"), ("Kochav", "Hebrew", "star"),
    ("Shamayim", "Hebrew", "sky"), ("Yareach", "Hebrew", "moon"),

    # --- Pacific --------------------------------------------------------
    ("Lani", "Hawaiian", "sky"), ("Lagi", "Samoan", "sky"),
    ("Masina", "Samoan", "moon"), ("Vula", "Fijian", "moon"),
    ("Fetia", "Tahitian", "star"), ("Hetuu", "Rapa Nui", "star"),
    ("Iju", "Marshallese", "star"), ("Fitun", "Tetum", "star"),
    ("Pution", "Chamorro", "star"),
]


def main():
    data = iss.load()
    existing = {w["word"].lower() for w in data["pool"]}

    # --- 1. withdraw the bad words -------------------------------------
    data.setdefault("withdrawn", [])
    for bad, reason in WITHDRAW.items():
        hit = next((w for w in data["pool"] if w["word"] == bad), None)
        if not hit:
            continue
        affected = [e for e in data["register"] if e.get("core") == bad]
        for e in affected:
            data["withdrawn"].append({
                "id": e["id"], "withdrawn_name": e["name"],
                "reason": reason,
                "note": "Name withdrawn because the word it used was not real. "
                        "Recorded here rather than deleted."})
            data["register"].remove(e)
        data["pool"].remove(hit)
        existing.discard(bad.lower())
        print(f"withdrawn: {bad} — {reason}"
              f" ({len(affected)} name(s) affected)")

    # --- 2. expand the pool ---------------------------------------------
    added = 0
    for word, lang, meaning in NEW_WORDS:
        if lang == "SKIP" or meaning not in ("star", "sky", "moon"):
            continue
        if word.lower() in existing:
            continue
        data["pool"].append({"word": word, "language": lang,
                             "meaning": meaning, "vouched_by": None})
        existing.add(word.lower())
        added += 1

    # --- 3. reissue the withdrawn objects against the new pool ----------
    for w in data["withdrawn"]:
        if any(e["id"] == w["id"] for e in data["register"]):
            continue
        stem = w["withdrawn_name"].split()[0]
        chosen, name, suffix = iss.issue_name(
            w["id"], stem, data["pool"], iss.taken_pairs(data["register"]))
        data["register"].append({
            "id": w["id"], "stem": stem, "name": name,
            "core": chosen["word"], "language": chosen["language"],
            "meaning": chosen["meaning"], "suffix": suffix,
            "class": "", "existing_name": False,
            "replaces": w["withdrawn_name"]})
        print(f"reissued: {w['id']} — {w['withdrawn_name']} -> {name}")

    iss.save(data)
    langs = len(set(w["language"] for w in data["pool"]))
    print(f"\npool: {len(data['pool'])} words across {langs} languages "
          f"(+{added} added)")
    print(f"register: {len(data['register'])} entries, "
          f"{len(data['withdrawn'])} withdrawn and recorded")


if __name__ == "__main__":
    main()
