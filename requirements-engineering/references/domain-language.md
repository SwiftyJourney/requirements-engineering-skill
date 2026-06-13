# Domain Language Alignment

Use this when:
- Domain terminology is inconsistent across BDD specs, use cases, models, and code
- Renaming domain concepts as understanding evolves
- Building a glossary for the project
- Reviewing specifications for language consistency

Skip this file if:
- You need to write BDD stories. Use `bdd-narratives.md`.
- You need to define model properties. Use `model-specs-and-contracts.md`.

Jump to:
- [Why Domain Language Matters](#why-domain-language-matters)
- [The Renaming Pattern](#the-renaming-pattern)
- [Domain Glossary Template](#domain-glossary-template)
- [Alignment Checklist](#alignment-checklist)
- [Common Misalignment Signals](#common-misalignment-signals)

---

## Why Domain Language Matters

The same term must appear consistently across ALL artifacts:

| Artifact | Example term |
|---|---|
| BDD Narrative | "image feed" |
| Acceptance Criteria | "image feed" |
| Use Case | "image feed" |
| Model Spec | `FeedImage` |
| Payload Contract | `"items": [...]` (Feed Image objects) |
| Code | `struct FeedImage` |

When terms diverge, ambiguity creeps in. "Feed Items" in the use case but "Feed Images" in the model creates confusion about whether these are the same concept.

**The canonical term is the one the domain experts use** (ubiquitous language). Code and specs conform to the experts' vocabulary, not the other way around — when in doubt, ask what the people who own the domain call it.

---

## The Renaming Pattern

Domain understanding evolves. When it does, rename **everywhere** — not just in one artifact.

### Real-world example (image feed case study)

The project initially used "Feed Items" as the domain term, then renamed to "Feed Images" — not because of the team's evolving taste, but because **"Images" is the term the domain experts use in the specs** (ubiquitous language). The source of the canonical name is the domain expert's vocabulary.

**Before:**
```
Use Case: Load Feed Items
Model: FeedItem (id, description, location, imageURL)
BDD: "System creates feed items from valid data"
Code: struct FeedItem { ... }
```

**After (renamed consistently):**
```
Use Case: Load Image Feed
Model: FeedImage (id, description, location, url)
BDD: "System creates image feed from valid data"
Code: struct FeedImage { ... }
```

**What changed:**
- "Feed Items" -> "Feed Images" / "Image Feed" (across all artifacts)
- `FeedItem` -> `FeedImage` (model name)
- `imageURL` -> `url` (property name simplified — it's obvious from context)
- All use case steps, BDD scenarios, and code updated simultaneously

**Key principle:** A domain rename is an atomic operation across ALL artifacts. Never rename in code without renaming in specifications, and vice versa.

---

## Domain Glossary Template

Maintain a glossary mapping terms to their definitions and usage:

```
## Domain Glossary

| Term | Definition | Used in |
|---|---|---|
| Image Feed | A list of images with metadata (description, location) displayed to the customer | BDD, Use Cases, Model Spec, Code |
| Feed Image | A single image entry in the feed with id, description, location, and URL | Model Spec, Payload Contract, Code |
| Image Comment | A user comment associated with a specific feed image | BDD, Use Cases, Model Spec, Code |
| Cache | Local persistence of feed data for offline access | BDD (offline narrative), Use Cases (cache/validate) |
| Remote | The server-side API providing feed data | Use Cases (load from remote), Payload Contract |
```

**Rules:**
- One row per domain concept
- Definition must be business-focused (not implementation-focused)
- "Used in" column tracks where the term appears — if a term is missing from an artifact, that's a gap

---

## Alignment Checklist

When reviewing a specification for language consistency:

1. **Pick a domain entity** (e.g., "Feed Image")
2. **Trace it through all artifacts:**
   - BDD Narrative: Does it use the same term?
   - Acceptance Criteria: Same term?
   - Use Case name and steps: Same term?
   - Model Spec table header: Same term?
   - Payload Contract JSON keys: Consistent mapping?
   - Flowchart / diagrams: Same term?
3. **Flag any divergence** — even "image" vs "Image" vs "images" matters
4. **Check plural/singular consistency** — "Feed Images" (the collection) vs "Feed Image" (one item) should follow a clear convention

---

## Common Misalignment Signals

| Signal | Problem | Fix |
|---|---|---|
| BDD says "items" but model says "images" | Domain term divergence | Rename to the more domain-specific term |
| Use case says "Load Feed" but code says `RemoteFeedLoader` | Missing domain alignment | Decide if it's "Load Feed" or "Load Feed From Remote" |
| JSON key is `"image"` but model property is `url` | Property name mismatch | Document the mapping in Model Specs or rename for consistency |
| Plural in BDD ("feed items"), singular in model (`FeedItem`) | Inconsistent pluralization | Establish convention: collections are plural, entities are singular |
| Abbreviations in code (`desc`) but full words in specs (`description`) | Abbreviation creep | Use full words everywhere; abbreviations lose meaning over time |
| Different terms for the same concept in different features | Cross-feature inconsistency | Build a shared glossary and enforce it |

---

## Guardrails

- Do not rename a term in one artifact without renaming it in all others
- Do not use generic terms ("item", "thing", "data") when domain-specific terms exist
- Do not abbreviate in specifications — save abbreviations (if any) for code identifiers only
- Do not assume "everyone knows what we mean" — if a term could be ambiguous, define it in the glossary

## Verification

- [ ] A domain glossary exists with all key terms defined
- [ ] Every domain entity uses the same name in BDD, use cases, models, and code
- [ ] No generic placeholders remain ("item", "data", "object") where domain terms should be
- [ ] Property names in Model Spec tables match the domain language
- [ ] Plural/singular usage is consistent across all artifacts
