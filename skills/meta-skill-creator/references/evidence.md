# Evidence Model

Use this file to decide what evidence a generated skill package should collect before design, validation, or release. It is intentionally source-abstracted: public packages should keep durable principles and decision impacts, not private run logs, local machine state, or copied third-party wording.

## Evidence Card Shape

Each evidence card should answer:

- `source_url_or_path`: public URL, local path, or user-provided material reference.
- `source_type`: official documentation, open specification, high-signal example, user material, failure report, benchmark, or counterexample.
- `freshness`: current, dated, stale-risk, or unknown.
- `claim`: what the evidence says.
- `relevance`: why it changes this skill package.
- `confidence`: high, medium, or low.
- `counterevidence`: what might make the claim weaker.
- `decision_impact`: which trigger, reference, asset, script, eval, or release gate changes because of it.
- `translated_asset_or_eval`: where the learning appears in the package.

## Online Evidence Standard

Use online evidence when current external facts can affect the skill. A local-only sweep is not deep research for domains with changing platform rules, APIs, public tools, policies, marketplace behavior, current best practices, or competitor workflows.

A complete online evidence packet contains:

- `Source Map`: official docs, open standards, high-signal examples, user material, failure reports, and counterexamples checked.
- `Key Findings`: facts that change a package decision.
- `Counterevidence`: conflicting, stale, host-specific, or unverifiable claims.
- `Write-in Decision`: where each finding belongs, or why it should not become a durable rule.

If online access is unavailable, write `online-unavailable` and list the sources that should be checked later. Do not mark the package `ready` when online evidence is required but unavailable.

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

## Write-In Decision Rules

Evidence can be written into the skill only when it changes future behavior.

| Destination | Write when | Do not write when |
|---|---|---|
| `SKILL.md` | The finding changes trigger scope, first action, hard stop, resource routing, or validation lens | It is long research, platform trivia, or a one-run summary |
| `references/` | The finding becomes a reusable domain rule, evidence rule, artifact-chain rule, failure mode, or release gate | It copies a source's wording, structure, examples, or visual system |
| `assets/` | The finding becomes a reusable brief, checklist, worksheet, or run-record template | It only helps the current conversation |
| `scripts/` | The finding can be checked deterministically or automated safely | It requires model judgment or user taste |
| `evals/` | The finding defines a trigger, near-miss, false-positive, output-quality, baseline, or regression case | It is only an impressive demo |
| `examples/` | The finding can be shown as a small non-private input/output pair | It contains private data, fake proof, or internal scoring |

If a finding does not prevent a concrete failure or improve repeatability, keep it in the run record and choose `none-with-reason`.

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
