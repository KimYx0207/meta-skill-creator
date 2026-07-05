---
name: meta-skill-creator
description: 创建、重构或验收可复用技能包。适用于把重复工作流做成跨宿主能力包，并明确触发规则、第一动作、渐进加载、资产模板、脚本校验、触发评测、基线对比、验收证据、闭环治理、公开交付边界和不可伪造的运行证明；也适用于清理冗余参考、拆分人读模板与机器结构数据、补齐首次公开前的验收记录、记录运行反馈、生成写回或不写回决定。当用户提到"做一个 skill / 改 skill / 优化 skill / 评审 skill / 加 trigger eval / 加 release gate / 加 baseline / 准备开源 / 做闭环 / 写回改进"时，必须使用本技能；不要用普通提示词改写 SKILL.md。一旦涉及 skill 设计、改写、评审、对比、验收、量化打分、冗余清理、frontmatter 加字段、加 license、加 compatibility、闭环复盘，立刻调用本 skill。
compatibility: Requires Python 3.10+. Local scripts use python3; offline evidence fetch only requires local files, online fetch requires network access.
allowed-tools: Read Glob Grep Bash(python3:*) Write Edit
license: MIT
---

# 元技能创建器

用这个技能把可重复工作流做成能运行、能验收、能迁移的技能包。产物不是“更长的提示词”，而是一个默认入口很轻、细节按需加载、校验方法可复现的能力包。

## 核心契约

- 从用户真实工作流出发，不从个人偏好的模板出发。
- 写文件前先证明这件事值得技能化；一次性任务不要硬做成技能包。
- `SKILL.md` 只保留路由面：触发、第一动作、渐进加载、硬停止和验证。
- 详细研究、产品设计、包计划、触发评测、验收方法和模板放到 `references/`、`assets/`、`evals/`、`scripts/`。
- 需要补全模糊意图、让用户多次选择或先锁 MVP 再批量生成的 skill，必须设计 Codex `request_user_input` / Claude Code `AskUserQuestion` 等宿主原生决策面；Markdown 选择卡只能是降级等待界面，不能冒充真实确认。
- 图片、视频、演示文稿、文档、报表、仪表盘或其他渲染产物，优先检查 Image2 / 宿主原生能力；MCP、脚本、SVG、静态预览是降级或辅助路线，必须有降级证据。
- 外部材料只能抽象成质量原则；不要复制别人的命名、页面结构、视觉系统、提示词、示例或商业话术。
- 每次交付都要闭环：记录运行证据、评审发现、`writeback` / `proposal` / `none-with-reason` / `blocked` 决策，并把可复用学习写回对应 reference、template、validator、eval 或 example。

## 渐进加载

只读当前阶段需要的文件：

| 当前阶段 | 读取 | 何时使用 |
|---|---|---|
| 意图与领域研究 | `references/intent-domain-research.md`、`assets/domain-research-brief-template.md` | 用户输入模糊、领域陌生、像战略判断，或可能只是一次性提示词；先写领域研究简报，证据不足标 `research-needed`。 |
| 表面与产物链 | `references/experience-surface-model.md` | Skill 要产出文件、媒体、截图、演示文稿、报告、仪表盘或其他可见产物。 |
| 产品化设计 | `references/product-design.md` | 需要决定包内文件、3 分钟可见结果、用户旅程或首次公开表面。 |
| 运行契约 | `references/skill-contract.md` | 写入或改动候选技能包前使用。 |
| 来源抽象边界 | `references/source-abstraction-boundary.md` | 使用外部案例、内部样例或竞品材料时，先抽象再重写。 |
| 包计划 | `assets/package-plan-template.md` | 编辑前映射 `SKILL.md`、参考文件、资产、脚本、评测和示例。 |
| 多模态/工具路线 | `references/multimodal-tooling.md`、`assets/multimodal-prompt-brief-template.md` | Skill 依赖 Image2、宿主媒体能力、MCP、本地渲染器或脚本；先记录本地能力清单和多模态简报。 |
| 交互式决策与 MVP 门 | `references/interactive-mvp-product-skill.md` | Skill 要在模糊意图下弹多决策、锁定风格/封面/首屏/MVP 后批量生产，或要跨 Codex、Claude Code 宿主复用确认流程。 |
| 评测设计 | `references/evaluation-method.md`、`evals/trigger-eval.json` | 设计触发评测、输出评测、基线对比、回归或验收检查。 |
| 发布门禁 | `references/release-gate.md`、`assets/acceptance-run-template.md` | 声称可以分发、迁移或交付给别人使用前。 |
| 闭环治理 | `references/closed-loop-governance.md`、`assets/loop-run-record-template.md` | 验收、失败、复盘、漂移、发布准备或用户要求“闭环”时；必须写明运行记录和写回决策。 |

`assets/` 里的 `.md` 是给人填写的工作模板，`.json` 是给脚本或校验读取的结构数据；只有创建对应产物时才读取。`scripts/` 只在校验、转换或打包时运行，不要把脚本内容粘进对话上下文。

## 工作流

1. 分类：判断是 `new-skill`、`refactor-skill`、`evaluate-skill`、`package-plan`，还是 `not-a-skill`。
2. Fetch 与研究：只收集会改变包决策、产物表面、工具路线或验收标准的证据。
3. 设计：确定结果、触发边界、输入输出、本地能力路线、交互式决策面、MVP 锁定门、包结构和公开失败模式。
4. 构建：只创建或修改当前目标必须触碰的最小文件集。
5. 验证：运行包校验、闭环校验和领域校验；报告结构证据、产物证据、运行证据和人工确认分别证明了什么。
6. 闭环：填写运行记录；决定 `writeback`、`proposal`、`none-with-reason` 或 `blocked`；只有可复用学习才写回规则，不能把聊天总结冒充闭环。

## 包结构

默认文件：

- `SKILL.md`：轻入口，负责触发和执行契约。
- `references/`：领域规则、产品模型、能力路线、来源抽象、评测方法、发布门禁。
- `assets/`：可填写模板、工作表、结构数据或提示词简报。
- `scripts/`：确定性校验、转换、渲染或包检查。
- `evals/`：触发评测和回归用例。
- `examples/`：小而真实的输入/输出示例，不写私有历史、内部评分或假运行证据。

只有当新文件能防止具体失败，或能让 Skill 更容易跑通时才添加。不要为了保存研究笔记而新增参考文件。

## 硬停止

遇到以下情况先停止并说明阻塞：

- 任务只是一次性提示词，不是可重复工作流。
- 领域表面靠猜，没有用户材料、本地证据或当前来源证据支撑。
- 多模态 Skill 没有本地能力清单和输出证据路线。
- 需要用户多轮决策或 MVP 确认，却没有原生选择工具、降级等待界面、确认状态字段和批量生成停止规则。
- 包依赖生成文件，但没有办法证明文件、截图、媒体或渲染结果存在。
- 触发范围和另一个活跃技能包重叠，却没有路由边界。
- 设计会暴露私有评测历史、内部复盘、实现伤痕，或让人看出模仿某个外部项目。

## 验证

在包根目录运行：

```bash
python scripts/check_meta_skill_package.py .
python scripts/check_closed_loop.py .
```

如果生成的包有自己的脚本，也要按实际产物运行。验证时必须分清结构检查、生成产物证据、运行/工具证据和人工验收；一个层面的通过不能替代全部通过。

## 最终报告

用中文报告：改了哪些文件、包决策、触发边界、渐进加载图、校验命令、证明层级、闭环决策和剩余风险。给一个小的前后对照或输出片段，让用户能判断这个技能包是否真的更容易使用。
