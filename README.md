# Mechanical Engineering Research Skill

**A Codex skill for thermal-fluid mechanical engineering research, technical writing, data analysis, presentations, and AI-assisted workflows.**

Reusable research guidance for heat transfer, fluid mechanics, boiling, CFD, experiments, literature review, manuscript writing, plotting, presentation design, and machine learning tools for mechanical engineers.

**Works with:** OpenAI Codex skills

[![Skill](https://img.shields.io/badge/Codex-Skill-blue?style=for-the-badge)](mechanical-engineering-research/SKILL.md)
[![Domain](https://img.shields.io/badge/Domain-Thermal--Fluids-orange?style=for-the-badge)](#capabilities)
[![Validation](https://img.shields.io/badge/Skill-Validated-brightgreen?style=for-the-badge)](#validation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/hanhuark/mechanical-engineering-research-skill?style=for-the-badge)](https://github.com/hanhuark/mechanical-engineering-research-skill/stargazers)

---

## What Is This?

This repository publishes a single Codex skill: `mechanical-engineering-research`.

Codex skills are modular instruction packages that give an AI coding/research agent specialized workflows and reference knowledge. This skill helps Codex behave like a stronger thermal-fluid research assistant: more source-aware, more critical, more careful with assumptions, and better aligned with graduate-level research practice.

Each skill includes:

- **`SKILL.md`**: routing instructions, research workflow, and when to load each reference
- **Reference docs**: detailed guidance for literature review, technical writing, data analysis, presentations, and AI/ML tools
- **Agent metadata**: Codex UI metadata in `agents/openai.yaml`

---

## Quick Install

### OpenAI Codex

Clone the repository:

```powershell
git clone https://github.com/hanhuark/mechanical-engineering-research-skill.git
cd mechanical-engineering-research-skill
```

Copy the skill into your Codex skills directory:

```powershell
Copy-Item -Recurse .\mechanical-engineering-research "$env:USERPROFILE\.codex\skills\mechanical-engineering-research" -Force
```

Restart Codex if the skill is not discovered immediately.

### Manual Installation

Copy this folder:

```text
mechanical-engineering-research/
```

into:

```text
~/.codex/skills/
```

On Windows, that is usually:

```text
C:\Users\<you>\.codex\skills\
```

---

## Capabilities

| Area | What The Skill Helps With | Reference |
|---|---|---|
| Research workflow | Source-aware thermal-fluid research, assumptions, correlations, trade studies, validation | [`SKILL.md`](mechanical-engineering-research/SKILL.md) |
| Literature review | Critical review, seminal-work tracing, citation past/future, review figures, benchmark tables | [`literature-review.md`](mechanical-engineering-research/references/literature-review.md) |
| Technical writing | Introduction logic, methodology detail, modeling assumptions, results discussion | [`technical-writing-analysis.md`](mechanical-engineering-research/references/technical-writing-analysis.md) |
| Data analysis | Baseline case analysis, hypothesis-driven DOE, plotting, figure interpretation | [`technical-writing-analysis.md`](mechanical-engineering-research/references/technical-writing-analysis.md) |
| Research coding | Reproducible scripts, notebooks, data pipelines, plotting code, simulation automation, code review | [`research-coding.md`](mechanical-engineering-research/references/research-coding.md) |
| Presentations | Slide logic, graphics-first storytelling, speaker notes, videos/animations, backup slides | [`presentation-slides.md`](mechanical-engineering-research/references/presentation-slides.md) |
| AI/ML tools | BubbleID, SeqReg, CFDTwin, DataDroid-LAM, sensor fusion, surrogate modeling | [`ai-tools-thermal-fluids.md`](mechanical-engineering-research/references/ai-tools-thermal-fluids.md) |
| Briefs | Concise research brief structure for decision-ready engineering summaries | [`brief-template.md`](mechanical-engineering-research/references/brief-template.md) |

---

## Skill Structure

```text
mechanical-engineering-research/
  SKILL.md
  agents/
    openai.yaml
  references/
    ai-tools-thermal-fluids.md
    brief-template.md
    literature-review.md
    presentation-slides.md
    research-coding.md
    technical-writing-analysis.md
```

---

## Usage Examples

### Literature Review

```text
Use the mechanical-engineering-research skill to develop a critical literature review on this thermal-fluid research topic. Synthesize the main theories, methods, limitations, unresolved challenges, and future directions instead of writing a paper-by-paper summary.
```

### Data Analysis Plan

```text
Use the mechanical-engineering-research skill to design a hypothesis-driven DOE for these experiments or simulations. Start from a baseline case, identify the mechanism being tested, and choose cases that can support or refute the hypothesis.
```

### Figure Discussion

```text
Use the mechanical-engineering-research skill to write the results discussion for this figure. Follow description, observation, physical explanation, and comparison with existing work.
```

### Research Coding

```text
Use the mechanical-engineering-research skill to write a reproducible Python analysis pipeline for this experiment. Start with one baseline case, preserve raw data, make units explicit, and generate publication-quality plots.
```

### Research Presentation

```text
Use the mechanical-engineering-research skill to create a 12-slide conference talk outline from this paper, with graphics-first slides and complementary speaker notes.
```

### AI For Thermal Fluids

```text
Use the mechanical-engineering-research skill to plan a BubbleID/SeqReg workflow for extracting boiling interface dynamics and predicting heat flux from videos and acoustic signals.
```

---

## Update Workflow

Use this repository as the canonical source for future improvements.

```powershell
cd mechanical-engineering-research-skill
git pull
```

Edit files under:

```text
mechanical-engineering-research/
```

Validate the skill:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\mechanical-engineering-research"
```

Commit and push:

```powershell
git add mechanical-engineering-research README.md CONTRIBUTING.md
git commit -m "Improve research skill guidance"
git push
```

Copy the updated skill into your local Codex skills directory when you want to use the latest version:

```powershell
Copy-Item -Recurse .\mechanical-engineering-research "$env:USERPROFILE\.codex\skills\mechanical-engineering-research" -Force
```

---

## Validation

This skill was validated with Codex's skill validator:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\mechanical-engineering-research"
```

Expected result:

```text
Skill is valid!
```

---

## Related Tools And References

The AI/ML guidance references several thermal-fluid and mechanical-engineering tools:

| Tool | Use |
|---|---|
| [BubbleID](https://github.com/cldunlap73/BubbleID) | Computer vision for bubble and interface dynamics |
| [SeqReg](https://github.com/cldunlap73/SeqReg) | Sequence regression for boiling and sensor data |
| [CFDTwin](https://github.com/UARK-NED3/CFDTwin) | CFD surrogate modeling and digital-twin workflows |
| [DataDroid-LAM](https://github.com/spier16/DataDroid-LAM) | Lab analysis and automation tooling |
| [MEEG-54403](https://github.com/hanhuark/MEEG-54403) | Machine Learning for Mechanical Engineers course material |

---

## FAQ

**Is this a general mechanical engineering skill?**

It is focused on thermal-fluid research, but many workflows also help with broader mechanical engineering research, technical writing, data analysis, and presentations.

**Does the skill replace reading papers or doing experiments?**

No. The skill explicitly treats literature review, doing, and communication as integrated. It should help plan, analyze, synthesize, and write research more effectively.

**Can I use this with Claude Code, Cursor, or other agents?**

The repository is authored as a Codex skill using `SKILL.md`. Other agents may be able to reuse the markdown guidance manually, but no conversion scripts are included yet.

**How should I contribute improvements?**

Add reusable guidance, not one-off facts. Keep `SKILL.md` concise and put detailed workflows in `references/`. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

**Will updates break my local skill?**

The skill is intentionally simple: one folder with markdown references. Pull updates, validate, and copy the folder into `~/.codex/skills/`.

---

## Contributing

Contributions are welcome. Good contributions improve reusable research practice:

- clearer thermal-fluid research workflows
- stronger literature-review synthesis methods
- technical writing and results-discussion guidance
- data-analysis, plotting, and DOE practices
- reproducible research coding practices
- presentation design patterns
- AI/ML workflows for mechanical engineering

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details.

---

## License

MIT License. See [`LICENSE`](LICENSE) for details.
