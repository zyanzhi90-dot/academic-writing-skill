# Paper type: algorithmic or device

The argument proposes a procedure, tool, or system and must show that it performs reliably and advantageously.

For a robotics system, compare the task and assumptions, claimed guarantee or
capability, component or proof, tested condition, and boundary before revising
section order. The shared robotics body reference supplies the domain checks;
an ablation is useful where it isolates a component, not obligatory per module.

## What the reader expects

- a clear problem formulation and the precise scope being claimed
- the proposed procedure or device, described to a level a peer could re-implement
- a fair comparison against credible baselines under matched conditions
- ablations or controls when needed to isolate a claimed component or mechanism
- failure modes, runtime/cost characteristics, and applicability boundaries

## Polishing priorities

- Keep "what the system is," "why it works," and "how well it works" distinguishable. Preserve reasonable body-section organization and integrated abstracts or local paragraphs when their scientific relations are clear.
- Tie performance claims to author-supported evidence and the comparison objects, metrics, and conditions needed to interpret them. Include a dataset or baseline when relevant and provided; preserve necessary boundaries.
- Avoid marketing verbs (`leverages`, `enables`, `empowers`) unless they carry information.
- The Discussion should name the failure modes the experiments revealed, not only the wins.
