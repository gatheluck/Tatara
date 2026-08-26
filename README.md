<div align="center">

# 🔥 Tatara 鑪

**Smelt the scattered literature down to two things: where the field actually stands, and where nobody has been.**

A plugin for Claude Code.

</div>

---

## ⚒️ Why "Tatara"?

**Tatara (鑪)** is the traditional Japanese iron smelting process. You load a clay furnace with
*satetsu* (砂鉄, iron sand) and charcoal, and keep it burning for three days and three nights.
What comes out is **tamahagane (玉鋼)** — the steel that becomes the cutting edge of a Japanese sword.

The role this tool plays for research is the role tatara plays for the sword.

> **Tatara is not the forging. It is the step before forging, the one that makes the material.**
> And the quality of the blade is capped by the quality of the tamahagane you got here.

Research works the same way. The experiments and the writing come later, but **what question you
ask** is decided here — and how good that question is depends on how accurately you read the
terrain at this stage.

### The stages map one to one

| Tatara 🔥 | This tool |
|---|---|
| **Kanna-nagashi (鉄穴流し)** — break down the hillside, sluice it through channels, and let **specific gravity separate out the iron sand** | **Stage 1–2** — sweep along two independent routes, keep only primary sources |
| **Load the furnace** — iron sand and charcoal, three days and three nights | **Stage 3** — cross-check the two sweeps into a state-of-the-art table and a coverage matrix |
| **The murage (村下) reads the color of the flame** | **The human decision point.** Not delegated to a machine |
| **Break the kera (鉧)** — sort the bloom into tamahagane, iron, and slag | **Stage 4** — go break your own gap claim, and **keep only what survives** |
| Only a fraction of the bloom is usable as tamahagane | **Yield is around 10%** (→ Principle 10) |

**Throwing away slag is not failure. It is the process.**
Here too, a gap claim that collapses is a success (→ Principle 11).

### 📔 Glossary

Japanese terms are kept in romanization with the kanji, rather than translated — translating them
erases where the metaphor comes from.

| Term | Kanji | What it is |
|---|---|---|
| **tatara** | 鑪 | The traditional Japanese iron smelting furnace, and the process run in it |
| **satetsu** | 砂鉄 | Iron sand. The raw input, scattered through ordinary hillside soil |
| **kanna-nagashi** | 鉄穴流し | Sluicing the hillside through water channels so specific gravity separates the iron sand out |
| **kera** | 鉧 | The bloom — the mass pulled from the furnace at the end of a run |
| **tamahagane** | 玉鋼 | The highest grade of steel sorted out of the kera. Becomes the cutting edge of a sword |
| **murage** | 村下 | The master smelter, who judges the furnace by the color of the flame |
| **abumi** | 鐙 | A stirrup. The author's other project, named for the tool that lets a rider stand firm |

### 🐎 Relationship to Abumi

The author's other project, **Abumi (鐙)**, is an always-on agent harness. An *abumi* is a stirrup —
forged iron tack, the thing that **lets a rider stand firm**.

> **Tatara makes the material. Abumi lets you stand.**

The dependency between the tools runs the same way. **Scope the research with Tatara, then run it
with Abumi.**

---

## 📖 Contents

- [🎯 What this is for](#-what-this-is-for)
- [📦 Install](#-install)
- [🚀 Quickstart](#-quickstart)
- [📂 **Where the output accumulates**](#-where-the-output-accumulates) ← read this first in practice
- [🛠️ The skills](#️-the-skills)
- [📐 Why it is built this way](#-why-it-is-built-this-way)
- [🩹 Troubleshooting](#-troubleshooting)

---

## 🎯 What this is for

There are only two outputs.

| Output | What it is |
|---|---|
| 📊 **"Here is what existing methods can do"** | The state of the art, with actual numbers |
| 🕳️ **"Here is what nobody has done"** | The gap, with the search scope that backs it |

### ✅ Good fit

- Starting a new research topic and needing to **map where the field actually stands**
- Wanting to check "has someone already done this?" **in a form that leaves a record**, not an impression
- Writing up novelty or positioning **so that a reader can falsify it later**

### ❌ Bad fit

- The implementation itself (this tool stops at settling the topic)
- One-off fact lookups (just search)
- Questions with a single determinate answer

### 🧭 What this tool refuses to do

**It never asks a model whether something is novel.**
"Is this novel?" is a claim of absence, and absence cannot be verified. Instead it asks
**"What is the closest existing work, and exactly how does it differ?"**
The output becomes a **citation** rather than a judgment, and a reader can go check it.

**Every gap claim carries its search scope.**
Not "nobody has done this," but
**"Not found across A, B, and C as of YYYY-MM-DD. The closest is X."**

**It goes after its own gap claims.**
Stage 4's job is to destroy your claim. Each time one breaks, the claim gets more specific and its
support **moves from your own judgment to someone else's words**.

---

## 📦 Install

### 🧪 Try it

```bash
claude --plugin-dir /path/to/tatara
```

After it starts, open `/help` → **Custom commands**. Six entries under `tatara:` means you're set 🎉

### 🏠 Keep it

Drop it under `~/.claude/skills/` and it loads automatically from the next session.

```bash
git clone <this-repo> ~/.claude/skills/tatara
```

For a team, distribute through a
[plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces).

Run `/reload-plugins` after editing.

> 🌏 **Language.** The skills are written in English, but they instruct agents to write in
> **your** language. Talk to Claude in Japanese and the artifacts come out in Japanese.

---

## 🚀 Quickstart

Start Claude Code **in your research repository** (where the output lives — see the next section):

### 1️⃣ Build the furnace

```
/tatara:init differentiable solvers for fluid simulation
```

Creates `tamahagane/2026-08-25-differentiable-fluid-solvers/` and a `context.md`.
It will ask about anything load-bearing that's missing.

### 2️⃣ Gather iron sand (external Deep Research)

```
/tatara:dr-prompt
```

Produces `deep-research-prompt.md`. **Paste the prompt body into ChatGPT (or similar)**, then
**download the result as Markdown** and save it to `deep-research-output.md` unedited.

> 💡 This is the only manual step. External Deep Research is UI-only.

### 3️⃣ Gather along a different route

```
/tatara:sweep
```

**You can start this without waiting for the external run to finish.** In fact you *should* start
it before reading those results — that's what keeps the two routes independent.

### 4️⃣ Load the furnace

```
/tatara:synthesize
```

Cross-checks both sides into `synthesis.md` — the state-of-the-art table and the coverage matrix.

### 5️⃣ Break the kera

```
/tatara:verify
```

**Goes after the gap.** Patents, non-English literature, primary sources nobody actually read —
whatever it takes to find out if "nobody has done this" holds up.

### 🔨 Any time: settle it by running it

```
/tatara:spike does the tokenizer's offset mapping survive normalization?
```

Takes a technical dispute and settles it with the smallest program that decides it.

---

## 📂 Where the output accumulates

### 🚫 Nothing accumulates in this repository

**This repo holds the tool only.** Research artifacts are created **in whichever repository you
started Claude Code in.**

As a guard, this repo's `.gitignore` excludes `tamahagane/` and `projects/`. If you slip and work here, the artifacts
don't contaminate the tool.

### 🗂️ Expected layout

```
~/your-workspace/
├── tatara/                      🔥 the tool (safe to publish)
│   ├── skills/
│   ├── reference/
│   └── templates/
│
└── tamahagane/                  📚 the artifacts (keep this one private)
    ├── 2026-08-25-differentiable-fluid-solvers/
    ├── 2026-09-10-long-context-retrieval-eval/
    └── 2026-10-02-sparse-moe-routing/
```

**Point it wherever you like.** `init` resolves the location in this order and stops at the first
one that yields a path:

| # | Source | Notes |
|---|---|---|
| 1 | `${user_config.tamahagane_path}` | Prompted at plugin-enable time. **Only works for an installed plugin** — see the warning |
| 2 | `~/.claude/tatara.json` → `tamahagane_path` | **The one that always works.** Recommended |
| 3 | `.tatara.json` in the current repository | Per-workspace override |
| 4 | Ask, then offer to save the answer to `~/.claude/tatara.json` | So it is only asked once |

```json
{
  "tamahagane_path": "/absolute/path/to/tamahagane"
}
```

> ⚠️ **`${user_config.*}` does not work with `--plugin-dir`.**
> That flag loads the plugin for a single session without installing it, so there is no plugin ID
> and the config has nowhere to live. Skills still load fine; only the substitution is absent.
> **Use `~/.claude/tatara.json` instead.**
>
> Related trap: `pluginConfigs` is read only from managed settings, `--settings`, and **user**
> settings. Anything written to a project's `.claude/settings.json` is **silently ignored** — a
> deliberate guard against repository-borne injection. `enabledPlugins` *is* honored at project
> scope, so the asymmetry is easy to trip over.

> 🧷 **`tamahagane_path` deliberately has no `default` in `plugin.json`.**
> A default would make source 1 always return a value, which would shadow sources 2–4 and break
> the chain. Leave it undeclared.

The name comes from what a tatara run actually produces. If you point it at a repository that
already uses a `projects/` subdirectory, that convention is followed instead.

### 📁 Inside one project

Each project is **self-contained**.

```
tamahagane/YYYY-MM-DD-{slug}/
├── context.md                  problem, focus, open questions
├── deep-research-prompt.md     Stage 0. Never edited after sending (reproducibility record)
├── deep-research-output.md     Stage 1. Saved verbatim
├── cc-research/                Stage 2. One file per agent
├── synthesis/                  Stage 3. One file per cross-check dimension
├── synthesis.md                ⭐ the deliverable: state of the art + gaps + open + corrections
├── verify/                     Stage 4. Gap attacks, primary-source retrieval, spikes
│   └── spike_*.py                every version of a spike script is kept
├── plan.md                     research plan, once the topic settles
└── worklog.md                  what happened at each stage, and why
```

> 📖 **You only need to read `synthesis.md`.**
> A project runs 5,000–10,000 lines, but the part you read is about 300.
> The rest is there for when you want to trace a claim back to its source.

### 🔗 Why keep all projects in one place

**Topics stored in the same tamahagane directory can be read by later topics.**

Stage 2 includes an agent whose job is mining local context — it **goes through the other projects
in the same repository**. External Deep Research cannot do this in principle, and it **gets more
valuable as you accumulate**.

On the first real run, that agent surfaced:

- that the topic was **already an official research objective of the organization**
- that an **internal benchmark already contained the exact task**, with measured numbers
- technical constraints already established on the forward direction of the same problem
- **23 recorded failures**

→ The design implication: **keep the artifacts together in one repository.**

### 🔒 Confidential material

Stage 2's local mining **picks up things that cannot leave the building.**

- Every skill instructs agents to tag such items with **🔒** and **isolate them in a separate section**
- `synthesis.md` keeps §1–§3 public-only, with confidential material quarantined
- ⚠️ **Do not make the artifact repository public.** If you must, build a step that mechanically
  strips 🔒 sections first

**The tool itself contains nothing confidential.** Only this side is safe to publish.

---

## 🛠️ The skills

| Skill | Stage | What it does | Manual work |
|---|---|---|---|
| 🌱 `init` | — | Scaffold the project. Ask about missing premises | answer questions |
| 📝 `dr-prompt` | 0 | Generate the prompt for external Deep Research | **paste and save** |
| ⛏️ `sweep` | 2 | Investigate independently on this side (parallel agents) | none |
| 🔥 `synthesize` | 3 | Cross-check → state-of-the-art table + coverage matrix | none |
| 🔨 `verify` | 4 | **Go break the gap.** Retrieve unread primary sources | none |
| ⚡ `spike` | any | Settle a technical dispute **by executing** | approve installs |

### ❓ Why separate stages?

Claude Code's dynamic workflows **cannot take user input mid-run**. Per the official docs: "For
sign-off between stages, run each stage as its own workflow." This isn't a preference — it's a
constraint.

---

## 📐 Why it is built this way

**The tool is deliberately thin.** 470 lines of skills, 121 lines of principles.

The reason is measured.

> Of the explained variance in performance and behavior, **the base model accounts for 41.4% and
> the scaffold for 1.5%**
> — arXiv:2604.18805 (8 domains, 25,000+ agent runs)

Elaborate procedure buys you the 1.5% side. So **the complexity budget goes entirely into mechanical
checking** instead. The same paper reports that **evidence is ignored in 68% of traces** — that gap
only closes when a machine is made to do the cross-checking.

### 📜 Eleven principles at the center

[`reference/principles.md`](reference/principles.md)

| # | Principle |
|---|---|
| 1 | **Never ask a model whether something is novel** — ask for the closest work and the exact difference |
| 2 | **Every gap claim carries its search scope** — literal queries, databases, date, nearest hit |
| 3 | **Never build a structural claim out of abstracts** — the most expensive mistake |
| 4 | **Never let an LLM judge quality** — only things that can be checked |
| 5 | **Keep the verifier outside the generator** |
| 6 | **Run two routes independently; neither one's conclusion is final alone** |
| 7 | **Change the route, not the vocabulary** |
| 8 | **Every number carries its provenance** — synthetic or real |
| 9 | **Never select on excitement** — select on `cost-to-test` |
| 10 | **Assume ~10% yield when deciding how many candidates to raise** |
| 11 | **A gap claim breaking is a success** |

Each one is backed in [`reference/evidence.md`](reference/evidence.md), with **citations (arXiv IDs)
and measured numbers**. The grounds are written out so that you can decide a principle is obsolete
when the situation changes.

### 🧪 Track record

**Run 1**: a cross-modal correspondence problem (2026-08).
14 agents plus 4 spike iterations, 9,623 lines of artifacts.

- 🔨 The gap claim was **rewritten three times**, ending up supported by **the closest prior work's
  own author saying the problem was unsolved**
- ⚡ The spike surfaced **five of my own errors** (**zero were found by discussion**)
- 🔀 The two independent routes overlapped on **exactly one paper**. Either alone would have missed most of it
- 📋 **Ten errors recorded**, two of them violations of Principle 3 (structure built from abstracts)

---

## 🩹 Troubleshooting

<details>
<summary><b>The skills don't show up</b></summary>

Run `/reload-plugins`. If that doesn't do it, run `claude plugin validate <path>`.
Check that `skills/` and friends are **not** inside `.claude-plugin/` — they belong at the plugin root.
</details>

<details>
<summary><b>An agent dies while writing a long file</b></summary>

Known. Every skill already requires "Write a skeleton, then Edit section by section," and it still
happens. **Don't re-run the research — resume with `SendMessage` so the transcript survives.**
Only the output was lost; the findings are still in the agent.
</details>

<details>
<summary><b>Search stops working partway through</b></summary>

WebSearch runs out at 200 calls per agent. Split hard targets across several narrowly-scoped agents.
</details>

<details>
<summary><b>Patent databases are unreachable</b></summary>

Espacenet, J-PlatPat, and WIPO Patentscope don't work with static fetching.
Google Patents IP-blocks after roughly a dozen queries.
**A browser usually gets through**, so grabbing the one decisive document by hand is faster.
</details>

<details>
<summary><b>A paywall is blocking the full text</b></summary>

[`reference/principles.md`](reference/principles.md) has a section of retrieval routes that have
actually worked (Google Books snippet search, taking the WAF cookie before hitting the PDF, and
others). **Several documents reported as "all routes failed" were retrieved through a different one.**
</details>

---

<div align="center">

**MIT License**

🔥 *satetsu* (砂鉄) → *tamahagane* (玉鋼) 🗡️

<sub>from iron sand to sword steel</sub>

</div>
