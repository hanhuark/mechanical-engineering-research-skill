# Contributing

Thank you for improving this skill.

## Guidelines

- Keep `SKILL.md` concise and focused on routing, workflow, and reference selection.
- Put detailed guidance in `mechanical-engineering-research/references/`.
- Prefer reusable research heuristics over project-specific details.
- Preserve source-aware reasoning: separate evidence, assumptions, inference, and uncertainty.
- Validate the skill before opening a pull request.

## Validation

Run:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\mechanical-engineering-research"
```

## Review Checklist

- Does the change help future research, writing, analysis, plotting, presentation, or AI/ML work?
- Is the guidance concise enough to be useful in a skill context?
- Are new reference files linked from `SKILL.md`?
- Are examples generalizable beyond one paper, dataset, or presentation?
