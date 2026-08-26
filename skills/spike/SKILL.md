---
description: Settle a technical dispute by executing rather than arguing. Write the smallest code that decides it, hit it, and leave the result in a file.
argument-hint: <the dispute to settle>
disable-model-invocation: true
---

# spike — settle it by running it

> ⚡ **Read the flame.** What discussion won't decide, fire it and find out.

Read `${CLAUDE_PLUGIN_ROOT}/reference/principles.md` first.

Dispute: $ARGUMENTS

**Write in the user's language.**

## When to use this

**When the argument is split, and running it would tell you.**

Typical situations:
- Sources conflict, and one side is inference while the other is a primary source
- "Impossible in principle" versus "just being thrown away"
- **What you can actually get out of** some API or library is the premise of the argument

Measurement beats opinion. **One primary source can outweigh a majority holding an inference.**

## Procedure

### 1. Narrow the dispute to a single point

**If you can't narrow it, you aren't at the spike stage yet.**

Not "is this hard," but "**can X be obtained from Y**."
Drop whatever the parties already agree on (that it's many-to-one, say) out of the dispute.

Write the narrowed dispute down first, along with the **nature of the evidence** on each side
(primary source / measurement / inference).

### 2. Build the smallest reproduction

- **Isolate the environment** (conda env / venv / a temp directory). It has to be undoable by deletion
- If dependencies need installing, **estimate the size and check with the user**
- Keep the test subject **minimal** — but it has to **actually touch the dispute**
  (if the dispute is about the hard case, a test input that only covers the easy case proves nothing)

### 3. Introspect the API

Assume nothing. Have it enumerate **what is actually exposed**.
Documentation and binary do diverge. **The local `--help` / `dir()` is the authority.**

### 4. Hit it

Try several routes. **Never skip the rest because one went through** (an early `break` makes you
miss things).

### 5. Distrust your own measurement

**The biggest failure of a spike is the measurement itself being wrong.**

Real cases:
- Matching at distance zero → **adjacent elements that merely touch also come out at distance
  zero.** The definition of a match was too loose
- Duplicate enumeration of elements → candidates always came out in pairs
- Assuming a method name (`Extent()` vs `Size()`) → wrongly displayed as "couldn't retrieve it"
- Wrong number of arguments, so `TypeError` → misjudged as "that API doesn't exist"

**If a result looks off, suspect your own code first.**
Suspect it hardest when the result came out convenient.

### 6. Record it

Write the result under `verify/`. **Keep every version of the script** (so the trail of the errors
stays readable).

Always write:

- **The dispute, and the nature of the evidence on each side**
- **The measured values** (as numbers. Not "it worked," but how many out of how many)
- **The verdict** — which side was right. **Both can be partly right**
- **The limits of this spike** — one test shape? one set of conditions? what wasn't tried?
- **The errors you made** — what you got wrong, how, and how it came to light

## Guarding against over-reading

- **Never generalize from a measurement taken under one condition.** State what you didn't try
- **Read the old literature in that field** (Principle 3).
  What you "discovered" may have been written down decades ago.
  A spike's contribution is usually limited to "**how it is exposed in today's tools**"

## When you're done

Move the corresponding contradiction in `synthesis.md` to "settled."
**Leave whatever didn't get settled under open.** Never blur it.
