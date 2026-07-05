# 闭环运行记录模板

## 运行信息

- run_id:
- date:
- skill_name:
- run_type: new-skill / refactor-skill / evaluate-skill / package-plan / release-check
- operator:
- runtime_host: Codex / Claude Code / other

## Intent Core

- original_user_request:
- target_user:
- pressure_scenario:
- final_artifact:
- success_criteria:
- non_goals:

## Evidence Fetch

- local_evidence_read:
- external_or_current_evidence_read:
- unavailable_evidence:
- counterevidence:
- design_changing_facts:

## Product Surface

- first_visible_result:
- native_medium:
- artifact_chain:
- real_input_required:
- generated_input_allowed:
- must_not_fabricate:

## Package Contract

- trigger_boundary:
- input_contract:
- output_contract:
- file_map:
- failure_modes:
- verification_route:

## Verification Evidence

- structure_check:
- contract_check:
- artifact_check:
- runtime_check:
- human_check:
- evidence_level: structure / contract / artifact / runtime / human
- accepted_risk:

## Findings

| finding_id | severity | evidence | fix_or_decision | status |
|---|---|---|---|---|
| F-001 |  |  |  | open |

## Loop Decision

- decision: writeback / proposal / none-with-reason / blocked
- decision_reason:
- writeback_targets:
- proposal_targets:
- blocked_reason:
- next_run_reuse_key:

## Scar Record

Fill only when a failure should prevent future repeats.

- failure_pattern:
- prevention_rule:
- regression_check:
- owner:

