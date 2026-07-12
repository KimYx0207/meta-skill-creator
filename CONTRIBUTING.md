# Contributing

This repository publishes `meta-skill-creator` as a clean source package. The source of truth is:

- `skills/meta-skill-creator/`

Do not commit runtime projections, local state, generated graph output, acceptance scratch space, payment images, or machine-specific paths.

## Workflow

Use this sequence for non-trivial changes:

1. Critical Thinking: route explicit skill creation, maintenance, validation, or release requests to the matching task class; record user result, scope, non-goals, risk, and first evidence route. Do not reject an explicit creation request because it looks one-off.
2. Fetch: read the relevant `SKILL.md`, direct references, validators, examples, user-provided material, graph/search anchors, current official sources when external facts matter, high-signal examples, and counterevidence.
3. Deep Thinking: map package boundaries, runtime compatibility, artifact chain, tool route, acceptance criteria, evidence layers, originality risks, and release risks before editing.
4. Review: run validators and report which proof layer passed: structure, contract, runtime/tool, artifact, baseline/regression, human review, and loop decision.

Top-level creation-rule work must also satisfy `skills/meta-skill-creator/references/creation-rule-standard.md`. A change that only makes the prose longer, without stage outputs and pass/fail criteria, is not accepted.

## Editing Rules

- Keep `SKILL.md` focused on trigger, first action, routing, hard stops, and validation.
- Put durable rules in `references/`, templates in `assets/`, deterministic checks in `scripts/`, trigger cases in `evals/`, and small examples in `examples/`.
- Treat external projects as research only. Do not copy their project names, directory schemes, prompts, examples, page structure, visual identity, or distinctive wording.
- Do not claim public readiness from structure checks alone.
- End acceptance or failure with one loop decision: `writeback`, `proposal`, `none-with-reason`, or `blocked`.

## Verification

Run from the repository root:

```bash
python skills/meta-skill-creator/scripts/check_meta_skill_package.py skills/meta-skill-creator
python skills/meta-skill-creator/scripts/check_closed_loop.py skills/meta-skill-creator
```

These checks cover package structure and closed-loop contract coverage. A release still needs clean-session acceptance, baseline comparison, real artifact or runtime evidence when relevant, and human review.
