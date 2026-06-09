# Example: Boiling Literature Matrix

## Review Question

What evidence should be synthesized before claiming that an AI-assisted diagnostic improves boiling heat-transfer interpretation?

## Matrix Structure

| Source family | Mechanism or method | Extract | Validity limits to record | Likely gap |
|---|---|---|---|---|
| Classical pool-boiling correlations | Heat flux, wall superheat, nucleation behavior | Variables, surface condition, pressure, fluid, uncertainty | Surface material, roughness, orientation, pressure, fluid purity | Limited transfer to new surfaces or diagnostics |
| High-speed visualization studies | Bubble departure, coalescence, dry spot dynamics | Frame rate, resolution, segmentation method, synchronized heat flux | Optical access, lighting, depth of field, field of view | Difficult to generalize across fluids and surfaces |
| IR thermography studies | Wall-temperature fields and transient hot spots | Calibration, emissivity, spatial resolution, conduction correction | Substrate thickness, coating, viewing angle | Thermal spreading can blur local events |
| Acoustic or multimodal sensing | Non-visual signatures of boiling regimes | Sensor placement, sampling rate, label source, noise rejection | Facility dependence, coupling path, background noise | Label transfer across rigs is uncertain |
| AI/ML classification or regression | Regime labels, heat-flux prediction, event detection | Train/test split, data source, metrics, failure cases | Leakage across videos or repeated runs, out-of-distribution tests | Accuracy may not imply physical interpretability |

## Synthesis Pattern

The review should not simply list papers. It should connect three evidence layers:

1. **Thermal mechanism:** nucleation, microlayer evaporation, coalescence, dryout, and rewetting.
2. **Measurement access:** what each diagnostic can and cannot observe.
3. **Inference risk:** what an AI or statistical model may learn from facility-specific artifacts rather than boiling physics.

## Output Figure Idea

Create a mechanism-to-diagnostic map: rows are boiling mechanisms, columns are optical, IR, acoustic, electrical, and ML-derived observables. Each cell should mark direct evidence, indirect evidence, or unsupported inference.
