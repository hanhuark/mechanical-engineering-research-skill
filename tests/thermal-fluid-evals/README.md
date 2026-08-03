# Thermal-Fluid Eval Fixtures

These fixtures are lightweight prompt scenarios for checking whether the skill preserves thermal-fluid rigor across research, writing, code, release, and teaching work. They do not execute model evaluation by themselves; they define the behaviors a reviewer should expect from the skill.

The repository validation script checks that the fixture file contains at least ten scenarios and that each scenario has multiple expected checks. Script behavior is tested separately in `tests/test_skill_scripts.py`.
