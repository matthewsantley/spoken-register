# Outreach drafts

Written to be copied, edited and sent. Nothing here should go out unchanged —
they read better in your own voice, and a post that sounds drafted is worse
than one that sounds like a person.

**Order matters.** Everything in wave one is about getting words checked.
Everything in wave two is weaker while the pool sits at zero confirmed. Don't
skip ahead.

**On mentioning AI.** Every draft below says the project was built with AI
help. Reddit will work it out anyway, and it lands completely differently if
you said it first. Stated plainly it costs nothing; discovered later it becomes
the only thing anyone talks about.

---

# WAVE ONE — getting the words checked

## 1. r/asklinguistics

*Check the subreddit rules first — some ban link posts. If so, describe it and
put the link in a comment.*

**Title:** I've built a naming scheme that uses the words for "star", "sky" and
"moon" from 117 languages. I don't speak most of them and I need checking.

**Body:**

Exoplanets get catalogue names like `Kepler-452b` or, at the worse end,
`OGLE-2005-BLG-390L b`. Fine for astronomers, useless for anyone talking to the
public — NASA gave up on that second one and nicknamed it Hoth.

I've built an open list that gives each object a second name meant for saying
out loud. Two parts: the standard abbreviation for its constellation, then a
word from a shared pool. The rule holding the pool together is that every word
in it means "star", "sky" or "moon" in some human language. The idea is that
every culture named the sky, so the sky gets named after the sky, and nobody's
mythology gets imposed on anyone else's.

The pool currently holds 229 words from 117 languages. **None of them has been
confirmed by a speaker, and I only speak English.**

That's not hypothetical caution. While assembling it I found two entries I had
simply invented — one recorded as Lithuanian for "sky", one as Greenlandic for
"star". Neither is a real word. I caught them by accident, which is not a
method, and I have no reason to think they were the only two.

So: https://matthewsantley.github.io/spoken-register/words.html

Filter by a language you speak. If a word is wrong, wrong in a way I wouldn't
notice, or would sound strange to an actual speaker, there's a one-click way to
tell me on each row. Even one word checked is useful.

Two things I'd also value opinions on:

- I strip diacritics for the register spelling (*tähti* is stored as *Tahti*).
  Necessary for a machine-readable identifier, but I'm aware of what it does
  to a language. Is there a better convention?
- Words are assigned to stars by algorithm, so no human picks which language
  goes with which star. Does that actually avoid the problem I think it
  avoids, or have I just moved it somewhere less visible?

Built with AI assistance, which is also how the two invented words got in.
Whole thing is open source and MIT licensed.

---

## 2. A single-language subreddit (template)

*One at a time, not a spree. Rewrite for each. Check self-promotion rules.
Examples: r/Cymraeg, r/Suomi, r/learndutch, r/Nahuatl, r/tamil.*

**Title:** Are these [LANGUAGE] words right? Three of them are being used to
name planets.

**Body:**

I've built an open list that gives exoplanets names people can actually say,
instead of codes like `Kepler-452b`. Each name uses a word meaning "star",
"sky" or "moon" from one of 117 languages.

Three are [LANGUAGE]: **[WORD]**, **[WORD]** and **[WORD]**, recorded as
meaning [MEANING], [MEANING] and [MEANING].

I don't speak [LANGUAGE]. Nobody who does has checked these. Two words in an
earlier version turned out to be things I'd invented outright, so I'd rather
ask than assume.

Are they right? Right spelling, right meaning, and would they sound normal
rather than odd to someone who speaks the language?

https://matthewsantley.github.io/spoken-register/words.html — search
"[LANGUAGE]" and there's a button on each row.

If a better word exists, or if the language should be represented differently,
I'd rather hear it now than after these names are in use. Built with AI help,
open source, no commercial angle.

---

## 3. Wikitongues, or any language-documentation organisation

**Subject:** 117 languages used in an open naming project — none verified, and
I'd like that fixed

Hello,

I've built an open register that gives stars and exoplanets pronounceable
names, as an alternative to catalogue codes like `OGLE-2005-BLG-390L b`. It's
free, MIT licensed, and there is no product behind it.

The distinctive part of each name comes from a pool of words meaning "star",
"sky" or "moon", drawn from 117 languages. It currently holds 229 words. Not
one has been confirmed by a speaker.

I'm conscious of the shape of that problem: a monolingual English speaker in
Lancashire has assembled words from languages across the world and put them on
a public site. Two entries turned out to be outright fabrications before I
caught them. The whole design records which language each word came from,
precisely so origin is credited rather than absorbed, but that only works if
the origins are right.

I'm not asking for endorsement. I'm asking whether there's a sensible way to
get these checked, or whether the approach itself is one your community would
push back on. If it is, I'd genuinely rather know.

The word list, with the language of every entry:
https://matthewsantley.github.io/spoken-register/words.html

The reasoning, including where I think it's weak:
https://matthewsantley.github.io/spoken-register/skyname-proposal.pdf

Built with AI assistance, which I mention because it's how the two invented
words got in.

Matthew John Santley
mattsantley@hotmail.com

---

## 4. Mastodon

*Under 500 characters. Tag #linguistics #languages #astronomy.*

Exoplanets are named things like OGLE-2005-BLG-390L b. NASA gave up and called
that one Hoth.

I've built an open list giving them sayable names, using the words for
star/sky/moon from 117 languages.

229 words. Zero confirmed by an actual speaker. I speak one language.

If you speak any of these, one word checked would help:
https://matthewsantley.github.io/spoken-register/words.html

#linguistics #languages #astronomy

---

# WAVE TWO — once you have vouched words

*Don't send these yet. "Zero confirmed" is a fair criticism and you can't
answer it. Twenty confirmed and it's a different conversation.*

## 5. r/space or r/astronomy

*Expect a rough ride. The three objections will be: the IAU already does this,
you can't rename things, and the pool is unvetted. Answer all three in the post
rather than in the comments.*

**Title:** Exoplanet catalogue names are unusable on television, so I built an
alias register. Would like it pulled apart.

**Body:**

`Kepler-452b` is one of the easy ones. `OGLE-2005-BLG-390L b` held the record
for most distant planet known — NASA nicknamed it Hoth because nobody could say
the real thing, and PBS eventually ran a documentary called "Yes, There's
Really a Frozen Exoplanet Named Hoth".

That's the problem. Catalogue codes are excellent identifiers and hopeless
names, and the display layer nobody built is where a presenter is left reading
a database row ID out loud.

So I've built the alias table. **It renames nothing.** Catalogue IDs stay the
identifier of record. This is a second name for saying out loud.

Two parts. The IAU constellation abbreviation, so the name tells you where to
look. Then a word from a pool where every entry means "star", "sky" or "moon"
in some human language — assigned by algorithm, so no person chooses which
language goes with which star. A closing vowel marks the planet, and a whole
system shares one word:

TRAPPIST-1 b through h → **Aqr Zvaigzde-a, -e, -i, -o, -u, -ae, -ea**

Anything with an existing proper name keeps it. Dimidium stays Dimidium.

Three objections you'll have, answered up front:

- **The IAU already does this.** NameExoWorlds has covered a few hundred out of
  six thousand, by public campaign. That's not a scaling mechanism, and this
  needs nobody's permission to be useful.
- **The pool isn't verified.** Correct, and it's the biggest problem. 229 words,
  117 languages, zero confirmed by speakers. Two were outright fabrications
  before I caught them. That's flagged on every page.
- **This was built with AI help.** Yes. It's also how those two words got in.
  I've caught several design errors since; I won't have caught them all.

https://matthewsantley.github.io/spoken-register/

Tell me what's wrong with it.

---

## 6. Science journalist or BBC Sky at Night Magazine

**Subject:** The naming problem you hit every time you write about exoplanets

Hello [NAME],

You'll have run into this: you want to write about a planet and its name is
`OGLE-2005-BLG-390L b`. NASA had the same problem and nicknamed it Hoth.

I've built an open register that gives objects like that a second name meant
for saying out loud — one that also tells the reader which constellation to
look in. It renames nothing; catalogue codes stay exactly as they are.

TRAPPIST-1's seven planets become Aqr Zvaigzde-a through -ea. Same system,
audibly related, and the "Aqr" says Aquarius.

It's free, open source, and there's nothing to sign up to. What I'd like to
know is whether it's any use to someone who does this for a living, or whether
it solves a problem you don't actually have. A blunt answer either way would be
worth a lot to me.

Register and reasoning: https://matthewsantley.github.io/spoken-register/

Matthew John Santley — 30 years as an analyst and developer, no background in
astronomy, which is either the problem or the point.

---

## 7. Planetarium or observatory outreach team

**Subject:** Something for the "and this planet is called" moment in a show

Hello,

A question from outside your field. When you're presenting and you reach an
exoplanet, what do you actually call it? I'm guessing you either skip the name
or say "a planet in the constellation Cygnus", because `Kepler-452b` stops a
room.

I've built an open list giving those objects a spoken name alongside the
catalogue code. Kepler-452b becomes Cyg Stjarna-a — "Cyg" for Cygnus, so the
name itself tells the audience where to look. TRAPPIST-1's seven planets share
one word and differ only by their final vowel, so they sound like a family.

I'd like to know whether this is useful to someone who presents to the public,
or whether I've invented a solution to a problem you solved years ago in a way
I haven't thought of. If it's the latter I'd genuinely like to hear how.

Free, open source, nothing to join:
https://matthewsantley.github.io/spoken-register/

Matthew John Santley
mattsantley@hotmail.com

---

# WAVE THREE — last, not first

## 8. IAU Working Group on Star Names

*Send only with vouched words and some adoption behind you. The letter is short
on purpose: they will read the site, not the email.*

**Subject:** A pronounceable alias register for exoplanets — seeking criticism,
not endorsement

Dear colleagues,

I've built and published an open alias register that gives exoplanets a
pronounceable second name for public use. It is not a naming proposal in the
sense your group handles: catalogue identifiers remain the identifier of
record, existing proper names are recorded and kept rather than replaced, and
nothing in the scientific literature would change.

Its design tries to respect the concerns I understand your group to hold. Words
are drawn from a pool where every entry is the ordinary noun for "star", "sky"
or "moon" in some human language — no mythology, no commemoration of
individuals, no nation's figures. Assignment is by algorithm rather than by any
person's choice. Language of origin is recorded with each word so that
provenance is credited.

I am writing for criticism rather than approval. Specifically: is the
underlying idea sound, and are there objections obvious to your group that I
have not anticipated? I would rather hear them now.

Register: https://matthewsantley.github.io/spoken-register/
Reasoning, including its known weaknesses:
https://matthewsantley.github.io/spoken-register/skyname-proposal.pdf

Yours sincerely,
Matthew John Santley
mattsantley@hotmail.com

---

# Practical notes

**Don't post everywhere in one day.** One post, then wait and answer everything
it generates. A thread with unanswered questions does more damage than no
thread.

**The reply that matters most** is someone saying a word is wrong. Fix it
quickly and visibly, and thank them by name in the register. That behaviour is
what makes the next person bother.

**Have an answer ready for "why not just use the IAU's names".** It's the first
thing anyone knowledgeable will say, and "a few hundred out of six thousand,
by public vote, and it needs no permission to exist" is a good one.

**If a thread turns hostile, don't argue the design.** Ask what they'd do
instead. Most of the time there isn't an answer, and asking is more persuasive
than defending.
