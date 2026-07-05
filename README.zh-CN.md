# Meta Skill Creator

Meta Skill Creator 是一个用来设计、重构、评审 Agent Skill 的技能包。

它不是“美化提示词”的工具，而是帮助 Agent 判断一个重复工作流是否值得技能化，并把它推进到领域研究、产品表面、包结构、验证、发布门禁和闭环写回。

一个合格的 skill 包不应该只看起来完整，还要能说明：它解决什么问题、读了什么证据、在哪里运行、怎么验证、失败后写回哪里。

## 仓库内容

| 路径 | 用途 |
|---|---|
| `skills/meta-skill-creator/` | 源 skill 包 |
| `skills/meta-skill-creator/SKILL.md` | 轻量触发和路由入口 |
| `skills/meta-skill-creator/references/` | 领域、产品、评测、发布和闭环规则 |
| `skills/meta-skill-creator/assets/` | 包计划和运行记录模板 |
| `skills/meta-skill-creator/scripts/` | 包结构和闭环校验脚本 |
| `skills/meta-skill-creator/evals/` | 触发评测用例 |
| `skills/meta-skill-creator/examples/` | 小型输入/输出示例 |
| `CONTRIBUTING.md` | 维护流程和发布校验规则 |

## 方法

```mermaid
flowchart LR
    C["Critical Thinking<br/>判断请求类型"] --> F["Fetch<br/>收集会改变决策的证据"]
    F --> D["Deep Thinking<br/>设计包和门禁"]
    D --> R["Review<br/>区分证明层级"]
    R --> L["Loop<br/>写回、提案、延后或阻塞"]
```

## 安装

把源 skill 包复制到对应运行时的 skill 目录即可。

Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R skills/meta-skill-creator ~/.claude/skills/meta-skill-creator
```

Codex 项目级 skill:

```bash
mkdir -p .codex/skills
cp -R skills/meta-skill-creator .codex/skills/meta-skill-creator
```

Codex 兼容用户级 skill:

```bash
mkdir -p ~/.agents/skills
cp -R skills/meta-skill-creator ~/.agents/skills/meta-skill-creator
```

## 校验

在仓库根目录运行：

```bash
python skills/meta-skill-creator/scripts/check_meta_skill_package.py skills/meta-skill-creator
python skills/meta-skill-creator/scripts/check_closed_loop.py skills/meta-skill-creator
```

这些检查只能证明包结构和闭环契约存在，不能单独证明公开发布就绪。公开发布还需要干净会话验收、baseline 对比、真实产物/运行证据，以及人工评审。

## 质量标准

一个可用的 skill 包至少应该有：

- 简洁的 `SKILL.md`
- 先做领域研究，再做设计
- 明确的最终产物链路
- 触发评测和输出评测
- 至少一个非文档资产或确定性脚本
- 能区分结构、运行、产物、人工确认的发布门禁
- 闭环决策：`writeback`、`proposal`、`none-with-reason` 或 `blocked`

## 贡献

维护流程、编辑规则、原创边界和发布校验见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 协议

MIT。见 [LICENSE](LICENSE) 和 [NOTICE](NOTICE)。
