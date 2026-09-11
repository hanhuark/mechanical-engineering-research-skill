# Changelog

All notable changes to the Thermal-Fluid Research Workflow Plugin are documented here.

## Unreleased

### Changed

- Added reader-first manuscript guidance derived from iterative technical-paper revision: distinguish the research gap from the present contribution, state the consequence of the gap, and explain what data integration or modeling is used to accomplish.
- Added abstract, introduction, and conclusion checks that reduce redundant, indirect, terminology-heavy prose while preserving technical meaning and claim boundaries.
- Updated Han Hu drafting and revision commands to require a concise narrative audit for high-level manuscript sections.

## v0.4.0 - 2026-09-08

### Added

- A `research-schematic-design` skill for publication-quality, editable scientific schematics, graphical abstracts, facility diagrams, and research workflows.
- A reusable schematic brief, native-vector and hybrid production guidance, scientific visual QA, and the `me-build-schematic` workflow prompt.

### Changed

- Made native editable geometry the default for technical labels, arrows, units, and legends. Image generation is limited to controlled visual concepts that are rebuilt and verified before delivery.

## v0.3.1 - 2026-09-08

### Added

- An anti-formulaic technical-writing reference for abstracts, manuscripts, proposals, and reviewer responses.
- Context-sensitive checks for detail-heavy abstracts, empty contrast transitions, vague `establish` claims, unnecessary hyphenated compounds, and em-dash clauses.

### Changed

- Added the editorial-quality check to research-writing and mentor-review workflows without treating writing style as evidence of AI authorship.

## v0.3.0 - 2026-09-08

### Added

- Focused skills for thermal-fluid analysis, research writing and literature, proposal development, research data analysis, research slide design, and constructive research mentor review.
- A general `reviewer-author-loop` skill and reusable command for iterative review, revision, verification, re-review, and human-pause decisions.
- Portable, task-specific reference bundles for writing/literature, proposal, data-analysis, and slide-design skills.

### Changed

- Kept `mechanical-engineering-research` as the backward-compatible coordinator while adding task-specific routing to avoid loading unrelated instructions.
- Updated Codex and Claude plugin metadata and README documentation for the modular suite.

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
