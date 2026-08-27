---
description: Turn synthesis.md into a single self-contained HTML page for sharing with colleagues who did not follow the research. Derived from the markdown, never authored separately.
argument-hint: [project directory]
disable-model-invocation: true
---

# report — make it readable for someone else

> 🗡️ **Finish the blade.** The tamahagane (玉鋼) is already made; this is the part you hand to
> someone else.

Read `${CLAUDE_PLUGIN_ROOT}/reference/principles.md` first.

Target: $ARGUMENTS (ask if omitted).

**Write in the user's language.**

## What this is for

`synthesis.md` runs 300–600 lines of dense tables. It is correct, and it is hard to read for anyone
who was not there. This makes a version a colleague can open, skim, and understand — **on their own,
without asking you questions.**

Intended for **internal sharing**. Not a public artifact.

## The one hard rule

**Derive everything from `synthesis.md`. Write no new claims.**

Two documents that say slightly different things is worse than one dense document. If something is
unclear in the markdown, **fix the markdown and regenerate** — do not fix it only in the HTML.

If you find yourself wanting to add a sentence that isn't in the source, that sentence belongs in
`synthesis.md`. Put it there first.

## What must survive the translation

These are the parts most likely to be lost when something is "made readable," and losing them
inverts the meaning.

| Must survive | Why |
|---|---|
| **The provenance column** (synthetic / real / unknown) | A number without it reads as established fact |
| **Search scope on every gap** | Without it, "nobody has done this" is unfalsifiable |
| **Gap status** (✅ ⚠️ ❌) | A broken gap that looks intact is the worst possible outcome |
| **The corrections record** | It tells the reader how much to trust the rest |
| **The revision log** | Shows which claims have been attacked and which are new |
| **🔒 marks** | Keep them visible. The reader may forward this further |

**A reader who skims only the headings should still come away with the right amount of doubt.**

## Output

`report.html` in the project directory. **One file. No external requests.**

- All CSS inline. No CDN, no web fonts, no analytics
- Must open correctly from `file://` and survive being emailed as an attachment
- System font stack

## Structure

1. **Header** — topic, date, revision number, one-line scope of what was searched
2. **The short version** (§0) — first screen, no scrolling
3. **What changed in this revision** — if the source has it
4. **Sticky table of contents** — a 500-line document needs jump links
5. The sections, in source order
6. **Footer** — "Derived from `synthesis.md`. Evidence lives in `verify/` and `cc-research/`."

## Visual treatment

Only where it makes something easier to read. **A decorative figure implies content that isn't
there.**

### Provenance and status → badges, never color alone

Every badge carries **an icon and a word**. Color is a third, redundant channel — so it still reads
in grayscale, in forced-colors mode, and for a colorblind reader.

| Value | Treatment |
|---|---|
| real data | ✅ solid, "real" |
| synthetic | ⚗️ outlined, "synthetic" |
| unknown | ⚠️ hatched, "unknown" |
| ✅ gap survived | green chip |
| ⚠️ partly broken | amber chip |
| ❌ broken | red chip, **body text struck through in the heading only, never in the explanation** |

Reserve those four status colors for status. **Never reuse them to distinguish one method from
another.**

### The coverage matrix → an actual matrix

This is the single biggest readability win. A three-axis coverage table flattened into rows is
nearly unreadable; as a grid, the empty cells are visible at a glance.

- Filled cell: tinted, with the count and a link to the row
- **Empty cell: distinct by both fill and a dashed border** — not by color alone
- Label the axes. State what an empty cell means, in words, next to the grid

### Distributions → inline bars, not charts

For a handful of numbers (the four-bucket distribution, counts per source), put a bar **inside the
table cell**. Do not build a chart for four values.

### Long tables → make them scannable

- Sticky header row
- The provenance column visually separated from the data columns
- Wide tables scroll horizontally inside their own container, never breaking the page

### If a real chart is genuinely needed

Rare here. If one is: **use a dataviz skill if the environment has one.** Otherwise — one axis
(never two y-scales), a legend whenever there are two or more series, hues assigned in fixed order
and never cycled, and recessive grid lines.

## Dark mode

Support it with `prefers-color-scheme`. **Choose the dark values; do not invert the light ones.**
Check that the badges still read.

## What not to do

- **Do not summarize away the caveats.** "98.04%" without "synthetic only" is a false statement
- **Do not drop the corrections section** because it looks unflattering. It is the reason the rest
  is credible
- **Do not add figures that restate a sentence.** If the sentence was clear, the figure is noise
- **Do not reorder sections to build a narrative.** Source order, so the two documents stay
  comparable
- **Do not soften ❌.** A broken gap stays visibly broken

## When you're done

Tell the user the file path and **one line on what it does not contain** (anything in the source
you could not render faithfully).

Open it and look at it before saying it is finished — the layout is not verifiable by reasoning.
