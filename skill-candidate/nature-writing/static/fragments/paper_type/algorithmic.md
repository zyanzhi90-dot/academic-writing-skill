# Paper type: algorithmic or device

A procedure, tool, or system is proposed; the paper must show it performs reliably and advantageously.

## Argument chain

`task definition + scope -> what the system is -> why it works (design rationale) -> how well it works (evaluation) -> diagnostic comparison when needed -> failure modes + cost characteristics -> applicability boundary`

For robotics systems, map each promised capability or guarantee to its
operating assumptions, component or proof, test, and boundary before ordering
the sections. Use an ablation when it discriminates a claimed component role;
do not require one experiment for every module. See the conditionally loaded
shared robotics body reference.

## Drafting rules

- Make "what the system is," "why it works," and "how well it works" distinguishable. Organize body sections by their evidence roles; abstracts and local paragraphs may combine these functions when their scientific relations remain clear.
- Tie each performance claim to the author-supported evidence and the comparison objects, metrics, and conditions needed to interpret it. Include a dataset or baseline when relevant and provided; keep necessary boundaries attached to the claim.
- Avoid marketing verbs (`leverages`, `enables`, `empowers`) unless they carry concrete information.
- The Discussion must name the failure modes the experiments revealed, not only the wins. Reviewers trust papers that report their own limits.

## Module / pipeline writing

For module-level writing (each component of a pipeline), open `references/method.md` for:

- the three-element pattern (motivation, mechanism, evidence)
- module-motivation templates
- overview-template for the pipeline figure caption + first paragraph
