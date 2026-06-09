---
description: Check thermal-fluid equations, empirical correlations, and dimensionless groups for validity range, assumptions, units, and claim strength.
---

# Thermal-Fluid Correlation Check

Use `mechanical-engineering-research` to audit equations, correlations, property models, and dimensionless groups before they are used in a manuscript, proposal, design memo, or code workflow.

Workflow:

1. Identify the system, geometry, fluid, boundary conditions, and target metric.
2. List every equation, correlation, empirical constant, and dimensionless group being used.
3. Check validity limits: Reynolds, Prandtl, Nusselt, Rayleigh, Weber, Bond, Mach, phase-change regime, geometry, roughness, orientation, and property range.
4. Check unit consistency and whether properties are evaluated at bulk, wall, film, saturation, or reference temperature.
5. Compare the correlation against the claimed mechanism and output metric.
6. Mark each use as valid, conditionally valid, unsupported, or invalid.

Expected output:

- correlation inventory
- validity-range table
- assumptions and missing inputs
- claim-strength assessment
- safer wording or replacement checks
- next calculations or source lookups
