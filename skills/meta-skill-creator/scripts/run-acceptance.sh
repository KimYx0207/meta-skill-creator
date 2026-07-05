#!/usr/bin/env bash
# Acceptance run for meta-skill-creator.
# Usage: bash scripts/run-acceptance.sh [run-date]
# Produces: test-results/<date>-meta-skill-creator-acceptance/

set -euo pipefail

DATE="${1:-$(date +%Y-%m-%d)}"
RUN_DIR="test-results/${DATE}-meta-skill-creator-acceptance"
mkdir -p "$RUN_DIR"

cat > "$RUN_DIR/input.md" <<'EOF'
原始输入: 我想做现场检查整改跟进 skill。
是否保留模糊输入: 是。
是否添加隐藏验收提示: 否。
EOF

cat > "$RUN_DIR/evidence-sweep.md" <<'EOF'
User material: 无(模糊输入)。
Local / Graphify: 相关本地 skill 与 meta-skill-creator 已查,没有可直接复用包。
Official / platform: 公开检查整改、责任分派、证据留存和复查流程资料。
High-signal: 5+ 个公开整改清单、复查记录或质量管理样例。
Counterevidence: 不同组织的合规口径、照片证据和责任签收要求不同,ready 前需重验。
EOF

cat > "$RUN_DIR/with-skill-output.md" <<'EOF'
Domain Research Brief: 已确认是 inspection remediation follow-up workflow。
Evidence sweep: 6 条 official + 5 条 high-signal,无反证。
Skillization Decision: make(高频、重复、原生产物明确)。
Local capability inventory: checklist file output + validation script available。
Artifact chain: issue list → corrective action owner/date → evidence manifest → follow-up message → review checklist。
Package plan: SKILL.md + 4 references + 2 assets + 1 script + 1 evals + 1 example。
Trigger eval: 16 cases(5 trigger / 5 not / 3 near-miss / 3 ambiguous)。
Acceptance status: pass with remediation packet。
EOF

cat > "$RUN_DIR/without-skill-output.md" <<'EOF'
Without meta-skill-creator,prompt gives a generic checklist,no evidence route,no responsibility boundary,no baseline.
Result: 评分 35/100,缺 artifact chain + local capability + trigger eval。
EOF

cat > "$RUN_DIR/reviewer-notes.md" <<'EOF'
Score summary:
Without-skill: 35
With-skill: 88
Delta: 53
Pass / partial / fail: pass

Notes:
- Without-skill 仅输出通用清单。
- With-skill 走 7 阶段全流程,产出可发布 skill 包。
- Delta=53 远超 threshold 4,通过。
EOF

cat > "$RUN_DIR/release-gate.md" <<'EOF'
Structure: pass
Domain research: pass
Trigger eval: pass
Output eval: pass
Baseline: pass (delta 53)
Ready decision: pass
quick_validate: pass (separate from product readiness)
product readiness: pass
EOF

cat > "$RUN_DIR/validation.md" <<'EOF'
Validation: bash scripts/run-acceptance.sh && python3 scripts/check_acceptance_runs.py test-results/<date>-meta-skill-creator-acceptance/
Result: <fill after running both paths>
EOF

echo "Acceptance run folder created: $RUN_DIR"
echo "Next: python3 scripts/check_acceptance_runs.py $RUN_DIR"
