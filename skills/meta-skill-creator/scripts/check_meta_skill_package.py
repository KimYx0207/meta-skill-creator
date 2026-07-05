#!/usr/bin/env python3
"""校验 meta-skill-creator 风格的 Skill 包。

这个本地门禁用来防止只有文案、没有契约和验收的包。它要求包里包含
领域研究、产品设计、契约、模板、评测和示例，但不等于真实用户质量证明。
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Windows 控制台默认 GBK，强制 UTF-8 输出避免中文乱码
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REQUIRED_FILES = [
    "SKILL.md",
    "references/intent-domain-research.md",
    "references/experience-surface-model.md",
    "references/product-design.md",
    "references/skill-contract.md",
    "references/evidence.md",
    "references/source-abstraction-boundary.md",
    "references/multimodal-tooling.md",
    "references/release-gate.md",
    "references/evaluation-method.md",
    "references/closed-loop-governance.md",
    "assets/domain-research-brief-template.md",
    "assets/skill-contract-template.md",
    "assets/package-plan-template.md",
    "assets/product-design-board-template.md",
    "assets/multimodal-prompt-brief-template.md",
    "assets/acceptance-run-template.md",
    "assets/loop-run-record-template.md",
    "evals/trigger-eval.json",
    "scripts/check_acceptance_runs.py",
    "scripts/check_closed_loop.py",
    "examples/example-input.md",
    "examples/example-output.md",
]

KEY_PHRASES = {
    "SKILL.md": ["意图与领域研究", "领域研究简报", "research-needed", "Fetch", "基线", "触发评测", "包计划", "发布门禁", "本地能力清单", "多模态简报", "闭环治理", "运行记录", "none-with-reason"],
    "references/intent-domain-research.md": ["No Guessing Rule", "Domain Research Brief", "Fetch Before", "research-needed", "Research-To-Design Chain", "Local capability inventory"],
    "references/experience-surface-model.md": ["Artifact Chain", "Surface After Domain Research", "worked example", "Local Capability Inventory"],
    "references/product-design.md": ["3 分钟可见结果", "体验流程设计", "例子不是元规则", "当前边界", "先做意图领域研究", "Local Capability", "Multimodal", "Loop Closure Board"],
    "references/skill-contract.md": ["Domain Research Contract", "Experience Surface Contract", "Trigger Contract", "Eval Contract", "Boundary Contract", "Local Capability / Multimodal Contract"],
    "references/multimodal-tooling.md": ["Capability Inventory", "Multimodal Brief Contract", "Route Selection Rule", "Output evidence", "Image2 / host-native", "Downgrade proof"],
    "references/release-gate.md": ["发布门禁", "十四项门禁", "证据扫查", "验收运行记录", "就绪规则", "闭环", "none-with-reason"],
    "references/closed-loop-governance.md": ["闭环定义", "原创循环", "阶段契约", "写回决策", "证据分层", "漂移信号", "原创边界", "nextRunReuseKey"],
    "assets/domain-research-brief-template.md": ["原始意图", "领域假设", "技能化决定", "本地能力清单"],
    "assets/multimodal-prompt-brief-template.md": ["能力清单", "产物简报", "提示词变体", "验证"],
    "assets/acceptance-run-template.md": ["运行类型", "读取边界", "校验命令", "证据分层", "分数与判定"],
    "assets/loop-run-record-template.md": ["Intent Core", "Evidence Fetch", "Product Surface", "Package Contract", "Verification Evidence", "Loop Decision", "Scar Record", "next_run_reuse_key"],
    "scripts/check_acceptance_runs.py": ["REQUIRED_FILES", "score delta", "Acceptance run check"],
    "scripts/check_closed_loop.py": ["REQUIRED_FILES", "BANNED_EXTERNAL_MARKERS", "Closed-loop check"],
    "references/evaluation-method.md": ["Unknown Domain Research Test", "research-needed", "Domain Research Brief", "Multimodal Tool Route Regression", "No Domain Research Brief", "Surface guessed", "baseline", "Domain Research", "multimodal", "Loop Closure"],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    root = root.resolve()
    failures: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            failures.append(f"缺少必需文件：{rel}")

    skill_path = root / "SKILL.md"
    if skill_path.exists():
        skill = read(skill_path)
        fm = parse_frontmatter(skill)
        if fm.get("name") != root.name:
            failures.append("SKILL.md frontmatter 的 name 必须与目录名一致")
        desc = fm.get("description", "")
        if len(desc) < 120:
            failures.append("SKILL.md description 太弱，无法稳定路由触发")
        if len(skill.splitlines()) > 500:
            failures.append("SKILL.md 应低于 500 行；细节应移动到 references")

    trigger_path = root / "evals/trigger-eval.json"
    if trigger_path.exists():
        data = json.loads(read(trigger_path))
        cases = data.get("cases", [])
        counts: dict[str, int] = {}
        for case in cases:
            case_type = case.get("type", "unknown")
            counts[case_type] = counts.get(case_type, 0) + 1
        expected = {"should-trigger": 5, "should-not-trigger": 5, "near-miss": 3, "ambiguous": 3}
        for case_type, minimum in expected.items():
            if counts.get(case_type, 0) < minimum:
                failures.append(f"触发评测至少需要 {minimum} 个 {case_type} 用例")

    for rel, phrases in KEY_PHRASES.items():
        path = root / rel
        if not path.exists():
            continue
        text = read(path).lower()
        for phrase in phrases:
            if phrase.lower() not in text:
                failures.append(f"{rel} 缺少关键短语：{phrase}")

    if failures:
        print("Meta skill package check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Meta skill package check passed.")
    print(f"已检查 {len(REQUIRED_FILES)} 个必需文件：{root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
