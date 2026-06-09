# Example: Proposal Aims Rewrite

## Weak Version

> Aim 1: Develop a novel cooling system.
>
> Aim 2: Use CFD and machine learning to optimize performance.
>
> Aim 3: Demonstrate broad impact for energy systems.

## Diagnosis

The aims are broad but not reviewable. They do not define the technical barrier, hypothesis, validation method, success metric, risk, or expected output. CFD and machine learning appear as activities rather than an integrated evidence chain.

## Stronger Version

**Overall goal:** Establish and validate a compact cooling strategy that maintains target device temperature while reducing pumping-power penalty under transient heat loads.

| Aim | Reviewer-ready structure |
|---|---|
| Aim 1 | Quantify the coupled heat-transfer and pressure-drop limits of three candidate channel geometries under matched heat flux and flow constraints. Success metric: thermal resistance and pumping power measured with propagated uncertainty. |
| Aim 2 | Validate a reduced-order model against baseline experiments and targeted CFD cases to identify geometry and flow regimes where the model remains predictive. Success metric: prediction error below a stated threshold across held-out operating conditions. |
| Aim 3 | Demonstrate transient thermal control on the best-performing geometry and define design rules for scale-up. Success metric: temperature overshoot, settling time, pressure-drop penalty, and repeatability across repeated tests. |

## Risk and Alternative Logic

| Risk | Alternative |
|---|---|
| CFD does not match measured heat-transfer coefficients | Use CFD only for mechanism visualization and rely on calibrated reduced-order model for design rules |
| Pressure drop erases thermal benefit | Re-rank geometries by thermal resistance per pumping power |
| ML model overfits one facility | Split train/test by geometry or operating condition, not by random frames from the same run |
