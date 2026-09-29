## Draft

### Introduction

In hand-guided robotic work, an operator steers a tool while the tool remains in contact with its environment. This setting arises in tasks such as carving and in repeated grinding or polishing. Contact can disturb the tool path even as the operator continues to guide it. The controller therefore has to support *maneuverability*, meaning that the robot remains easy for the person to guide, and *contact stability*, meaning stable interaction and trajectory tracking during environmental contact. Here, *maneuverability* describes guiding effort; it is not a kinematic dexterity measure derived from the robot Jacobian.

These objectives are coupled through robot impedance. Increasing impedance can help resist an environmental disturbance, but may also require the operator to exert more force to steer the tool. Reducing guiding effort too far may, in turn, compromise contact behavior. A controller for simultaneous human guidance and environmental contact must account for this coupling; combining a controller designed for each interaction separately does not, by itself, establish that both objectives will be met.

Research on human–robot interaction offers several ways to interpret or respond to operator guidance, including impedance adjustment from surface electromyography, estimation of human impedance from measured force and position, velocity-based parameter adjustment, inference of intent from movement patterns, and modification of the robot’s reference trajectory. Work on robot–environment interaction has addressed contact forces and disturbances through feedback, learning, planned contact forces, impedance selection, and adjustments during the transition into contact. These lines of work provide relevant components, but the studies described in the author material do not establish how human guidance and uncertain environmental contact should be handled within the same interaction model.

We address this setting by using information from human guidance to preserve *maneuverability* while adapting robot impedance to environmental disturbances in support of *contact stability*. For non-repetitive tasks, the approach uses adaptive impedance learning under the assumption that the environment coefficients and rest position remain constant. For repetitive tasks with spatially periodic disturbances, it uses an iterative version. In the stated interaction model, the controller is designed without prior knowledge of the disturbance or the human reference position. The manuscript analyzes stability and examines the approach on the H-MAN robot using virtual disturbances, physical carving, and repeated grinding or polishing. The conditions of the analysis and the outcomes of those studies must determine the strength of any performance claim.

### Related Work

**Human guidance and impedance adaptation.** One line of human–robot interaction research adjusts robot impedance using surface electromyography as an indication of the operator’s state. Signal variation and constraints associated with neuromuscular information can limit the use of this route. Other approaches measure human force and position directly and infer human impedance from those observations. Both lines seek to make robot behavior responsive to the person, but the material provided here does not show that the cited approaches also address an unknown environment in simultaneous contact with the guided tool.

**Movement-based interpretation of guidance.** Human guidance has also been addressed through velocity-based rules for adjusting control parameters, through intent inference from movement probability distributions or time series, and through changes to the robot’s reference trajectory rather than its impedance. These approaches differ in what they infer from the operator and which control quantity they change. Their relevance to the present task is the use of guidance information; whether they maintain the desired contact behavior under concurrent, uncertain environmental disturbance requires examination of the individual studies.

**Control of robot–environment contact.** Research focused on the environment side has used feedback, neural methods, and iterative learning to respond to contact forces or disturbances. Other methods generate desired contact forces through feedforward force, impedance, and trajectory design. Reinforcement learning has been used to select impedance parameters from rewards informed by contact force, while fuzzy adjustment of impedance has been used to smooth the transition from free motion into contact. These methods address meaningful contact-control problems. In the work described by the author notes, however, the guiding person is not part of the same interaction model used to formulate environmental contact.

The present study connects these two strands at the point where their control objectives interact. It uses human guidance information to support *maneuverability* and adapts impedance in response to environmental disturbance to support *contact stability*. Its adaptive and iterative versions correspond, respectively, to non-repetitive contact under constant environment coefficients and rest position, and to repetitive work with spatially periodic disturbance. This distinction defines the proposed setting; comparison with specific prior controllers will require the corresponding source papers and evaluation results.

## Section outline

- **Introduction:** task and terms → impedance coupling → relevant research gap → proposed approach and study route.
- **Related Work:** human-state and impedance methods → movement-based guidance methods → environment-contact methods → relationship to the present setting.

## Assumptions or missing inputs

- The Introduction treats the two controller versions as parts of one approach. The author should confirm their exact relationship and preferred technical names.
- Primary references are needed for every prior-work group. No citations were supplied, so none were invented.
- The stability assumptions, comparisons, and experimental outcomes are needed before claiming that the approach achieves either objective or outperforms another controller.

## Claim–evidence map

- **Claim:** Human guiding effort and contact behavior are coupled through impedance. **Evidence:** author’s control rationale. **Status:** supported as motivation; quantitative trade-off needs evidence.
- **Claim:** The approach addresses non-repetitive and spatially periodic repetitive disturbances under different conditions. **Evidence:** author’s method description. **Status:** supported as a design description.
- **Claim:** The approach maintains *maneuverability* and *contact stability*. **Evidence:** stability analysis and H-MAN studies are listed, but their findings are not supplied. **Status:** needs evidence.

## 结构说明

引言先定义双重交互任务，再说明阻抗为何把两个目标耦合起来；独立的 Related Work 按技术路线组织，避免把“已有研究未覆盖本问题”写成“已有方法无效”。全文只预告稳定性分析和实验，不预判结果。