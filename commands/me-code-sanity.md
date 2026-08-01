---
description: Run a fast preflight on thermal-fluid research code for units, baselines, leakage, physics checks, and result traceability.
---

# Thermal-Fluid Code Sanity Review

Use `mechanical-engineering-research` for a fast preflight of code used for experiments, CFD post-processing, plotting, or AI/ML workflows. Escalate to `me-code-review` when architecture, refactoring, packaging, or release readiness is in scope.

Workflow:

1. Identify the research question, input data, expected output, and baseline case.
2. Check units, property sources, coordinate systems, time bases, sign conventions, and saved intermediate data.
3. Check that raw data are preserved and processing stages are reproducible.
4. Add sanity checks from conservation laws, correlations, analytical limits, known benchmark cases, or dimensional analysis.
5. For AI/ML workflows, check train/validation/test separation across meaningful thermal-fluid conditions.
6. Check that plots are traceable to data and that figure labels, uncertainty, and case metadata are publication-ready.

Expected output:

- code-risk findings ordered by severity
- missing physics or data checks
- reproducibility improvements
- lightweight tests or assertions
- plot and artifact traceability checklist
