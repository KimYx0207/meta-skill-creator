# Skill Contract: meta-skill-creator

## Result Definition

- 用户：需要批量创建、重写、评审 Agent Skills 的产品 owner 或执行 agent。
- 压力场景：旧 Skill Creator 只能生成结构完整的 skill，但用户发现结果不满足交付级质量。
- 用户最终品：一个能审查、能运行、能评测、能持续改进的 skill 产品包，并且能说明目标用户如何从输入得到可见最终产物。
- 3 分钟可见结果：Skill Design Board，说明 Domain Research Brief、领域模型、平台/工作表面、用户最终品、主题到产物的生成链、杀手机制、包结构和必跑 eval。
- 成功标准：输出不是空泛提示词，而是 contract + package plan + assets/scripts/templates + evals + verification summary。
- 一票否决：没有 Domain Research Brief、没有体验表面、没有 artifact chain、没有 trigger eval、没有 baseline、没有非文档资产、没有用户最终品定义，却宣称 ready。

## Trigger Contract

### Should Trigger

- 用户说“做一个 skill / 创建 skill / 改 skill / 优化 skill”。
- 用户说“原 Skill Creator 不够好，要打磨造 skill 的规则”。
- 用户要把一个流程沉淀成可复用 agent 能力。
- 用户要求 trigger eval、baseline、A/B、release gate、skill 产品设计。
- 用户要求审查为什么现有 skill 只是文档完整但产品弱。

### Should Not Trigger

- 用户只要一次性提示词，不想创建可复用能力。
- 用户只要普通文案润色、翻译、总结。
- 用户要安装插件、创建 API key、部署服务，而不是设计 skill。
- 用户要对已有代码做一般 bug fix。
- 用户要做交付说明但不涉及 skill 创建或评审。

### Near-Miss

- “帮我写个流程”：如果是一次性流程，不触发；如果要复用成 agent 能力，触发。
- “帮我做个模板”：如果模板服务于 skill 包，触发；如果只是单个文档模板，不触发。
- “这个 skill 不行”：如果要诊断/重写 skill，触发；如果只是解释一次输出，不触发。

### Ambiguous Handling

先判断三个维度：是否重复使用、是否有稳定输入输出、是否需要 bundled resources。三项至少两项为是，进入 skill 化；否则给一次性方案。

## Domain Research Contract

- Raw user intent:
- Suspected domain(s):
- Evidence read:
- Evidence sweep attempted:
- Unavailable evidence paths:
- Users / roles:
- Case variables that must not become fixed scope:
- Pressure moments:
- Existing workflow:
- Native artifacts:
- Work surfaces / tools:
- Local capability inventory:
- Primary tool / MCP / script route:
- Output evidence route:
- First judgment standard:
- Required real inputs:
- Generated components:
- Must not simulate:
- Counterevidence:
- Decision: `make` / `do-not-make` / `research-needed`

If this contract is missing or evidence-thin, stop before writing `SKILL.md`.

## Input / Output Contract

### Required Input

- skill idea 或 existing skill path，
- 用户最终想达成的结果，
- 目标用户或使用场景，
- 当前失败点或质量担忧。

### Optional Input

- 外部参考项目，
- 样例输入/输出，
- 平台限制，
- 用户偏好的文件结构，
- 是否要安装为系统 skill。

### Missing Information Behavior

低风险缺失时先产出 design candidate，并标注 assumption。高风险缺失（覆盖系统 skill、删除文件、发布、安装、联网付费）必须停下确认。

### Output Shape

默认输出一个 skill package plan 或候选目录。若用户要求落地，则创建完整候选包：`SKILL.md`、`references/`、`assets/` 或 `scripts/`、`evals/`、`examples/` 和验证摘要。

## Experience Surface Contract

This contract is filled after Domain Research Contract, not before it.

- Platform / work surface:
- Native medium:
- First user-visible artifact:
- Full final package:
- Audience judgment standard:
- Theme/material to artifact chain:
- What must be real user material:
- What can be generated:
- What must not be simulated:

## Local Capability / Multimodal Contract

Required when the candidate can output images, video, audio, slides, documents, dashboards, rendered previews, or generated files.

- Current host tools available:
- MCP/plugin tools available:
- Existing local scripts/assets:
- Cost or approval boundary:
- Primary generation/render route:
- Fallback route:
- Structured multimodal brief required:
- Output evidence required:
- Claim boundary if generation cannot run:

Example for a social image-text workflow:

```text
theme
-> target reader and note intent
-> cover promise
-> 3:4 cover image route
-> 6-8 image page scripts
-> image prompts or generated cards
-> title/body/tags/comments/DM
-> manifest + publish brief + self-check
```

## Package Contract

- `SKILL.md`：只放触发、工作流、资源路由、验收口径。
- `references/intent-domain-research.md`：领域研究规则、no guessing rule、research-needed 停止条件。
- `references/product-design.md`：用户、痛点、产品流程、信息架构、质量分层。
- `references/evidence.md`：外部/内部证据卡和反证。
- `references/source-abstraction-boundary.md`：来源抽象和不复制边界。
- `references/release-gate.md`：ready 门禁。
- `references/multimodal-tooling.md`：本地工具发现、多模态结构化 brief 和输出证据规则。
- `assets/*.md`：可复制模板。
- `scripts/check_meta_skill_package.py`：防止包只是文档壳。
- `evals/`：trigger、output、baseline、regression。

## Boundary Contract

- 不替用户擅自覆盖系统级 `skill-creator`。
- 不把第三方样本写成官方标准。
- 不把单个案例里的目标岗位、受众标签、公司名、部门名、栏目名或验收短语写死进 `description`、trigger、scope、默认栏目或拒绝交付规则；除非用户明确要求岗位专用 skill，或证据说明这是合规/安全/领域边界。
- 不用 star 或 README 宣称直接证明交付级。
- 不承诺自动生成的 skill 一定优于人工策划。
- 不把 quick validate 当成产品质量证明。

## Eval Contract

- Trigger eval：至少 5 正、5 负、3 near-miss、3 ambiguous。
- Output eval：至少覆盖模糊输入、信息不足、风险边界、真实材料、最终品评分。
- Baseline：同一任务 without-skill vs with-skill。
- Regression：新版本 vs 旧版本。
- Human review：ready 前需要用户可见输出反馈。
- Drift signals：误触发、漏触发、输出空泛、资产未使用、本地工具/MCP 未使用、多模态提示词泛化、baseline 无优势、真实感或可用性反馈不达标。
