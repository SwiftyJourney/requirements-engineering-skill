# Feature Specification Workflow

Use this when:
- Building a complete feature specification from scratch
- Adding a new feature to an existing specification
- Reviewing a specification for completeness
- Understanding how requirements map to architecture and tests

Skip this file if:
- You need a specific artifact template. Check the Reference Router in `SKILL.md` for the right file.

Jump to:
- [Feature Specification Block](#feature-specification-block)
- [Incremental Feature Development](#incremental-feature-development)
- [Requirements-to-Architecture Traceability](#requirements-to-architecture-traceability)
- [Living Specification](#living-specification)
- [Complete Feature Specification Template](#complete-feature-specification-template)

---

## Feature Specification Block

Each feature is a **self-contained block** with the artifacts it warrants. This block can be understood independently — a developer reading just the Feed feature spec has everything needed to implement it.

> **Include the artifacts the feature needs — not a mandatory seven.** Default to the full set for a non-trivial networked feature, but omit the ones that don't apply. The real Image Comments feature (Phase 4 below) is online-only, so it has **one** narrative, **one** use case, **no** cache/validate use cases, and **no** Cancel course — and that is correct. A feature reusing an existing model needs **no** new Model Spec. The architecture diagram is **app-level** and shared (see below), not one-per-feature.

**Structure of one feature block:**

```
## [Feature Name] Feature Specs

### Story: [Clear, user-focused title]

### Narrative #1
As a [user type]
I want [action]
So I can [value]

#### Scenarios (Acceptance criteria)
Given [precondition]
When [action]
Then [outcome]

## Use Cases

### [Use Case 1 Name]
#### Data:
- [inputs]
#### Primary course (happy path):
1. [steps]
#### [Error] -- error course (sad path):
1. [error handling]

### [Use Case 2 Name]
[...]

## Model Specs
### [Entity Name]
| Property | Type |
[...]

### Payload contract
[HTTP method + path + JSON]

## Flowchart
[Mermaid — per feature]

## Architecture
[App-level module dependency diagram — one shared graph, updated as modules are added]
```

> **Flowchart vs Architecture diagram.** The flowchart is **per feature** (one decision flow per feature). The architecture diagram is **app-level**: a single shared dependency graph for the whole system, updated each time a new module lands (the case study kept it as one exported image at the bottom of the README, not one-per-feature). When you "add Architecture to a feature block," you are really updating the shared app diagram to include that feature's module.

---

## Incremental Feature Development

Features are added as **independent blocks** without disrupting existing specifications.

### Example: image feed case study progression

The real case-study README grew over ~2 years, and its git history is the honest picture of how a specification actually evolves — not a clean four-phase drop, but a sequence of clarifications, renames, and extractions. The material commits (paraphrased messages verbatim):

| When | Commit message | What changed in the spec |
|---|---|---|
| Start | "Initial commit with feature requirements" | Both narratives (online **and** offline) land together; three use cases (Load Feed, Load Feed Fallback (Cache), Save Feed Items); Feed Item model with `imageURL`; payload `GET *url* (TBD)`. Offline AC has only **two** scenarios — no seven-day rule yet. |
| +2 mo | "Clarify caching requirements" | Offline AC expands **2 -> 3 scenarios** (the seven-day expiry is *discovered* here); use cases renamed to Load Feed **From Remote** / **From Cache** / **Cache Feed**; error courses made specific (invalid-data, connectivity). |
| +1 wk | "Remove references of 'Items' in favor of 'Images' ... used by domain experts" | Domain rename across every artifact: "Feed Items" -> "Image Feed"; model "Feed Item" -> "Feed Image"; property `imageURL` -> `url`. |
| +1 mo | "Extract 'Validate Feed Cache Use Case' ... from 'Load Feed From Cache Use Case'" | The cache-deletion side effect is pulled out of the Load (query) into a new Validate (command) use case — separation of concerns (CQS). |
| +6 mo | "Add `Load Feed Image Data` use cases" | The per-image binary layer: Load Feed Image Data From Remote/From Cache, introducing the **Cancel course** ("does not deliver image data nor error"). |
| +2 wk | "Add 'Cache Feed Image Data Use Case'" | Completes the image-data trio. |
| +1 yr | "Update README with comments feature and new architecture diagram" | A whole independent **Image Comments** feature block (1 narrative, 1 use case, ImageComment + Author models); the feed payload URL is finalized `TBD` -> `GET /feed`. |

Read as conceptual phases, that history is: **(1)** the Feed feature; **(2)** clarify + rename + extract Validate (all *before* any image-data work); **(3)** the image-data layer with its Cancel course; **(4)** the independent Comments feature. The idealized "add a clean block per feature" is only half the story — just as much of the evolution is *refining* an existing block (expanding AC, renaming terms, extracting a use case) as *adding* a new one.

**Key patterns:**
- Each new feature is a self-contained block; existing specs are modified only when understanding of that feature changes (the AC expansion, the rename, the Validate extraction).
- The Comments feature deliberately ships **fewer** artifacts than the Feed — online-only, so no offline narrative, no cache/validate use cases, no Cancel course. Artifact count follows behavior, not a quota.
- Commit the spec change with the same discipline as code, using messages that name the *requirements* decision ("Clarify caching requirements", "Extract ... Use Case") — the git log then reads as the story of how understanding evolved.

---

## Requirements-to-Architecture Traceability

Every requirement artifact maps to a concrete implementation artifact:

| Requirement Artifact | Maps to in Code | Example |
|---|---|---|
| BDD Acceptance Criteria | Acceptance tests | `FeedAcceptanceTests` |
| Use Case (name) | Use-case class or protocol | `LoadFeedFromRemoteUseCase` |
| Use Case Data section | Method parameters | `func load(url: URL)` |
| Use Case Primary course steps | Method implementation | Sequential operations |
| Use Case Error courses | Error types / throwing | `enum Error { case invalidData }` |
| Use Case Cancel course | Cancellation handling | `Task.isCancelled` checks |
| Model Spec | Domain model struct | `struct FeedImage: Hashable, Sendable` |
| Model Spec Property/Type | Stored properties | `let id: UUID` |
| Payload Contract | Decodable mapping struct | `private struct RemoteFeedItem: Decodable` |
| Payload Contract JSON keys | Coding keys | `"image"` -> `url` property |
| Flowchart | Test scenarios / control flow | Decision branches = test cases |
| Architecture Diagram | Module structure / SPM targets | `EssentialFeed`, `EssentialFeediOS` |

**Traceability principle**: If you can't point from a requirement artifact to code and back, something is missing.

> The "Maps to in Code" column is illustrative of the handoff target, not a prescription for *how* to implement. The implementation patterns (composition root, `Sendable`/`@MainActor`, SPM target layout, `Task.isCancelled`) belong to the **ios-architecture-expert** skill — this skill stops at the specification and hands off there.

---

## Living Specification

Requirements evolve with code. The specification is never "done" — it is a living document.

> **Contracts sharpen last.** A payload contract can legitimately begin as `GET *url* (TBD)` and stay that way for a long time — in the case study the feed URL was `TBD` for nearly two years before it was finalized to `GET /feed`. The *shape* (status code, keys, optionality, nesting) is agreed early because that is what unblocks parallel work; the concrete endpoint can be filled in once the backend confirms it. Marking a field `TBD` is a valid specification state, not an omission.

### When to update specifications

| Event | What to update |
|---|---|
| New feature added | Add complete feature block |
| Domain term renamed | Update ALL artifacts (see `domain-language.md`) |
| Use case responsibility split | Extract new use case, update existing |
| New error case discovered | Add error course to use case + BDD scenario |
| API contract changed | Update payload contract + model spec if needed |
| Architecture changed | Update architecture diagram |

### Commit discipline

When updating requirements, commit the specification change alongside the code change. This keeps the specification in sync with the code and makes the git history tell the story of how understanding evolved.

---

## Complete Feature Specification Template

Use this template for each new feature:

```markdown
## [Feature Name] Feature Specs

### Story: [Story title — clear, user-focused]

### Narrative #1

```
As a [specific user type]
I want [specific action/feature]
So I can [specific business value]
```

#### Scenarios (Acceptance criteria)

```
Given [specific precondition]
 When [specific user action]
 Then [specific expected outcome]
  And [additional outcomes if applicable]
```

[Add Narrative #2, #3 as needed for different user types or contexts]

---

## Use Cases

### [Use Case Name]

#### Data:
- [Input 1]
- [Input 2]

#### Primary course (happy path):
1. Execute "[Command Name]" command with above data.
2. System [validates/downloads/fetches] [data].
3. System [creates/transforms] [domain objects] from valid data.
4. System delivers [domain objects].

#### Cancel course:
1. System does not deliver [domain objects] nor error.

#### [Error Type] -- error course (sad path):
1. System delivers [specific error].

#### [Another Error Type] -- error course (sad path):
1. System delivers [specific error].

---

## Model Specs

### [Entity Name]

| Property      | Type                |
|---------------|---------------------|
| `[property]`  | `[Type]`            |
| `[property]`  | `[Type]` (optional) |

### Payload contract

```
[HTTP METHOD] /[path]

[status code] RESPONSE

{
    "[key]": [
        {
            "[property]": "[example value]",
            "[optional_property]": "[example value]"
        },
        {
            "[property]": "[example value]"
        }
    ]
}
```

---

## Flowchart

```mermaid
flowchart TD
    Start[User action] --> Fetch[Fetch from remote]
    Fetch --> Success{Success?}
    Success -->|Yes| Cache[Cache data]
    Success -->|No| Fallback[Load from cache]
    Cache --> Display[Display to user]
    Fallback --> HasCache{Has cache?}
    HasCache -->|Yes| Display
    HasCache -->|No| Error[Show error]
```

## Architecture (app-level — update the shared diagram, don't make a new one per feature)

```mermaid
graph TB
    subgraph "Feature Module"
        Model[Domain Model]
        Protocol[Use Case Protocol]
    end
    subgraph "API Module"
        Endpoint[Endpoint]
        Mapper[Mapper]
    end
    subgraph "Cache Module"
        Store[Store Protocol]
        Loader[Local Loader]
    end
    Mapper --> Model
    Loader --> Model
    Endpoint --> Protocol
    Store --> Protocol
```
```

---

## Guardrails

- Do not pad a feature with artifacts it doesn't need — include the ones its behavior warrants (an online-only feature needs no offline narrative, cache use case, or Cancel course; a feature reusing a model needs no new Model Spec)
- Do not draw a separate architecture diagram per feature — there is ONE shared app-level dependency graph; update it as modules are added
- Do not modify existing feature specs unless the understanding of that feature has changed
- Do not break traceability — every requirement must map to testable code
- Do not write specifications that can only be understood with additional context — each feature block must be self-contained

## Verification

- [ ] Feature specification includes the artifacts the feature warrants (full set for a non-trivial networked feature; fewer for online-only / model-reusing features)
- [ ] Feature block is self-contained (can be understood independently)
- [ ] Architecture diagram is the shared app-level graph (not a per-feature one)
- [ ] Each use case has Data, Primary, Error, and Cancel courses where applicable
- [ ] Model Specs use Property/Type tables
- [ ] Payload Contract shows HTTP method, path, status code, and JSON
- [ ] Flowchart includes error branches
- [ ] Architecture diagram shows module dependencies
- [ ] Domain terminology is consistent across all artifacts
- [ ] Traceability: every artifact maps to implementation
