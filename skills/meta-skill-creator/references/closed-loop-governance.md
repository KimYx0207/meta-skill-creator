# 闭环治理

`meta-skill-creator` 的目标不是一次性生成一个 skill 文件夹，而是让每次技能化都能形成可复查、可复用、可改进的产品循环。

## 闭环定义

一个 skill 包只有同时满足下面四件事，才算进入闭环：

1. 有稳定的意图核心：用户是谁、压力场景是什么、最终产物是什么、成功标准是什么。
2. 有可检查的证据链：领域研究、工具能力、产物证据、验证命令、人工确认分层记录。
3. 有运行记录：每次验收或失败都能说明读了什么、产出了什么、验证了什么、缺了什么。
4. 有下一轮动作：明确 `writeback`、`proposal`、`none-with-reason` 或 `blocked`，不能只写“下次优化”。

## 原创循环

```text
Intent Core
-> Evidence Fetch
-> Product Surface
-> Package Contract
-> Build Pass
-> Evidence Review
-> Runtime / Artifact Verification
-> Loop Decision
-> Writeback or Next Proposal
-> Updated Skill Contract
```

这条循环必须保持轻入口：`SKILL.md` 只负责路由和硬门，细节放到 references、assets、scripts、evals、examples。闭环不是把主文件写长，而是让每个长期学习点都有归属。

## 阶段契约

| 阶段 | 必须留下什么 | 不通过时回到哪里 |
|---|---|---|
| Intent Core | 原始意图、用户、最终产物、成功标准、非目标 | 回到意图澄清 |
| Evidence Fetch | 已读证据、不可得证据、反证、会改变设计的事实 | 回到研究 |
| Product Surface | 用户第一眼看到的产物、原生媒介、素材真假边界 | 回到表面发现 |
| Package Contract | 触发、输入输出、文件地图、失败模式、验证路线 | 回到包计划 |
| Build Pass | 实际文件、资产、脚本、评测用例 | 回到构建 |
| Evidence Review | 结构、产物、运行、人工确认四层证据判断 | 回到评审 |
| Verification | 命令、日志、文件、截图、导出物或人工确认 | 回到验证 |
| Loop Decision | 写回、提案、不写回原因、阻塞原因 | 回到闭环决策 |

## 写回决策

每次验收后必须四选一：

- `writeback`：发现了长期规则，直接写回 source skill 的 reference、template、validator、eval 或 example。
- `proposal`：发现了长期规则，但需要用户或 reviewer 决策，先写改进提案。
- `none-with-reason`：本次只是一次性状态，没有可复用学习，写清原因。
- `blocked`：缺少真实证据、工具、权限、人工确认或运行产物，不能闭环。

禁止把聊天总结、记忆写入或漂亮复盘当作闭环。闭环必须改变可执行规则，或明确说明为什么不应该改变。

## 证据分层

| 层级 | 能证明什么 | 不能证明什么 |
|---|---|---|
| Structure | 文件存在、frontmatter、必需资源和关键短语 | 产品质量 |
| Contract | 输入输出、触发、边界、失败模式 | 真实运行 |
| Artifact | 产物文件、截图、导出物、可见页面 | 用户满意 |
| Runtime | 宿主工具、脚本、MCP、原生能力真实执行 | 长期稳定 |
| Human | 用户或 reviewer 确认 | 自动回归 |

任何最终报告都要说明自己处在哪一层。结构通过不能替代运行通过；运行通过也不能替代用户确认。

## 漂移信号

出现下面任一信号时，必须进入下一轮闭环，而不是继续局部补丁：

- 同类失败第二次出现。
- 用户纠正的是同一个质量问题。
- 结构校验通过但真实产物不可用。
- 触发范围与另一个 skill 重叠。
- 依赖宿主能力，但没有宿主执行证据。
- 生成了新模板，却没有 validator 或 acceptance 字段接住。
- 外部事实或平台规则发生变化。

## 原创边界

外部材料只允许转成抽象机制，例如“需要跨平台契约”“需要安装模拟”“需要证据一致性检查”。不允许复制外部项目名称、目录命名、页面结构、营销句、示例任务、报告布局或专有术语。

吸收外部材料时必须做三步：

1. 抽象机制：这个机制防止什么失败？
2. 本地重写：用本项目自己的领域语言和文件边界表达。
3. 可执行化：落到 validator、template、eval、example 或 release gate。

如果某个想法只能靠保留对方命名才说清，说明还没有吸收，只是搬运，必须放弃。

## 最小闭环产物

每个准备交付的 skill 至少要有：

- `assets/loop-run-record-template.md` 填写后的运行记录。
- `references/closed-loop-governance.md` 中的写回决策。
- validator 或 review checklist 能检查闭环字段。
- 至少一个 `nextRunReuseKey` 或 `none-with-reason`。
- 如果有失败，失败必须绑定预防规则和回归检查。

