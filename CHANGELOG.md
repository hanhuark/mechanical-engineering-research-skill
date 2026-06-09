# Changelog

All notable changes to the Thermal-Fluid Research Workflow Plugin are documented here.

## v0.2.0 - 2026-06-09

### Added

- Public README repositioning around thermal-fluid rigor and concrete failure modes.
- Two-minute demo showing how the skill downgrades an overclaimed CFD result into defensible engineering feedback.
- GitHub-rendered Mermaid workflow diagram plus editable source in [`assets/workflow.mmd`](assets/workflow.mmd).
- Showcase examples for CFD review, heat-exchanger design comparison, boiling literature synthesis, proposal aims, and figure discussion.
- Seven named micro-workflow prompts:
  - `me-correlation-check`
  - `me-cfd-review`
  - `me-experiment-plan`
  - `me-lit-matrix`
  - `me-figure-discussion`
  - `me-proposal-aims`
  - `me-code-sanity`
- Repository validation script and GitHub Actions workflow.
- Thermal-fluid eval fixture set with ten prompt scenarios and expected checks.
- Simplified Chinese and Traditional Chinese README files.
- Discovery topic recommendations in [`docs/GITHUB_TOPICS.md`](docs/GITHUB_TOPICS.md).

### Changed

- Bumped Codex and Claude plugin metadata from `0.1.0` to `0.2.0`.
- Updated plugin descriptions, keywords, and default prompts for CFD review, correlation checks, experiment planning, and thermal-fluid validity.
- Clarified that generic academic workflows provide process scaffolding while this plugin supplies domain judgment.

## v0.1.0 - 2026-06-02

### Added

- Initial plugin-style packaging for the `mechanical-engineering-research` skill.
- Codex and Claude plugin manifests.
- Core workflow prompts for literature review, proposals, section writing, data analysis, slides, and code review.
