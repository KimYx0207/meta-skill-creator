# 交互式决策与 MVP 产品化 Skill 模式

## 什么时候读

当要创建或重构的 skill 需要在用户意图模糊时逐步补全方向、通过宿主原生弹框让用户做多次选择、先确认一个 MVP 样张/封面/首屏/关键参数，再批量生成完整案例或文件包时读取本文件。

## 目标

这类 skill 的核心不是“问更多问题”，而是把不确定性压缩成少量会改变结果的产品决策，并在 MVP 被确认后立刻进入生产线。用户不应该被问一串开放题，也不应该在确认关键方向后又被问“要不要做到完整”。

合格设计必须回答：

- 哪些输入可以由 AI 默认补全，哪些必须由用户选择。
- 哪些选择应放进 Codex `request_user_input`、Claude Code `AskUserQuestion` 或宿主等价原生选择界面。
- Markdown 选择卡什么时候作为降级等待界面。
- MVP 是什么：封面图、首屏样张、样式稿、数据口径、流程图、页面机制或其他最小可验收样张。
- MVP 确认后可以并行生成哪些内容。
- 哪些状态不能冒充 `human_confirmed`。
- 生成完成后用什么证据证明文件、图片、预览或媒体确实存在。

## 决策状态

所有交互式 skill 必须显式记录决策状态：

```text
human_confirmed：用户原话、Codex request_user_input、Claude Code AskUserQuestion 或宿主等价选择工具返回。
explicit_auto_permission：用户明确说“你定/不用问/按推荐直接做”，同时记录 AI 推荐理由和风险。
blocked_pending_human_decision：缺少关键选择，必须停止，不能继续生成最终产物。
choice_confirmation_unverifiable：执行环境里看不到原生选择返回，也看不到后续用户消息，不能宣称已确认。
```

`推荐项`、`默认项`、`上一轮模型总结`、`HookPrompt scope`、`后台线程计划` 都不是人类确认。

## 原生决策面优先级

默认优先级：

1. 宿主原生选择工具：Codex `request_user_input`、Claude Code `AskUserQuestion`、ChatGPT 原生选择卡或等价可审计交互。
2. Markdown 决策卡：只在没有原生选择面时使用，输出后必须停止等待用户回复。
3. AI 自动选择：只有用户明确预授权时使用，状态写 `explicit_auto_permission`，不是 `human_confirmed`。

不要把 Markdown 卡片写成“已弹框”，也不要在没有工具返回时说“用户已选择”。

## 弹框设计原则

弹框只问会改变成品方向的问题。一个弹框最多承载 3-5 个互斥选项，必要时提供“混合/手动输入/按推荐继续”。不要把每个细节拆成独立问题造成用户疲劳。

每个选项必须包含：

- `label`：用户看得懂的选择名。
- `what_changes`：选它会改变什么产物。
- `recommended`：是否推荐，且只能推荐一个。
- `risk`：选择风险或适用边界。
- `next_action`：选中后下一步生成什么。

## 模糊意图补全矩阵

创建 skill 时，把用户模糊意图拆成下面的补全矩阵，并只把关键项放进弹框：

```text
目标：用户最终想拿什么。
受众：给谁看、什么时候看。
语气/风格：稳重、销售、真实、专业、艺术、极简等。
素材真实度：真实素材、模拟素材、抽象视觉、数据来源。
媒介表面：图文、演示文稿、网页、PDF、视频、仪表盘等。
验收瞬间：用户第一眼看什么，决定继续还是退回。
风险边界：平台合规、不可伪造、隐私、来源、导流、版权。
MVP 样张：最小可确认样张是什么。
批量范围：MVP 确认后一次性生成哪些组件。
```

## MVP 锁定门

MVP 不是一个随便的示例，而是批量生产前的最小决策合约。它必须同时锁定：

- 内容承诺：标题、封面字、核心结论、页面主张或数据口径。
- 视觉承诺：构图、主体、风格、留白、色彩、素材真实度。
- 结构承诺：后续页面/图片/章节/文件会怎样展开。
- 验收标准：缩略图可读、首屏方向明确、元素不遮挡、可编辑层成立等。
- 批量许可：确认后是否直接生成全套。

MVP 确认后的默认行为是执行生产线。不得再弹“这次要做到哪一步”“是否只做文案”“是否只做封面/首屏”之类范围降级问题，除非用户刚刚明确要求暂停或缩小范围。

## 并行生产线

MVP 确认后，skill 应把可并行事项拆开：

```text
内容线：标题组 / 正文 / 大纲 / 话术 / 标签 / 来源说明
视觉线：封面 / 内页 / 透明元素 / 图表氛围 / 图片资产
结构线：演示页面 / 图文页 / 文件包 / 工作台 / manifest
校验线：预览导出 / 可编辑层 / 图片证据 / 布局检查 / 平台风险
交付线：用户可见摘要 / 文件路径 / 缺口 / 下一步可改项
```

并行不等于跳过证据。每条线都必须能说明完成、部分完成或阻塞。

## 验收字段

交互式 MVP skill 至少生成或记录这些字段：

```json
{
  "decision_surface": "request_user_input | AskUserQuestion | markdown_fallback | explicit_auto_permission",
  "fuzzy_intent_completion": {
    "goal": "...",
    "audience": "...",
    "style": "...",
    "material_truth_level": "...",
    "risk_boundary": "..."
  },
  "mvp_gate": {
    "mvp_type": "cover | first_slide | style_draft | data_slice | prototype",
    "presented_to_user": true,
    "confirmed_before_batch": true,
    "confirmation_evidence": "...",
    "batch_generation_allowed": true
  },
  "batch_plan": {
    "content_jobs": [],
    "visual_jobs": [],
    "assembly_jobs": [],
    "validation_jobs": []
  },
  "delivery_state": "complete | partial | blocked"
}
```

## 一票否决

- 需要人类选择，却没有原生选择工具返回或可见用户回复，就声称已确认。
- MVP 没有展示给用户，却开始批量生成。
- 用户确认 MVP 后，又把范围降级成文案、提示词或单张图。
- 生成类 skill 把旧文件、旧图、示例图写成本轮新产物。
- 多模态 skill 没有 Image2/宿主原生能力路线和降级证据。
- 文件型 skill 没有文件存在、导出预览或校验结果，却写“已完成”。

## 写入包结构建议

- `SKILL.md`：只写触发、第一动作、MVP 门和硬停止。
- `references/interactive-mvp-*.md`：写详细决策流程、状态和一票否决。
- `assets/*-decision-card-template.md`：写可复制的 Markdown 降级卡。
- `assets/*-mvp-gate-template.json`：写机器可校验的 MVP 状态。
- `scripts/check-*-mvp-state.*`：校验是否缺确认、伪确认或确认后未批量生成。
- `evals/`：放模糊输入、预授权输入、缺工具输入、确认后批量生成输入、伪确认失败输入。
