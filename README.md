# The Spoken Register

An open alias table giving stars and exoplanets names a person can say,
remember and repeat.

Catalogue identifiers like `Kepler-452b` are excellent primary keys and poor
names. This project doesn't try to replace them. It adds the display layer
that was never built: a pronounceable alias, anchored to the constellation the
object sits in, with its distinctive part drawn from a pool of words meaning
"star", "sky" or "moon" in human languages worldwide.

**Matthew John Santley** · mattsantley@hotmail.com · draft 0.1

## What's here

| File | What it is |
|---|---|
| `register.json` | **The record.** Every name ever issued, plus the word pool. |
| `issue.py` | The tool that issues names and writes them to the register. |
| `expand.py` | One-off batch loader. Derives constellations from coordinates via astropy. |
| `audit.py` | Checks every entry's constellation against the sky. `--fix` corrects them. |
| `verify.py` | Records which pool words were found in published reference sources. |
| `index.html` | The public page. Reads `register.json` and displays it. |
| `contribute.html` | Contributor page: proposal previews and how assignment works. |
| `words.html` | The word pool by language, with a route to confirm or correct each entry. |
| `skyname-proposal.md` | The proposal paper explaining the scheme and why. |

## Running it

The page reads `register.json` over HTTP, so serve the folder rather than
opening the file directly:

```
python3 -m http.server
```

Then open http://localhost:8000/index.html

Opening `index.html` straight from disk still works — it falls back to a
snapshot embedded in the page and says so in a banner — but the live file is
the authority.

## Issuing a name

```
./issue.py add "TOI-2109 b" Cyg "ultra-hot giant"
./issue.py check
./issue.py sync
```

`add` hashes the catalogue ID **once**, picks a word, probes forward if that
word is already used in that constellation, and writes the result to
`register.json`. After that the file is the authority and the hash is history.
`check` validates the register. `sync` refreshes the offline snapshot inside
`index.html`.

**Never regenerate `register.json` from scratch.** Insert a word into the
middle of the pool rather than appending it and every name would shift
silently. Names are issued once and appended, never recomputed.

## Adding a word to the pool

```
./issue.py word "Tähti" "Finnish" star
./issue.py vouch "Tähti" "name of the speaker who confirmed it"
```

Every word carries two independent fields.

`checked` records whether the word was found in published reference sources —
177 of 229 so far — 147 confirmed, 30 valid variants — with four corrected where sources disagreed. Run
`./verify.py` to see the breakdown.

`vouched_by` records a speaker who confirmed it. All 229 are currently empty.

The two are deliberately separate. A dictionary catches a misspelling or an
invention. Only a speaker catches a word that is correct on paper and wrong in
use. The
pool was assembled from reference sources and has not been checked by native
speakers. A word that means "star" in a dictionary can mean something
regrettable in a neighbouring dialect, and only speakers catch that. Treat the
whole pool as unvetted until those fields fill in.

## Contributing

**Checking a word is the most useful thing you can do.** The word list is at
`words.html` on the live site. Each entry has a one-click route to confirm or
correct it, by email or by GitHub issue.

There are three issue templates: confirm a word, correct a word, add your
language. Email works just as well and needs no account.

For code or register changes, open a pull request against `register.json`. Run
`./issue.py check` first.

The page has a preview panel that shows what the tool would issue and prints
the exact command and JSON line to submit. The page itself never writes
anything.

## Licence

- Code and data (`issue.py`, `register.json`, `index.html`): MIT — see `LICENSE`
- The paper: CC BY 4.0 — see `LICENSE-PAPER`
