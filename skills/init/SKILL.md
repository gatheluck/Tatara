---
description: Create a new research project for a topic. Sets up the directory, context.md, and worklog.md so the project is ready to enter Stage 0.
argument-hint: <description of the research topic>
disable-model-invocation: true
---

# init — create the research project

> 🌱 **Build the furnace.** Decide what is going to be smelted, and prepare the place the record lives.

Read `${CLAUDE_PLUGIN_ROOT}/reference/principles.md` first. Every stage that follows obeys it.

**Write every artifact in the user's language.**

## What to do

Create a research project for the topic "$ARGUMENTS".

### 1. Decide where it goes

Create `projects/YYYY-MM-DD-{short-slug}/` **in the current working repository**. Use today's date.
The slug is alphanumerics and hyphens. Follow whatever convention the repository already uses.

> ⚠️ **Never create it inside this plugin's repository.**
> Keep the tool and the artifacts apart. Artifacts can contain confidential material (🔒),
> and the plugin side is meant to be published.
>
> If you are currently inside the plugin repository (it has `skills/` and `.claude-plugin/`),
> **ask the user where to create it.**

**Other projects already sitting in the same `projects/` is a good thing.**
Stage 2's local mining goes through them. External research cannot do this in principle, and it
gets more valuable as you accumulate.

### 2. Write `context.md`

Use `${CLAUDE_PLUGIN_ROOT}/templates/context.md` as the template.

**Fill in only what the user's description supports.** Leave any field you cannot fill marked
**"unresolved."** Never fill one in by guessing.

These in particular are mandatory.

- **The problem statement** (what and what, and what you want done with them)
- **Why it looks hard** — but state explicitly that this is a working hypothesis, to be confirmed
  or refuted by the research. Never treat what you wrote here as fact
- **A provisional list of what this problem is called across fields** — the starting point for
  closing gaps in Stage 4. **Never put this list into the Deep Research prompt**
  (Principle 7 / seed leakage)
- **The focus** — what you want out of this. The default is two things: where the field stands,
  and where the gap is

### 3. Look for neighboring projects

If anything in the repository looks related, list it in `context.md`.
**Stage 2 digs here. There is information external research cannot reach in principle.**

### 4. Create `worklog.md`

Empty is fine. Each stage appends its record.

### 5. Check for missing premises

**Deep Research has a hard cap on how many times you can run it. The prompt has to land on the
first try.**
If a question is still open that would substantially change the scope of the search, ask the user
with `AskUserQuestion`.

Ask only about things where **the answer changes what gets searched.**
**If you can defer the answer and turn it into a research item instead, do that and don't ask.**

## When you're done

Tell the user the next step is `/tatara:dr-prompt`.
