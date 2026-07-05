# Meta Skill Creator

> English version: [README.en.md](README.en.md)

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
| `docs/images/` | 联系方式和支持二维码 |
| `CONTRIBUTING.md` | 维护流程和发布校验规则 |

## 方法

```text
Critical Thinking -> Fetch -> Deep Thinking -> Review -> Loop
```

这个流程的重点是分清证明层级：

- Critical Thinking：先判断请求类型和是否值得技能化。
- Fetch：读取会改变决策的证据，而不是凭熟悉样例套模板。
- Deep Thinking：设计包结构、产物链、工具路线和发布门禁。
- Review：区分结构校验、运行证据、产物证据和人工确认。
- Loop：写回、提案、延后或阻塞，不能把聊天总结冒充闭环。

## 联网深度研究怎么做

深度研究不是只读本地文件。只要任务涉及会变化的信息，就必须联网；例如平台规则、API/SDK、运行时能力、开源项目、竞品实践、政策合规、价格、模型能力、工具可用性和社区最佳实践。

一次合格的联网研究至少要产出：

1. **来源地图**：官方文档、开放标准、高信号项目、用户材料、失败案例和反证分别查了什么。
2. **关键结论**：哪些事实会改变 skill 的触发边界、产物链、工具路线、文件结构、评测或发布门禁。
3. **反证和不确定性**：哪些信息过期、冲突、不适用于当前宿主，或需要用户确认。
4. **写入位置**：结论进入 `SKILL.md`、`references/`、`assets/`、`scripts/`、`evals/`、`examples/`，还是只作为本次运行记录。

如果当前环境不能联网，必须写清楚“哪些在线来源不可用”。这时可以给出 `research-needed`、`blocked` 或带假设的设计草案，但不能宣称 ready。

## 什么能写进 Skill

研究结果必须先通过写入判断，不能把看到的资料直接塞进 skill：

| 写入位置 | 能写什么 | 不能写什么 |
|---|---|---|
| `SKILL.md` | 触发边界、第一动作、硬停止、资源路由、验证口径 | 长篇研究、平台细节、一次性总结 |
| `references/` | 领域规则、证据模型、产物链、失败模式、发布门禁 | 未抽象的竞品结构、别人的话术、私有运行日志 |
| `assets/` | 可复用模板、brief、checklist、运行记录表 | 只对一次任务有用的草稿 |
| `scripts/` | 可重复、确定性的校验/转换/生成动作 | 需要模型自由发挥的判断 |
| `evals/` | 触发、误触发、近似输入、输出质量和回归用例 | 只证明“看起来不错”的样例 |
| `examples/` | 小而真实的输入/输出示例 | 私有客户信息、假运行证据、内部评分 |

写入的最低门槛：它必须能防止一个具体失败，或让下一次运行更稳定、更可验证。否则只记录为运行证据，不写进长期规则。

## 公开依据

- [Anthropic: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Claude Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [OpenAI Codex Agent Skills docs](https://developers.openai.com/codex/skills)
- [OpenAI API Skills docs](https://developers.openai.com/api/docs/guides/tools-skills)
- [Agent Skills open specification](https://agentskills.io/specification)

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

- 轻入口但证据重的 `SKILL.md`
- 先做领域研究，再做设计
- 必要时联网深度研究，并记录来源、关键结论和反证
- 明确的最终产物链路
- 触发评测和输出评测
- 至少一个非文档资产或确定性脚本
- 能区分结构、运行、产物、人工确认的发布门禁
- 闭环决策：`writeback`、`proposal`、`none-with-reason` 或 `blocked`

## 联系方式

<div align="center">

扫码联系作者。

<img src="docs/images/contact-qr.png" width="720" alt="联系二维码">

微信公众号：<strong>老金带你玩AI</strong>

</div>

## 支持

<div align="center">

如果 Meta Skill Creator 对你有帮助，可以请作者喝杯咖啡。

<table>
<tr><th>微信支付</th><th>支付宝</th></tr>
<tr>
<td align="center"><img src="docs/images/wechat-pay.jpg" width="260" alt="微信收款码"></td>
<td align="center"><img src="docs/images/alipay.jpg" width="260" alt="支付宝收款码"></td>
</tr>
</table>

</div>

## 贡献

维护流程、编辑规则、原创边界和发布校验见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 协议

MIT。见 [LICENSE](LICENSE) 和 [NOTICE](NOTICE)。
