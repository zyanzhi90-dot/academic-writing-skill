## Draft

### Stability criteria

The stability analysis starts from a force-balance model of an underwater hexapod with six C-shaped legs and eight thrusters: four lateral and four vertical. During walking on rough terrain, the model accounts for body and leg support, thruster forces and moments, fluid and inertial loads, cable forces, leg–terrain friction, and motor torque limits. The analysis treats the legs as massless rigid semicircles, places the body centre of mass at the centre of the hip-joint plane, and assumes identical leg motors and constant, identical friction coefficients at all contacts. These assumptions define the scope of the calculated stability conditions.

The first criterion isolates the vertical thrust component, \(F_y\). Force balance, friction, and motor torque constraints define an allowable interval \([F_{\min},F_{\max}]\); a tested component is admitted when \(F_{\min}\leq F_y\leq F_{\max}\). Its margin to the nearer bound is \(\min(F_y-F_{\min},\,F_{\max}-F_y)\). At the upper bound, supporting-leg torque limits can become active. At the lower bound, contact force may be insufficient to resist fluid and inertial loads, allowing slip. Adjusting vertical thrust can enlarge the calculated margin, although choosing thrust solely to maximize that margin can restrict walking flexibility.

The vertical-thrust criterion holds lateral thrust and stabilizing moments outside its search. It may therefore reject a condition for which a feasible combination of thruster forces and moments exists. The subsequent six-dimensional criterion searches over those combinations under the modeled constraints. Its formulation includes model relaxations and a robust variant that imposes stricter friction constraints. It assesses feasibility in a broader thrust space; it is neither the same test as the vertical interval nor an unconditional stability guarantee for the physical robot.

### Validation results

Simulations on modeled rough terrain examined how the allowable regions changed with loads and model parameters and evaluated stability enhancement through thrust adjustment. These analyses test the criteria within the stated model assumptions. They do not establish that the same allowable regions apply when terrain friction, leg geometry, or mass distribution depart from those assumptions.

Physical climbing trials in a pool used a curved ramp and stairs. Groups with different thrust settings compared the two criteria and their associated enhancement approaches. The reported observations are consistent with adjusting thrusters and joint torques to maintain the desired locomotion on those tested terrains. They support practical feasibility under the tested conditions, but do not establish a probability of success or robustness across other terrain and load conditions.

## Notes

- **Terminology:** “vertical-thrust criterion” refers to the \(F_y\) interval and its margin; “six-dimensional criterion” refers to feasibility over thruster forces and moments. The two names denote distinct tests.
- **Claim–evidence boundary:** The model defines admissible conditions; the simulations assess modeled allowable regions; the pool trials provide physical observations on a ramp and stairs. None alone establishes a guarantee on arbitrary real terrain.
- **Missing inputs:** Exact simulation outcomes, trial group settings, measured locomotion outcomes, and the six-dimensional relaxation details are needed for a quantitative Results account.