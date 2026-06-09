# Contributing

Thank you for improving this thermal-fluid research workflow plugin.

## Guidelines

- Keep `SKILL.md` concise and focused on routing, workflow, and reference selection.
- Put detailed guidance in `skills/mechanical-engineering-research/references/`.
- Put reusable workflow prompts in `commands/`.
- Put public-safe examples in `examples/showcase/`.
- Add or update eval scenarios in `tests/thermal-fluid-evals/prompt-fixtures.json` when changing expected skill behavior.
- Prefer reusable research heuristics over project-specific details.
- Preserve source-aware reasoning: separate evidence, assumptions, inference, and uncertainty.
- Validate the repository, skill, and plugin before opening a pull request.

## Validation

Run:

```powershell
python scripts\validate_repo.py
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\mechanical-engineering-research"
python "$env:USERPROFILE\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" "."
```

## Review Checklist

- Does the change help future research, writing, analysis, plotting, presentation, or AI/ML work?
- Is the guidance concise enough to be useful in a skill context?
- Are new reference files linked from `SKILL.md`?
- Are new workflow prompts placed in `commands/` when they are reusable across tasks?
- Are examples generalizable beyond one paper, dataset, or presentation?
- Do new examples avoid private data, sponsor-specific details, and unsupported source claims?
- Do eval fixtures include concrete expected checks rather than vague quality statements?
