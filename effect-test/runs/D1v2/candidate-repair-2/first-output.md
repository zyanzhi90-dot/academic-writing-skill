## Draft

### Introduction

In hand-guided robotic work, an operator directs a tool while the tool may also contact an environment whose properties are unknown. This occurs in tasks such as carving and in repeated grinding or polishing. Contact forces can disturb the tool path, so the robot must remain easy for the person to guide while sustaining stable contact and tracking the intended motion. We refer to ease of human guidance as *maneuverability* and to stable interaction and trajectory tracking during environmental contact as *contact stability*. Here, *maneuverability* describes the operator’s experience of guiding the robot; it is not a Jacobian-based measure of kinematic dexterity.

These objectives are coupled through robot impedance. Increasing impedance can help resist disturbances from the environment, but may require the operator to exert more force. Reducing the effort needed for guidance too far may, in turn, compromise contact behavior. The problem is therefore to regulate impedance for two simultaneous interactions: the human guiding the robot and the environment acting on its tool. Treating the two objectives as separate control problems does not by itself resolve their competing demands.

Research on human–robot interaction offers several ways to interpret guidance and adjust robot behavior. Research on robot–environment interaction offers ways to regulate contact forces or respond to disturbances. The relationship between the two matters when guidance and uncertain contact occur at the same time: an impedance change made to resist the environment also changes what the operator feels. This motivates a control design that uses human guidance information while adapting robot impedance to environmental disturbances.

In this study, we develop adaptive impedance learning for nonrepetitive tasks under the condition that the environment coefficients and its stationary *rest position* remain constant. We also develop an iterative version for spatially periodic disturbances in repetitive tasks. In the interaction model considered here, the controller is designed without prior knowledge of the disturbance or the human’s reference position. We examine the design through stability analysis and studies on the H-MAN robot involving virtual disturbances, physical carving, and repeated grinding or polishing.

### Related Work

**Human-guided robot control.** One line of work adjusts robot impedance using surface electromyography to obtain information about the operator. Its use depends on signals that can fluctuate and on constraints associated with the neuromuscular system. Other approaches measure human force and position directly and infer human impedance from those measurements. These routes differ in what they observe and infer, but both address how the robot should respond to human guidance. [Citations needed for the individual approaches and their stated constraints.]

Human guidance has also been addressed through velocity-based parameter rules, intent inference from distributions of motion or time series, and changes to the robot’s reference trajectory rather than its impedance. These methods offer different ways to interpret or accommodate the operator’s motion. For a tool that is simultaneously contacting an unknown environment, however, the control decision must also account for how environmental disturbances affect the path and how impedance changes affect the operator’s effort. [Citations needed for each method group.]

**Robot–environment contact control.** Feedback, neural, and iterative-learning approaches have been used to address contact forces or disturbances. Other methods combine feedforward force, impedance, and trajectory design to produce a desired contact force. Reinforcement-learning approaches can use contact-force information in a reward to select impedance parameters, while fuzzy adjustment of impedance has been used to smooth the transition from free motion to contact. These approaches address distinct contact-control needs; their value does not depend on whether they model a human operator. [Citations needed for the individual approaches.]

The present setting links the two interaction partners through the same impedance: a change that helps the tool resist a disturbance may make human guidance more demanding. The approaches described above motivate control of either guidance or environmental contact, but do not, on the information available here, establish how their objectives should be coordinated during simultaneous hand guidance and unknown contact. Our design uses guidance information to support *maneuverability* while adapting impedance to support *contact stability*. It treats nonrepetitive contact under constant environment coefficients and *rest position*, and spatially periodic disturbances in repetitive work, as distinct operating conditions.

## Notes for the author

**Section outline**

- Introduction: task and definitions → impedance trade-off → joint control question → study design and evaluation route.
- Related Work: human-guidance approaches → environmental-contact approaches → the interaction that connects them.

**Assumptions or missing inputs**

- Full references are needed for every prior-work group and for the stated limits of surface-electromyography-based control. The bracketed citation markers are placeholders, not citations.
- The notes identify stability analysis and H-MAN studies, but provide no outcomes or proof conditions. The draft therefore describes these as evaluation routes and makes no performance claim.
- *Maneuverability*, *contact stability*, and *rest position* follow the author’s supplied terminology.

**Claim–evidence map**

| Claim | Evidence supplied | Status |
|---|---|---|
| Impedance couples guidance effort and resistance to contact disturbances | Author’s stated control trade-off | Supported as motivation |
| The study develops adaptive and iterative versions for different disturbance conditions | Author’s stated design | Supported as a design description |
| The design achieves improved performance or a particular stability guarantee | No results or proof conditions supplied | Not claimed |

**结构说明：**引言采用“任务与技术矛盾→共同控制问题→研究方案”的路径；独立 Related Work 按“人体引导”和“环境接触”两条研究路线组织，最后说明两者在同一阻抗控制中的关系。