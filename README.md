# Meta Skill Creator

Meta Skill Creator is an Agent Skill package for designing, refactoring, and reviewing reusable skills.

It helps an agent decide whether a repeated workflow deserves to become a skill, then guides domain research, product-surface design, package structure, validation, release gates, and closed-loop writeback.

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
| `CONTRIBUTING.md` | Maintainer workflow and verification rules |

## Method

```mermaid
flowchart LR
    C["Critical Thinking<br/>Classify the request"] --> F["Fetch<br/>Gather decision-grade evidence"]
    F --> D["Deep Thinking<br/>Design package and gates"]
    D --> R["Review<br/>Separate proof layers"]
    R --> L["Loop<br/>Write back, propose, defer, or block"]
```

## Install

Install the skill by copying the source package into the skill directory used by your runtime.

Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R skills/meta-skill-creator ~/.claude/skills/meta-skill-creator
```

Codex project skill:

```bash
mkdir -p .codex/skills
cp -R skills/meta-skill-creator .codex/skills/meta-skill-creator
```

Codex-compatible user skill:

```bash
mkdir -p ~/.agents/skills
cp -R skills/meta-skill-creator ~/.agents/skills/meta-skill-creator
```

## Validate

Run from the repository root:

```bash
python skills/meta-skill-creator/scripts/check_meta_skill_package.py skills/meta-skill-creator
python skills/meta-skill-creator/scripts/check_closed_loop.py skills/meta-skill-creator
```

These checks prove package structure and closed-loop contract coverage. They do not prove public release readiness by themselves. Public readiness still needs clean-session acceptance, baseline comparison, real artifact/runtime evidence when relevant, and human review.

## Quality Bar

A usable skill package should include:

- a concise `SKILL.md`
- domain research before design
- a clear final artifact chain
- trigger and output evaluation
- at least one non-document asset or deterministic script
- release gates that separate structure, runtime, artifact, and human evidence
- a loop decision: `writeback`, `proposal`, `none-with-reason`, or `blocked`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the maintainer workflow, editing rules, originality boundary, and release checks.

## License

MIT. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
