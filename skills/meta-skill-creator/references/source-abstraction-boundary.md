# Source Abstraction Boundary

## Purpose

Use outside or internal examples only as abstract evidence about quality, failure modes, packaging discipline, and verification. Do not preserve source names, directory signatures, examples, visual systems, prompt wording, target-role labels, stakeholder labels, or sales language in public Skill packages.

## Allowed Abstractions

1. Progressive disclosure: keep the entry lean and route details to references.
2. Package discipline: separate trigger rules, contracts, assets, scripts, evals, and examples.
3. Visible artifacts: examples should show realistic outputs, not empty templates.
4. Deterministic helpers: scripts and validators prevent repeated manual misses.
5. Trigger discipline: descriptions are routing contracts and need eval coverage.
6. Baseline comparison: prove the Skill changes output quality or execution reliability.
7. Claim boundaries: unsupported tools, missing evidence, and platform limits must be visible.
8. Case variables: role labels, audience labels, company names, department names, and one-run acceptance phrases become configurable fields or examples, not fixed scope.

## Forbidden Carryover

- No source project names or creator names.
- No copied prompt structure, titles, examples, visual systems, page layouts, or commercial language.
- No hardcoded stakeholder or target-role labels from a single case, such as boss/sales/teacher/operator, unless the user explicitly asks for a role-specific skill or the evidence map justifies role-locked scope.
- No case-specific rejection rule such as "the sales section must contain X" unless that role-specific rule is the actual durable product contract.
- No star count, popularity, course reputation, or social proof as a quality claim.
- No internal review score, incident history, or private acceptance state in public-facing package instructions.

## Local Translation

| Abstract pattern | Local package expression |
|---|---|
| Compact runtime entry | `SKILL.md` routing and hard stops |
| Contract-first design | `references/skill-contract.md` |
| Package plan | `assets/package-plan-template.md` |
| Eval method | `references/evaluation-method.md` and `evals/` |
| Tool route evidence | `references/multimodal-tooling.md` |
| Distribution gate | `references/release-gate.md` |
