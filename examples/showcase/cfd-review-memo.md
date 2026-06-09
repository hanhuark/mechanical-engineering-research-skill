# Example: CFD Review Memo

## Input

> Our CFD proves that the finned heat sink is optimal. The model used steady RANS with a k-epsilon turbulence model, constant air properties, one mesh, and an outlet pressure boundary. The average heat-transfer coefficient is 32% higher than the baseline. Pressure drop is not included.

## Plugin-Style Review

**Bottom line:** The CFD result may support a limited comparison between two simulated geometries, but it does not prove optimality. The claim should be narrowed until the simulation setup, validation, pressure-drop penalty, and design space are documented.

| Check | Concern | Why it matters | Next action |
|---|---|---|---|
| Regime | Reynolds range is not stated | The turbulence model cannot be judged without knowing whether the flow is laminar, transitional, or turbulent | Report Reynolds number based on hydraulic diameter and inlet velocity |
| Mesh | Only one mesh is mentioned | Heat-transfer coefficient is sensitive to near-wall resolution | Add grid-independence study and wall-normal resolution metrics |
| Wall treatment | y+ and wall function treatment are absent | RANS heat-transfer prediction depends strongly on wall treatment | Report y+, wall functions, and thermal boundary-layer treatment |
| Properties | Constant air properties are assumed | Acceptability depends on the temperature rise | State reference temperature and compare with variable-property sensitivity |
| Validation | No benchmark or experiment is cited | CFD alone is not evidence unless bounded by validation | Compare against a canonical case, correlation, or experimental measurement |
| Tradeoff | Pressure drop omitted | Heat-transfer gain can be canceled by pumping/fan power | Report pressure drop, thermal resistance, and performance per pumping power |
| Optimization | Design space absent | "Optimal" requires constraints and objective function | Define geometry variables, objective, constraints, and search range |

## Safer Claim

> In the tested CFD cases, the finned geometry increased the predicted average heat-transfer coefficient by 32% relative to the baseline. This result should be interpreted as a preliminary simulation trend until grid independence, wall-treatment sensitivity, pressure-drop penalty, and validation against benchmark data are completed.
