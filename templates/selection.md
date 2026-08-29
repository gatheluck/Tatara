# selection — {topic}

**Written {date}. Revision {N}.** The deliverable for a **selection** track.

Material: {N} external Deep Research runs + {N} agents.

> This is a decision, not a survey. A survey maps the field; this picks one and says why.
> If you find yourself writing "the strengths are X and the weaknesses are Y" with no numbers
> attached, you are writing a survey. Stop and get the numbers.

## How to read this

- **§0 The decision** — what to use, in one line
- **§1 Candidates** — everything considered, and why the rest were dropped
- **§2 The comparison** — the table the decision rests on
- **§3 Fit to our situation** — the part external research cannot produce
- **§4 What would reverse this** — the conditions under which we pick differently
- **§5 What we could not check** — honest holes

**Numbers carry a provenance column.** A figure measured on a public benchmark is not a prediction
about our data.

🔒 = confidential.

---

# §0 The decision

**Use {X}.**

{Two or three sentences. The reason, and the single biggest thing being given up.}

Runner-up: {Y}, because {…}. It becomes the choice if {condition}.

---

# §1 Candidates

Everything that was considered. **Include the ones ruled out** — a reader needs to know they were
looked at, and the next person needs to know not to re-litigate them.

| Candidate | Year | Status | Why ruled in / out |
|---|---|---|---|
| | | shortlisted / ruled out | |

**Search scope** — how the candidate list was assembled, so a reader can judge whether it is
complete: {databases, queries, code hosts, date}.

---

# §2 The comparison

| Candidate | Input format | Pretraining | Reported value | **Provenance** | **Code** | **Runs on our data** | Blocker |
|---|---|---|---|---|---|---|---|
| | B-Rep / mesh / point cloud / … | self-supervised? scale? | the actual number | ✅ real / ⚗️ synthetic / ⚠️ unknown | link, licence, last commit | yes / no / untested | |

**Every column earns its place:**

| Column | What it decides |
|---|---|
| **Input format** | A method that consumes something we do not have is not a candidate, whatever it scores |
| **Pretraining** | Whether it can exploit the data we actually hold |
| **Reported value** | Adjectives do not compare. Numbers do |
| **Provenance** | A public-benchmark number is not a claim about our data |
| **Code** | A method you cannot run is a paper, not an option. Licence and last commit both matter |
| **Runs on our data** | The only column that is about us. Mark it **untested** rather than guessing |
| **Blocker** | The thing that would stop adoption, stated plainly |

> ⚠️ **`untested` is a legitimate value and must be used.** Writing `yes` on a method nobody ran is
> how a selection turns into a wish.

---

# §3 Fit to our situation

**The part external research cannot produce.** Draw it from local context: prior projects,
internal measurements, existing implementations, recorded failures.

| Our constraint | Consequence for the choice |
|---|---|
| data we hold ({format}, {scale}) | |
| compute available | |
| downstream task | |
| what we already built | |
| what we already tried and dropped | |

## 🔒 Internal

---

# §4 What would reverse this

**A selection without this cannot be revisited — only re-argued.**

This plays the role that search scope plays for a gap claim: scope makes an absence falsifiable,
these conditions make a choice revisable.

| # | If this happens | We switch to | How we would notice |
|---|---|---|---|
| 1 | | | |

Also record **what was deliberately accepted**: the known downside of the choice, so nobody
rediscovers it in three months and treats it as a surprise.

---

# §5 What we could not check

| Item | Why not | What it would take |
|---|---|---|

**Anything marked `untested` in §2 belongs here too.**

---

# §6 Tracing a claim

| File | What is in it |
|---|---|
