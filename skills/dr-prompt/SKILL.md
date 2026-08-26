---
description: Generate the prompt to hand to an external Deep Research service (ChatGPT or similar). Stage 0. A human copies it and runs it.
argument-hint: [project directory]
disable-model-invocation: true
---

# dr-prompt — generate the prompt for external Deep Research

> ⛏️ **Go collect the satetsu (砂鉄) — the external route.** Decide what the outside Deep Research gets sent to dig for.

Read `${CLAUDE_PLUGIN_ROOT}/reference/principles.md` first.

Target project: $ARGUMENTS (if omitted, the most recent one, or ask).
Read its `context.md` before you write.

**Write the prompt in the user's language.** The quoted lines below fix the wording, not the language.

## Where it goes

`deep-research-prompt.md`. **Never edit it after sending** — it is the reproducibility record.

## What the prompt must contain

| Requirement | Why |
|---|---|
| **Link straight to the original papers and primary sources** (not by way of surveys) | The precondition for the later cross-check to work at all |
| Inline citations and source metadata | Same |
| Have it mark any bibliographic detail it cannot confirm as "unconfirmed" | Hallucinated citations are real. Never let it guess a year or a venue |
| **The limitations the authors wrote themselves, quoted verbatim** | **Raw material for the gap. Extracting fact, not passing judgment** (Principle 1) |
| **Actual numbers** (data scale, accuracy, compute) | "High accuracy" cannot be cross-checked (Principle 8) |
| Draw boundaries by period, field, and condition | Coverage is not something to expect |
| **Reports of failure and limitation, weighted the same** | Negative results rarely get published. Demand them explicitly |

## What must never go in

- **A list of field names or method names.** Even if `context.md` has a provisional list,
  **never hand it over**. It turns the responder into a form-filler and kills off the names you
  never thought of (seed leakage)
- **The question "where is the novelty?"** (Principle 1)
- **Your own read of the situation, or your conclusions.** It contaminates the material the
  synthesis gets built from

## Instead: make enumerating the terms a required step

Rather than handing over field names, **make the enumeration itself part of the task**.

> Before you start searching, enumerate as many technical terms as you can that could refer to
> this problem, or to a structurally identical one. Cross the vocabularies of several fields, and
> include **at least one language other than English** that is likely to have its own literature
> on this topic.
> **State the enumerated terms at the top of the report**, then run a search for each one.

That list at the top later becomes the material for measuring **what never got searched**.

> 🌏 **Why insist on a non-English language.** On the first real run, the era that both sweeps
> reported as thinnest in English turned out to be the *thickest* in Japanese — a lineage of eight
> papers from 1991–2000, all freely available, that neither sweep had found. Pick whichever
> language the field is actually written in: Japanese and Chinese for manufacturing and CAD,
> German for mechanical engineering and standards, and so on.

## The one line that prevents sycophancy

Always include it.

> Do not accommodate the problem statement I have given you.
> **If this problem statement is itself already solved, say so.**

## Output format to specify

- The list of research goes in a **table**. Columns: input format / granularity of correspondence /
  scope it handles / evaluation method and actual numbers / source
- An **inline citation** immediately after every claim
- **The list of terms used to search**, at the top of the report

## Record fields to leave in the file

Alongside the prompt body, create fields to record the following.

- Whether the prompt was sent unmodified
- **Deep Research's clarifying questions, and the answers given**
- **The research plan it proposed** (verbatim)
- Whether the source scope was adjusted mid-run
- Date and time of the run

### ⚠️ Operational note (measured)

**Deep Research does not always ask clarifying questions.** Sometimes only a plan appears, and if
you leave it alone it starts on its own. **The plan is the only point of intervention.**
Never write the prompt assuming the questions will come.

## Instructions to hand to the human

1. Paste the prompt body (inside the code block) **verbatim**
2. **Read the research plan when it appears.** If the scope is off, fix it here
3. When it finishes, **download as Markdown** and save it to `deep-research-output.md` **unedited**
   (do not copy-paste — most services support Markdown export)

## When you're done

**Stage 2 can start in parallel, without waiting for Deep Research to finish.**
Next is `/tatara:sweep`.
