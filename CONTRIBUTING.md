# Contributing

This repository publishes `meta-skill-creator` as a clean source package. The source of truth is:

- `skills/meta-skill-creator/`

Do not commit runtime projections, local state, generated graph output, acceptance scratch space, payment images, or machine-specific paths.

## Workflow

Use this sequence for non-trivial changes:

1. Critical Thinking: classify the request as skill design, package maintenance, documentation, validation, or release preparation.
2. Fetch: read the relevant `SKILL.md`, direct references, validators, examples, and user-provided material.
3. Deep Thinking: map package boundaries, runtime compatibility, evidence layers, originality risks, and release risks.
4. Review: run validators and report which proof layer passed.

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
