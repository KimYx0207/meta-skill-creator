# Meta Skill Creator

Meta Skill Creator is an Agent Skill package for designing, refactoring, and reviewing reusable skills.

When a user explicitly asks to create, refactor, or review a skill, it enters that route directly. The package then guides domain research, product-surface design, package structure, validation, release gates, and closed-loop writeback.

This is not a prompt beautifier. A good skill package should prove what it does, where it runs, what evidence it used, and what must happen after a failure.

## What This Repository Contains

| Path | Purpose |
|---|---|
| `skills/meta-skill-creator/` | Source skill package |
| `skills/meta-skill-creator/SKILL.md` | Lightweight trigger and routing entry |
| `skills/meta-skill-creator/references/` | Domain, product, evaluation, release, and loop rules |
| `skills/meta-skill-creator/assets/` | Fillable templates for package planning and run records |
| `skills/meta-skill-creator/scripts/` | Package and loop validators |
| `skills/meta-skill-creator/evals/` | Trigger evaluation cases |
| `skills/meta-skill-creator/examples/` | Small input/output examples |
| `docs/images/` | Contact and support QR images |
| `CONTRIBUTING.md` | Maintainer workflow and verification rules |

## Method

```text
Critical Thinking -> Fetch -> Deep Thinking -> Review -> Loop
```

The point of this flow is to keep proof layers separate:

- Critical Thinking: identify the request type and route an explicit skill request directly into creation.
- Fetch: read evidence that can change the decision, instead of copying a familiar example.
- Deep Thinking: design package structure, artifact chain, tool route, and release gates.
- Review: separate structure checks, runtime evidence, artifact evidence, and human confirmation.
- Loop: write back, propose, defer, or block; do not treat a chat summary as closure.

## Top-Level Creation Rule Acceptance Criteria

A top-level creation rule is not a longer prompt. It is an executable and reviewable stage contract. The full standard is in `skills/meta-skill-creator/references/creation-rule-standard.md`.

| Stage | Required output | Pass standard |
|---|---|---|
| Critical Thinking | Task class, user result, scope, non-goals, risk, first evidence route | An explicit creation request is not rejected; the next step gathers evidence for the right design instead of writing from a generic template |
| Fetch | Source map, evidence read, unavailable evidence, key findings, counterevidence, decision impact | Each key design judgment is evidence-backed or assumption-marked; online research is used when required |
| Deep Thinking | Package contract, artifact chain, tool route, write-in destination, acceptance plan | Each new file or rule prevents a named failure mode, and acceptance can be checked |
| Review | Validation commands, proof layers, artifact/runtime evidence, ready level, loop decision | Structure pass is not treated as quality proof; failures become writeback, proposal, deferral, or blocked status |

Minimum bar: a creation rule without stage outputs, pass/fail conditions, failure handling, and loop decision is not accepted.

## How Network Deep Research Works

Deep research is not local-file reading only. If the task depends on information that can change, the agent must use online research. This includes platform rules, APIs/SDKs, runtime capabilities, open-source projects, competitor practice, policy/compliance, pricing, model capabilities, tool availability, and current community practice.

A qualified online research pass should produce:

1. **Source map**: which official docs, open standards, high-signal projects, user material, failure cases, and counterexamples were checked.
2. **Key findings**: which facts change trigger boundaries, artifact chain, tool route, file structure, evals, or release gates.
3. **Counterevidence and uncertainty**: what is stale, conflicting, host-specific, or still needs user confirmation.
4. **Write-in destination**: whether the finding belongs in `SKILL.md`, `references/`, `assets/`, `scripts/`, `evals/`, `examples/`, or only the run record.

If the environment cannot access the network, state which online sources were unavailable. In that case the output may be `research-needed`, `blocked`, or an assumption-marked design candidate, but it must not claim release readiness.

## What Can Be Written Into A Skill

Research findings must pass a write-in decision before becoming durable skill rules:

| Destination | Write this | Do not write this |
|---|---|---|
| `SKILL.md` | Trigger boundaries, first action, hard stops, resource routing, verification lens | Long research, platform details, one-off summaries |
| `references/` | Domain rules, evidence model, artifact chain, failure modes, release gates | Unabstracted competitor structure, copied wording, private run logs |
| `assets/` | Reusable templates, briefs, checklists, run-record forms | Drafts useful for only one task |
| `scripts/` | Repeatable deterministic checks, transforms, or generation helpers | Judgment that requires model discretion |
| `evals/` | Trigger, false-positive, near-miss, output-quality, and regression cases | Examples that only prove the output looked good once |
| `examples/` | Small realistic input/output examples | Private customer data, fake run evidence, internal scores |

Minimum write-in bar: the finding must prevent a concrete failure or make the next run more stable and verifiable. Otherwise, keep it as run evidence and do not turn it into a long-term rule.

## Public Sources

- [Anthropic: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Claude Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [OpenAI Codex Agent Skills docs](https://developers.openai.com/codex/skills)
- [OpenAI API Skills docs](https://developers.openai.com/api/docs/guides/tools-skills)
- [OpenAI Prompt Guidance](https://developers.openai.com/api/docs/guides/prompt-guidance)
- [OpenAI Evaluation Best Practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Agent Skills open specification](https://agentskills.io/specification)

## Install

First download this repository and enter the repository root. That is the directory that contains `skills/meta-skill-creator`.

Windows PowerShell:

```powershell
git clone https://github.com/KimYx0207/meta-skill-creator.git
Set-Location meta-skill-creator
Test-Path .\skills\meta-skill-creator\SKILL.md
```

If the last command returns `True`, install the skill.

Claude Code global skill:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse -Force -Path ".\skills\meta-skill-creator" -Destination "$env:USERPROFILE\.claude\skills\meta-skill-creator"
```

Codex project skill, installed into another project:

```powershell
$Project = "D:\codex_project\test-kim-skillcreater"
New-Item -ItemType Directory -Force -Path "$Project\.codex\skills" | Out-Null
Copy-Item -Recurse -Force -Path ".\skills\meta-skill-creator" -Destination "$Project\.codex\skills\meta-skill-creator"
```

Codex-compatible user skill:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -Recurse -Force -Path ".\skills\meta-skill-creator" -Destination "$env:USERPROFILE\.agents\skills\meta-skill-creator"
```

macOS / Linux / Git Bash:

```bash
git clone https://github.com/KimYx0207/meta-skill-creator.git
cd meta-skill-creator
test -f skills/meta-skill-creator/SKILL.md
```

Claude Code global skill:

```bash
mkdir -p ~/.claude/skills
cp -R skills/meta-skill-creator ~/.claude/skills/meta-skill-creator
```

Codex project skill, installed into the current project:

```bash
mkdir -p .codex/skills
cp -R skills/meta-skill-creator .codex/skills/meta-skill-creator
```

Codex-compatible user skill:

```bash
mkdir -p ~/.agents/skills
cp -R skills/meta-skill-creator ~/.agents/skills/meta-skill-creator
```

Common error: if your current directory is not this repository root, `skills/meta-skill-creator` does not exist. Clone the repository first, or change the `Copy-Item` / `cp` source path to the repository path you downloaded.

## Validate

Run from the repository root:

```bash
python skills/meta-skill-creator/scripts/check_meta_skill_package.py skills/meta-skill-creator
python skills/meta-skill-creator/scripts/check_closed_loop.py skills/meta-skill-creator
```

These checks prove package structure and closed-loop contract coverage. They do not prove public release readiness by themselves. Public readiness still needs clean-session acceptance, baseline comparison, real artifact/runtime evidence when relevant, and human review.

## Quality Bar

A usable skill package should include:

- a light-entry but evidence-heavy `SKILL.md`
- domain research before design
- network deep research when facts may have changed, with sources, key findings, and counterevidence
- a clear final artifact chain
- trigger and output evaluation
- at least one non-document asset or deterministic script
- release gates that separate structure, runtime, artifact, and human evidence
- a loop decision: `writeback`, `proposal`, `none-with-reason`, or `blocked`

## Contact

<div align="center">

Scan the QR code to contact the author.

<img src="docs/images/contact-qr.png" width="720" alt="Contact QR">

WeChat Official Account: <strong>老金带你玩AI</strong>

</div>

## Support

<div align="center">

If Meta Skill Creator has been useful, support the project with a coffee.

<table>
<tr><th>WeChat Pay</th><th>Alipay</th></tr>
<tr>
<td align="center"><img src="docs/images/wechat-pay.jpg" width="260" alt="WeChat Pay QR"></td>
<td align="center"><img src="docs/images/alipay.jpg" width="260" alt="Alipay QR"></td>
</tr>
</table>

</div>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the maintainer workflow, editing rules, originality boundary, and release checks.

## License

MIT. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
