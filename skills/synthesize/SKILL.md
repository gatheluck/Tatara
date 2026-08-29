---
description: Stage 3. Cross-check external Deep Research against this side's sweep into a state-of-the-art table and a coverage matrix. Gaps fall out mechanically, as empty cells in the matrix.
argument-hint: [project directory]
disable-model-invocation: true
---

# synthesize — the cross-check

> 🔥 **Load the furnace.** Cross-check the satetsu (砂鉄, iron sand) from both routes into a
> state-of-the-art table and a coverage matrix.

Read `${CLAUDE_PLUGIN_ROOT}/reference/principles.md` first.

Target: $ARGUMENTS (ask if omitted).

**Write in the user's language.** Instruct every agent to do the same.

## Handling a large input

External Deep Research output can run to tens of thousands of characters.
**After compaction, a file over 5,000 tokens loses its body and becomes a path reference.**

→ **Don't load it into the main context. Split it across subagents, one per dimension.**
Each agent reads **both** the DR output and this side's sweep, and cross-checks them along its
own dimension.

## Which deliverable — read `Track:` in `context.md`

| Track | Template | Shape |
|---|---|---|
| **novelty** | `${CLAUDE_PLUGIN_ROOT}/templates/synthesis.md` | state of the art → gaps → open → corrections |
| **selection** | `${CLAUDE_PLUGIN_ROOT}/templates/selection.md` | decision → candidates → comparison → fit → what reverses it |

**The cross-check agents below run either way.** Coverage and contradiction matter for both; only
the assembled document differs.

**On a selection track, weight them differently.** Whether the code exists, what licence it carries,
and what input format it consumes decide more than the citation graph does. A method nobody can run
is not a candidate whatever it scores. S1 becomes a candidate table rather than a coverage matrix,
and S4 asks whether the *candidate list* is complete rather than whether an absence claim holds.

## Agents to launch (split by dimension)

### S1. Method inventory and coverage matrix
Build the merged table. **It must carry a "source" column** — `DR only` / `CC only` / `both`.

Then build the **coverage matrix**. The axes depend on the topic — say,
"correspondence granularity × supported scope × handling of annotations."

> ⚠️ **Make them leave empty cells empty. Never let them write what an empty cell means.**
> **Never let them judge** "this is where the novelty is." Placing facts is the entire job.

Gaps come out as **holes in a matrix, not as opinions**. Interpretation is the human's.

### S2. Data and measurability
The merged dataset table. **Add a column that separates "actually accessed" from "only read a
description of."**
On "can this problem be evaluated quantitatively as things stand," **put both sides' views side by
side.** **Never let the agent write its own judgment.**

### S3. Limitations and contradictions ★the most important one downstream
- Collect the limitations the authors wrote themselves, **as verbatim quotes**
- **Enumerate every disagreement between DR and CC.** For each:

| Point | Claim A | Claim B | **Nature of evidence A/B** | **What it would take to settle it** |

**Nature of evidence** = `verbatim from a primary source` / `measured by actual access` /
`second-hand description` / `inference`

> **Never resolve a contradiction. Laying them out is the job.**
> Never let them declare which side is right.

### S4. Reconciling the search scope
Line up the terms DR used (they should be at the top of its report) against the routes this side
took. Identify **the territory neither one searched** — vocabulary / database / era / language /
document type.

**Make them check patents and non-English literature explicitly.** Practical technique sometimes
never reaches a paper.

This becomes the Stage 4 search plan as it stands.
**But require the plan to include a retrievability check** (some databases you can name, you cannot
actually get at).

## The human does the integration

Once all four are in, assemble `synthesis.md` yourself. **Never have an agent write it.**

Structure:

1. **State of the art** — every row is a claim of existence. **A "provenance" column is mandatory**
   (synthetic / real data / unknown)
2. **Gaps** — each one carries its **search scope** (literal query strings / databases / date / the
   nearest hit)
3. **Open** — whatever is not settled. Write down **what it would take to settle it**
4. **Corrections** — your own errors, as they came to light along the way

## When you're done

`/tatara:verify`. **Hunt for counterexamples.**
