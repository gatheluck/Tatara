# 🔥 principles — what every skill follows

> The core of **Tatara (鑪)**. The skills are thin. **These eleven are the substance.**

**Grounded in empirical research and measured operation.** Citations in [`evidence.md`](evidence.md).
If you can't follow one, write down why in the artifact.

---

## 1. Never ask a model whether something is novel

**Do not ask "is this novel?"**
Ask instead: **"What is the closest existing work, and exactly how does it differ?"**

- "This is novel" → a claim of absence. Unverifiable
- "The closest is X, and the difference is Y" → **verifiable**. Read X and check

The output becomes a **citation** rather than a judgment.

## 2. Every gap claim carries its search scope

A claim of absence only means something once its boundary is drawn. If the following are missing,
the gap doesn't count.

| Record | Example |
|---|---|
| What you searched for | **the literal query strings** |
| Where you searched | database names (arXiv / OpenAlex / patents / J-STAGE / …) |
| As of when | retrieval date |
| The nearest hit | the paper, and why it is "close but different" |

Write it as: **"Not found across A, B, and C as of YYYY-MM-DD. The closest is X."**
Never "nobody has done this."

## 3. Never build a structural claim out of abstracts

**This is the most expensive mistake available.**

- Anything taken from an abstract is only "the abstract says X" — claim no more than that
- **Structural claims — disputes, lineages, gaps — wait until you have read the full text**
- A single word in an abstract is not the author's position. **The body often uses a different word**
- Before judging your own measurement "novel," **read the old literature in that field**

## 4. Never let an LLM judge quality

Do not use it as an accept/reject gate. Only things that can be **checked**:

- does the citation exist (verbatim comparison)
- does the code run
- do the numbers reproduce

## 5. Keep the verifier outside the generator

You can only say "verified" when **the means of verification sits outside the thing that generated
the claim**. Artifacts hide inside a system's own verification loop.

## 6. Run two routes independently; neither one's conclusion is final alone

Run external Deep Research and your own agent sweep **without letting either see the other.**
**Until they are cross-checked, neither conclusion is settled.**

Disagreement carries the most information. Sort into four buckets:

| Bucket | Meaning |
|---|---|
| Agreement | both say the same thing. Higher confidence |
| **Contradiction** | they conflict. **Needs resolution. Most informative** |
| One side only | may be an artifact of asymmetric access |
| **Gap** | neither answers it |

## 7. Change the route, not the vocabulary

**Clever paraphrases don't work.** Plain words against a **different database** hit more often.
Change the discovery mechanism itself: citation graphs, code, dataset back-references, patents,
non-English sources.

## 8. Every number carries its provenance

**Never mix numbers measured on synthetic data with numbers measured on real data.**
Put a provenance column in the table. If you can't determine it, write **"unknown."**

## 9. Never select on excitement

How exciting an idea feels at conception is **negatively correlated** with how it scores after
execution. Select on `cost-to-test` — the cheapest step that would verify it.
**Impose it at selection time, not at ideation time.**

## 10. Assume ~10% yield when deciding how many candidates to raise

Measured: ~10% of ideas are promising, ~7% are implemented correctly on the first attempt,
5–6 out of 40 ideas improve anything, 42% of experiments fail on coding errors.

**If you only raise three candidates, zero or one will survive.**

## 11. A gap claim breaking is a success

Gap claims are supposed to get rewritten. **Each break makes the claim more specific and moves its
support from your own judgment to someone else's words.**

A gap that survived several attacks is stronger than one that was never attacked.

---

## Operational constraints (measured)

- **Connections drop while writing long files in one shot.** Require every agent to
  "Write a skeleton, then Edit section by section, 100–200 lines per call"
- If one dies, **resume it with the transcript intact. Do not make it redo the research**
  (you pay for it twice)
- **Subagents see none of the parent conversation or its files.** Briefs must stand alone
- **After compaction, files over 5,000 tokens lose their body** and become a path reference.
  Split long inputs across subagents by section
- **WebSearch runs out at 200 calls per agent.** Split hard targets across several agents
- **Check retrievability before committing to a search plan.** Hit one representative target first

## Retrieval routes that have actually worked

| Route | Where it helps |
|---|---|
| **Google Books snippet search** | Springer LNCS/CCIS volumes. Returns **body text verbatim with page numbers** |
| **Take the WAF cookie first, then hit the PDF directly** | Sites that look like an empty JS shell |
| **Publicly-funded project sites** | Often obligated to publish results. **Search in the local language** |
| Co-author's company press material | Companies sometimes post the English full text for free |
| Institutional repository scans | Even without a text layer, **render to image and read it** |
| A citing paper's description | When the original is unreachable. **Always label it as second-hand** |

**Never Read a PDF directly.** Check size with `curl -sI` first.

---

## Language

Skills and reference material are written in English so the tool is portable.
**Artifacts are written in the user's language** — every skill instructs agents accordingly.
Talk to Claude in Japanese and `synthesis.md` comes out in Japanese.

Japanese terms that name the tool's own metaphor are kept in romanization with the kanji on first
use — *tatara* (鑪), *tamahagane* (玉鋼), *kera* (鉧), *kanna-nagashi* (鉄穴流し), *murage* (村下).
Translating them would erase where the metaphor comes from.
