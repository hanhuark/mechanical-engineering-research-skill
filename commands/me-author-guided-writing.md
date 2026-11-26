---
description: Interview the author, then draft or revise technical writing with AI one unit at a time from an author decision record, preserving the scientific story, evidence boundaries, and reader clarity.
---

# Author-Guided Technical Writing

Use `mechanical-engineering-research` with `author-guided-ai-writing.md` and `author-interview-question-bank.md` for a manuscript, proposal, report, review, or response that will be drafted or revised with AI assistance.

1. **Read everything first.** Treat the manuscript, figures, notes, and comments as reference. Extract the facts they contain; do not draft yet. Read any earlier version the author approved, such as a conference paper, and quote it in round 1. Load the author's style references before proposing any wording.
2. **Interview the author in rounds.** Ask numbered rounds of 3 to 5 questions, top-down from the story to the conclusion. Do not construct the author's answers: story-level questions carry no suggested answer, vague answers get at most two follow-ups that ask only for the missing element, and an unanswered question becomes an open decision. Do not ask navigation or approval questions. For a single paragraph, ask the 2 to 3 question short form. Skip the interview on "no interview" or when the record already covers the section.
3. **Keep the record.** Create or update `author-decision-record.md` in the manuscript folder after every round, with the author's story answers verbatim. Run requested or revealed analyses between rounds and record their results with file paths. Ask for explicit confirmation only of entries the author has not seen.
4. **Draft one unit at a time.** Use the whole manuscript as reference and one paragraph, or one figure with its discussion, as the task. Draft only from the record and the material, and keep `[OPEN Dn: ...]` placeholders where a decision is open. Run the prose metrics on every unit draft before showing it, and report what changed, which record entries it used, and the metrics.
5. **Review at the argument level.** Run the six reader-recovery questions and classify each as accept, revise, or evidence needed. Update the record before the text when a comment changes a recorded decision.
6. **Finish with a consistency pass.** Check terms and symbols, repeated numbers, claim verbs, cross-references, and limitations stated twice against the record. Then run the sentence-level clarity and anti-formulaic pass.

Expected output:

- interview rounds and the author's answers
- `author-decision-record.md`, including open decisions and what would resolve each
- unit-by-unit drafts or revisions with change notes
- accept/revise/evidence-needed decision record from the reader-recovery review
- consistency pass report
