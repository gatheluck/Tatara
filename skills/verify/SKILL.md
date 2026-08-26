---
description: Stage 4. Go break the gaps and retrieve the primary sources nobody read. A gap that breaks is a success. Only what survives becomes a claim.
argument-hint: [project directory]
disable-model-invocation: true
---

# verify — go break the gap

> 🔨 **Break the kera (鉧).** Hammer it apart and sort it into tamahagane (玉鋼) and slag.
> **Breaking is the process, not a failure.**

Read `${CLAUDE_PLUGIN_ROOT}/reference/principles.md` first.

Target: $ARGUMENTS (ask if omitted). Read `synthesis.md` and `synthesis/S4-*.md`.

**Write in the user's language.** Instruct every agent to do the same.

## What this stage is for

**Find out whether the gap is real. If it breaks, that's a success.**

Every break makes the claim more specific and moves its support from your own judgment to
**someone else's words**.
A gap that broke a few times and survived is **stronger than one that was never attacked**
(Principle 11).

## What to launch

### 1. Break the gap (the main assault)

**Make finding something the goal.** Not "confirm that it isn't there."

- **Never let them reuse Stage 3's queries.** Those only return the same results
- Search with **different vocabulary, a different database, the name another field uses**
- Vary the verb too (transfer / propagate / migrate / lift / associate / link / bind / ground …)

> ⚠️ **Clever paraphrases usually don't work** (measured).
> Plain, direct words against **a different database** hit more often. Don't sink time into
> vocabulary search.

**What this looked like in practice.** On the first real run, a list of eight "clever" alternative
terms was prepared in advance — borrowed jargon from adjacent fields, inverted phrasings, the
abstract name for the same relation. **Every one came back empty.**

What hit was a plain conjunction of the words a practitioner would actually use to describe the
problem, run against a database the earlier stages had never touched.

**Budget accordingly: one pass on vocabulary, then spend the rest on new databases.**

If the coverage matrix left **work you couldn't place**, pin it down with a primary source.
Placing it fills a gap.

### 2. The territory nobody searched

What S4 listed. In particular:

- **Patents** — a technique with no paper behind it but a shipping product feature is in the
  patents. But Espacenet / J-PlatPat / WIPO often **can't be used with static fetching**.
  Google Patents **IP-blocks after a dozen-odd queries**. **Test one representative target first**
- **Non-English literature** — sometimes it surfaces from nothing more than confirming a term
  exists. An era that looks thin in English can be the thickest one in another language
- Standards documents, dissertations, corporate technical journals

### 3. Retrieve the primary sources nobody read ★top priority

**The ones where only the number gets quoted and the body was never read.** Until these are
resolved, the state-of-the-art table isn't final.

Pin down:
- **What data that number was measured on — synthetic or real** (Principle 8)
- The preconditions (what is given as input)
- **The limitations the authors wrote themselves** (verbatim quote)

For paywalls, work through "Retrieval routes that have actually worked" in `principles.md`.
**Several documents reported as "all routes failed" were retrieved through a different one.**

### 4. Mechanical checking

The things settled by collation rather than by argument.

| Target | How |
|---|---|
| Citation | Does it exist, and does its content match the claim — compare verbatim |
| Code | Actually run it |
| Numbers | Re-run and regenerate them |
| Contradictions | Pin them down with a primary source |

**If a technical dispute is still open, `/tatara:spike`. Argument won't settle it.**

## What every agent is held to

- **Make finding something the goal, but never write down that a thing exists when it doesn't**
- Record every term searched and every database, **as literal strings, all of them** (you need this
  to claim a gap at all)
- If it couldn't be retrieved, write "**not retrievable**" **with the result for each route**.
  Never fill the hole in by guessing
- **State item by item whether the body was read or only the abstract** (Principle 3)
- **WebSearch runs out at 200 calls.** Narrow the target on the hard ones
- **Write a skeleton, then Edit to append, 100 lines per call**

## Where the output goes

One file per agent under `verify/`.

## When you're done

**Update `synthesis.md`.** Move the gaps that broke into the corrections record, and rewrite what
survived as the claim.

**Record the fact that the claim was rewritten.** Make it clear which revision this is.

Then **the human decides.** The direction of the research does not get settled here.
