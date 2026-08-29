---
description: Turn synthesis.md into a single self-contained HTML page a colleague can read on their own. Reorganized for the reader, with background and definitions added; findings and numbers derived strictly from the source.
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

`synthesis.md` runs 300–600 lines of dense tables. It is correct, and unreadable to anyone who was
not there. This produces a version a colleague can open and understand **on their own, without
asking you questions.**

Internal sharing. Not a public artifact.

### Ask who is reading it

Before writing, ask. The answer changes how much background is needed and which sections lead.

- **A researcher in the same field** — knows the domain, not this investigation
- **A manager or a neighboring team** — needs the "so what" first, tolerates less detail
- **Your future self** — the least background, the most detail

Default to the first if the user doesn't say.

---

## Two rules, and they are different

### Rule 1 — never add a finding

**Every claim, number, caveat, and citation comes from `synthesis.md`.** If you want to state
something the source does not, it belongs in the source: fix `synthesis.md` and regenerate.

Two documents that disagree are worse than one dense document.

### Rule 2 — you are expected to add prose

**Background, definitions, framing, and structure are not findings.** Writing them is the job.

> ⚠️ These two got conflated in an earlier version of this skill, which told you to put *any*
> sentence not in the source into `synthesis.md` first. That is wrong and it produced an unreadable
> report. "A raster image is a grid of pixels" does not belong in a research record.

**Test**: could a reader dispute it by checking a source? Then it's a finding — Rule 1.
Is it something any practitioner would nod at? Then it's prose — Rule 2, write it.

---

## What must survive

The parts most likely to be lost when something is "made readable." Losing them inverts the meaning.

| Must survive | Why |
|---|---|
| **Provenance** (synthetic / real / unknown) | A number without it reads as established fact |
| **Search scope on every gap** | Without it, "nobody has done this" is unfalsifiable |
| **Gap status** — including the refuted ones | A refuted gap that looks intact is the worst outcome |
| **The corrections record** | It tells the reader how much to trust the rest |
| **🔒 marks** | **Keep the mark, keep the content.** A reader may forward this file, and needs to see which parts cannot go further |

Scope may be stated in plain words — "19 queries, 0 hits; the nearest work used rendered images, not
conversions" reads better than a list of twelve database names, and says as much. **Push the
database list to the detail section rather than deleting it.**

## What must be added

Not optional. Without these the page is a format conversion, not a report.

| Must add | What it is |
|---|---|
| **Background** | What the problem is, for someone who has never thought about it. Two or three short sections |
| **Definitions, up front** | Every term, metric, and named work explained **at first use**. A short "read this part first" block near the top |
| **A reading guide** | "3 minutes: §3. 15 minutes: §3–7. Everything: all of it." |
| **A glossary at the end** | For terms the reader meets again later |
| **Implications for us** | **Only if the source has them** — usually in the 🔒 sections. Do not invent them |

---

## Order: organize for the reader, not for the process

`synthesis.md` is ordered by research stage — state of the art, gaps, open, corrections. That is the
order the work happened in, not the order anyone wants to read.

**Reorganize by question.** A recommended sequence:

1. Background — what the problem is
2. Terms — the ones needed to read on
3. **The conclusion**
4. **One section per question the reader actually has** ("does it get cheaper?", "does accuracy
   improve?", "how much data does it need?")
5. What it means for us — *if the source supports it*
6. What nobody has answered yet — the gaps, with scope
7. What to do next
8. **How much to trust this** — the corrections record, reframed. Same content, but the reader now
   understands why they are reading it
9. Detail tables
10. Glossary

**Regrouping the evidence under reader-facing questions is allowed and expected.**
**Adding a claim the source does not make is not.** That line is Rule 1.

Keep a short section-ID mapping at the end so the two documents can still be compared.

## Length: relocate, don't compress

The reference report is **longer** than its source. It is not a summary. The dense tables moved to a
detail section near the back, and the front carries explanation.

**Do not shorten by dropping caveats.** Move detail back; keep the front readable.

---

## Visual treatment

Only where it makes something easier to read. **A decorative figure implies content that isn't
there.**

### Provenance and status → badges, never color alone

Every badge carries **an icon and a word**, so it still reads in grayscale and for a colorblind
reader.

| Value | Badge |
|---|---|
| real data | ✅ real |
| synthetic | ⚗️ synthetic |
| unknown | ⚠️ unknown |
| 🔒 internal | keep the lock visible |

Reserve status colors for status. **Never reuse them to distinguish one method from another.**

### The coverage matrix → an actual matrix

Filled cell: tinted, with the count. **Empty cell: distinct by both fill and a dashed border** — not
by color alone. Label the axes, and say in words what an empty cell means.

### Distributions → inline bars

Put the bar inside the table cell. **Do not build a chart for four values.**

### Long tables → collapsible, in a detail section

Sticky header row; horizontal scroll inside its own container. Group them under one "detail"
heading rather than interleaving them with the prose.

### If a real chart is genuinely needed

Rare here. Use a dataviz skill if the environment has one. Otherwise: one axis (never two y-scales),
a legend for two or more series, hues in fixed order, recessive grid lines.

## Output

`report.html` in the project directory. **One file. No external requests.**
All CSS inline, system font stack, must work from `file://` and as an email attachment.
Support `prefers-color-scheme`; choose the dark values rather than inverting.

---

## What not to do

**Fidelity**

- Do not summarize away the caveats. "98.04%" without "synthetic only" is a false statement
- Do not drop the corrections. They are the reason the rest is credible
- Do not soften a refuted gap
- Do not invent implications the source does not support

**Readability**

- **No internal jargon in the body** — agent names, section IDs (`S3b`, `V2`, `2f`), file paths,
  "Stage 4", cross-references like "#7". The reader has never seen the pipeline
- **No named work, metric, or abbreviation without an explanation at first use**
- **No number without saying what it measures**
- No figure that restates a sentence

---

## Check it mechanically before saying it is done

These are runnable. Do them.

1. **Terms used before they are defined** — list every named work, metric, and abbreviation in the
   body, and confirm each has an explanation at or before first use
2. **Internal jargon** — grep the output for `cc-research`, `synthesis/`, `Stage `, `S1`–`S4`,
   `V1`–`V9`, `2a`–`2z`. Hits in body text are defects; hits in a source-pointer footer are fine
3. **Provenance** — every reported number carries a badge
4. **Gaps** — every gap carries its scope
5. **🔒** — every internal item still carries the mark

Then **open it and look at it.** Layout is not verifiable by reasoning.

## A worked example may exist

If `../_reference/report-example.html` exists next to the project directory, **read it before
writing.** It is a real report that came out well, and one example settles more than this
specification does.

## When you're done

Give the file path, and **one line on anything in the source you could not render faithfully.**
