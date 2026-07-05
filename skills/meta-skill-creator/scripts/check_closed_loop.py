#!/usr/bin/env python3
"""Check the closed-loop contract for a meta-skill-creator package."""

from __future__ import annotations

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REQUIRED_FILES = [
    "references/closed-loop-governance.md",
    "assets/loop-run-record-template.md",
    "scripts/check_closed_loop.py",
]

REQUIRED_PHRASES = {
    "references/closed-loop-governance.md": [
        "Intent Core",
        "Evidence Fetch",
        "Product Surface",
        "Package Contract",
        "Evidence Review",
        "Loop Decision",
        "writeback",
        "proposal",
        "none-with-reason",
        "blocked",
        "nextRunReuseKey",
        "原创边界",
        "证据分层",
    ],
    "assets/loop-run-record-template.md": [
        "Intent Core",
        "Evidence Fetch",
        "Product Surface",
        "Package Contract",
        "Verification Evidence",
        "Loop Decision",
        "Scar Record",
        "next_run_reuse_key",
    ],
    "SKILL.md": [
        "闭环治理",
        "运行记录",
        "writeback",
        "none-with-reason",
    ],
    "references/release-gate.md": [
        "十四项门禁",
        "闭环",
        "writeback",
        "none-with-reason",
    ],
}

BANNED_EXTERNAL_MARKERS = [
    "yao" + "-meta-skill",
    "Yao " + "Meta Skill",
    "Y" + "AO",
    "Skill " + "OS",
    "Review " + "Studio",
    "Skill " + "Atlas",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    root = root.resolve()
    failures: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            failures.append(f"缺少闭环文件：{rel}")

    for rel, phrases in REQUIRED_PHRASES.items():
        path = root / rel
        if not path.exists():
            failures.append(f"缺少待检查文件：{rel}")
            continue
        text = read(path)
        lower = text.lower()
        for phrase in phrases:
            if phrase.lower() not in lower:
                failures.append(f"{rel} 缺少闭环关键短语：{phrase}")

    checked_exts = {".md", ".py", ".json", ".txt", ".sh"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in checked_exts:
            continue
        text = read(path)
        for marker in BANNED_EXTERNAL_MARKERS:
            if marker in text:
                failures.append(f"{path.relative_to(root)} 含外部可识别标记：{marker}")

    if failures:
        print("Closed-loop check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Closed-loop check passed.")
    print(f"已检查闭环契约：{root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
