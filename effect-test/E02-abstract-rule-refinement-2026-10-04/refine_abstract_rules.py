"""Surgically refine only the three existing Abstract-specific candidate files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
writing = ROOT / "skill-candidate/nature-writing/static/fragments/section/abstract.md"
polishing = ROOT / "skill-candidate/nature-polishing/static/fragments/section/abstract.md"
reference = ROOT / "skill-candidate/nature-writing/references/abstract.md"
discussion = """If the user asks to discuss the abstract first, give a short Chinese main line
with the intended emphasis and major inclusions and omissions. For a direct
drafting or polishing request, make the same decisions internally and proceed
without a confirmation stage.
"""
evidence = """## Verification expression

Use `Numerical simulation results demonstrate …` (A07) as the default
realization for supported numerical findings and `Experimental studies are also carried out to …` (A04) for an actual experimental study purpose. Read
their English and selection notes from the loaded example reference. Adapt
the evidence object, action strength and complement to author science; use
another approved main-reference realization when it better fits the evidence
and established style. A study purpose is not a demonstrated result.

Select the contribution-level finding supported by each retained evidence
source. A supported capability, comparison or task-dependent effect can be
specific without itemizing each setting or curve. Report a shared finding
jointly when the sources support it; retain separate findings when their
differences matter to the contribution or its evidence boundary. Keep numbers,
platforms and individual observations only when they materially establish or
bound that finding. Do not turn an observed trend into an unconditional claim.

Match theoretical guarantees to their model, object, strength and necessary
conditions. Retain a condition that defines a contribution or limits its
guarantee; omit proof detail that does neither. Preserve the distinction between
theory, simulation and experiment, and the scope of each source when combining
their conclusions. Do not invent results or close with generic validity.
"""
delivery = """## Delivery check

Compare the complete paragraph, consecutive sentences and meaningful phrases
with the selected real English and author facts. Check contribution relations
and content necessity as well as object names, terminology, conditions, syntax
and collocations. Follow the actual length requirement; otherwise use the
selected abstracts' information load to cut excess background and detail.
Repair missing scientific links, unsupported claims and departures from the
author's established style. Preserve correct mature wording and reasonable
variants that express the same supported relationship; the availability of
another wording does not require a change. Place consequential unresolved
author questions outside the abstract.
"""
writing_rules = """## Contribution and reference adaptation

Establish the author-supported contributions, distinguishing the proposed
designs from the established tools they use. For each key design retained,
decide its task role and how it provides the claimed effect or advantage.
Keep an information source, a compensated uncertainty, an output handoff or
another enabling relation when the reader needs it to understand that effect;
leave out internal calculations that do not explain it. A technical name can
suffice when its role is clear; otherwise state the necessary relation.

Choose the main reference by these scientific relationships. Adapt its
whole-paragraph content choices and consecutive sentence logic, replacing
objects, designs, purposes, effects, conditions and evidence with author facts.
Use its actual mature syntax and wording directly where applicable. Fit better
local realizations from other references into the same argument. Establish
this correspondence while composing, rather than choosing an independent
outline and adding a few borrowed phrases afterwards.

Judge consecutive sentences together: is the design's role clear, does its
information or action explain the advantage, and does its output lead to the
next object? Restore a missing contribution relation before shortening;
remove accurate details that do not serve it or delimit the claim. These are
content decisions, not a requirement for every paper to have every relation,
or for every contribution to fit one sentence. Preserve necessary object
identity and scientific scope.
"""
polishing_rules = """## Polishing priorities

Establish the author-supported contributions and distinguish proposed designs
from established tools. Check whether each retained key design has a clear
task role and whether its action or information explains its claimed effect.
Keep an information source, compensated uncertainty, output handoff or other
enabling relation when the explanation depends on it; omit internal calculations
that do not serve that relation. A technical name suffices when its role is
already clear. Restore a missing scientific link before shortening.

Match these relationships to the selected reference's actual whole paragraph
and consecutive sentences. Preserve an already sound argument; repair the
affected sentence group using the reference's content choices, mature syntax
and specific wording, with author facts replacing its scientific content.
Combine better local realizations from other references within that argument.
Judge groups and their phrases by contribution understanding, support and
necessary scope. Not every paper needs every relation or the same sentence count.
"""

for path, marker, rules in ((writing, "## Diagnostics before submitting the draft", writing_rules),
                            (polishing, "## Polishing priorities", polishing_rules)):
    old = path.read_text(encoding="utf-8")
    assert old.count(marker) == 1
    prefix = old[:old.index(marker)]
    new = prefix + rules + "\n" + discussion + "\n" + evidence + "\n" + delivery
    path.write_text(new, encoding="utf-8", newline="\n")
    print(path.relative_to(ROOT), "words", len(old.split()), "->", len(new.split()))

old = reference.read_text(encoding="utf-8")
new = old.replace(
    "For the contribution sentence(s), usually mention the technical term/name only; do not explain every detailed step.",
    "State the design's task role and supported advantage; include the enabling relation needed to understand them, without listing implementation steps.")
new = new.replace(
    "For the implementation sentence(s), usually mention the technical term/name only; do not explain every detailed step.",
    "Name the implementation and explain how its design provides the stated role or advantage; omit internal steps that do not serve that explanation.")
new = new.replace(
    'The ability to express "contribution + advantage" in one sentence is very important for writing a good abstract.',
    "Keep each contribution connected to its advantage; use consecutive sentences when an enabling relation needs explanation, rather than forcing both into one sentence.")
assert old != new
reference.write_text(new, encoding="utf-8", newline="\n")
print(reference.relative_to(ROOT), "three decision notes refined; options and examples preserved")
