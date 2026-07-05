# Experience Surface Model

This is not the first design pass. Read `references/intent-domain-research.md` first.

The old failure mode is making a generic skill package before understanding the user's actual domain. A product-grade skill first researches the intent domain, then names the surface where the result lives: social platform, document, dashboard, presentation, spreadsheet, chat reply, video, workflow handoff, local tool, or another domain-native surface.

## 1. Surface After Domain Research

Before writing `SKILL.md`, use the Domain Research Brief to answer:

1. What platform, channel, or work surface is this for?
2. What does the user finally see, send, publish, present, or operate?
3. What medium is native to that surface: image, text, video, slide, table, file, HTML, checklist, script output, or a bundle?
4. What does the audience judge first?
5. Which part must be generated, and which part must be requested from the user as real material?
6. Which current host tools, MCP/plugin tools, scripts, or local assets can generate or render the native artifact?
7. What output evidence proves the artifact was really generated, exported, rendered, or displayed?
8. What is the "looks real / feels useful" standard on this surface?
9. What would make the output obviously AI, fake, unusable, or off-platform?

If these answers are unclear, return `research-needed`; do not borrow a surface from any familiar example.

## 2. Artifact Chain

Use this chain before package planning:

```text
raw user intent
-> Domain Research Brief
-> user and pressure moment
-> platform/work surface
-> audience expectation
-> component map
-> local capability inventory and tool route
-> generation pipeline
-> final artifact package
-> acceptance gate
```

The component map must name the real deliverables. For example:

- Social image-text platform: cover, image/page scripts, image prompts or generated images, title, body, hashtags, platform-safe interaction boundary, publish brief.
- Presentation workflow: preview, page map, slide HTML/PDF/images, speaker notes, audience questions, export manifest.
- Long-form article platform: title set, cover card, Markdown draft, HTML/mobile preview, publish checklist, image slots.
- Short video: hook, voiceover, shot list, subtitles, cover frame, teleprompter, publish brief.
- Excel insight: source table, cleaned fields, charts, insight brief, decision recommendation, privacy notes.
- Factory inspection corrective action: finding list, root-cause notes, evidence photos, responsible owner, deadline,整改 plan, verification checklist, risk boundary. Only use this after evidence confirms the workflow.
- Pet clinic follow-up: patient/pet record inputs, visit summary, medication boundary, reminder schedule, owner message, escalation signal. Only use this after evidence confirms the workflow and safety boundary.

## 3. Social Image-Text Worked Example After Research

### Platform Surface

This example represents a mobile social content surface where image-text notes are judged quickly in a feed. The first visible layer is cover image plus title; the user then swipes through image pages and reads the caption/body. The skill must design the image-text package, not only the written caption.

Current public references used for this surface model:

- public platform guidance for cover, post pages, and detail pages,
- creator guides that emphasize cover/title connection, vertical mobile visuals, and image plus text working together,
- user failure evidence showing that copy-only workflows miss visual prompts, generated images, mobile small-preview checks, and platform-safe interaction boundaries.

### Input

```text
主题：我最近用 AI 做工作复盘，想发到图文平台，不想像广告。
素材：一些真实工作场景、截图可以后补。
目标：让同类职场人收藏，并在公开评论里讨论模板方法。
```

### Correct Artifact Chain

```text
theme
-> target reader:职场个人 IP / 想提效的人
-> note intent:经验复盘 + 可公开讨论的模板方法
-> cover promise:一句话说清收益但不夸张
-> visual route:职场桌面真实感 / 信息卡 / 截图打码
-> local tool route: Image2 / host-native image tool first; image MCP only after unavailable/failure proof; static card only as fallback
-> image package:1 cover + 6-8 inner pages
-> text package:title + body + tags + comment replies + interaction boundary
-> publish package:PNG/SVG cards + manifest + publish brief
-> acceptance:手机小图可读、标题兑现、素材真实、无假截图、无夸张承诺
```

### Required Output Components

1. Platform and audience judgment.
2. Theme-to-note angle selection.
3. Cover concept and cover text.
4. Cover image prompt or generated cover image.
5. Page-by-page image script for 6-8 image cards.
6. Image prompts for each page, with tool variants if useful.
7. Body caption that sounds like a real person, not an ad.
8. Hashtags related to the actual topic.
9. Platform-safe comment replies and interaction boundary.
10. Material gap list: what must be real, what can be simulated, what cannot be simulated.
11. Publish package and final self-check.

### Failure Examples

Bad:

```text
给 10 个标题 + 一段正文 + 标签。
```

Why bad: it ignores the platform's image-text surface and leaves the user without cover, images, visual direction, or publishable cards.

Good:

```text
给 3 个选题角度，选 1 个主推角度；
生成封面字和 3:4 封面提示词；
生成 6-8 页图文脚本；
生成每页结构化图片提示词；
有 Image2 / host-native 生图工具时先生成封面/关键页并记录证据；只有 Image2 不可用或失败时，才降级到图片 MCP；
写正文、标签、平台安全互动边界；
输出素材缺口和发布前自检；
有工具时生成图文卡片包。
```

Why good: it follows the user's actual production job on the platform.

## 4. Design Rule

For any new skill, the package plan must include:

- Domain Research Brief.
- Surface Definition.
- Native Artifact Components.
- Local Capability Inventory.
- Multimodal Structured Brief when non-text artifacts are involved.
- Generation Pipeline.
- Material Truth Boundary.
- Acceptance Gate.

If these are missing, `meta-skill-creator` must return to Critical/Fetch and mark `research-needed` instead of writing the skill.
