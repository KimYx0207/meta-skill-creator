#!/usr/bin/env python3
"""Validate meta-skill-creator acceptance run folders.

This checks that baseline and self-acceptance evidence exists in a reproducible
shape. It does not judge semantic quality by itself; it prevents empty markdown
or structure-only runs from being treated as release evidence.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "input.md",
    "evidence-sweep.md",
    "without-skill-output.md",
    "with-skill-output.md",
    "reviewer-notes.md",
    "release-gate.md",
    "validation.md",
]

REQUIRED_PHRASES = {
    "evidence-sweep.md": [
        "User material",
        "Local / Graphify",
        "Official / platform",
        "High-signal",
        "Counterevidence",
    ],
    "with-skill-output.md": [
        "Domain Research Brief",
        "Evidence sweep",
        "Skillization Decision",
    ],
    "reviewer-notes.md": [
        "Score summary",
        "Without-skill",
        "With-skill",
        "Delta",
        "Pass / partial / fail",
    ],
    "release-gate.md": [
        "Structure",
        "Domain research",
        "Baseline",
        "Ready decision",
    ],
    "validation.md": [
        "Validation",
        "Result",
    ],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_score(text: str) -> tuple[int | None, int | None, int | None]:
    without = with_skill = delta = None
    for label, var in [
        (r"Without-skill", "without"),
        (r"With-skill", "with"),
        (r"Delta", "delta"),
    ]:
        match = re.search(label + r"\s*[:=]\s*(-?\d+)", text, re.I)
        if not match:
            continue
        value = int(match.group(1))
        if var == "without":
            without = value
        elif var == "with":
            with_skill = value
        else:
            delta = value
    if delta is None and without is not None and with_skill is not None:
        delta = with_skill - without
    return without, with_skill, delta


def validate_run(run_dir: Path) -> list[str]:
    failures: list[str] = []
    for rel in REQUIRED_FILES:
        path = run_dir / rel
        if not path.exists():
            failures.append(f"{run_dir}: missing {rel}")
            continue
        text = read(path)
        if len(text.strip()) < 120:
            failures.append(f"{run_dir}: {rel} is too thin")
        for phrase in REQUIRED_PHRASES.get(rel, []):
            if phrase.lower() not in text.lower():
                failures.append(f"{run_dir}: {rel} missing phrase {phrase!r}")

    notes_path = run_dir / "reviewer-notes.md"
    if notes_path.exists():
        without, with_skill, delta = parse_score(read(notes_path))
        if without is None or with_skill is None or delta is None:
            failures.append(f"{run_dir}: reviewer-notes.md missing parseable scores")
        elif delta < 4:
            failures.append(f"{run_dir}: score delta must be >= 4, got {delta}")

    release_path = run_dir / "release-gate.md"
    if release_path.exists():
        release = read(release_path).lower()
        if "ready decision: pass" not in release and "ready decision: partial" not in release:
            failures.append(f"{run_dir}: release-gate.md needs Ready decision: pass or partial")
        if "quick_validate" in release and "product readiness" not in release:
            failures.append(f"{run_dir}: release-gate.md must separate quick_validate from product readiness")

    return failures


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_acceptance_runs.py <run_dir> [<run_dir> ...]")
        return 2

    failures: list[str] = []
    for arg in sys.argv[1:]:
        run_dir = Path(arg).resolve()
        if not run_dir.exists():
            failures.append(f"missing run dir: {run_dir}")
            continue
        failures.extend(validate_run(run_dir))

    if failures:
        print("Acceptance run check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Acceptance run check passed.")
    print(f"Checked {len(sys.argv) - 1} run folder(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

