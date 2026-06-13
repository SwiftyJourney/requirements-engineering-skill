---
name: requirements-engineering
description: >-
  Use this skill to turn vague, ambiguous, or "lousy" requirements into precise,
  testable specifications BEFORE any code is written -- even when the user never
  says "BDD", "use case", or "acceptance criteria". Trigger when someone has a
  half-baked feature idea, an under-specified ticket, or a business brief that's
  "open to interpretation" and needs it pinned down: clarifying questions,
  As-a/I-want/So-that narratives, Given/When/Then acceptance criteria, use cases
  (data inputs, happy path, error and cancel courses), model-spec tables,
  request/response payload contracts, flowcharts, and module-dependency diagrams.
  This is the SPECIFICATION altitude -- WHAT to build and the contracts to honor.
  Hand off the implementation to the iOS architecture skill (composition root,
  layers, packages, concurrency), SwiftUI view code, and Swift Testing syntax --
  do NOT use this skill to write or refactor that code, only to define what it
  must satisfy.
---

# Requirements Engineering

## Agent Behavior Contract

When this skill is active, follow these rules **strictly**:

1. **Include the artifacts the feature warrants** — the full set (BDD Narrative, Acceptance Criteria, Use Cases, Model Specs, Payload Contract, Flowchart, Architecture Diagram) for a non-trivial networked feature, but omit ones that don't apply: an online-only feature needs no offline narrative, cache use case, or Cancel course; a feature reusing a model needs no new Model Spec. The architecture diagram is one shared **app-level** graph, not one per feature.
2. **Never accept vague requirements without asking clarifying questions first** — Who are the user types? What happens offline? What are the error cases?
3. **Use domain-specific language consistently across all artifacts** — if the domain says "image feed" not "feed items", use "image feed" everywhere.
4. **Every use case must have a Data section** listing ALL inputs, a Primary course, at least one Error course, and a Cancel course where applicable.
5. **Model Specs must use Property/Type tables** — not prose descriptions.
6. **Payload Contracts must show HTTP method, path, status code, and example JSON** — including optional fields demonstrated by omission.
7. **Requirements are living specifications** — iterate and refine as understanding evolves, do not treat as one-time documents.

---

## Requirements Diagnostic Table

| Symptom | First check | Smallest fix | Deep dive |
|---|---|---|---|
| Requirement is "susceptible to personal interpretation" | Missing user types / scenarios | Ask clarifying questions, split into narratives | `references/bdd-narratives.md` |
| BDD scenario covers only happy path | Missing error/offline/edge cases | Add error courses and cancellation | `references/use-cases.md` |
| Use case mixes multiple responsibilities | Separation of concerns | Extract into focused use cases (Load vs Validate vs Cache) | `references/use-cases.md` |
| No data contract between frontend and backend | Missing model specs / payload | Add Property/Type table + JSON contract | `references/model-specs-and-contracts.md` |
| Domain terms inconsistent across docs | Language alignment gap | Audit and rename terms consistently | `references/domain-language.md` |
| Diagram shows only happy path | Missing error flows | Add error/fallback branches | `references/diagrams.md` |
| Architecture diagram is generic boxes | Missing module dependencies | Show actual module dependency graph | `references/diagrams.md` |
| No traceability from requirements to code | Missing artifact mapping | Map BDD -> tests, use cases -> classes | `references/feature-specification-workflow.md` |

---

## Gotchas

- **Dependency-arrow notation carries two facts, not one.** Head fill = "is-a/conforms-to" (open) vs. "depends-on" (filled); line style on a filled head = strong (solid, a stored `let`) vs. weak (dashed, a method parameter). Four meanings, easy to get wrong — always include a legend. See `references/diagrams.md`.
- **A query that mutates state is the smell.** Load is a side-effect-free query; deleting the cache is a command — split them (CQS). The case study briefly put a delete on the Load path, then extracted `Validate Cache`. See `references/use-cases.md`.
- **Collection-empty ≠ single-resource-empty.** An empty/expired *collection* cache is an empty success ("delivers no images"); an empty *single keyed resource* (image data by URL) is a **not-found error**.
- **Optionality is shown by omission, not prose.** In payload-contract JSON, include the optional field in some example items and omit it from others — never write "(optional)" only in prose or use `null`.
- **The canonical domain term is the domain experts' word**, not the team's preference (ubiquitous language). "Images" replaced "Items" because that's what the experts call them.
- **Artifact count follows behavior, not a quota.** Don't pad an online-only feature with offline narratives and Cancel courses to "complete the seven".

---

## Feature Specification Artifacts

A feature draws from this catalog of artifacts — use the ones its behavior warrants (the full set for a non-trivial networked feature; fewer for online-only or model-reusing features):

| # | Artifact | Purpose | Template |
|---|---|---|---|
| 1 | BDD Narrative | Define who, what, why per user type | `references/bdd-narratives.md` |
| 2 | Acceptance Criteria | Given/When/Then scenarios | `references/bdd-narratives.md` |
| 3 | Use Cases | Step-by-step system behavior (Data/Primary/Error/Cancel) | `references/use-cases.md` |
| 4 | Model Specs | Property/Type tables for domain entities | `references/model-specs-and-contracts.md` |
| 5 | Payload Contract | HTTP method + path + response JSON | `references/model-specs-and-contracts.md` |
| 6 | Flowchart | Decision flow with error branches | `references/diagrams.md` |
| 7 | Architecture Diagram | Module dependency graph | `references/diagrams.md` |

---

## The 6-Step Process

1. **Identify** — Recognize vague requirements ("susceptible to personal interpretation")
2. **Clarify** — Ask Who / What / Where / When / Why / How
3. **Specify BDD** — Write narratives and acceptance criteria -> `references/bdd-narratives.md`
4. **Define Use Cases** — Write procedural steps with cancel courses -> `references/use-cases.md`
5. **Model & Contract** — Create model specs and payload contracts -> `references/model-specs-and-contracts.md`
6. **Visualize & Document** — Generate diagrams, compile feature spec -> `references/diagrams.md`, `references/feature-specification-workflow.md`

> End-to-end guide: [feature-specification-workflow.md](references/feature-specification-workflow.md)

---

## Guardrails

- Do not accept "As a user, I want X, So I can X" — always specify concrete user types
- Do not write use cases without a Data section listing all inputs
- Do not omit Cancel courses for operations involving network or async work
- Do not mix domain terms — if BDD says "image feed", use case must say "image feed", not "feed items"
- Do not create architecture diagrams without showing module dependencies and protocol boundaries
- Do not treat requirements as a one-time document — they evolve with the code
- Do not include implementation details in BDD narratives — keep them behavioral
- Do not describe models as prose — use Property/Type tables

---

## Verification Checklist

When reviewing a feature specification:

1. Every BDD narrative specifies a concrete user type (not just "user")
2. Every acceptance criterion has Given/When/Then with specific preconditions
3. Every use case has Data, Primary course, and at least one Error course
4. Cancel courses exist for all cancellable operations
5. Model Specs have Property/Type tables for every domain entity
6. Payload Contract shows HTTP method, path, status code, and example JSON
7. Flowchart includes error/fallback branches (not just happy path)
8. Architecture diagram shows module dependencies (not generic boxes)
9. Domain terminology is consistent across every artifact
10. Feature specification is self-contained (could be understood independently)

---

## Reference Router

Open the smallest reference that matches the question:

- **Narratives & Criteria**
  - [bdd-narratives.md](references/bdd-narratives.md) — BDD stories, user narratives, acceptance criteria, scenario patterns
- **System Behavior**
  - [use-cases.md](references/use-cases.md) — use case structure, courses, separation of concerns
- **Data Contracts**
  - [model-specs-and-contracts.md](references/model-specs-and-contracts.md) — model specs, payload contracts, JSON examples
- **Visual Communication**
  - [diagrams.md](references/diagrams.md) — flowcharts, architecture, sequence, state diagrams
- **Domain Consistency**
  - [domain-language.md](references/domain-language.md) — terminology alignment, renaming patterns
- **Workflow**
  - [feature-specification-workflow.md](references/feature-specification-workflow.md) — end-to-end feature spec, traceability
