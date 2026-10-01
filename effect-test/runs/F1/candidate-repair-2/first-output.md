**Routing:** manuscript; algorithmic paper; Introduction, Method, Analysis, Experiments, Discussion, and Conclusion; English; generic robotics journal.

**Central argument:** A motion model trained from multiple demonstrations can generate point-to-point references for an adaptive neural controller, with the model demonstrated on pouring and drawing tasks and tracking evaluated separately on a Baxter arm carrying a payload.

## Draft

### Introduction

Learning a robot movement from demonstration involves two related tasks. A motion model must turn recorded trajectories into a reference that can be reproduced or adapted to a new start, goal, or duration. The robot must then track that reference despite differences between its modeled and actual dynamics. Addressing the first task does not, by itself, resolve the second, particularly when a manipulator carries an uncertain payload.

Dynamic-system motion models provide a way to generate stable, extensible trajectories. A conventional dynamic movement primitive (DMP) can represent a point-to-point motion from one demonstration, but its original locally weighted regression formulation treats multiple demonstrations as separate models rather than combining their features in one DMP. Probabilistic models based on a Gaussian mixture model (GMM) and Gaussian mixture regression (GMR) offer a way to encode variation across demonstrations. Separately, uncertain manipulator dynamics motivate adaptive tracking control. These are distinct problems in reference generation and physical execution.

This study combines a demonstration-based motion model with an adaptive neural controller. Phase–forcing samples from multiple demonstrations are modeled by a GMM, and GMR estimates the forcing function of a single DMP. The resulting joint trajectory is supplied to a controller that uses a radial basis function neural network (RBFNN) to approximate uncertain dynamics while enforcing a prescribed position-error envelope. Analysis addresses conditional boundedness of the closed-loop system. Baxter experiments examine controller tracking with a payload and demonstrate motion reproduction and goal adaptation in pouring and drawing tasks. Each experiment evaluates the component and operating conditions it actually tests.

### Method

#### System architecture and motion scope

The system has two components in sequence. The learned DMP generates a reference trajectory from guided demonstrations; the adaptive neural controller uses that trajectory as the desired manipulator motion. The motion model is described for one-dimensional point-to-point trajectories, such as an individual joint coordinate. Cartesian motion can likewise be represented through one-dimensional components. This representation defines how a movement is generated; it does not specify how accurately a physical robot will track it.

#### Combining demonstrations in one motion model

The DMP contains a spring–damper component directed toward a goal, a decaying phase variable, a bounded nonlinear forcing function, a start and goal, and a positive time constant. For each recorded demonstration, position, velocity, and acceleration provide samples of the nonlinear forcing function at corresponding phase values. Samples from multiple demonstrations of the same task form a combined phase–forcing data set. A GMM encodes this data set, and GMR estimates the phase-dependent forcing function used by one DMP.

The generated movement can be adapted by changing its start and goal, while changing the time constant changes its duration. Under the stated condition that the nonlinear forcing function is bounded, the phase-dependent forcing term decays and the DMP tends toward its goal. To moderate initial acceleration, an exponentially converging intermediate state replaces the fixed goal in the spring–damper component. Because that state converges to the goal, this modification retains the stated goal-convergence behavior.

#### Adaptive neural trajectory tracking

The manipulator dynamics are represented as

\[
M(\theta)\ddot{\theta}+C(\theta,\dot{\theta})\dot{\theta}
+G_0(\theta)+\tau_p=\tau,
\]

where \(\tau_p\) is payload torque and \(\tau\) is commanded torque. The DMP-generated joint trajectory is the reference \(\theta_d\). The position controller forms a desired joint velocity from that reference, and the velocity controller generates torque. An RBFNN in the velocity controller approximates uncertain dynamics, including effects relevant to tracking under an unknown payload.

A time-varying performance function sets a decaying envelope for position error:

\[
\delta(t)=(\delta_0-\delta_\infty)e^{-at}+\delta_\infty,
\]

with positive parameters and \(\delta_\infty<\delta_0\). The controller is designed so that bounded transformed position error supports the prescribed transient bound. This envelope concerns position tracking; it is separate from the DMP’s goal-convergence property.

### Analysis

#### Conditional motion and closed-loop properties

The motion-model argument depends on the decaying phase variable and a bounded nonlinear forcing function. As the phase-dependent forcing contribution diminishes, the spring–damper component directs the generated trajectory toward its goal. The exponentially converging intermediate state changes the initial response while preserving convergence of the goal input. These properties concern the generated reference, not tracking error on the robot.

For the controller, the stated Lyapunov analysis establishes **semiglobal uniform boundedness** of closed-loop signals when \(\theta_d\) and \(\dot{\theta}_d\) are bounded. Boundedness of the transformed error supports the prescribed position-error envelope. The result is conditional on the reference and controller assumptions; it does not establish global, asymptotic, finite-time, or fixed-time convergence. The physical experiments provide a separate observation of tracking on the tested robot.

### Experiments

#### Payload tracking on Baxter

Controller tracking was tested on a Baxter robot, which has two seven-degree-of-freedom arms. For this comparison, the left gripper carried a 0.94 kg payload. A circular Cartesian trajectory at fixed orientation was converted to joint references by inverse kinematics. The controller was evaluated with neural learning disabled and enabled.

With learning disabled, joint tracking errors were relatively high. With learning enabled, all tested joint errors lay within \([-0.04,0.04]\) rad, and the compensation torque increased. This comparison supports improved tracking under the reported payload and trajectory conditions. It does not quantify a statistical effect or establish performance across other payloads or operating ranges.

#### Pouring motion reproduction and goal change

Five guided demonstrations of a pouring task moved four joints while the remaining joints stayed fixed. The combined demonstrations were used to learn a DMP that reproduced the task motion. When the goal was changed, the learned model guided Baxter to pour into another cup while retaining the motion profile. This test illustrates reproduction and goal adaptation for the demonstrated pouring task; no numerical success rate was reported.

#### Drawing from irregular demonstrations

In a separate drawing task, five irregular human-guided demonstrations were learned in task space. The resulting drawn curve was smoother than the demonstrated paths. Sensor measurement errors were identified as one possible contributor to distortion in the recorded paths. The drawing result shows the behavior of the learned motion model in this task, without isolating the cause of the irregularities or measuring generalization across a population of tasks.

### Discussion

The two sets of experiments support complementary, narrower conclusions about the combined system. The pouring and drawing tests show that the learned motion model can produce usable task trajectories from the supplied demonstrations and adapt a pouring movement to a changed goal. The payload comparison shows that neural learning improved observed joint tracking for the tested circular trajectory. Together, they illustrate a route from demonstration to physical execution, while leaving the contributions of the two components experimentally distinct.

Combining phase–forcing data through GMM and GMR addresses the single-model use of multiple demonstrations that the original locally weighted regression formulation does not provide. The reported motion tests demonstrate the behavior of the resulting DMP, but do not isolate the separate effects of GMM and GMR. Likewise, the increased compensation torque is consistent with the controller responding to uncertain dynamics; the comparison does not identify how much of the tracking change is attributable specifically to payload compensation.

The theoretical and empirical claims have different scopes. The boundedness result applies under its stated reference and controller conditions, whereas the error range is an observation from one reported Baxter tracking setup. The pouring and drawing examples establish task-specific behavior, without a measured success rate over arbitrary tasks. Testing additional payloads and trajectories would clarify the controller’s operating range; a component comparison within the motion model would clarify which part of the probabilistic representation accounts for its observed behavior.

### Conclusion

This study connects a DMP learned from multiple demonstrations to adaptive neural tracking on a robot manipulator. Conditional analysis supports bounded closed-loop behavior, while Baxter tests show improved tracking in the reported payload experiment and task-specific motion reproduction and adaptation in pouring and drawing. The evidence supports these demonstrated settings and does not establish performance for arbitrary tasks, payloads, or uncontrolled contact.

## Notes

**Terminology ledger**

| Canonical term | First-use definition or role |
|---|---|
| DMP | Dynamic movement primitive; generates reference trajectories |
| GMM / GMR | Gaussian mixture model encodes combined phase–forcing samples; Gaussian mixture regression estimates the forcing function |
| RBFNN | Radial basis function neural network; approximates uncertain dynamics in the controller |
| \(\theta_d\) | DMP-generated desired joint trajectory |
| \(\tau_p\) / \(\tau\) | Payload torque / commanded torque |
| \(\delta(t)\) | Decaying position-error performance envelope |

**Assumptions or missing inputs:** The four pouring joints are not named in the supplied notes, so the draft does not name them. Controller gains, RBFNN architecture and update law, GMM specification, proof conditions beyond those supplied, trial counts, and quantitative pouring or drawing outcomes are also absent. These details are needed for a reproducible final Methods and Results account. Prior-work citations require author verification.

**Claim–evidence map:** Multiple-demonstration motion generation is supported by the stated GMM/GMR construction and the task demonstrations. Conditional closed-loop boundedness is supported by the reported Lyapunov analysis, with proof details still needed. Improved tracking is supported by the enabled-versus-disabled comparison on the loaded Baxter arm. Broader generalization and the separate contributions of GMM and GMR need further evidence.

**Main-text discipline audit:** The tracking comparison and two task demonstrations form the main evidence chain. The conditional guarantee and the distinct scope of each test remain beside the claims they bound. No earlier draft was supplied, so a before-and-after word count does not apply.