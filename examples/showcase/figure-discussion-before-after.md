# Example: Figure Discussion Before and After

## Figure Context

Synthetic figure: heat-transfer coefficient versus Reynolds number for a baseline channel and a ribbed channel. Error bars show propagated uncertainty from temperature, flow, and heat-input measurements.

## Before

> Figure 4 shows that the ribbed channel performs better than the baseline. The heat-transfer coefficient increases with Reynolds number for both cases. The ribbed channel is therefore a superior design.

## Problems

- "Performs better" ignores pressure-drop penalty.
- The mechanism is not explained.
- The uncertainty is not interpreted.
- "Superior design" overclaims a single thermal metric.
- No comparison is made to expected scaling or literature behavior.

## After

> Figure 4 shows that the heat-transfer coefficient increases with Reynolds number for both channels, consistent with stronger forced convection as inertial transport increases. At matched Reynolds number, the ribbed channel produces a higher coefficient than the smooth baseline, which is consistent with boundary-layer disruption and secondary mixing near the rib features. The difference is largest at the upper end of the tested range, where the larger inertial contribution makes rib-induced mixing more effective. The uncertainty bands remain separated for most cases above Re = 900, so the measured enhancement is likely larger than the experimental uncertainty in that range. This thermal benefit should not yet be interpreted as an overall design advantage because the figure does not include pressure drop, pumping power, or manufacturability constraints.

## Follow-Up Checks

1. Add pressure-drop and pumping-power comparison.
2. Compare the smooth-channel trend with an appropriate internal-flow correlation.
3. Report whether the flow is developing or fully developed.
4. State whether properties are evaluated at bulk, wall, or film temperature.
