# Han Hu Research And Writing Style Preferences

Use this reference when the user asks to match Han Hu's style, infer preferences from a prior workspace, revise a review article, write about open datasets/software/benchmarks, prepare an Overleaf or journal submission package, or make thermal-fluid AI writing feel like the user's own work.

## Concise Section Revisions

Use the description-observation-explanation-conclusion sequence in [technical-writing-analysis.md](technical-writing-analysis.md). Combine related plots when they explain one consistent story, and add a short purpose statement when needed to connect a subsection. Prefer essential table notes in the main text over an explanatory paragraph below the table; preserve venue-required footnotes. Apply the same concision to conclusions while retaining the principal finding and its evidence boundary.

## Core Research Posture

Frame work as a useful contribution to a technical community, not as self-promotion.

- Start from an important transport or thermal-management problem.
- Explain the coupled physics before introducing AI, software, or data infrastructure.
- Treat AI/ML as a tool for probing, predicting, reconstructing, or organizing thermal-fluid behavior, not as the final point of the work.
- Separate what is measured, simulated, inferred, proposed, and community-dependent.
- When the user's lab resources are discussed, present them as case studies or seed efforts within a broader field-wide ecosystem.

## Preferred Manuscript Logic

Build manuscripts through a narrowing technical story.

1. Establish the two-phase transport or thermal-management need.
2. Explain the coupled physical mechanisms.
3. Explain why the mechanisms span scales and make physics-based modeling difficult.
4. Motivate multimodal data and data-driven modeling as ways to probe different projections of the same process.
5. Introduce the organizing framework, taxonomy, benchmark, or method.
6. Review existing datasets, models, tools, and gaps using that framework.
7. Close with community infrastructure, limitations, and specific future work.

When two figures express related ideas, give each figure a distinct job in the prose. For example, one figure may show many coupled mechanisms, while the next shows the multiscale nature of heat transfer. Do not cite both in one overloaded sentence unless their roles are explicitly separated.

## Review Article Style

Write review articles as synthesis and infrastructure guidance, not as annotated bibliographies.

- Organize the review around a framework, mechanism, modality, dimensionality, workflow, or benchmark need.
- Use taxonomies to help readers map their own datasets or methods into the review.
- Discuss representative papers deeply only when they clarify a method, mechanism, limitation, or benchmark pattern.
- Group background references by category and discuss key papers selectively.
- Include tables and figures that do analytical work: taxonomy tables, dataset inventories, benchmark matrices, readiness scorecards, metadata workflows, or roadmap figures.
- Avoid one-lab dominance. If NED3 resources are included, balance them with third-party resources and explicitly state that NED3 is an implementation case, not the center of the review.

## Open Data, Software, And Benchmark Framing

For open thermal-fluid datasets and AI tools, emphasize reuse infrastructure.

- Describe datasets by data object, modality, S+TD class, physics metadata, labels, split strategy, decoders, and benchmark task.
- Use the S+TD idea when helpful: 0+0D point/tabular data, 0+1D time series, 1+0D/1+1D profiles, 2+0D images, 2+1D videos or fields, 3+0D/3+1D simulation fields, and mixed multimodal records.
- Connect each data class to plausible AI tasks: regression, sequence learning, segmentation, classification, surrogate modeling, inverse reconstruction, scientific ML, cross-domain transfer, or multimodal fusion.
- Treat benchmark datasets as staged community efforts unless a complete benchmark already exists. It is acceptable to propose or seed a benchmark, but do not overclaim that a small initial dataset solves the benchmark problem.
- Emphasize cross-laboratory splits, run-held-out splits, surface-held-out splits, fluid-held-out splits, geometry-held-out splits, and heat-load-path-held-out splits when discussing generalization.
- Include baseline models, raw-to-processed provenance, uncertainty, failure cases, and rules about external data in benchmark proposals.

## Physics Metadata And Data Curation

For thermal-fluid databanks, make physics metadata central.

- Go beyond normal catalog fields such as title, author, keywords, file type, and license.
- Include geometry, fluid, pressure, heater size, surface condition, heat flux, HTC, CHF, operating path, calibration, sensor locations, sampling rate, frame rate, spatial scale, synchronization, uncertainty, and data-reduction equations.
- Include mechanism-level quantities when useful: Jakob number, Capillary number, Weber number, Bond number, Reynolds number, Boiling number, Rayleigh-Taylor wavelength, vapor fraction, Zuber-scaled heat flux, or other problem-specific dimensionless groups.
- Describe curation as a workflow: contributor upload, metadata extraction, data cataloging, high-dimensional profiling, consistency checks against existing datasets and physical laws, standardization, and warehouse/archive storage.
- Support metadata scrapers and registered feature-detection algorithms for legacy spreadsheets, text files, images, videos, waveforms, and simulation outputs.

## Citation And Literature Hygiene

Be strict with citation coherence.

- Use first-author-last-name plus "et al." in prose. Avoid listing many author names in the main text.
- Avoid author-chain labels such as "Kharangate-Mudawar-Kim-Qiu-Zhou" or similar group strings.
- Number references by order of first appearance when the manuscript uses numeric citations.
- Every reference should be cited; every citation should resolve to the intended reference.
- After moving text, tables, or figure captions, re-run citation and reference consistency checks.
- In figure captions, verify permission statements and reference numbers semantically, not only mechanically.
- Disclose preprints, arXiv versions, or prior public versions transparently in cover letters when submitting an expanded journal version.

## Figure And Table Preferences

Figures and tables should carry the argument.

- Each figure should have a clear role in the manuscript narrative.
- Do not use placeholder recommendation figures in a final paper; either include the figure and discuss it, or remove it.
- Place figures near the text that motivates them when possible.
- Use `Figure~\ref{...}` and `Table~\ref{...}` rather than hard-coded figure or table numbers.
- Captions should define the purpose of the figure and enough context to stand alone.
- For review tables, include columns that help readers act: data modality, S+TD class, AI task, metadata needs, benchmark readiness, availability, and evidence level.
- Separate dataset/software availability created by the authors from third-party resources reviewed in the article.

## Writing Preferences

Prefer clear, compact, technical prose.

- Use paragraph topic sentences and make each paragraph build from context to implication.
- Build each technical paragraph around one job: establish the engineering context, identify a mechanism or gap, state the method, present the evidence, and give the bounded implication. Do not replace connected exposition with a sequence of short factual sentences.
- Avoid too many colon-led clauses in the main text.
- Avoid repeated sentences that say the same idea in two ways.
- Use "indicates" for evidence-supported interpretation, "suggests" for weaker inference, and "demonstrates" only when the evidence directly supports the claim.
- Avoid hype. Prefer "seed benchmark," "case study," "representative example," "proposed community mechanism," or "future infrastructure" when the work is preliminary.
- Keep acknowledgments, availability statements, and cover letters transparent and concise.

## Calibrated Journal-Manuscript Revision

When revising a manuscript to match this style, preserve the science while making the evidence chain more direct. Revise at the section and paragraph level before making sentence-level edits; a generic simplification pass is not enough.

- Use a dense abstract: need, specific gap, compact method, two to three quantitative findings when the underlying data support them, and a scope-bounded implication. Do not use the abstract to repeat background or defer the outcome to the body.
- Construct the introduction as a narrowing funnel. Synthesize prior work by application, architecture, material, diagnostic method, or modeling approach; then identify a specific unresolved physical, manufacturing, measurement, or design problem. Do not claim that no related work exists when adjacent approaches exist.
- Make the final introduction paragraph concrete: what was fabricated, measured, modeled, compared, or validated; the operating range and material or geometry scope; and the resulting physical insight or design capability.
- State experimental and model boundaries explicitly: the system boundary, coordinate convention, imposed and inferred quantities, sensor or image-derived metrics, calibration, uncertainty, and the difference between an effective fitted property and an intrinsic material property.
- Treat each results figure as an argument. Orient the reader, report the observed and quantitative difference, relate it to the physical architecture or mechanism, then state the design implication. Use a limitation only where it changes interpretation.
- Put caveats near the affected claim and make them specific. Name the unmeasured quantity, uncertain boundary, untested condition, or model-form limitation once; avoid repeating defensive statements after every result.
- Write conclusions as two to four numbered, cumulative findings. Each finding should state the result, its physical interpretation, and its bounded implication rather than restating a section heading or the abstract.
- Avoid casual or meta-writing, including rhetorical questions, reader-directed language, "the current work," "the present work," and generic statements such as "This study establishes" when a direct technical subject is available. Prefer a declarative, evidence-linked statement.
- Retain meaningful limitations, uncertainty, and provenance. Do not solve a substantive evidence gap by only weakening the prose; identify the analysis, validation, or new measurement needed.

## Figure And Results Language

- Use `Fig. 6a`, not "panel a," when referring to a subfigure, unless the target journal requires another convention.
- Use Arial consistently in publication figures unless the journal template requires a different font. Keep font size, axis spacing, line weights, legends, and uncertainty notation consistent across related figures.
- Define symbols, units, coordinate directions, sample states, and statistical quantities in the figure or caption. Make uncertainty graphics meaningful: identify whether bars show standard deviation, confidence interval, propagated uncertainty, or another measure.
- Describe a plotted effective property by its physical role and fitting basis. For example, distinguish an effective in-plane conductivity used to characterize composite heat spreading from an intrinsic constituent conductivity.

## Overleaf And Submission Habits

For LaTeX/Overleaf submission packages:

- Identify the true source file and remove stale alternate manuscript files before submission.
- Keep only files needed for production: the active `.tex`, bibliography/support files if useful, and referenced figures.
- Use a short README only when it helps production compile the source, such as noting XeLaTeX and the main file.
- If a journal system rejects a zip, prepare a flat individual-upload package with figure paths adjusted so uploaded figures sit beside the main `.tex` file.
- Keep the review PDF and source files conceptually separate: the PDF is for review, while the source is for production.
- For cover letters, state journal fit, contribution, originality/no-parallel-submission, conflicts, author approval, and any preprint relationship.

## Patterns From Author Revisions Of AI Drafts

These patterns come from comparing three of the author's manuscripts across versions: the AI draft, the AI revision after many rounds of the author's comments, and the author's own direct revision. Each pattern below appeared in at least two of the three manuscripts, or is stated as a single-manuscript habit. The examples are synthetic.

**Name things the way the field names them.** Name test conditions by the boiling regime visible in the images, model regimes by the physical limit that governs them, and figures, baselines, and section headings by the field's standard categories. A coined label such as `closure branch` or `high-flux arm` becomes `evaporation-limited regime` or `near CHF`, and "the wall-temperature record" becomes "the boiling curves".

**Use literal verbs.** Do not give instruments, features, or models human actions. "Acoustic emission reaches the vapor dynamics" becomes "acoustic emission sensing characterizes the vapor dynamics without optical access", and "the model receives frames and returns masks" becomes a description of the input images and the output masks. Report prior work in the present perfect or the passive.

**Open an analysis with its purpose and the variable changed.** "To evaluate the effect of temporal context on prediction, we have varied the number of frames per sequence from 1 to 32." The first person and the present perfect are both acceptable here. The form "To examine X, Fig. N plots Y against Z" also works. Name the object directly instead of writing "how X influences Y".

**Build each figure paragraph in four steps.** State what the figure plots, Y against X and under which conditions; give the values as an ordered progression tied to each method or condition, pairing them with `respectively` where that is shorter; close the observation with a `Thus,` takeaway; then give the physical reading with `may` or `could` when the mechanism is inferred. Delete derived ratios and differences that the reader can compute from the stated values.

**State headline findings directly.** "The temporal model is shown to reduce the prediction error by half" states a finding. "It is observed that" is acceptable occasionally, though not as the opener of every paragraph.

**Use "this work", "this study", and "we" for scope and ownership.** They are appropriate for local definitions ("In this work, a case is one nominal mass flux"), purpose openers, the opening of the conclusion, and the group's own prior work ("In our previous work, we proposed..."). Avoid them for self-evaluation, as in "this study establishes".

**Place a limitation once, where it applies, and frame it by its consequence.** Two forms recur. A fitness-for-purpose sentence: "Although the acoustic calibration is less precise than a reference hydrophone, it is sufficient for the steady-state comparison in this work." A validation paragraph placed directly after the comparison figure: name the sources of scatter, state how inputs the literature did not report were treated, then write "Within these limitations, the data follow the predicted trend" and give the mechanism. Delete a stand-alone limitations section, a list of validation needs, and one-line verdicts that deny a claim or announce a limit.

**Keep provenance out of the main text.** Delete narration of how data were transcribed, audited, or reconstructed, and inventories of files, workbooks, and code. State the inputs that were used, with citations.

**End the introduction with a plain preview.** The last paragraph says what is done and with which analyses, in plain terms; the passive voice is acceptable. Leave result numbers, definitions, and data-release statements out of it.

**For model papers, state the advance as physics.** Frame the contribution as the physical term added to a named conservation equation, justify each input by the physical definition of the quantity it feeds, mark model outputs as `predicted` or `modeled`, and number the assumptions and state each one positively. When one dimensionless group carries the result, give it a physical meaning.

**Single-manuscript habits.** `including` introduces the members of a set and `i.e.,` an equivalent. In Word manuscripts, figure and table callouts in running text were set in bold; follow the venue for this.

## Abstract, Conclusion, And Sentence Length

- End the abstract on the strongest physical finding or design implication, with its scope built into the sentence. Do not end on a disclaimer, a statement of what the work does not establish, a data or code release, a workflow summary, or a count of records and sources.
- Write the conclusion as one connected paragraph in the present tense, unnumbered unless the venue requires a list. Use "is shown to" for the headline findings, and leave out figure citations and lists of further validation needs.
- Measured on prose only, the author's own sentences average 19 to 22 words, with 6 percent or less above 35 words. The coordinator's `han-hu-research-style.md` carries the full measured prose targets.
