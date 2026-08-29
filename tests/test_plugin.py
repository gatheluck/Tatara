#!/usr/bin/env python3
"""Structural tests for the Tatara plugin.

The plugin is instructions, not code, so these are structural and content
invariants rather than behavioural tests. They exist because every defect
shipped so far was mechanically detectable: an unbalanced code fence, a stale
skill count, leftovers from a rename, a misspelled standard entity name.

Run:  python3 tests/test_plugin.py
No dependencies. Exit code 0 means green.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAILURES: list[str] = []
CHECKS = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    if not ok:
        FAILURES.append(f"{name}" + (f"\n      {detail}" if detail else ""))


def md_files() -> list[pathlib.Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def skill_dirs() -> list[pathlib.Path]:
    return sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())


def frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


# ---------------------------------------------------------------- manifest
def test_manifest():
    p = ROOT / ".claude-plugin" / "plugin.json"
    check("manifest exists", p.exists())
    if not p.exists():
        return
    try:
        d = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        check("manifest parses", False, str(e))
        return
    check("manifest parses", True)
    check("manifest has name", d.get("name") == "tatara", f"got {d.get('name')!r}")
    check(
        "tamahagane_path has no default",
        "default" not in d.get("userConfig", {}).get("tamahagane_path", {}),
        "a default would shadow the fallback chain",
    )


# ---------------------------------------------------------------- skills
def test_every_skill_is_well_formed():
    for d in skill_dirs():
        f = d / "SKILL.md"
        check(f"{d.name}: SKILL.md exists", f.exists())
        if not f.exists():
            continue
        fm = frontmatter(f.read_text())
        check(f"{d.name}: has description", bool(fm.get("description")))
        check(
            f"{d.name}: disable-model-invocation is true",
            fm.get("disable-model-invocation") == "true",
            "skills must not fire on their own",
        )


def test_every_skill_reads_the_principles():
    for d in skill_dirs():
        f = d / "SKILL.md"
        if not f.exists():
            continue
        check(
            f"{d.name}: reads principles.md",
            "reference/principles.md" in f.read_text(),
            "the principles are the substance; a skill that skips them is unmoored",
        )


def test_every_skill_defers_the_output_language():
    for d in skill_dirs():
        f = d / "SKILL.md"
        if not f.exists():
            continue
        t = f.read_text()
        check(
            f"{d.name}: defers the output language",
            "user's language" in t,
            "artifacts follow the user, so the language must not be hardcoded",
        )


# ---------------------------------------------------------------- references
def test_plugin_root_references_resolve():
    for f in md_files():
        for ref in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([^\s`)]+)", f.read_text()):
            target = ROOT / ref.rstrip(".,")
            check(
                f"{f.relative_to(ROOT)}: ${{CLAUDE_PLUGIN_ROOT}}/{ref} resolves",
                target.exists(),
            )


def test_relative_doc_links_resolve():
    for f in md_files():
        for link in re.findall(r"\]\((?!https?:|#)([^)]+)\)", f.read_text()):
            link = link.split("#")[0]
            if not link or link.startswith("$"):
                continue
            check(
                f"{f.relative_to(ROOT)}: link {link} resolves",
                (f.parent / link).exists(),
            )


# ---------------------------------------------------------------- markdown
def test_code_fences_are_balanced():
    for f in md_files():
        n = len(re.findall(r"^```", f.read_text(), re.M))
        check(
            f"{f.relative_to(ROOT)}: fences balanced",
            n % 2 == 0,
            f"{n} fence markers — an odd count swallows the rest of the file",
        )


def test_headings_have_a_space_after_the_hashes():
    for f in md_files():
        bad = [
            ln for ln in f.read_text().split("\n")
            if re.match(r"^#{1,6}[^#\s]", ln)
        ]
        check(
            f"{f.relative_to(ROOT)}: headings well formed",
            not bad,
            f"no space after #: {bad[:2]}",
        )


# ---------------------------------------------------------------- content
def test_readme_skill_count_matches_reality():
    n = len(skill_dirs())
    words = {5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    t = (ROOT / "README.md").read_text()
    check(
        "README states the real skill count",
        f"{words.get(n, str(n))} entries" in t,
        f"{n} skills on disk; README says otherwise",
    )


def test_no_stale_break_terminology():
    allowed = ("Break the kera", "break down the hillside", "break the independence",
               "breaking the kera", "broken commit", "breaking the page",
               "early `break`", "break\nthe chain")
    for f in md_files():
        for i, ln in enumerate(f.read_text().split("\n"), 1):
            if re.search(r"\bbroken\b|\bbreak the gap\b|breaking is", ln, re.I):
                if not any(a in ln for a in allowed):
                    check(
                        f"{f.relative_to(ROOT)}:{i}: says refuted, not broken",
                        False,
                        ln.strip()[:80],
                    )


def test_no_leftovers_from_the_rename():
    for f in md_files():
        check(
            f"{f.relative_to(ROOT)}: no research-scope leftovers",
            "research-scope" not in f.read_text(),
        )


# ---------------------------------------------------------------- NEW: tracks
def test_init_asks_which_track():
    t = (ROOT / "skills" / "init" / "SKILL.md").read_text().lower()
    check(
        "init asks which track the topic is",
        "selection" in t and "novelty" in t,
        "a selection task and a novelty task need different pipelines",
    )


def test_a_selection_template_exists():
    p = ROOT / "templates" / "selection.md"
    check("templates/selection.md exists", p.exists())
    if not p.exists():
        return
    t = p.read_text()
    for needle, why in [
        ("provenance", "a reported number without provenance cannot be compared"),
        ("code", "a method you cannot run is not a candidate"),
        ("untested", "guessing 'yes' on a method nobody ran turns a selection into a wish"),
        # the concept, not one phrasing of it: the choice must be revisable
        ("reverse", "a selection must carry the conditions that reverse it"),
    ]:
        check(
            f"selection template covers {needle!r}",
            needle.lower() in t.lower(),
            why,
        )


def test_synthesize_branches_on_the_track():
    t = (ROOT / "skills" / "synthesize" / "SKILL.md").read_text().lower()
    check(
        "synthesize branches on the track",
        "selection" in t,
        "a selection task produces a decision table, not a gap list",
    )


def test_verify_branches_on_the_track():
    t = (ROOT / "skills" / "verify" / "SKILL.md").read_text().lower()
    check(
        "verify branches on the track",
        "selection" in t,
        "for selection, attack the front-runner instead of the gap",
    )


def test_readme_documents_both_tracks():
    t = (ROOT / "README.md").read_text().lower()
    check(
        "README documents both tracks",
        "selection" in t and "novelty" in t,
    )


# ---------------------------------------------------------------- run
def main() -> int:
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    if FAILURES:
        print(f"\n  FAILED  {len(FAILURES)} of {CHECKS} checks\n")
        for f in FAILURES:
            print(f"    ✗ {f}")
        print()
        return 1
    print(f"\n  ok  {CHECKS} checks\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
