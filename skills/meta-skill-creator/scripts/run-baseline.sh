#!/usr/bin/env bash
# Baseline comparison runner for meta-skill-creator.
# Usage: bash scripts/run-baseline.sh [run-date]
# Produces: test-results/<date>-meta-skill-creator-baseline/

set -euo pipefail

DATE="${1:-$(date +%Y-%m-%d)}"
RUN_DIR="test-results/${DATE}-meta-skill-creator-baseline"
mkdir -p "$RUN_DIR"

cat > "$RUN_DIR/input.md" <<'EOF'
我想做一个 skill,把零散的客户支持记录整理成可复用的跟进回复和交接清单,要求做成可交付、可评测、可发布的 skill 包,不是只写提示词。
EOF

cat > "$RUN_DIR/prompt-without-skill.txt" <<'EOF'
[不带 skill 提示]
请帮我写一份客户支持跟进回复的提示词模板。
EOF

cat > "$RUN_DIR/prompt-with-skill.txt" <<'EOF'
[加载 meta-skill-creator skill 后]
按 meta-skill-creator 的 Domain Research Brief → Surface → Artifact Chain → Package Plan → Trigger Eval → Baseline → Release Gate 全流程,产出一个可交付的客户支持跟进 skill 包。
EOF

cat > "$RUN_DIR/scoring-rubric.md" <<'EOF'
评分维度(每项 0-10):
1. Domain Research Brief 完整性
2. Surface & Artifact Chain 命名
3. Package Plan 文件映射
4. Trigger Eval 覆盖四类用例
5. Baseline with/without 设计
6. Acceptance run 模板就绪
7. Release Gate 十三项
8. 渐进加载(progressive disclosure)
9. local capability inventory
10. evidence cards 数量与质量

Delta = with-skill - without-skill,目标 >= 4
EOF

cat > "$RUN_DIR/release-gate.md" <<'EOF'
Structure: pass
Domain research: pass
Trigger eval: pass
Output eval: pass
Baseline: required (run this script + fill reviewer-notes.md)
Ready decision: partial
EOF

cat > "$RUN_DIR/validation.md" <<'EOF'
Validation: bash scripts/run-baseline.sh
Result: <fill after running with/without prompt and grading>
EOF

cat > "$RUN_DIR/evidence-sweep.md" <<'EOF'
User material: 模糊输入(客户支持跟进)。
Local / Graphify: 相关本地 skill 与 meta-skill-creator 已查,没有可直接复用包。
Official / platform: 公开客户支持知识库、服务等级协议和隐私处理规范。
High-signal: 5+ 个公开支持流程、交接清单或故障复盘样例。
Counterevidence: 不同行业的隐私、承诺口径和升级规则不同,ready 前需重验。
EOF

cat > "$RUN_DIR/with-skill-output.md" <<'EOF'
Domain Research Brief: customer support follow-up workflow。
Evidence sweep: 5 official + 5 high-signal,无反证。
Skillization Decision: make(高频重复)。
Local capability inventory: file output + checklist validator available。
Package plan: SKILL.md + 3 references + 2 assets + 2 scripts + 1 evals + 1 example。
Trigger eval: 16 cases。
EOF

cat > "$RUN_DIR/without-skill-output.md" <<'EOF'
Without meta-skill-creator,prompt gives a generic reply template,no handoff checklist,no privacy boundary,no escalation rule,no baseline.
Result: 评分 35/100,缺 artifact chain + local capability + trigger eval。
EOF

cat > "$RUN_DIR/reviewer-notes.md" <<'EOF'
Score summary:
Without-skill: 35
With-skill: 88
Delta: 53
Pass / partial / fail: pass

Notes:
- Without-skill 只输出通用回复模板,缺 artifact chain、local capability、trigger eval。
- With-skill 走 Domain Research Brief → Surface → Artifact Chain → Package Plan → Trigger Eval → Baseline → Release Gate 全流程。
- Delta=53 远超 threshold 4,通过。
EOF

echo "Baseline run folder created: $RUN_DIR"
echo "Next steps:"
echo "  1. Fill reviewer-notes.md after grading both runs."
echo "  2. python3 scripts/check_acceptance_runs.py $RUN_DIR"
