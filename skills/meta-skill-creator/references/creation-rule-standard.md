# Creation Rule Standard

This reference defines what a top-level creation rule must contain before `meta-skill-creator` writes or accepts a reusable skill package.

A creation rule is not a long prompt. It is a reusable operating contract for an agent: when to trigger, what evidence to fetch, what decisions to make, what artifacts to produce, how to verify them, and when to stop.

## Evidence Basis

This standard is distilled from current agent-skill and agent-evaluation practice:

- Agent Skills systems use progressive disclosure: metadata first, `SKILL.md` when triggered, references/assets/scripts only when needed.
- OpenAI prompt guidance emphasizes outcome, success criteria, constraints, context, stopping conditions, and missing-evidence behavior.
- Agent and eval guidance emphasizes task-specific eval objectives, datasets, metrics, comparisons, continuous regression checks, trajectories, final outcomes, and human review.
- Context engineering practice treats instructions, tools, retrieved evidence, run state, and history as a limited shared context that must be curated.
- Public skill formats converge on portable packages with `SKILL.md`, optional `references/`, `assets/`, and `scripts/`; deterministic scripts and audit logs are stronger than prose-only claims.

Do not copy outside wording or package structure into generated skills. Convert public research into abstract failure-prevention rules, validators, templates, and eval cases.

## Case Variable Boundary

Do not turn a single user's example into a durable rule by accident.

Names such as "boss", "sales", "teacher", "operator", "finance", "product", a company name, a department, a platform account, or a one-run audience label are case variables unless the user explicitly asks for a role-specific skill or the domain has a safety/compliance reason to lock the role.

Default handling:

- Put case roles into input fields such as `recipient_role`, `stakeholder_view`, `audience`, `review_lens`, or `handoff_target`.
- Keep them in examples or eval cases when they demonstrate a failure mode.
- Do not write them into `description`, trigger scope, default output sections, hard stops, release gates, or "reject delivery" rules as fixed labels.
- Convert role-specific requirements into functional requirements. For example, do not hardcode "boss quick-read must include whether to continue investing"; use "each requested decision view must include the decision question, evidence, and next action."

Allowed exceptions:

- The user explicitly requests a skill only for that role or department.
- Legal, medical, financial, security, or platform rules require role-specific boundaries.
- The target role is the domain itself, not a sample audience, and the evidence map explains why it must be locked.

If a role is locked, record why it is durable scope rather than a case variable.

## Required Anatomy

Every top-level creation rule must define these fields before build:

| Field | Required content | Failure if missing |
|---|---|---|
| Trigger boundary | When to use, when not to use, near-miss and ambiguous cases | Skill misfires or never fires |
| User result | Real user, pressure moment, final artifact, acceptance moment | Output optimizes for the prompt instead of the job |
| Scope | Included work, excluded work, destructive or external-state boundaries | Agent expands the task silently |
| Case variable boundary | Which names, target roles, stakeholder labels, industries, companies, example sections, and acceptance phrases are one-run variables | One example becomes a hardcoded skill rule |
| Evidence model | Required user material, local sources, graph/search, official sources, high-signal examples, counterevidence | Design is guessed |
| Stage contract | Critical Thinking, Fetch, Deep Thinking, Review, Loop inputs and outputs | Process becomes a slogan |
| Artifact chain | Raw input to native final artifact, including intermediate boards and generated files | Skill produces only prose |
| Tool route | Host-native, MCP/plugin, local script, fallback, permission and cost boundary | Agent simulates capability |
| Decision surface | Questions, choices, MVP lock, stop state, default if user does not answer | User confirmation is faked |
| Acceptance criteria | Pass/fail checks for structure, evidence, output, runtime, artifact, human review | Ready claim is unverifiable |
| Failure handling | `research-needed`, `blocked`, `partial`, `none-with-reason`, rollback or retry rule | Failures become ad hoc patches |
| Writeback rule | Which findings update `SKILL.md`, `references/`, `assets/`, `scripts`, `evals`, or examples | Learning stays in chat history |

## Stage Contract

Use this contract for every non-trivial skill creation, refactor, evaluation, or release-readiness run.

### 1. Critical Thinking

Purpose: decide whether the request should become a skill, what kind of package it is, and what would count as success.

Inputs:

- Raw user request and any provided files, examples, prior failures, or acceptance wording.
- Existing repo/package state if the task touches a current skill.

Required actions:

- Classify the task as `new-skill`, `refactor-skill`, `evaluate-skill`, `package-plan`, `release-prep`, or `not-a-skill`.
- Identify user, pressure moment, final artifact, and why ordinary prompting is insufficient.
- Separate durable scope from case variables such as names, target roles, stakeholder labels, industries, companies, example sections, and one-run acceptance phrases.
- Name scope, non-goals, destructive or external-state risks, and likely proof layers.
- Decide the first evidence route and whether online research may be required.

Required output:

- Critical brief with task class, skillization decision candidate, user result, scope, risk, and needed evidence.

Pass criteria:

- A reviewer can tell what job the skill solves, what it must not do, and what evidence would change the decision.
- The next action is evidence fetching, not file writing.

Fail conditions:

- No user result or final artifact is named.
- A one-off prompt is forced into a skill.
- The agent starts from a familiar template, platform, or example before classifying the request.

### 2. Fetch

Purpose: collect only evidence that can change package decisions, artifact shape, tool route, or acceptance criteria.

Inputs:

- Critical brief.
- User material and current package files.
- Relevant graph/search anchors, official docs, platform docs, high-signal examples, local scripts/assets, and counterevidence.

Required actions:

- Read the directly relevant `SKILL.md`, referenced files, validators, templates, evals, examples, and user material.
- Query local graph or local search when available.
- Use online research when the user asks for deep research or when current external facts affect safety, platform behavior, compatibility, or release claims.
- Record unavailable paths instead of pretending they were checked.
- Extract decision impact, not trivia.

Required output:

- Evidence map with sources read, unavailable sources, key findings, counterevidence, and decision impact.

Pass criteria:

- Each important claim is tied to evidence or marked as an assumption.
- `research-needed` is allowed only after the available evidence sweep has been attempted.
- External facts that may drift are verified with current sources before becoming durable rules.

Fail conditions:

- Local files are treated as deep research when online evidence is required.
- The evidence list contains sources but no decision impact.
- Counterevidence, unavailable paths, or uncertainty are omitted.

### 3. Deep Thinking

Purpose: synthesize the evidence into a package contract and build plan without exposing hidden reasoning.

Inputs:

- Critical brief.
- Evidence map.
- Existing package structure and validators.

Required actions:

- Define the result contract: trigger, input, output, artifact chain, tool route, safety/originality boundary, and fallback.
- Define the case-variable contract: which roles, audiences, stakeholder views, labels, and acceptance phrases stay configurable instead of becoming fixed skill rules.
- Choose the smallest package structure that prevents real failure modes.
- Decide what belongs in `SKILL.md`, `references/`, `assets/`, `scripts/`, `evals`, and `examples`.
- Define test cases and acceptance criteria before or alongside edits.
- For interactive or multimodal skills, define native decision surfaces, MVP lock, capability inventory, and output evidence route.

Required output:

- Package plan and acceptance plan with files to edit/create, rules to add, validators to run, and proof layers expected.

Pass criteria:

- Every new file or rule has a named failure mode it prevents.
- Example-specific roles or stakeholder labels are represented as variables unless there is explicit evidence for locking them.
- Acceptance criteria are specific enough that another reviewer can mark pass/fail.
- The plan separates structure checks, runtime/tool proof, artifact proof, baseline proof, and human confirmation.

Fail conditions:

- The plan says "improve" without measurable criteria.
- `SKILL.md` becomes an encyclopedia instead of a light router.
- Tool capability or generated artifact claims have no proof route.

### 4. Review

Purpose: verify the package against the acceptance plan and decide whether it is ready, partial, blocked, or needs writeback.

Inputs:

- Modified package or candidate output.
- Acceptance plan.
- Validator output, artifact evidence, runtime logs, screenshots/files when relevant, and reviewer notes.

Required actions:

- Run available validators and generated-package scripts.
- Check trigger evals, output evals, baseline/regression evidence, release gate, and loop record as applicable.
- Inspect whether the visible final artifact would satisfy the user result.
- Record what each proof layer proves and does not prove.
- Issue one loop decision: `writeback`, `proposal`, `none-with-reason`, or `blocked`.

Required output:

- Review brief with pass/fail by proof layer, missing evidence, ready level, loop decision, and next drift action.

Pass criteria:

- No ready claim is made from structure-only checks.
- Failures produce a prevention rule, eval, template change, validator change, or explicit `none-with-reason`.
- The final report names commands run and remaining risk.

Fail conditions:

- Validator pass is presented as user-visible quality proof.
- Human or runtime evidence is claimed without actual artifact/run evidence.
- No loop decision is recorded.

## Acceptance Matrix

Use this table as the minimum reviewer checklist for top-level creation rules.

| Gate | Must pass | Evidence |
|---|---|---|
| Critical gate | Task class, user result, scope, non-goals, risk, and first evidence route are explicit | Critical brief |
| Fetch gate | User/local/graph/official/high-signal/counterevidence sweep attempted as available | Evidence map |
| Research gate | Current external facts checked when they can affect design or release claims | Source map and decision impact |
| Contract gate | Trigger, input, output, artifact chain, tool route, boundary, and fallback are defined | Skill contract or package plan |
| Variable gate | Case-specific roles, audiences, labels, company names, and example acceptance phrases are kept as variables unless explicitly justified | Case variable boundary |
| Package gate | Each file exists for a reason and maps to a failure mode | Package map |
| Eval gate | Trigger, output, baseline/regression, and risky/ambiguous cases are defined | `evals/` and acceptance plan |
| Runtime gate | Scripts/tools/native routes are run or honestly marked unavailable/partial/blocked | Command logs or capability notes |
| Artifact gate | Final files, screenshots, widgets, documents, media, or reports exist when promised | Artifact evidence |
| Human gate | Human review or explicit absence of human review is recorded | Reviewer notes |
| Loop gate | `writeback` / `proposal` / `none-with-reason` / `blocked` is recorded with next reuse key | Loop run record |

Minimum pass: Critical, Fetch, Contract, Package, Eval, and Loop gates must pass for an operating candidate. Runtime, Artifact, Research, Baseline, and Human gates must pass when the skill claims release readiness, public compatibility, generated artifacts, external-platform behavior, or superiority over a baseline.

## Hard Stops

Stop before writing or claiming ready when:

- Critical brief is missing.
- Evidence sweep has not been attempted.
- A current external claim is unverified.
- Acceptance criteria are absent or cannot be checked.
- A sample role or stakeholder label is hardcoded into trigger, scope, default sections, or reject-delivery rules without explicit durable-scope justification.
- The final artifact is unnamed.
- The package has no eval or validator path.
- The skill requires user decisions but has no decision surface or stop state.
- A generated artifact is promised without an output evidence route.
- The run has no loop decision.

## Output Discipline

Do not ask the agent to reveal hidden chain-of-thought. The visible deliverable should include:

- decision summaries,
- evidence maps,
- option comparisons,
- acceptance tables,
- commands run,
- proof-layer judgment,
- uncertainty and blockers.

The rule is simple: private reasoning may guide the work, but durable rules must be inspectable, executable, and reviewable.
