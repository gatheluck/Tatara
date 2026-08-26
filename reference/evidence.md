# 📚 evidence — the grounds for each principle

> What the eleven principles of **Tatara (鑪)** actually rest on. **Citations and measurements, not
> general reasoning.**

Each principle in [`principles.md`](principles.md) is backed by published empirical research (with
arXiv IDs) and by numbers measured in real operation. **The grounds are all written down so that the
principles can be discarded when the situation changes.**

---

## Empirical research

### LLM ideas look novel, and lose ground once executed

- **[arXiv:2409.04109](https://arxiv.org/abs/2409.04109)** (Si, Yang, Hashimoto; accepted at ICLR
  2025). Blind review by 100+ NLP researchers. **LLM ideas score significantly higher on novelty**
  (4.84 → 5.64, p<0.01). **No significant difference on feasibility** (p=1.00 / 0.36)
- **[arXiv:2506.20803](https://arxiv.org/abs/2506.20803)** (Ideation-Execution Gap).
  43 people spent **100+ hours each** implementing → **only the AI-generated ideas dropped
  significantly** (overall −1.976), and the gap disappeared. Human-generated ideas barely moved
  (within ±0.08)

→ **Principle 9** (don't select on excitement).
For AI-generated ideas, excitement at conception is **negatively correlated** with the post-execution
score (r=−0.321, ρ=−0.386).

### LLM self-evaluation does not work

From the same paper: the best pairwise judge reaches balanced accuracy **53.3%**, below the 56.1%
agreement between human reviewers. The AI Scientist's reviewer sits at **43.3% — worse than random**.

→ **Principles 1, 4, 5**.

### Scaling generation does not buy diversity

**200 non-duplicates out of 4000 seeds (5%)** — and that was with an explicit instruction to avoid
duplicates.

- **arXiv:2605.08956**: models from independent providers converge semantically.
  *"querying multiple AI systems... is effectively sampling from a single model"*
- **arXiv:2606.08251** (~6,749 scientists, 25,139 evaluation sets):
  **no model proposes a null hypothesis on its own**

→ **Principle 7** (route over vocabulary), **Principle 10** (yield).

### Scaffolding contributes little

**arXiv:2604.18805** (8 domains, 25,000+ agent runs):
of the variance, **41.4% is the base model and 1.5% is the scaffold**.
*"scaffold engineering alone cannot repair them."*
The same paper finds that **evidence is ignored in 68% of traces**.

→ **Don't over-engineer the tooling. Spend the complexity on mechanical verification.**

### LLM judging cannot measure quality

| Source | Finding |
|---|---|
| ChemCrow (*Nature MI* 2024) | LLM judges prefer a **fluent error** over a grounded correct answer |
| Agent Laboratory (arXiv:2501.04227) | The automated reviewer runs **+2.3 points** more generous than humans and does not predict human scores |
| AI-Researcher (arXiv:2505.18705) | **68 points** of spread between judges on the same paper |
| BadScientist (ACL 2026) | **Fabricated papers with zero experiments** are accepted **52–82%** of the time |
| Dycke & Gurevych (arXiv:2508.21422) | Injected logical flaws have **no significant effect** on automated review |

→ **Principle 4**.

### Automated novelty judgment fails

- Beel et al. (SIGIR Forum 2025, the only independent reproduction of the AI Scientist):
  the novelty check **misclassified all 12 proposals as "novel"**
- HindSight: **LLM-judged novelty is negatively correlated with real impact** (ρ=−0.29)
- Dolphin (ACL 2025): the novelty judgment is made by **the same model that did the generating**
  (circular)
- AutoResearchBench: even the best-performing model finds only **9.39% of the literature**

→ **Principles 1, 2**. **A search that surfaces 9% of the literature cannot support "nobody has
done this."**

### Artifacts hide inside the verification loop

**AI CUDA Engineer** (Sakana AI, 2025-02). The 10–100× headline turned out to be an artifact of the
system **exploiting its own evaluation harness**.
Independent reproduction (EvoEngineer, arXiv:2510.03760): on the public data, **1.13× → 0.82×**,
successes **63 → 22**. Re-run correctly, the median is **1.10–1.19×**.
**The catch came from outside within 48 hours, not from the lab's internal review.**

→ **Principle 5**.

### Agents win the short horizon, humans the long one

**RE-Bench** (METR, arXiv:2411.15114):
at 2 hours agents are **4×** humans → the lines cross at 8 hours → **at 32 hours humans are 2×**.
Cost: $123 for the agent versus $1,855 for the human.

### Nearly half of adversarial review findings miss

Measured on **adversarial-loop**: 5–15 actionable findings per 3 iterations, **40–70% confirmation
rate**.
→ "Review, then fix everything" is wrong. **Triage → verify → fix.**

### The actual yield numbers

| Source | Number |
|---|---|
| Carl (Autoscience) | **10%** of ideas are promising; **7%** are implemented correctly on the first attempt after green-light |
| Dolphin | **5–6 of 40** proposals improve anything; roughly **50%** are never even executed |
| Beel et al. | **42%** of experiments fail on coding errors; **57%** of manuscripts contain hallucinated results |

→ **Principle 10**.

### Hallucinated citations are real

- **arXiv:2605.07723** (authors include arXiv founder Ginsparg): an audit of 111 million references
  across 2.5 million papers. **146,932 hallucinated citations in 2025 alone**
- **arXiv:2607.00738**: roughly **1 in 20** NeurIPS / USENIX papers from 2025 contains two or more
  hallucinated references. **Verification costs about $0.04 per paper**

→ **Principle 4** (verbatim citation checking is cheap; there is no reason to skip it).

---

## Measured in operation (2026-08, first application)

The subject was a cross-modal correspondence problem. 14 agents plus a
spike, 9,623 lines of artifacts.

### Running the two routes independently

**Exactly one paper overlapped as directly relevant work.**

| Origin | Lines (of 143) |
|---|---|
| DR only | 8 |
| CC only | 126 |
| Both | 9 |

**Count and value do not track each other.** DR contributed 8 lines, but two of them were the most
directly relevant work found in the entire investigation.

**The channels had different strengths** — DR found papers behind subscriptions, CC found open data.

→ **Principle 6**.

### The effect of changing the discovery mechanism

On "section views," DR used **the right terms and returned nothing**.
CC started from the README of a GitHub repository with no associated paper (★10), followed the
citation graph, and reached **12 hits**.

Meanwhile the **clever alternative vocabulary struck out entirely**
(borrowed jargon from adjacent fields, inverted phrasings, abstract names for the same relation).
What worked was a plain conjunction of the words a practitioner would use for the problem.

→ **Principle 7**.

### Building structure out of abstracts, and getting it wrong

Working from the wording of two abstracts, the agent reported detecting "a 26-year-old dispute about
granularity," then placed its own spike measurements in that context and declared it had "settled the
dispute empirically."

**After reading 8 full texts:**
- **There was no dispute.** A table in one of the papers explicitly calls the two approaches
  "complementary," and no direct controversy exists in the literature
- One of the two "words in the abstract" is a different word in the body
- **And the thing it measured was already written out in the body of a 1996 survey**

→ **Principle 3**. **This single error was the most expensive one.**

### The gap was rewritten three times

| Version | Claim | How it broke |
|---|---|---|
| 1 | Nobody has worked at this granularity | **Destroyed.** 15 years of work in another language, and **upstream** of a lineage we already knew |
| 2 | No work discovers correspondences when none are given | Partially survived |
| 3 | No one has solved the inverse problem | **The author of the nearest prior work states outright that it is "difficult, with no good solution at present"** |

**The support moved from my own judgment to someone else's words.**

→ **Principle 11**.

### The spike exposed five of my own errors

Mismatches at zero distance / double-counted elements / an early `break` / a wrong method name / the
wrong number of arguments.

**Each one surfaced on a run, one per run. The discussion found none of them.**

### Operational constraints

- **Four connection drops.** Every one of them while writing out a long file after the research was
  already finished
- **WebSearch runs out at 200 calls per agent.** A working detour got cut off mid-way
- **Some of the planned search targets turned out to be unusable.** Espacenet / J-PlatPat / WIPO
  cannot be fetched statically, and Google Patents IP-blocked us after 17 queries
- **An agent that returned a single line burned 49,271 tokens** (all preamble). That said, agents
  with matching shapes inside the same run share the prompt cache

### Retrieval routes that worked

- **Google Books snippet search** — Springer CCIS volumes. Broke through on a paper reported as
  unreachable by every other route. **Returned body text verbatim, with page numbers**
- **Take the WAF cookie first, then hit the PDF link directly** — for sites reported as "an empty JS
  shell"
- **Publicly-funded project sites** (searched in the local language), and co-author companies' press
  material
- **Rendering institutional-repository scans to image and reading them** (4 of 8)
