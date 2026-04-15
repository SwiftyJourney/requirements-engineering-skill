---
name: requirements-engineering
description: >
  Transform vague or incomplete requirements into well-defined, testable
  specifications using BDD (Behavior-Driven Development), Use Cases,
  Model Specs, Payload Contracts, flowcharts, and architecture diagrams.
  Use this skill when users need help with (1) Refining unclear or "lousy"
  requirements, (2) Writing user stories with clear narratives and acceptance
  criteria, (3) Creating use cases for software features, (4) Defining model
  specs and payload contracts, (5) Generating flowcharts and architecture
  diagrams, (6) Bridging technical and business requirements, or
  (7) Converting feature ideas into implementable specifications.
---

# Requirements Engineering — Essential Developer Methodology

## Agent Behavior Contract

When this skill is active, follow these rules **strictly**:

1. **Every feature specification must include all 7 artifacts**: BDD Narrative, Acceptance Criteria, Use Cases, Model Specs, Payload Contract, Flowchart, Architecture Diagram.
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

## Feature Specification Artifacts

Each feature must be self-contained with these 7 artifacts:

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
9. Domain terminology is consistent across all 7 artifacts
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
- **Navigation index**
  - [references/_index.md](references/_index.md)
