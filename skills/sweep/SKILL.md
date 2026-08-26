---
description: Stage 2. Investigate on this side, independently of the external Deep Research. Run parallel agents that each change the discovery mechanism.
argument-hint: [project directory]
disable-model-invocation: true
---

# sweep — the independent investigation on this side

> ⛏️ **Go collect the satetsu (砂鉄) — our own route.** A different place, dug a different way. What settles out has a different specific gravity.

Read `${CLAUDE_PLUGIN_ROOT}/reference/principles.md` first.

Target: $ARGUMENTS (if omitted, ask). Read its `context.md`.

**Have every agent write its artifacts in the user's language.**

## [Most important] Never break the independence

**Never read `deep-research-output.md` yourself before starting this stage.**
Write the briefs after reading it and the independence is gone, which makes the later cross-check
meaningless.

**Forbid it explicitly** for each agent as well.

> ⚠️ Never read `deep-research-output.md` or `deep-research-prompt.md`.
> Your role is to investigate independently of them.

## The split is about reach, not about which model is smarter

| | External Deep Research | This side |
|---|---|---|
| Broad web sweep | ◎ | ○ |
| **Local files** (past projects, internal memos) | ✕ | ◎ |
| **Fetching a repository and reading what's inside** | ✕ | ◎ |
| **Running code to check a number** | ✕ | ◎ |
| Course correction mid-run | ◎ | ✕ |

## The agents to stand up (add or drop them to fit the topic)

**Never repeat the same web search. Change the discovery mechanism** (Principle 7).

### a. Literature discovery along a different route
Keyword search is what the external DR is doing. Use **a different way of arriving**.

- **Citation graph traversal** — pick 2–4 seed papers and walk **2–3 hops** forward and backward
  (OpenAlex works without authentication. Semantic Scholar throws 429 easily)
- **Enter through the code** — GitHub / Papers with Code / Hugging Face.
  **Implementations that never became papers** surface here. Commercial products too
- **Work backward from the dataset** — find the papers that use that data

**Have them record which route got them there.** You evaluate how well each route worked later.

### b. Mining the local context
Related projects in the repository, past investigations, known constraints, **records of failure**.
**Information external research cannot reach in principle.**

### c. Checking data and benchmarks on the ground
Separate "the paper says so" from "you can actually get it."
**Make them actually access it.** Scale in actual numbers. If it cannot be obtained, record the
reason (404 / 403 / application required).

### d. The forward direction and adjacent fields
The reverse of the problem, or fields solving a structurally identical one.
**Whatever is called "hard" in the forward direction is a hard part in reverse too.**

## What every agent is required to do

- **Go to the primary source.** Never treat a claim from a secondary summary as fact
- **Never Read a PDF directly.** Use the HTML version. If there is no other option, check the size
  first
- Mark any bibliographic detail you cannot confirm as "unconfirmed." **Never write down a paper
  whose existence you could not confirm**
- **Never judge "whether this is novel"** (Principle 1)
- Record the terms searched and the databases used **as literal strings** (Principle 2)
- **Write a skeleton, then Edit section by section, 100–200 lines per call** (against dropped
  connections)
- Tag confidential material with 🔒 and **isolate it in its own section**. Never mix it in with
  public information

## What to record about each piece of research

Input format / **granularity of correspondence** (what gets matched to what) / scope it handles /
methodological framework / **evaluation and actual numbers** / source /
**the limitations the authors wrote themselves (quoted verbatim)**

## Where it goes

**A separate file per agent** under `cc-research/`. This avoids conflicts.

## When you're done

If the external Deep Research results are in, next is `/tatara:synthesize`.
