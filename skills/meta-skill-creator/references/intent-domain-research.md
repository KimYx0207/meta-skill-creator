# Intent Domain Research

This is the upstream layer for every skill created by `meta-skill-creator`.

Do not start from a familiar platform example. Do not guess the user's workflow from a category name. First research the intent domain, then derive the work surface, native artifacts, generation chain, package plan, and evals.

## No Guessing Rule

Any claim about a domain, platform, artifact, workflow, quality standard, or user expectation is a hypothesis until it is supported by evidence.

Valid evidence can include:

- user-provided material or prior failed outputs,
- local existing skills, domain rules, examples, scripts, or test results,
- current host tools, MCP/plugin tools, and local generation/render scripts,
- Graphify query results, followed by source-file verification,
- official docs, product docs, marketplace docs, or platform rules,
- high-signal open-source projects, templates, tools, or workflows,
- user discussions that expose failure modes or unmet jobs,
- counterevidence that limits what the skill must not claim or simulate.

## Fetch Before `research-needed`

`research-needed` is a valid decision only after an evidence sweep, not before one.

Before returning `research-needed`, attempt the available retrieval path:

1. Read user-provided material and prior failed outputs.
2. Query local graph or search local skills for adjacent domain rules, examples, scripts, and test results.
3. Discover current host tools, MCP/plugin tools, and existing local scripts/assets that can produce the target native artifact.
4. Check official/platform/product docs when the domain has rules, compliance, safety, or current behavior.
5. Check high-signal projects, templates, tools, or marketplace examples for native artifact patterns.
6. Check user failure discussions or internal failure logs for common rejection modes.
7. Record counterevidence and boundaries.

If network, local sources, or user materials are unavailable, say exactly which retrieval path was unavailable.

If the evidence is still too thin after the sweep, return `research-needed`. Do not write `SKILL.md` yet.

## Domain Research Brief

Every candidate skill starts with this brief:

- Raw user intent:
- Suspected domain(s):
- Domain confidence:
- Evidence read:
- Evidence sweep attempted:
- Unavailable evidence paths:
- Users / roles:
- Pressure moments:
- Existing workflow:
- Native artifacts:
- Work surfaces / platforms / tools:
- Local capability inventory:
- Primary generation / render route:
- Fallback route:
- Output evidence route:
- What the user or audience judges first:
- Quality standards:
- Common failure modes:
- Required real inputs:
- Generated components:
- Things not to simulate:
- High-signal examples:
- Counterevidence / boundary:
- Decision: `make` / `do-not-make` / `research-needed`
- Next research queries:

The brief can be short, but it cannot be absent.

## Research-To-Design Chain

Use this chain before package planning:

```text
raw user intent
-> suspected domain as hypothesis
-> evidence sweep
-> Domain Research Brief
-> domain model: users, workflow, artifacts, tools, standards, failure modes
-> experience surface discovery
-> native artifact chain
-> generation pipeline
-> package plan
-> eval and release gate
```

The experience surface is downstream. It is not the first move.

## Domain Model Questions

Answer these from evidence:

1. Who is the real user, and what are they trying to get done?
2. What situation creates pressure or urgency?
3. What is the native unit of value in this domain: presentation, image-text note, spreadsheet insight, inspection remediation pack, follow-up message, script, checklist, dashboard, file bundle, or something else?
4. What tools, platforms, or handoff surfaces are normal in the domain?
5. What does a user judge in the first 10 seconds?
6. What makes an output accepted, rejected, risky, fake, or unusable?
7. Which inputs must be real material?
8. Which parts can be generated safely?
9. Which claims, screenshots, records, metrics, user feedback, or legal/medical/financial interpretations cannot be fabricated?
10. What deterministic checks, templates, scripts, or examples would prevent the common failures?
11. If the output is multimodal or rendered, what current local tool, MCP, script, or asset route should be used first?
12. What structured brief is needed before writing image/video/audio/document/slide/dashboard prompts?

## Cross-Domain Examples

These are examples of the method, not hardcoded routes.

### Social Image-Text Workflow

After research, this may be identified as a mobile image-text note surface. The native artifact is not only copy. It may require cover, image pages, visual prompts or generated cards, title, body, tags, platform-safe interaction boundary, material boundary, and publish brief.

### Presentation Workflow

After research, this may be identified as a workplace decision surface. The native artifact may be a presentation, page plan, executive summary, speaker notes, audience-question defense, PDF handoff, and visible preview.

### Excel Insight Brief

After research, this may be identified as a data-to-decision surface. The native artifact may be cleaned table, metric definitions, charts, insight brief, caveats, decision recommendation, and privacy notes.

### Unknown Or Niche Domain

For a request such as "make a pet clinic follow-up reminder skill" or "make a factory inspection corrective-action skill", do not borrow assumptions from any familiar platform or document type. First research the domain workflow, artifacts, compliance boundaries, tools, and acceptance standards. If those are not known yet, return `research-needed`.

## Hard Stop

Stop before writing runtime instructions when:

- there is no Domain Research Brief,
- `research-needed` is returned before attempting available evidence retrieval,
- the surface is guessed from a familiar example,
- a multimodal or rendered-artifact skill lacks current local capability inventory,
- a multimodal prompt is generic prose instead of a structured brief,
- the artifact chain is copied from another domain,
- the user role or pressure moment is unclear,
- the native artifact is unnamed,
- real-material boundaries are missing,
- evidence does not change any design decision,
- the package plan exists only because "skills should have files".
