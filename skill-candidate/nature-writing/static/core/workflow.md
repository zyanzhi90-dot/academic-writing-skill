# Writing workflow

Apply these steps within the requested scope. Reuse clear author content and
existing plans; support overall reasoning, specified-part drafting, and
feedback without mandatory sequential approval. Steps 1-3 organize the current
part, 3b resolves necessary ambiguity, 4-6 draft, 7-8 check, and 9 revises.

## 1. Build a one-sentence argument

> In [system/problem], we show [advance] using [approach], supported by [evidence], with [boundary].

Use this as an argument diagnostic, not a fill-in template. For a specified
part, establish its scientific purpose from the available author material;
do not require reconstruction or approval of the whole paper first. Surface
missing premises only when they prevent faithful work in the requested scope.

## 1b. Build the Terminology Ledger

On first contact with the material, extract the recurring terms, abbreviations, notation, and proper names into a Terminology Ledger before drafting any prose. Lock the canonical forms and reuse them across every section. See `../../../nature-shared/core/terminology-ledger.md`.

## 2. Choose section architecture

Pick the section structure from the relevant `section/*.md` fragment and, if needed, deeper patterns from `references/article-architecture.md`.

## 3. Map each paragraph to a governing question or object

Give each paragraph a recognizable governing question or technical object.
Context, gap, approach, result, comparison, mechanism, implication, and
limitation are useful function labels, but a paragraph may need several of
them to answer one question. Split when the governing question changes or a
claim loses its nearby evidence. In a robotics manuscript, use the loaded
`robotics-main-text.md` to check whether a paragraph group, rather than every
individual paragraph, completes a literature comparison.

## 3a. Allocate Results evidence before drafting

When the task includes Results, a full manuscript, main-text compression, or
main-versus-SI placement, load
`../../../nature-shared/core/main-text-discipline.md`. Classify each result as
core discovery, necessary support, qualification, robustness, heterogeneity,
provenance detail, alternative inference, or edge case. Build the shortest
sufficient main-text evidence chain and record the destination of everything
else. Do not bury conclusion-changing evidence in SI.

## 3b. Align the current task; clarify necessary ambiguities

For a request to discuss overall reasoning, provide the argument and dependency
or paragraph map for human discussion. For immediate specified-part drafting,
proceed when its scientific content is clear; an outline is available when
requested, not an approval requirement. Do not require reference-paper approval.

If an unresolved premise would change scientific meaning and prevents faithful
drafting, summarize the intended claim, evidence, scope, relevant terminology,
and uncertain point; ask only the necessary targeted questions and wait for
that information. Otherwise retain the supported scope and place material
missing-input notes outside prose. Do not repeat questions already answered.

For style feedback, calibrate from author-selected reference papers, the current
draft, or stated preferences; ask for a sample only if needed. In robotics work,
follow the loaded `robotics-writing-examples.md` instructions to coordinate main
and supplemental references. Learn organization, subject focus, syntax,
information order, and ordinary collocations; preserve author facts, terminology,
and evidence strength rather than matching hedging, length, or voice ratios.

## 4. Draft from evidence outward

Keep claims near the data that support them. Do not stack claims at the top of a section then leave evidence at the bottom.

For robotics abstracts and body work, apply the loaded shared example reference
during generation: read suitable cards' actual English and analysis, then adapt
their realization to the author's content. Preserve relevant reference choices
across parts; do not leave example use until a synonym pass after drafting.

## 5. Calibrate verbs to evidence strength

`show` / `demonstrate` need strong direct evidence. `suggest` / `indicate` are for trend-level or indirect evidence. `may` / `could` are for plausible but unverified mechanisms.

## 6. Remove unsupported novelty and universal claims

Sweep for `first`, `unique`, `unprecedented`, `comprehensive`, `complete`, `always`, `never`. Replace with bounded claims or delete.

## 7. Run a paragraph-flow check

- One recognizable governing question or object per paragraph; supporting
  functions may differ.
- The opening may be a condition, definition, problem, or claim if it makes the
  paragraph's purpose clear quickly.
- Trace what each sentence takes from earlier text and what it changes,
  tests, or qualifies. Do not insert a connective without the stated relation.

For full reverse-outlining, open `references/paragraph-flow.md`.

## 8. Return prose plus notes

Before delivery of robotics abstracts or body prose, perform the common internal
phrase-to-sentence-to-context check in the loaded `robotics-writing-examples.md`.
Fix determinate errors, recheck affected relations, and retain reasonable variants.
Output checked prose plus material assumptions, missing inputs, and evidence
questions outside the manuscript. The audit itself need not be printed. See
`output-format.md`.

## 9. Revise by targeted edit, not full rewrite

When the user reacts to a draft, "this is not what I meant" is usually local — a wrong claim, a mis-framed paragraph, the wrong result leading. Do not silently re-draft the whole section: a full rewrite breaks the paragraphs that were already right and forces the user to re-check everything.

- Change **only** the paragraphs or claims the user flagged; keep the rest verbatim.
- If a requested fix requires a structural change, explain its necessary scope
  and apply it within the authorized task; ask only when scientific intent is
  unresolved or the extension needs the author's decision.
- Keep the Terminology Ledger (step 1b) stable across revisions unless the user changes a term; never let a revision reintroduce a variant of a locked term.
- After revising, re-run relevant checks (steps 5-8), including the shared
  expression check on affected phrases, sentences, and contextual links in
  robotics abstracts/body work; retain reference choices unless redirected.
- If redirection changes the premise, use the corrected author meaning; resolve
  only remaining necessary ambiguity through step 3b.
- Every proposed addition triggers the main-text deletion check: identify the
  new sentence's function, find existing text with the same function, and prefer
  replacement or compression before appending. Re-run the paragraph necessity
  and claim-repetition checks after the edit.
