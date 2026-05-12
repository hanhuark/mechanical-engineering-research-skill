# Mechanical Engineering Research Skill

This repository publishes a Codex skill for thermal-fluid mechanical engineering research.

The skill helps Codex support:

- thermal-fluid literature review and research synthesis
- manuscript-style technical writing
- experimental and numerical data analysis
- hypothesis-driven design of experiments
- plotting and figure discussion
- research presentation planning
- AI/ML workflows for thermal-fluid systems

## Install

Copy the `mechanical-engineering-research` folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\mechanical-engineering-research "$env:USERPROFILE\.codex\skills\mechanical-engineering-research"
```

Restart Codex if the skill is not discovered immediately.

## Update Workflow

Use the repository as the canonical source for future improvements.

1. Edit files in `mechanical-engineering-research/`.
2. Validate the skill:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\mechanical-engineering-research"
```

3. Test the skill on realistic research, writing, analysis, or presentation tasks.
4. Commit changes with a short message describing the improvement.
5. Copy the updated skill folder back into your local Codex skills directory when you want to use the latest version.

## Skill Structure

```text
mechanical-engineering-research/
  SKILL.md
  agents/openai.yaml
  references/
    ai-tools-thermal-fluids.md
    brief-template.md
    literature-review.md
    presentation-slides.md
    technical-writing-analysis.md
```

## Contributing

Contributions should improve reusable research practice, not only add one-off facts.

Good contributions include:

- clearer workflows for thermal-fluid research
- stronger technical writing guidance
- better literature-review synthesis methods
- data-analysis and plotting practices
- presentation design patterns
- AI/ML tool workflows for mechanical engineering
- concise references that Codex should load only when needed

Keep the skill concise and source-aware. Put detailed guidance in `references/` and link it from `SKILL.md`.

## License

No license has been selected yet. Add a license before public release if you want others to legally reuse, modify, and redistribute the skill.
