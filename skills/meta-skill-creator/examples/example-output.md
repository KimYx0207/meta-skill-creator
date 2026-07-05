# Example Output: Skill Design Board

## Domain Research Brief

- Raw user intent: "make a customer-support follow-up skill from scattered notes."
- Suspected domain: customer support follow-up and internal handoff.
- Confidence: medium-high after support workflow examples, escalation rules, and privacy boundaries are reviewed.
- Users / roles: support agent, account owner, operations lead, or service manager.
- Pressure moment: customer history is scattered, tone must be careful, and the next owner needs enough context to act.
- Native artifacts: customer-facing reply, internal handoff checklist, escalation decision, missing-information list, and validation manifest.
- Work surface: text response plus structured checklist file.
- Must not simulate: fake commitments, fake approvals, unverified resolution status, or private customer data not present in the input.
- Decision: make skill; publish only after baseline evidence and a clean acceptance run are tested.

## Skillization Decision

- Decision: make skill.
- Reason: high-frequency workflow, stable input/output shape, repeatable package structure, and ordinary prompts often stop at a reply draft without handoff or escalation checks.

## User Result

- User: support operator handling scattered customer context.
- Final artifact: sendable reply, internal handoff checklist, escalation recommendation, and validation manifest.
- Three-minute visible result: first reply draft plus risk/missing-info checklist.

## Core Mechanism

Use a `support-follow-up-workbench`: convert scattered notes into facts, uncertainties, customer-facing language, owner handoff, escalation rule, and validation checks.

## Package Plan

```text
support-follow-up-skill/
  SKILL.md
  references/domain-rules.md
  references/tone-and-escalation.md
  references/failure-modes.md
  scripts/validate-follow-up.py
  assets/follow-up-brief-template.md
  examples/example-input.md
  examples/example-output.md
  evals/trigger-eval.json
  evals/output-eval.md
  evals/baseline-compare.md
  verification-summary.md
```

## Required Evals

- Trigger eval: should trigger on reusable support follow-up package requests; should not trigger on one-off reply polishing.
- Output eval: missing facts, angry customer, conflicting internal notes, privacy-sensitive details, and escalation uncertainty.
- Baseline: compare ordinary prompt reply against skill-produced reply plus handoff checklist.
- Regression: previous version versus new version on factual grounding, tone, escalation, and missing-info handling.

## Release Gate Status

- Structure: planned.
- Trigger: not run.
- Output: not run.
- Baseline: not run.
- Acceptance: not run.
- Evidence status: design candidate; publish after clean-session acceptance and baseline proof.
