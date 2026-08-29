# context — {topic}

## Research topic

{What and what, and what you want to do with them. One or two sentences}

## Problem setting

{Concretely. What is the input, and what is the output}

## Aim

{What becomes possible once this works}

## Why it looks hard (working hypothesis — to be verified)

> ⚠️ **The following is the view as of the start. It is what the research checks or refutes, not fact.**

- {…}

## Names it goes by in other fields (starting points for the gap hunt — to be extended)

> ⚠️ **Never put this list into the external Deep Research prompt** (seed leakage).
> It gets used at Stage 4, when hunting for counterexamples to the gaps.

- {…}

## Adjacent projects of my own

{Related projects inside this repository. Mined at Stage 2b. Information the external sweep cannot see}

- {path} — {relationship}

## Focus

**Weight it toward {academic novelty / feasibility of implementation / other}.** What should come out:

1. **"Here is what existing methods can do"** — the state of the art, with actual numbers
2. **"Here is what nobody has done"** — the gap, with its search scope

{State anything that is explicitly out of scope}

## Open

{Premises that aren't filled in yet. Never fill them in by guessing}

- {…}

## How this proceeds

Follow Stage 0–4 of the `tatara` plugin.

```
0. /tatara:dr-prompt   → deep-research-prompt.md
   ✋ paste into external DR → download Markdown → deep-research-output.md
2. /tatara:sweep       → cc-research/
3. /tatara:synthesize  → synthesis.md
4. /tatara:verify      → verify/
   ✋ the human decides
```

If a technical dispute comes up, `/tatara:spike`.
