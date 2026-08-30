# A Spoken Register for the Sky

## A proposal for human-readable aliases for stars and exoplanets

**Matthew John Santley**
Independent · Lancashire, United Kingdom
mattsantley@hotmail.com

**Draft 0.1 — for discussion — 30 August 2026**

Licensed CC BY 4.0. The reference implementation and register are separately licensed MIT.

---

## Abstract

Astronomical catalogue identifiers are excellent primary keys and poor names. They are unique, stable and machine-tractable, which is exactly what a catalogue needs. But when a broadcaster reads `2MASS J05551028+0724255` aloud to a general audience, the audience stops listening. This paper argues that the problem is not the identifier but the absence of a display layer above it, and proposes one: a *spoken register* of pronounceable aliases, built from words for "star", "sky" and "moon" contributed by every language that wants to take part, anchored to the constellation each object sits in.

The register is not a replacement for catalogue IDs and asks nothing of working astronomy. It is an alias table, maintained openly, for the few thousand objects that appear in public conversation.

---

## 1. The problem

Roughly six thousand exoplanets are currently confirmed. Almost all of them are known publicly by their discovery-survey identifier: `Kepler-452b`, `WASP-121b`, `TOI-700d`, `HD 209458 b`.

These names are unambiguous and unmemorable. Consider what a listener has to do to retain `Kepler-452b`:

- recognise "Kepler" as a telescope rather than a place
- retain a four-digit number that encodes nothing
- notice that the lowercase letter is doing significant work

Three separate cognitive tasks, none of which rewards the effort, because the number carries no information the listener can use. There is nothing to hook a memory onto and nothing to reason from. The name cannot be repeated to a friend the next day.

The result is a documented pattern in science communication: broadcasters either avoid naming objects at all ("a planet in the constellation Cygnus"), or they read the identifier out and the audience's attention drops. Neither is good. The sky is the most universally shared object of human curiosity, and we have made it sound like a parts catalogue.

## 2. Why the current system is the way it is

It is worth being clear that the existing system is not an accident or a failure of imagination. It solves real problems that any replacement must also solve.

**Scale.** The Gaia mission has catalogued close to two billion stars. There is no reservoir of memorable human names of that size, and no committee capable of issuing them.

**Uniqueness and stability.** A catalogue ID must resolve to exactly one object, permanently, across every paper ever published referencing it. Renaming breaks the literature.

**Machine tractability.** Many identifiers are coordinates. `2MASS J05551028+0724255` encodes a right ascension of 05h 55m 10.28s and a declination of +07° 24′ 25.5″. It is ugly precisely because it is useful: it tells an instrument where to point.

**Semantic caution.** Astronomy has been burned by meaningful names. A "planetary nebula" has nothing to do with planets. The "Great Attractor" oversells what is actually known. A meaningless number cannot become wrong when the measurement improves.

**Cultural caution.** The International Astronomical Union is deliberately careful about naming rights after a long history of European names being applied to everything visible. Its NameExoWorlds campaigns are slow and consultative by design, not by neglect.

Any proposal that ignores these constraints deserves to be ignored in turn.

## 3. The reframing

The insight this proposal rests on is borrowed from software engineering.

A database has a primary key and it has a display name. The primary key is unique, stable and meaningless — that is its job. The display name is readable, mutable and secondary — that is its job. Nobody argues that a customer record should have a readable primary key. Nobody argues that customers should be shown their database row ID.

Astronomy has built an excellent primary key and never built the display layer. Broadcasters are, in effect, reading row IDs out loud on television, because there is nothing else to read.

**The proposal is therefore not to rename anything.** It is to build the missing view.

## 4. Design principles

1. **Additive, never authoritative.** Catalogue IDs remain the identifier of record. The register is an alias table. Nothing in the astronomical literature needs to change.

2. **Defer to existing names.** Where an object already has a proper name — IAU-issued, traditional, Arabic, Greek, Polynesian — that name wins. The register records it and issues nothing new.

3. **Say the location.** The one durable, publicly meaningful fact about an object is which constellation it lies in. Constellation membership is fixed by IAU boundary, does not change with re-measurement, and is the fact a listener can act on. It goes in the name.

4. **Keep physics out of the name.** Classification changes when instruments improve. A "hot Jupiter" that turns out to be a brown dwarf must not require renaming. Class information travels alongside the name, never inside it.

5. **No culture privileged.** No mythology, no pantheon, no nation's heroes. The pool is the plainest possible noun.

6. **Deterministic, not chosen.** Assignment is by algorithm from the catalogue ID. No committee decides which language gets which star, because no human decides at all.

7. **Immutable once issued.** A name is generated once and then stored. It is never regenerated, because catalogue IDs occasionally change and a derived name that drifts is worse than no name.

## 5. The scheme

A register name has three fields. Two are part of the name; one travels with it.

### Field 1 — Stem (where it is)

The IAU three-letter constellation abbreviation, which already exists and is already standard: `Cyg` (Cygnus), `Peg` (Pegasus), `Aqr` (Aquarius), `Dor` (Dorado).

This costs nothing to adopt because astronomers already use these codes daily. It is the one field that requires no new agreement. It is Latin, which slightly undercuts the inclusion argument in Field 2 — but it is an existing shared standard rather than a fresh imposition, and it buys immediate familiarity.

### Field 2 — Core (the distinctive part)

A word from the global pool, assigned deterministically by hashing the catalogue ID.

**The unifying rule for the pool: every word means "star", "sky" or "moon" in some human language.**

This is the answer to the inclusion problem. Every human culture has looked up and named what it saw. The pool is built from those plain nouns — *nyota* (Swahili), *bituin* (Tagalog), *quyllur* (Quechua), *seren* (Welsh), *whetū* (Māori), *ulloriaq* (Inuktitut), *noquisi* (Cherokee), *biddéw* (Wolof), *kintana* (Malagasy).

Nobody's gods are imposed on anybody. No nation's explorers are commemorated. The sky is named, in every language, after the sky.

Language of origin is recorded in the register alongside the name, so the provenance is visible and creditable rather than erased.

### Field 3 — Suffix (which body in the system)

A star and its planets sit in the same place and share the same pool word: the word is issued to the *system*, not to each object separately. The suffix is the only thing that separates them.

The star takes no suffix. Each planet takes a vowel mapped from its IAU letter:

| IAU letter | Suffix |
|---|---|
| b | -a |
| c | -e |
| d | -i |
| e | -o |
| f | -u |
| g | -ae |
| h | -ea |

So the Kepler-452 system reads:

- Kepler-452, the star → **Cyg Stjarna**
- Kepler-452 b, the planet → **Cyg Stjarna-a**

### The class tag — spoken alongside, never part of the name

Every entry also carries a short descriptor: *the rocky world*, *the ultra-hot giant*, *the pulsar world*. It is what a presenter says immediately before the name — "the rocky world Aqr Quyllur-o" — in the same way one says "the physicist Marie Curie". The descriptor tells a listener what kind of object is coming. It is not part of what the object is called.

The distinction is load-bearing, and it is worth showing why.

Suppose the class were built into the name instead. WASP-12b is currently classified as a hot Jupiter, so call it `Aur Hotgiant-a`. If later measurements reclassified it — the boundary between large planets and small brown dwarfs is genuinely blurry, and objects have crossed it before — the name would become factually wrong. Correcting it means issuing a replacement, which breaks every article, broadcast and citation that used the original.

Holding the class outside the name makes that revision cost nothing. The name `Aur Yildiz-a` does not move. Only the spoken descriptor changes, from "the hot giant" to "the brown dwarf".

In database terms: the class tag is a column in the record, not part of the key. It is the mutable half of a design whose other half must never move.

## 6. Worked examples

These are the actual outputs of the reference implementation, not hand-picked illustrations.

| Catalogue ID | Constellation | Register name | Core word | Spoken as |
|---|---|---|---|---|
| Kepler-452 b | Cygnus | Cyg Stjarna-a | star, Icelandic | "the super-Earth Cyg Stjarna-a" |
| TRAPPIST-1 e | Aquarius | Aqr Quyllur-o | star, Quechua | "the rocky world Aqr Quyllur-o" |
| Proxima Centauri b | Centaurus | Cen Seren-a | star, Welsh | "the nearest world Cen Seren-a" |
| TOI-700 d | Dorado | Dor Noquisi-i | star, Cherokee | "the rocky world Dor Noquisi-i" |
| 51 Pegasi b | Pegasus | *Dimidium* | — | existing IAU name honoured |

The last row matters. Where a name exists, the register records and defers.

## 7. Governance and contribution

The register is a public, version-controlled data file. Two contribution paths:

**Adding a word.** Anyone may propose a word for the pool, with language, meaning, script, a rough pronunciation, and ideally a native-speaker attestation. Words are vetted before entry. This is not optional politeness: a word that means "star" in a dictionary may mean something regrettable in a neighbouring dialect, and only speakers can catch that.

**Adding an object.** Anyone may submit a catalogue ID with its constellation. The algorithm issues the name; no human chooses it.

Two rules keep the register honest:

- **Append-only.** A name, once issued, is never reassigned or withdrawn.
- **Rotation-fair.** Assignment probes forward through the pool on collision, so no language accumulates a disproportionate share within any constellation.

The register requires no institutional blessing to be useful. It is a lookup table published under an open licence. If it is good, it will be used.

## 8. Known problems

**Pool exhaustion in crowded constellations.** The Kepler field deposited thousands of planets into Cygnus alone. A pool of fifty words will not cover it. The pool must grow to several hundred, which is achievable — there are around seven thousand living languages — and the most crowded constellations may eventually need a compound core (`Cyg Nyota Rangi-a`). Ugly, but only where the density demands it.

**The Latin stem.** Discussed under Field 1. Defensible, but a genuine compromise rather than a solved problem.

**Vetting throughput.** The vetting requirement in §7 (Governance) is the real bottleneck, and it should be. A register that grows slowly and correctly beats one that grows fast and offends.

**Adoption.** The hardest problem, and not a technical one.

## 9. Adoption path

The full sky is not the target. The target is the set of objects that actually appear in documentaries, news articles and museum captions — perhaps two hundred objects, growing slowly.

1. Name that set properly, with a vetted pool.
2. Publish the register openly with the generator.
3. Get one science communicator to use it on air.

A single television producer adopting the register would do more for it than any committee approval. That is the whole strategy.

---

## Appendix A — Algorithm

```
issue_name(catalogue_id, constellation, planet_letter):

    if object has an existing proper name:
        record it and return it

    stem   = iau_abbreviation(constellation)
    index  = fnv1a(catalogue_id) mod pool_size

    while (stem, pool[index]) already issued in register:
        index = (index + 1) mod pool_size

    core   = pool[index].word
    suffix = vowel_map[planet_letter]

    name = stem + " " + core + "-" + suffix

    store name permanently against catalogue_id
    return name
```

The hash is computed **once**, at issue. The stored name is the record. It is never recomputed from the catalogue ID, because catalogue IDs can be merged, split or reclassified, and a name that drifts with them is not a name.

## Appendix B — Reference implementation

An implementation accompanies this paper: a register file (`register.json`), a
command-line tool that issues names into it (`issue.py`), and a page that reads
and displays it (`skyname.html`). The register currently holds 57 entries drawn
from 44 languages.

The tool enforces the immutability rule directly. Names are issued once and
appended; the file is never regenerated from catalogue IDs. A `check` command
validates the register for duplicate identifiers, unknown constellation codes
and stem-core collisions.

Correspondence and contributions to the address above.

## Appendix C — What this proposal does not do

- It does not rename any object in the astronomical literature.
- It does not require IAU approval, though it would welcome it.
- It does not attempt to name the two billion objects in Gaia.
- It does not encode distance, mass, temperature, or any other measured quantity.
- It does not claim the resulting names are beautiful. It claims they are sayable.
