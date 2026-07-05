# Evidence Model

Use this file to decide what evidence a generated skill package should collect before design, validation, or release. It is intentionally source-abstracted: public packages should keep durable principles and decision impacts, not private run logs, local machine state, or copied third-party wording.

## Evidence Card Shape

Each evidence card should answer:

- `source_type`: official documentation, open specification, high-signal example, user material, failure report, benchmark, or counterexample.
- `claim`: what the evidence says.
- `relevance`: why it changes this skill package.
- `confidence`: high, medium, or low.
- `counterevidence`: what might make the claim weaker.
- `decision_impact`: which trigger, reference, asset, script, eval, or release gate changes because of it.
- `translated_asset_or_eval`: where the learning appears in the package.

## Required Evidence Classes

### Official Or Platform Evidence

Use when the skill depends on a platform, runtime, file format, API, marketplace, policy, or public package standard.

Decision impact:

- define compatibility and installation boundaries
- prevent stale numeric limits or unsupported fields
- separate official behavior from community convention

### High-Signal Examples

Use when examples reveal quality bars, artifact shape, failure modes, or interaction patterns. Abstract the pattern; do not copy names, structure, examples, prompts, screenshots, visual identity, or marketing language.

Decision impact:

- choose final artifact chain
- define useful examples and non-examples
- improve evaluation rubrics

### User Material And Failure Evidence

Use when the user provides real workflow material, corrections, rejected outputs, acceptance criteria, or examples of past failure.

Decision impact:

- prioritize the user's real job over generic templates
- define hard stops and review gates
- decide whether a workflow deserves a reusable skill

### Benchmarks And Baselines

Use when claiming that the skill improves performance. A generated skill is not automatically better than a direct prompt; compare with-skill and without-skill runs when the claim matters.

Decision impact:

- add baseline runs
- set pass/fail thresholds
- avoid overclaiming release readiness

### Counterexamples

Use counterexamples to catch over-broad triggers, premature stopping, surface guessing, copied structure, or missing artifact evidence.

Decision impact:

- narrow trigger rules
- add eval cases
- require `research-needed`, `blocked`, or `none-with-reason` when evidence is insufficient

## Public Package Boundary

Public-facing skill packages may include:

- abstracted evidence classes
- reusable decision rules
- non-private examples
- links to official public standards when needed

Public-facing skill packages must not include:

- private acceptance logs
- local host state
- private user corrections
- internal review scores
- copied third-party prompts or directory schemes
- distinctive wording from another project

Evidence must change a design decision. If a card does not affect routing, package structure, validation, artifact output, or release gates, leave it out.
