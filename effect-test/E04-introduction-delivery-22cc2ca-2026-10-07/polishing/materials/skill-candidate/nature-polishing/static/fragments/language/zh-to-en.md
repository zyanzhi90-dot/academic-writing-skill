# Language: Chinese-to-English

When the source is Chinese or strongly Chinese-influenced English, do not translate clause-by-clause.

## Workflow

1. Extract the core propositions first. List them in plain English before drafting prose.
2. Reconstruct explicit logical links: contrast, cause, implication, limitation. Chinese academic prose often elides these connectives — restore them.
3. Verify terminology, causality, and hedging strength against the source.
4. Keep technical terms, gene/protein names, model names, dataset names, and statistical terms stable; do not "translate" them into rough paraphrases.
5. Load and apply the English sentence and paragraph rules from `language/en.md` only after the logic is rebuilt. In robotics body prose, use the shared robotics reference to keep measured signals, estimated quantities, controller inputs, and guarantees distinct.

## Common Chinese-influenced patterns to fix

- Topic-comment chains rewritten as subject-verb sentences.
- Strings of short clauses joined by commas — split or add connectives.
- Vague generalizations (`many studies have shown`) — convert to specific citations or remove.
- Hedging asymmetry: Chinese drafts often understate; English Nature-style asks for precise hedging matched to evidence strength, neither over- nor under-claiming.
- Repeated topic nouns require an identity check, not automatic pronoun
  replacement. Keep names that make actions or guarantees clear; replace or
  omit only when the referent and technical role remain unmistakable.
- Determine gap and method order from the current section, scientific content,
  and selected realizations; a method-first abstract need not acquire an
  invented gap or be reordered into an Introduction funnel.
