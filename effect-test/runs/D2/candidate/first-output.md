## Draft

### Stability criteria

We model the underwater hexapod as a body supported by six C-shaped legs and assisted by eight thrusters, four lateral and four vertical. The force-balance model accounts for leg–terrain contact, friction, thruster forces and moments, fluid and inertial loads, cable forces, and leg-motor torque limits. For this analysis, the legs have negligible mass, each leg is a rigid semicircle, and the body center of mass lies at the center of the hip-joint plane. The six motors are treated as identical, and all leg–terrain contacts share a constant friction coefficient. The criteria below therefore describe feasibility under these model assumptions.

The first criterion tests the vertical component of thrust, \(F_y\). Force balance, contact friction, and supporting-leg torque constraints define an allowable interval, \([F_{\min},F_{\max}]\). A tested value is admitted when \(F_{\min}\leq F_y\leq F_{\max}\), with its margin to the nearest interval boundary given by
\[
m_y=\min(F_y-F_{\min},\,F_{\max}-F_y).
\]
At the upper boundary, vertical thrust can bring a supporting leg to its torque limit. At the lower boundary, contact force can become insufficient to resist inertial and fluid loads, permitting slip. Adjusting vertical thrust can increase the computed margin, although selecting thrust solely to maximize that margin may restrict walking flexibility.

The interval test holds lateral thrust and moments outside its stabilizing choices. Consequently, failure of this test does not establish that the robot cannot be stabilized by its available thrusters. The subsequent six-dimensional criterion considers feasible thruster forces and moments together. Its formulation includes model relaxations and a robust variant that applies stricter friction constraints. It thus tests a broader set of thrust choices than the vertical interval, while retaining the scope of the modeled constraints; neither criterion by itself guarantees stability on arbitrary real terrain.

### Validation on modeled and physical terrain

Simulations on modeled rough terrain examined how allowable regions changed with loads and model parameters and evaluated stability enhancement through thrust adjustment. These results assess the criteria within the force-balance model. They also make the distinction between the two tests consequential: a vertical-thrust setting excluded by the interval may still warrant evaluation with the six-dimensional criterion when lateral forces or moments can contribute to balance.

Physical climbing trials in a pool then tested the approach on a curved ramp and stairs. Groups using different thrust settings compared the criteria and enhancement approaches. The reported observations are consistent with thruster and joint-torque adjustment helping the hexapod maintain the desired locomotion on those tested terrains. Because the supplied record gives neither numerical outcomes nor a general robustness estimate, these trials support a terrain-specific assessment rather than a claim of universal stability.

## Notes

**Section outline:** model and assumptions → vertical interval and margin → reason for the six-dimensional test → simulation scope → physical-trial scope.

| Canonical term | Meaning used here |
|---|---|
| Vertical-thrust criterion | Feasibility test for \(F_y\) within \([F_{\min},F_{\max}]\) |
| Six-dimensional criterion | Test using feasible thruster forces and moments |
| Stability margin, \(m_y\) | Distance from \(F_y\) to the nearer vertical interval boundary |
| Robust variant | Six-dimensional variant with stricter friction constraints |

**Assumptions or missing inputs:** The notes do not supply the detailed six-dimensional formulation, simulation values, trial outcomes by group, or quantitative uncertainty. Those are needed before making comparative performance or robustness claims.

**Claim–evidence map:** The vertical interval and its failure boundaries follow from the supplied model description; the broader scope of the six-dimensional test follows from its included forces and moments. Simulation supports model-level evaluation, and the pool trials support observations on the curved ramp and stairs. No proof guarantee for real terrain is asserted.