# 包计划模板

## 技能包名称

## 目录

## 为什么应该做成 Skill
- 领域研究简报决定：
- 可重复性：
- 专门流程：
- 可复用资产：
- 普通提示词的弱点：

## 文件地图

```text
<skill>/
  SKILL.md
  references/
    intent-domain-research.md 或 domain-rules.md
    multimodal-tooling.md（需要时）
  scripts/
  assets/
    multimodal-prompt-brief-template.md（需要时）
  examples/
  evals/
```

## 资源决策

| 文件 | 用途 | 防止的失败 | 读取/执行时机 |
|---|---|---|---|
| SKILL.md |  |  | 触发时 |
| references/intent-domain-research.md 或 references/domain-rules.md |  | 猜领域 / 猜工作流 | 接收输入 / 设计 |
| references/evidence.md |  |  | Fetch / 设计 |
| references/failure-modes.md |  |  | 输入有风险时 |
| references/multimodal-tooling.md |  | 缺本地工具/MCP 路线，或多模态提示词太泛 | 多模态/工具路线设计 |
| scripts/<name> |  |  | 校验 / 构建 |
| assets/<name> |  |  | 产物构建 |
| assets/multimodal-prompt-brief-template.md |  | 图片、媒体、文档提示词太泛 | 提示词/简报构建 |
| evals/<name> |  |  | 验证 |

## 非文档资产理由

## 示例产物计划

## 本地能力与多模态计划
- 是否产出非纯文本或渲染结果：
- 宿主工具：
- MCP / 插件工具：
- 既有本地脚本 / 资产：
- 优先路线：
- 降级路线：
- Image2 / 宿主原生能力降级到 MCP 前的证据：
- 必须保留的输出证据：

## 发布门禁计划
