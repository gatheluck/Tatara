# synthesis — {topic}

**Written {date}. Revision {N}.** The Stage 3–4 deliverable.

Material: {N} external Deep Research runs + {N} agents. {line count}

## What changed in revision {N}

> Put this first. **A claim that got rewritten is the most important thing on the page** — it tells
> the reader which parts have already survived an attack and which are new and untested.

| # | Change | Before → After |
|---|---|---|
| 1 | {…} | {…} |

*(Omit this section on revision 1.)*

## How to read this

- **§0 The short version** — the conclusion, before the 500 lines
- **§1 State of the art** — claims of existence. Every row is verifiable
- **§2 Gaps** — **always paired with the search scope**. These are claims of absence, so they are
  written in a form you can falsify
- **§3 Open** — what is not settled
- **§4 Corrections** — my own errors, as they came to light
- **§6 Tracing a claim** — which file holds the evidence

**Numbers carry a "provenance" column.** So that values from synthetic data and values from real
data never get mixed.

🔒 = confidential. Check before copying it anywhere.

---

# §0 The short version

{The conclusion in a handful of lines. Someone who reads only this section should come away with
the right belief, including the right amount of doubt.}

---

# §1 State of the art

| Work | Year | Input | Granularity | Supported scope | Reported value | **Provenance** | Source |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | synthetic / real / **unknown** | DR / CC / both |

**What can be read off this**
- {…}

## 1.x Standards, patents, products

{If there are any. Quote the conditions of applicability verbatim}

## 1.x Data

| Kind | Status |
|---|---|

## 1.x 🔒 Internal

---

# §2 Gaps

**These are claims of absence, so every one of them carries its search scope.**

Mark each one with its current status:

| Mark | Meaning |
|---|---|
| ✅ | survived every attack so far |
| ⚠️ | partly broken — narrower than it was |
| ❌ | **broken.** Kept on the page, because how it broke is evidence |

## 2.1 {name of the gap} — {✅ / ⚠️ / ❌}

**Claim**: {…}

**Grounds**: {someone else's words if at all possible. Stronger than your own judgment}

**Search scope** (as of {date})
- {N} external Deep Research runs
- {database}: {the literal query string}
- **Not searched**: {…}

**Closest existing work**: {…}. The difference is {…}

## 2.x A hole in our own search, not a gap in the literature

> **Keep these separate from the real gaps.** "Nobody has published this" and "we did not look
> there" produce the same silence, and only one of them is a research opportunity.

| What was never searched | Why it matters | Cost to close it |
|---|---|---|

---

# §3 Open

| # | Point | State | **What it would take to settle it** |
|---|---|---|---|

## 3.x Distribution across the four buckets

> The shape of the cross-check is itself a finding. If almost nothing landed in **agreement**, the
> two routes were looking at different things — say so.

| Bucket | Count | What that tells you |
|---|---|---|
| Agreement | | |
| Contradiction | | |
| One side only | | |
| Gap | | |

---

# §4 Corrections

| # | Error | Correct | How it came to light |
|---|---|---|---|

## Types of error

{If they can be classified. It prevents the next one}

## Added in revision {N}

{Errors found after the previous revision. Keep the old ones — the list is cumulative}

---

# §5 Next moves

{In descending order of confidence}

## 5.1 What not to do

{Write down the "temptation to restate it" you felt during the research. It guards against sycophancy}

## 5.x Out of reach

{What needs a human, a subscription, or an application. Recording it stops the next run from
burning time on the same wall}

---

# §6 Tracing a claim

{Which file holds what. A reader who doubts one line should be able to find its evidence without
opening all of them.}

| File | What is in it |
|---|---|
