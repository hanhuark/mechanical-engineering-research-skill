# Changelog

All notable changes to the Thermal-Fluid Research Workflow Plugin are documented here.

## Unreleased

### Added

- Added a proposal budget and budget-justification reference that builds the budget from sponsor rules and the institution's current workbook, states a source and effective date for every rate, separates participant support and workshop costs, confirms the subaward indirect-cost threshold, and reconciles the justification with the workbook and the narrative.
- Added an author-guided AI writing workflow that turns pre-draft scientific guidance and post-draft human review into a repeatable story brief, claim-evidence map, reader-recovery review, and revision sequence.
- Added the `me-author-guided-writing` prompt for manuscripts, proposals, reports, reviews, and responses developed with AI assistance.
- Added an author interview to the author-guided writing workflow, adapted from the round-based `grilling` skill. The AI reads the supplied material as reference, extracts its facts, and asks the author numbered rounds of questions from the story down to each figure. Story-level questions carry no suggested answer, vague answers get at most two follow-ups that ask only for the missing element, and unanswered questions become visible `[OPEN]` placeholders. Answers go into an author decision record kept with the manuscript, and drafting proceeds one unit at a time from that record, followed by a separate consistency pass. Includes a question bank, a record template, and four synthetic eval fixtures.
- Added prose metrics to `audit_technical_writing.py`: sentence-length mean, median, and 90th percentile, and counts and per-10,000-word rates of the constructions in the measured prose targets.
- Added a process case study of the author interview on one results section of an unpublished manuscript, with the lessons that changed the protocol.

### Changed

- Revised the author interview after its first live use: quote an earlier approved version in round 1, load the author's style references before proposing any wording, run requested or revealed analyses between rounds and verify every reference, treat answered rounds as confirmation, check limitations against the data, and run the prose metrics on every unit draft. Added three eval fixtures.
- Added writing preferences extracted from three of the author's manuscripts compared across AI draft, AI-supervised revision, and the author's own revision: field-standard names for regimes and conditions, literal verbs, purpose openers with the variable changed, a four-step figure paragraph, "is shown to" for headline findings, "this work" and "we" for scope, limitations framed by consequence and placed once, provenance kept out of the main text, a plain introduction preview, and physics-first framing for model papers. The abstract now ends on the strongest physical finding, and the conclusion is one connected paragraph by default.
- Corrected the sentence-length rows of the measured prose targets. The earlier mean of 15.2 words counted headings and table rows as sentences; measured on prose only, the author's own revisions average 19 to 22 words per sentence.

- Added a paragraph-opener and skeleton test: the first sentence of a paragraph delivers its central idea and the last delivers its message, so that the openers and closers read in sequence still carry the argument. Names the recurring failures, including an opener that points backward at buried context, one that announces a comparison instead of stating the finding, one carrying a number left over from the previous analysis, and one that forward-references what the paragraph has yet to introduce.
- Added a defensive-qualification rule: a limiting statement stays when it changes what a result means and is made once, and goes when it denies a claim no reader made or restates a limit the manuscript already carries. Includes the cuttable patterns, the rewrite of a negatively stated result, and the screening pass that collects candidates for judgment rather than deletion.
- Added a terminology audit for terms a reader cannot look up, covering the terms a paper runs on but never defines, one word carrying two technical senses, a term defined and then never used again, labels invented to carry a departing word, compressed nominal coinages, abbreviations expanded only in the nomenclature, and a named but unstated value that must be recovered from the released code or log rather than invented.
- Added measured prose targets taken from an author edit of an AI-drafted manuscript, with sentence-length and construction rates as the check in place of a judgment about whether a draft reads naturally, the six revision moves in order of payoff, and a warning about trading one construction tic for another.
- Added figure-centered results guidance: every results paragraph serves a figure, and the paragraph runs A-B-A from transition and description, through observe-explain pairs, to the take-home message and handoff.
- Added LaTeX packaging checks for stale build artifacts, including the empty `.bbl` that ships a package without a bibliography, the `-jobname` trap that leaves BibTeX output under another name, and the external records that go stale when a title changes.
- Replaced the binary-contrast guidance with a rule against defining a subject by what it is not. The frames `A rather than B`, `A, not B`, and `not B but A` are kept only when B is a real competing option. Otherwise the sentence names the actor, the action, and the object in common phrasing, with a before-and-after example. The diagnostic pass now also counts `, not`, `not … but`, and `instead of`.
- Refined concise section-revision guidance: describe figures before interpreting them, combine plots that support one argument, integrate essential table notes into the main text, and reconcile conclusions with the final results. Added checks for model identity, attribution scope, aggregation, and latency versus throughput, with synthetic evaluation scenarios.

- Added a caption-scope rule: a caption describes the figure, including the quantities, conditions, subfigure mapping, visual encodings, and the protocol or calibration behind the data, while results, interpretation, and the justification for a plotting choice belong in the section that argues from them; values already printed on the figure are not restated, and a bound that qualifies a claim moves with that claim.
- Added Han Hu style guidance for noun-first technical phrasing, evidence-specific vocabulary, and restraint in colon and semicolon clauses. The guidance replaces generic interrogative constructions and catch-all uses of `record` with the actual quantity, method, documentation, or evidence object.
- Added sentence-construction and emphasis guidance: subordinate clause-level parallel series so the distinctive claim occupies the main clause, distinguish genuine enumerations from rhetorical parallelism, require short sentences to carry specific content, remove definitional asides, prefer formal causal connectives over `because` and `so`, and avoid the binary `X rather than Y` contrast as a default connective.
- Added a parallel-detail check: consolidate lists of more than three items into the specific higher-level concept that carries the technical point, unless the individual items are needed for comparison, reproduction, boundary assessment, uncertainty treatment, or a distinct action.
- Added reader-first manuscript guidance derived from iterative technical-paper revision: distinguish the research gap from the present contribution, state the consequence of the gap, and explain what data integration or modeling is used to accomplish.
- Added abstract, introduction, and conclusion checks that reduce redundant, indirect, terminology-heavy prose while preserving technical meaning and claim boundaries.
- Updated Han Hu drafting and revision commands to require a concise narrative audit for high-level manuscript sections.
- Added an integrated seven-stage workflow for substantial research documents: decision framing, evidence mapping, narrative architecture, technical development, evidence-to-reader drafting, revision auditing, and package verification.
- Added literature-role mapping and revision-roadmap guidance so background sources, key comparisons, conflicting evidence, reviewer comments, and required technical actions remain traceable.

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
