# Example: Heat-Exchanger Design Matrix

## Decision

Select a compact liquid-cooled heat exchanger concept for an early laboratory prototype where manufacturability and measurement access matter as much as peak heat-transfer coefficient.

## Assumptions

- Single-phase water cooling.
- Low-to-moderate flow rate.
- Bench-scale prototype.
- Performance metric includes thermal resistance, pressure drop, manufacturability, and instrumentation access.

## Mechanism-Based Matrix

| Option | Heat-transfer mechanism | Pressure-drop risk | Prototype risk | Instrumentation access | Best use |
|---|---|---|---|---|---|
| Straight microchannels | High area-to-volume ratio and short conduction path | Medium to high | Medium, depends on machining tolerance | Good if pressure taps and thermocouples are planned early | Baseline and scaling study |
| Pin-fin array | Boundary-layer disruption and wake mixing | High | Medium to high | Moderate, local flow is complex | High-performance comparison |
| Serpentine channel | Long residence time and secondary flow in bends | Medium | Low to medium | Good | Robust first prototype |
| Porous insert | Enhanced mixing and surface contact | High and fouling-sensitive | High | Poor unless pressure drop is central | Exploratory concept only |

## Recommendation

Start with the serpentine channel or straight microchannel baseline, then add the pin-fin array as the aggressive comparator. The porous insert should not be the first prototype unless the research question is specifically about porous-media enhancement, because its pressure-drop, fouling, and diagnostic risks can obscure the thermal mechanism.

## Verification Steps

1. Estimate Reynolds number and expected flow regime for each channel.
2. Calculate pressure drop and pumping power before ranking heat-transfer coefficient.
3. Compare baseline thermal resistance with a simple analytical or empirical estimate.
4. Plan sensor locations before finalizing the geometry.
