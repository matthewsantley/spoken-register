#!/usr/bin/env python3
"""
verify.py — record what happened when each pool word was checked against
published reference sources.

This is NOT the same as a native speaker vouching for a word. It catches
outright fabrications and wrong spellings. It cannot catch a word that is
correct in a dictionary and wrong in a mouth.

Each word gets a `checked` field:
    confirmed  — a reference source gives this word for this meaning
    variant    — sources give a related form; both appear to be valid
    flagged    — sources disagree with the spelling or the word given
    unchecked  — not yet looked up
"""
import importlib.util
spec = importlib.util.spec_from_file_location("iss", "issue.py")
iss = importlib.util.module_from_spec(spec); spec.loader.exec_module(iss)

SOURCE = "indifferentlanguages.com word tables for star / sky / moon, cross-read against Wiktionary translation listings, Aug 2026"

CONFIRMED = """
Ster Yll Ulduz Bituin Bituon Sterk Debesis Nsoroma Xingxing Hvezda Stjerne Taht Tahti Etoile Stjer
Varskvlavi Stern Asteri Zetwal Tauraro Hoku Kochav Tara Csillag Stjarna
Kpakpando Bintang Realta Stella Hoshi Lintang Nakshatra Zhuldyz Inyenyeri
Byeol Zvaigzne Zvaigzde Kintana Whetu Od Storay Setareh Gwiazda Estrela
Stea Zvezda Fetu Hviezda Estrella Bentang Nyota Natchathiram Dao Yildiz
Sitara Yulduz Sao Seren Shtern Irawo Dolo Warawara Naledi Nyeredzi
Qiell Taevas Taivas Ciel Himmel Ouranos Himinn Speir Dangus Niebo Cer
Nebo Awyr Akash Haneul Aspan Tenger Vaanam Gokyuzu Osmon Sama Aseman
Sora Anga Semay Rangi Izulu Troi Lani Langit
Maan Hena Chereka Qamar Lusin Mjesec Mesic Kuu Lune Mtvare Mond Lalin
Wata Mahina Yareach Hold Tungl Onwa Gealach Tsuki Rembulan Dal Meness
Menulis Bulan Yueliang Marama Sar Spogmai Mah Ksiezyc Chann Luna Masina
Mwedzi Handa Dayax Buwan Nila Misyats Trang Lleuad Osupa Mwezi Volana
Chandra Quyllur Killa Citlali Metztli Taqqiq Kuyen Astgh Zvijezda Nyenyezi
""".split()

VARIANT = {
 "Izar": "sources give the definite form izarra; izar is the base form",
 "Kokeb": "Amharic script romanises variously; kokeb and kokebi both appear",
 "Najm": "najm (m) and najma (f) both current in Arabic",
 "Taruwa": "sources romanise the Sinhala as taruva",
 "Xiddig": "sources give the definite xiddiga; xiddig is the base form",
 "Kanyezi": "shortened from Zulu inkanyezi",
 "Kwenkwezi": "shortened from Xhosa inkwenkwezi",
 "Ilhuica": "shortened from Nahuatl ilhuicatl",
 "Zeru": "sources give the definite zerua; zeru is the base form",
 "Reul": "Scottish Gaelic has both reul and rionnag",
 "Kewkba": "Maltese has both kewkba and stilla",
 "Chukka": "Telugu has both chukka and nakshatram",
 "Zorya": "Ukrainian has both zorya and zirka",
 "Phkay": "Khmer has native phkay and the borrowing tara",
 "Tian": "Mandarin tian is sky or heaven; tiankong is the fuller noun",
 "Igwe": "Igbo igwe is sky or heaven; elu-igwe also given",
 "Ambaram": "Malayalam has both ambaram and aakaasham",
 "Hemel": "Dutch hemel is sky or heaven; lucht also given for sky",
 "Xingxing": "Mandarin xing alone also means star; xingxing is the everyday noun",
 "Ilargi": "sources give the definite ilargia; ilargi is the base form",
 "Selini": "Greek selini is the formal or astronomical word; fengari is the everyday one",
 "Chand": "Hindi chand is the everyday word; chandrama the fuller form",
 "Jun": "Nepali jun is common alongside the Sanskritic chandrama",
 "Chan": "Thai chan is the moon element of duang chan",
 "Khae": "Khmer khae is moon or month; preah chan is the fuller form",
 "Nyanga": "shortened from Zulu inyanga",
 "Hiv": "sources give Kurmanji hev or heyv; spelling varies",
 "Estel": "Catalan has both estel and estrella",
 "Ulloriaq": "sources attribute ulloriaq to Greenlandic (Kalaallisut); the pool records it as Inuktitut, which is closely related",
 "Hanwi": "sources give hanwi as Dakota; the pool records Lakota, a closely related variety",
}

FLAGGED = {}   # four earlier flags were corrected at source and rebuilt:
               # Bitoon->Bituon, Stere->Sterk, Debess->Debesis, Nsoromma->Nsoroma


def main():
    d = iss.load()
    counts = {"confirmed": 0, "variant": 0, "flagged": 0, "unchecked": 0}
    for w in d["pool"]:
        n = w["word"]
        if n in FLAGGED:
            w["checked"], w["check_note"] = "flagged", FLAGGED[n]
        elif n in VARIANT:
            w["checked"], w["check_note"] = "variant", VARIANT[n]
        elif n in CONFIRMED:
            w["checked"] = "confirmed"
            w.pop("check_note", None)
        else:
            w["checked"] = "unchecked"
            w.pop("check_note", None)
        counts[w["checked"]] += 1
    d["check_source"] = SOURCE
    iss.save(d)
    total = len(d["pool"])
    for k, v in counts.items():
        print(f"  {k:<10} {v:>4}   {v*100//total}%")
    print(f"\n{total} words. {counts['confirmed']+counts['variant']+counts['flagged']} "
          f"looked up against sources, {counts['unchecked']} still to do.")
    print("None vouched by a speaker — that is a separate thing.")


if __name__ == "__main__":
    main()
