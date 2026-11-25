# Design: Author Interview Mode for AI-Assisted Technical Writing

Status: approved November 25, 2026; implemented on branch `claude/author-interview-mode`. Live dry run pending.

## Problem

AI drafting of technical prose fails mainly on evidence, not on style. A model that is handed a manuscript and a request fills every gap in the author's reasoning with plausible general prose: an application-market opening, a methods inventory, an unbounded claim verb, a limitation softened instead of quantified. The existing author-guided workflow asks for an author story brief before drafting, but its command allows the AI to "ask for or construct" the brief, so the AI can complete the author's decisions itself.

Short, well-scoped tasks with all facts at hand (for example, administrative email) produce strong drafts because every claim can be checked and each unit has one job. The interview mode reproduces those conditions for manuscripts: the author supplies the decisions, the AI supplies the facts it can extract, and drafting proceeds one unit at a time against a written record.

The design adapts the round-based interview in the `grilling` skill (mattpocock/skills): questions are organized as a tree, each round asks the questions whose prerequisites are settled, facts are the AI's job, and decisions are the user's. It departs from that skill in one respect: story-level questions carry no recommended answer, because the quality of the result should depend on the author's understanding rather than on the author's acceptance of a plausible AI answer.

## Decisions

| Question | Decision |
| --- | --- |
| Recommended answers | Author answers story-level questions first, in their own words; the AI then challenges vagueness and mismatch with the manuscript. Editorial questions carry a recommended answer. |
| Pacing | Numbered rounds of 3 to 5 questions, top-down by level. |
| Trigger | Default before substantial drafting or structural revision. Short form for a single paragraph. Skipped when the user says "no interview" or the decision record already covers the section. |
| Weak answers | Recorded as open decisions. The text keeps a visible placeholder or a narrower claim; the AI never fills the answer. |
| Record | `author-decision-record.md` in the manuscript folder, updated after every round. |
| Packaging | Extend the existing author-guided workflow; no new sub-skill. |

## 1. Interview protocol

1. **Intake.** Read the full message, manuscript, figures, notes, and comments as reference. Do not draft. Extract facts from the material: measured quantities, instruments, sampling rates, sample sizes, what each figure plots, and terms already defined. Ask the author only for decisions and for facts that the material does not contain.
2. **Rounds.** Ask numbered rounds of 3 to 5 questions, top-down: story; title, abstract, and keywords; introduction paragraphs; methods; each figure with its discussion; limitations and conclusion. A round contains only questions whose prerequisites are answered.
3. **Author first, then challenge.** Story-level questions carry no suggested answer. After the author answers, compare the answer with the manuscript. Ask a follow-up for a vague answer (which quantity, compared with what, in which regime) and point out a mismatch with the current text. Allow at most two follow-ups per question. Editorial questions (keywords, term choice, section order) carry a recommended answer.
4. **Question quality.** Each question must require domain understanding to answer, and its answer must change the text. Each question quotes the sentence or names the figure that prompted it. Navigation and approval questions ("Shall we move to Section 2?", "Do you accept these changes?", "Anything else?") are not asked; the next step is stated in one line at the end of a round.
5. **Weak answers.** An "I don't know," or an answer that stays vague after two follow-ups, becomes an open decision. The affected text keeps a visible placeholder or a narrower claim. The end-of-interview report lists each open decision with what would resolve it: a reading, an analysis, a measurement, or a discussion with a co-author.
6. **Short form and skip.** A single-paragraph edit receives 2 to 3 questions: the paragraph's takeaway, its evidence, and its claim ceiling, minus any already answered in the record. The interview is skipped on "no interview" or when the record already covers the section.
7. **Completion.** The interview ends when every question at every level is answered or recorded as open and the author confirms the record. Drafting starts only then.

## 2. Question bank

A complete answer is specific (names a quantity, system, and regime), comparative (states the comparison), bounded (uses a claim verb and states what is not established), and traceable (points to a figure, table, equation, or source). A follow-up asks only for the missing element. Factual questions answered by the material are skipped; story questions are always asked.

- **Round 1, story (no suggested answers):** what the reader will know afterward that was not known before, in one sentence; the reader and what they will do differently; the exact missing measurement, explanation, or prediction and the barrier that kept it missing; the strongest supported claim and what it does not establish; the figure and panel that carry the claim.
- **Round 2, title, abstract, keywords:** the phenomenon term the title needs and the modifiers it can lose; whether the title exceeds the claim ceiling; the job of each abstract sentence and the one or two numbers a reader must retain; the sentence stating what the work does not establish, drafted first by the author; keywords, with AI recommendations.
- **Introduction, per 3 to 5 paragraphs:** the one sentence the reader must retain from each paragraph; the supporting citations and the limitation that leads to the next paragraph; the physical limit that motivates the work.
- **Methods:** the controlled variables and the instruments that set or measure them; the uncertainty and sampling rate of the measurement behind the main claim; missing records and the reported quantities they degrade.
- **Each figure:** the question the figure answers; the observation in one sentence with the governing number; the explanation and the alternative explanation, and whether the alternative is excluded or only made less likely; what the figure does not show; for model-derived results, the failure modes and whether a held-out set exists.
- **Limitations and conclusion:** the limitation that most changes the reading of the main result, quantified; the measurement or analysis that would remove it; the two or three conclusions with their claim verbs, reconciled with round 1.
- **Proposals and reviews:** a proposal replaces round 1 with hypothesis, preliminary evidence, decision rule, and risk. A review replaces it with the organizing comparison and the maturity of each evidence class.

## 3. Decision record and drafting

`author-decision-record.md` is created in the manuscript folder and updated after every round. It contains unpublished material and stays with the manuscript; the repository ships only a blank template. Sections: header (document, venue, date, skill version); story (author answers verbatim beside the agreed wording); claims (claim, evidence class, support, allowed verb, what is not established); fact sheet (quantities, instruments, rates, uncertainty, replication, missing records, extracted by the AI and confirmed by the author); terms and symbols; unit decisions (title term, abstract sentence jobs, keywords, paragraph takeaways, figure answers); open decisions (ID, question, consequence, resolution path, affected text); round log. The existing claim-evidence and symbol-unit ledgers may replace the claims and terms tables for a full manuscript.

Drafting rules:

- Draft only from the record and the supplied material. A sentence that depends on an open decision carries a placeholder such as `[OPEN D3: what Fig. 5 establishes]`.
- Use the whole manuscript as reference and one unit as the task: a paragraph, or a figure with its discussion.
- After each unit, report what changed, which record entries were used, and any new open decision.
- Run a separate consistency pass at the end: terms and symbols, repeated numbers, claim verbs against the record, cross-references, and limitations stated twice.
- Start a fresh session for a major section from the record and the manuscript.
- When a later comment changes a recorded decision, update the record before the text.

## 4. Files and tests

- `skills/mechanical-engineering-research/references/author-guided-ai-writing.md`: interview protocol, drafting rules, decision record, short-form depth.
- `skills/mechanical-engineering-research/references/author-interview-question-bank.md` (new): question bank.
- `skills/mechanical-engineering-research/assets/templates/author-decision-record.md` (new): blank template, required by `scripts/validate_repo.py`.
- `commands/me-author-guided-writing.md`: intake, interview rounds, record, unit drafting, reader review, consistency pass.
- `skills/research-writing-literature/SKILL.md`: trigger phrases and interview routing.
- `skills/mechanical-engineering-research/SKILL.md` and `README.md`: updated workflow descriptions.
- `CHANGELOG.md`: entry under Unreleased.
- `tests/thermal-fluid-evals/prompt-fixtures.json`: four synthetic fixtures covering full-manuscript intake, a vague answer, an unanswerable figure question, and a single-paragraph edit with and without "no interview."

Acceptance: `python scripts/validate_repo.py` passes, and a live dry run on one paragraph or figure follows the protocol.
