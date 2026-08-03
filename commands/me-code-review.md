---
description: Perform a full thermal-fluid research-code review covering architecture, reproducibility, units, physics, interfaces, tests, and released artifacts.
---

# Thermal-Fluid Research Code Review

Use `mechanical-engineering-research` for a full review or refactor of research code. Use `me-code-sanity` for a fast preflight.

Workflow:

1. Identify the research question and expected outputs.
2. Verify the baseline case is reproducible from raw inputs.
3. Check units, assumptions, constants, paths, metadata, and raw-data preservation.
4. Separate data processing, analysis, plotting, and simulation/ML execution when practical.
5. Add sanity checks based on physics, conservation laws, known correlations, or benchmark cases.
6. Confirm figures and tables can be traced back to scripts and processed data.
7. Review interfaces, deterministic ordering, tests, environment, package/repository structure, and release readiness.

Expected output:

- code review findings or implementation plan
- reproducibility checklist
- suggested project structure
- tests or sanity checks
- next refactor steps
