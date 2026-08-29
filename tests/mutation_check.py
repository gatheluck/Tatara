#!/usr/bin/env python3
"""Does the suite actually fail when the plugin is broken?

A passing test proves nothing on its own. This introduces known defects one at
a time, confirms the suite catches each, and restores the file.

Run:  python3 tests/mutation_check.py
"""

import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SUITE = ROOT / "tests" / "test_plugin.py"

MUTATIONS = [
    ("drop the reversal conditions from the selection template",
     "templates/selection.md",
     lambda t: t.replace("reverse", "X")),
    ("unbalance a code fence",
     "README.md",
     lambda t: t + "\n```\n"),
    ("point at a file that does not exist",
     "README.md",
     lambda t: t + "\nSee `${CLAUDE_PLUGIN_ROOT}/reference/nope.md`.\n"),
    ("say broken where it should say refuted",
     "skills/verify/SKILL.md",
     lambda t: t + "\nThe gap is broken.\n"),
    ("remove the language deferral from a skill",
     "skills/report/SKILL.md",
     lambda t: t.replace("user's language", "Japanese")),
    ("take a heading's space away",
     "templates/selection.md",
     lambda t: t.replace("# §0 The decision", "#§0 The decision")),
]


def suite_passes() -> bool:
    return subprocess.run(
        [sys.executable, str(SUITE)], capture_output=True
    ).returncode == 0


def main() -> int:
    if not suite_passes():
        print("\n  the suite is already red — fix that before mutating\n")
        return 1

    survived = []
    for label, rel, mutate in MUTATIONS:
        p = ROOT / rel
        original = p.read_text()
        p.write_text(mutate(original))
        caught = not suite_passes()
        p.write_text(original)
        print(f"  {'caught ✓' if caught else 'SURVIVED ✗'}  {label}")
        if not caught:
            survived.append(label)

    ok = suite_passes()
    print(f"\n  restored: {'clean' if ok else 'DIRTY — check the working tree'}")
    if survived:
        print(f"  {len(survived)} mutation(s) survived — those defects would ship\n")
        return 1
    print(f"  all {len(MUTATIONS)} mutations caught\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
