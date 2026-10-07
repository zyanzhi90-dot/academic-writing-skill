# Robotics manuscript body: evidence-grounded decisions

Load this file only when the central subject of a manuscript-body drafting,
restructuring, or polishing task is a robot control, learning, manipulation,
locomotion, or physical-interaction system. It also applies to an independent
Related Work section about such a system and to Chinese-to-English body prose.
Do not load it for an incidental robotics example, a non-robotics paper,
submission administration, titles or abstracts alone, or layout work.

This is a domain refinement of the requesting skill, not a new paper-writing
workflow or a journal policy. Author-provided facts and evidence, current venue
requirements, the shared non-invention and terminology rules, and the relevant
paper-type and section jobs remain in force. The examples below show decisions
under particular technical conditions; none is a required sentence pattern.
For concrete English realization and the common expression check, Introduction-only
work uses [robotics-introduction-examples.md](robotics-introduction-examples.md)
directly; other tasks use [robotics-writing-examples.md](robotics-writing-examples.md)
as routed by the requesting skill. The [19-paper evidence report](../../../机器人论文正文写作证据分析.md)
is an optional project lookup, not a runtime dependency.
PDF page numbers count from the first PDF page, not the printed journal page.

## Evidence and manuscript prose

- Distinguish an author-supported study limitation from missing information in
  the task input. An omitted test, result, or proof detail does not establish
  that the study did not perform it. State a scientific limitation only when
  author evidence supports it; otherwise bound the claim to the evidence given
  and request the missing information in author notes outside the manuscript.
- Keep descriptions of supplied materials, drafting uncertainty, requests for
  author confirmation, and submission-readiness advice outside manuscript
  prose, in the requesting skill's missing-input or revision notes. The prose
  should state the scientific problem, design, evidence, and supported scope.
  Retain necessary technical conditions and local evidence/citation placeholders.

## Whole manuscript and adjacent sections

- Map the task and operating assumptions to the claimed capability or
  guarantee, the design or proof that supports it, the comparison or experiment
  that tests it, and the boundary. Let a later section use or test something
  established earlier. A proof, simulation, and physical trial need not occur
  in one fixed order; state what each actually establishes. P15 pp.2–8
  §§II–IV aligns tracking, boundedness, and force goals with control and Baxter
  tests; P08 pp.2–8 §§II–V aligns output constraints with simulation and robot
  tests; P09 pp.4–8 places simulation before proof.
- For a multi-component system, state the function and failure risk of each
  component, then identify the evidence that separates its contribution when
  such evidence exists. Do not demand one experiment per module. P17 p.7 §V
  explicitly separates tests of its controller and motion model; P06 p.12
  §IV uses an ablation while holding the nominal trajectory fixed.
- A following subsection may arise from a named limitation of its predecessor.
  P18 p.8 §IV Remark 5 to §V moves from a conservative vertical-thrust test
  to a 6-D test. This is a **cross-section** link, not an adjacent-sentence
  example. Close by returning to the opening promise and distinguishing proof,
  observed performance, and extrapolation; P19 pp.11–12 §§VIII–IX explicitly
  bounds generalization from the tested robot and task.
- Apply the existing claim-repetition audit also to operating boundaries across
  sections, including Introduction and independent Related Work. Retain a
  repeated condition when it bounds a new guarantee, comparison, or inference;
  compress or delete a restatement that adds no reasoning. Keep each necessary
  qualifier attached to its claim rather than appending the same limitation
  inventory to every section. See `main-text-discipline.md` §9.

## Introduction and Related Work

- For Introduction, read the dedicated `robotics-introduction-examples.md`
  index directly. Its section, paragraph and expression material realizes the
  author's scientific line, field-value opening, literature capabilities,
  design reasons and effects, and conceptual content selection. Drafting and
  Polishing use the same material within their existing workflows.
- Choose a comparison axis that matters to the present decision: measured
  signal, controlled object, interaction partner, contact or terrain condition,
  guarantee, or generalization regime. A **group of paragraphs** performing
  one comparison task should collectively establish prior capability, its
  conditions, the remaining gap, and why that gap motivates the study. Each
  paragraph supplies only the part its own function requires. Do not force a
  gap or transition at every paragraph end.
- P11 pp.2–3 §I.A–C treats human–robot and robot–environment control in
  separate paragraph groups, then shows why their goals conflict when both
  interactions occur. P12 pp.1–3 §I distinguishes time-driven N-ADS from
  state-driven ADS, then compares stability and flexibility conditions. P18
  pp.1–4 §I.A–B groups models and criteria by assumptions before explaining
  why a leg-and-thruster robot needs a different test. P01 pp.1–2 §I moves
  from motion-only teaching to stiffness transfer and then generalization.
- For Introduction, the contribution should answer the particular unresolved
  condition and say what design addresses it and what supported role or guarantee
  follows. For independent Related Work, retain the connection to what design
  and evaluation address the unresolved condition. A continuous closing paragraph
  and a contribution list are both possible; choose by the paper and venue. Do not
  turn an author's missing method into the gap or dismiss prior methods without
  their actual scope. A separate Related Work section is optional: P19 §II
  uses one, whereas P11 places two literature lines inside §I.

## Paragraphs and consecutive sentences

- Give a paragraph one recognizable governing question or technical object.
  It may need purpose, input, operation, result, comparison, and qualification
  to answer that question. Its opening may be a condition, definition, problem,
  or claim. Split only when the governing question changes or a claim loses
  its nearby support. In P01 p.2 §II.A, one method passage moves from stiffness
  learning purpose to EMG input, estimated stiffness, and controller gains.
  P19 p.11 §VII.D keeps accuracy and execution-time evidence distinct and
  immediately qualifies the latter as not statistically significant.
- For adjacent sentences, identify what the first produces or leaves open and
  whether the next sentence uses, transforms, tests, or limits it. P01 p.2
  §II.A is a stiffness **information chain**, not one grammatical-subject chain:
  its successive subjects are the modality, endpoint stiffness, EMG signals,
  and estimated stiffness profile. P11 p.5 §IV moves from a repetitive-task
  condition to spatially periodic disturbance coefficients and then modifies
  the earlier controller. P19 p.5 §V moves from possible analytical estimation
  through hardware and human-arm dependencies to experimental estimation.
  A connective cannot stand in for the missing technical relation.

## Sentences and technical wording

- Choose a grammatical subject for the current claim: the authors for an
  attributable design decision, the measured or estimated quantity for its
  transformation, a comparator for a result, or the controlled system for a
  conditional guarantee. Active and passive voice both occur. P11 p.5 §IV
  uses “We modify here” for an author action; P01 p.2 §II.A uses a passive
  transfer sentence to track the estimated stiffness profile. Do not require
  adjacent sentences to repeat a grammatical subject or impose a voice ratio.
- Keep the operating domain, initial condition, controller, comparator, and
  scope close to the proposition they limit. P08 p.5 §III Theorem 1 states
  initial output constraints and the controller/adaptive-law condition with
  its fixed-time conclusion. P18 p.8 §IV gives separate consequences for
  vertical thrust that is too large and too small. Split overloaded prose by
  independently supportable propositions, while retaining explicit links from
  conditions to guarantees. Neither short definitions nor longer theorem
  statements fail merely by word count.
- Choose a verb by the operation and evidence, not by a general academic
  synonym list. P01 p.2 §II.A uses EMG to monitor activation, estimates
  endpoint stiffness, and transfers the estimated profile as controller gains:
  observing, inferring, and applying are different operations. P19 p.5 §V
  distinguishes a stability region that could be estimated analytically from
  one found experimentally. P08 p.8 §V.B distinguishes tracking performance
  from possible violation of output constraints. Preserve the metric,
  comparator, conditions, and type of support for “improve”, “outperform”,
  “significant”, and “guarantee”.
- Keep the qualifier next to the claim it bounds. P19 p.11 §VII.D says the
  execution-time trend is not statistically significant before offering a
  “probably because” explanation. P04 p.9 §IV marks a potential use “Though
  not demonstrated here”. Do not upgrade these to demonstrated benefits.
- Use one name for one technical object and different names for different
  assumptions or guarantees. P12 pp.1–2 §I separates N-ADS and ADS; P11
  pp.3–5 distinguishes nonrepetitive/adaptive and repetitive/iterative tasks;
  P18 pp.8–11 separates vertical from 6-D thrust. Finite-time (P02) and
  fixed-time (P08) are different guarantee names. Expand acronyms at first
  use and preserve established notation; grammatical inflection is allowed.
  Use “however”, “therefore”, or similar only when the propositions truly
  contrast or entail a consequence. P19 p.5 §V makes that relation explicit.

## Source anchors

The cited pages and sections are located in these user-provided PDFs:
[P01](../../../文献资料/A_DMPs-Based_Framework_for_Robot_Learning_and_Generalization_of_Humanlike_Variable_Impedance_Skills.pdf),
[P02](../../../文献资料/Adaptive_Parameter_Estimation_and_Control_Design_for_Robot_Manipulators_With_Finite-Time_Convergence.pdf),
[P04](../../../effect-test/E01-abstract-first-drafting-2026-10-02/materials/文献资料/Complementary_Stability_and_Loop_Shaping_for_Improved_HumanRobot_Interaction.pdf),
[P06](<../../../effect-test/E01-abstract-first-drafting-2026-10-02/materials/文献资料/Diffusion-Based Impedance Learning for Contact-Rich Manipulation Tasks.pdf>),
[P08](../../../文献资料/Fixed-Time_Neural_Control_of_Robot_Manipulator_With_Global_Stability_and_Guaranteed_Transient_Performance.pdf),
[P09](../../../文献资料/Human-Like_Adaptation_of_Force_and_Impedance_in_Stable_and_Unstable_Interactions.pdf),
[P11](../../../文献资料/Impedance_Learning_for_Human-Guided_Robots_in_Contact_With_Unknown_Environments.pdf),
[P12](../../../文献资料/Learning_a_Flexible_Neural_Energy_Function_With_a_Unique_Minimum_for_Globally_Stable_and_Accurate_Demonstration_Learning.pdf),
[P15](../../../文献资料/Neural_Control_of_Bimanual_Robots_With_Guaranteed_Global_Stability_and_Motion_Precision.pdf),
[P17](../../../文献资料/Robot_Learning_System_Based_on_Adaptive_Neural_Control_and_Dynamic_Movement_Primitives.pdf),
[P18](../../../文献资料/Stability_Criterion_and_Stability_Enhancement_for_a_Thruster-Assisted_Underwater_Hexapod_Robot.pdf),
[P19](../../../effect-test/E01-abstract-first-drafting-2026-10-02/materials/文献资料/Variable_Impedance_Control_of_Redundant_Manipulators_for_Intuitive_HumanRobot_Physical_Interaction.pdf).
