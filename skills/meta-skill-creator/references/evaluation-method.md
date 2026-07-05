# Evaluation Method

如何评估你用 `meta-skill-creator` 造出的 skill 是否真的有用，而不是一个长 prompt。首次发布时这里写的是评估契约；后续每次重要编辑后跑一遍，把失败写回对应 reference。

## 何时评估

- 造完一个新 skill，发布前。
- 改过 skill 的 trigger、references 或 scripts 之后。
- 准备声称 ready 之前。
- 用户要求闭环、复盘、持续改进或公开交付前。

## 1. Trigger 评估

用 `evals/trigger-eval.json` 跑触发测试，覆盖四类用例：

- should-trigger：明确该用本 skill 的场景。
- should-not-trigger：相邻但不该触发的任务。
- near-miss：模糊边界，需要判定。
- ambiguous：信息不足，需要澄清。

检查 description 是否精准触发、不误触相邻任务。description 太泛则永不触发，太宽则乱触发。

## 2. Output 评估

对模糊输入、不完整输入、高风险输入、真实素材输入跑 skill，检查输出：

- 是否以 Domain Research Brief 开头。**No Domain Research Brief = 不通过**。
- 是否从证据推导 surface，而不是从熟悉例子猜。**Surface guessed = Hard Cap**。
- 是否产出用户可见的最终 artifact。
- 未知领域是否在尝试证据检索后再返回 `research-needed`（**Unknown Domain Research Test**：先检索后停）。
- 多模态 skill 是否先探测本地工具、写结构化 brief、并按 route 顺序产出（**Multimodal Tool Route Regression**：Image2/host-native 优先，MCP 降级要证据）。
- 是否在没有真实输出证据时硬说 ready。

## 3. Baseline 对比

同一任务跑 with-skill vs without-skill。with-skill 必须在 Domain Research、artifact chain、package completeness 上明显更好，且不降低 release honesty。如果 with-skill 不明显更好，回产品设计。

## 4. Regression 检查

编辑后对比新旧版本，确认不引入新误触发、不丢领域研究纪律、不降多模态 brief 质量。首次发布无旧版可回归，这一节是面向未来编辑的契约。

## 5. Loop Closure 检查

每次验收或失败必须检查：

- 是否填写运行记录，且包含 Intent Core、Evidence Fetch、Product Surface、Package Contract、Verification Evidence、Loop Decision。
- 是否区分 structure / contract / artifact / runtime / human 证据层级。
- 是否给出 `writeback`、`proposal`、`none-with-reason` 或 `blocked`。
- 如果选择 `writeback`，是否写回 reference、asset、script、eval 或 example，而不是只写聊天总结。
- 如果选择 `blocked`，是否说明缺哪类证据和下一轮最小动作。
- 是否有 `next_run_reuse_key`，或明确说明为什么没有可复用学习。

无闭环记录的产物最多只能判为 L2 operating candidate；无闭环决策却声称 ready，直接失败。

## 6. Satisfaction 评分（/100）

| 维度 | 分 | 标准 |
|---|---:|---|
| User result definition | 8 | user / pressure / final artifact / success criteria |
| Domain Research | 13 | Brief + evidence + domain model + research-needed stop rule |
| Fetch before stop | 8 | 检索尝试 before research-needed |
| Experience surface | 8 | platform / medium / artifact chain from research |
| Skillization judgment | 8 | 为什么该 / 不该做成 skill |
| Evidence quality | 8 | 官方 / 高信号 / 用户失败 / 反证卡片 |
| Package design | 11 | 文件和资产对应 failure mode |
| Trigger eval | 8 | 正 / 负 / near-miss / ambiguous |
| Output eval | 8 | fuzzy / incomplete / risky / real-material / final artifact |
| Baseline and regression | 10 | with/without + A/B 计划 |
| Release honesty | 7 | ready 状态诚实 + next drift action 清楚 |
| Loop closure | 3 | 运行记录 + 写回/不写回决策 + next_run_reuse_key |

权重合计 = 8+13+8+8+8+8+11+8+8+10+7+3 = 100。

Hard Caps：无 Skill Contract ≤59；无 Domain Research Brief ≤49；research-needed 前未检索 ≤59；surface 瞎猜 ≤64；无 artifact chain ≤64；无 trigger eval ≤69；无 baseline ≤74；无非文档资产 ≤79；无用户最终品 ≤69；声称 ready 无可见测试 ≤84；无闭环决策 ≤79；失败无预防规则 ≤74。

## 7. Acceptance Run（clean-session 验收）

保存 run folder：

```text
test-results/<date>-<skill>-acceptance/
  input.md
  evidence-sweep.md
  without-skill-output.md
  with-skill-output.md
  reviewer-notes.md
  tool-capability.md
  release-gate.md
  validation.md
```

用 `python scripts/check_acceptance_runs.py <run_dir>` 验证。clean-session prompt 只用用户原始模糊意图，不附加验收提示词——那些规则应住在 skill 里，不能靠 prompt 喂给验收运行。

## 评估字段速查

- **Trigger Eval**：should-trigger / should-not-trigger / near-miss / ambiguous / expected description changes
- **Output Eval**：fuzzy / incomplete / risky-boundary / real-material / multimodal-tool-route / final artifact scoring
- **Tool & Multimodal**：local capability inventory / native-MCP-local route / Image2 host-native first proof / downgrade proof / structured brief / output evidence / clean-session check
- **Baseline**：prompt / without path / with path / scoring dimensions / result
- **Regression**：previous version / new version / comparison prompts / pass-fail threshold / regression found
- **Human Review**：reviewer / visible artifacts / feedback / next drift action
- **Loop Closure**：run record / evidence level / writeback decision / prevention rule / next_run_reuse_key

## Next Drift Action

评估失败时，把失败写回 `references/intent-domain-research.md`（领域研究问题）、`references/multimodal-tooling.md`（多模态路由问题）或 `references/release-gate.md`（发布门问题）。skill 保持 `evidence-blocked`，直到 clean-session acceptance 跑通且有独立复核。
