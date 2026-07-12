# Changelog

## Unreleased

## [1.0.0] - 2026-07-12

### Added

- Added standalone MIT `LICENSE` and `NOTICE`.
- Added closed-loop governance reference, run-record template, and closed-loop checker.
- Added bilingual README files for external users.
- Added contact and support QR images under `docs/images/`.
- Added `README.en.md` while making `README.md` the default Chinese entry.
- Added explicit network deep research and write-in decision rules to README and skill references.
- Added a top-level creation-rule standard with Critical Thinking, Fetch, Deep Thinking, Review, and Loop acceptance gates.

### Changed

- Explicit requests to create, refactor, or review a skill now enter the matching route directly; research can shape or pause the design, but does not override the user's creation intent.
- Replaced `not-a-skill` and `make` / `do-not-make` routing in creation rules, templates, product design, and trigger evals with `proceed` / `research-needed` / `blocked` creation routes.
- Added a trigger-eval case that protects an explicit creation request even when the workflow may be one-off.
- Reframed the repository as a clean source package instead of a local runtime workspace.
- Simplified licensing to MIT-only.
- Removed duplicate package-level README so the root README files are the public entry point.
- Replaced Mermaid rich rendering in README files with a plain text flow for stable GitHub display.
- Centered contact/support sections for GitHub README rendering.
- Replaced "concise skill" wording with a light-entry, evidence-heavy quality bar.
- Reworked install instructions with Windows PowerShell commands and an explicit clone/repository-root check.
- Hardened maintainer workflow and validator coverage around stage outputs, pass/fail criteria, and proof-layer reporting.
- Removed public-facing references to local development paths and runtime-copy directories.
