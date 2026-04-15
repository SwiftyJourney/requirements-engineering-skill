# Diagrams

Use this when:
- Creating flowcharts for feature workflows
- Drawing architecture or module dependency diagrams
- Generating sequence diagrams for component interactions
- Visualizing state machines

Skip this file if:
- You need BDD narratives. Use `bdd-narratives.md`.
- You need use case definitions. Use `use-cases.md`.

Jump to:
- [Diagram Selection](#diagram-selection)
- [Flowcharts](#1-flowcharts-behavioral-flow)
- [Architecture Diagrams](#2-architecture-diagrams-module-dependencies)
- [Sequence Diagrams](#3-sequence-diagrams-interaction-flow)
- [State Diagrams](#4-state-diagrams)
- [Drawing Conventions](#drawing-conventions)
- [Integration with Requirements](#integration-with-requirements)

---

## Diagram Selection

| Need | Diagram type | When to use |
|---|---|---|
| Show decisions and actions in sequence | Flowchart | Feature workflow with branching logic |
| Show module structure and dependencies | Architecture diagram | System overview, dependency graph |
| Show component interactions over time | Sequence diagram | Request/response flows between components |
| Show states and transitions | State diagram | Feature lifecycle, UI state machine |

---

## 1. Flowcharts (Behavioral Flow)

Show the sequence of decisions and actions in a feature workflow. **Must include error/fallback branches** — not just the happy path.

```mermaid
flowchart TD
    Start[Show feed screen] --> Fetch[Fetch new items]
    Fetch --> Success{Success?}
    Success -->|Yes| Cache[Cache new items]
    Success -->|No| LoadCache[Load items from cache]
    Cache --> Update[Update feed screen]
    LoadCache --> HasCache{Has Cache?}
    HasCache -->|Yes| Update
    HasCache -->|No| Error[Show error message]
    Update --> End[End]
    Error --> End
```

**Rules**:
- Every decision diamond must have at least two branches (success/failure)
- Error paths must terminate in a user-visible outcome (error message, fallback display)
- Each BDD scenario maps to a path through the flowchart

---

## 2. Architecture Diagrams (Module Dependencies)

Show the **actual module structure and dependency graph** — not generic boxes.

### Module Dependency Diagram

```mermaid
graph TB
    subgraph "Feature Module"
        FeedImage[Feed Image Model]
        FeedCache[FeedCache Protocol]
        FeedImageDataLoader[FeedImageDataLoader Protocol]
    end

    subgraph "API Module"
        FeedEndpoint[FeedEndpoint]
        FeedItemsMapper[FeedItemsMapper]
        HTTPClient[HTTPClient Protocol]
    end

    subgraph "Cache Module"
        FeedStore[FeedStore Protocol]
        LocalFeedLoader[LocalFeedLoader]
        FeedCachePolicy[FeedCachePolicy]
    end

    subgraph "UI Module"
        FeedViewController[FeedViewController]
        FeedImageCell[FeedImageCell]
    end

    subgraph "Composition Root"
        FeedService[FeedService]
        FeedUIComposer[FeedUIComposer]
    end

    FeedItemsMapper --> FeedImage
    LocalFeedLoader --> FeedImage
    FeedViewController --> FeedImage
    FeedService --> HTTPClient
    FeedService --> FeedStore
    FeedUIComposer --> FeedService
```

**Rules**:
- Group components into modules using subgraphs
- Show actual protocol/class names, not generic labels
- Dependencies flow inward: UI -> Feature, Cache -> Feature, API -> Feature
- Composition Root imports everything, Feature module depends on nothing

### Component Relationships (simpler overview)

```mermaid
graph TB
    subgraph "Presentation Layer"
        UI[UIViewController]
        Controller[FeedViewController]
    end

    subgraph "Business Logic"
        Loader[FeedLoader Protocol]
        Remote[RemoteFeedLoader]
        Local[LocalFeedLoader]
    end

    subgraph "Data Layer"
        API[HTTPClient]
        Store[FeedStore]
    end

    UI --> Controller
    Controller --> Loader
    Loader <|.. Remote
    Loader <|.. Local
    Remote --> API
    Local --> Store
```

---

## 3. Sequence Diagrams (Interaction Flow)

Show the interaction between components over time. **Must include alt/else blocks** for error handling.

```mermaid
sequenceDiagram
    participant User
    participant Controller
    participant RemoteLoader
    participant Cache

    User->>Controller: Request Feed
    Controller->>RemoteLoader: Load Feed
    alt Success
        RemoteLoader->>Controller: Feed Items
        Controller->>Cache: Save Items
        Controller->>User: Display Feed
    else Failure
        RemoteLoader->>Controller: Error
        Controller->>Cache: Load Cached Feed
        Cache->>Controller: Cached Items
        Controller->>User: Display Cached Feed
    end
```

---

## 4. State Diagrams

Show the different states a feature can be in and transitions between them.

```mermaid
stateDiagram-v2
    [*] --> Loading
    Loading --> Success: Data Retrieved
    Loading --> Error: Network Failure
    Success --> [*]
    Error --> LoadingCache: Fallback
    LoadingCache --> DisplayCache: Cache Available
    LoadingCache --> DisplayError: No Cache
    DisplayCache --> [*]
    DisplayError --> [*]
```

---

## Drawing Conventions

### Shape Conventions
- **Rectangles**: Components, modules, classes
- **Rounded rectangles**: Processes, actions
- **Diamonds**: Decision points, conditionals
- **Parallelograms**: Data, inputs/outputs
- **Circles**: Start/end states

### Arrow Styles
- **Solid arrows** (`-->`): Direct dependencies, data flow
- **Dashed arrows** (`-.->` or `-.->`): Creation, composition
- **Dotted arrows** (`<|..`): Protocol conformance, interfaces

### Color Coding (optional)
- **Green**: Happy path, success states
- **Red**: Error states, error handlers
- **Blue**: Data sources, external systems
- **Orange/Yellow**: Alternative paths, caching layers

---

## Integration with Requirements

Diagrams must directly support the written requirements:

| Requirement Artifact | Diagram Type | Mapping |
|---|---|---|
| BDD Scenarios | Flowchart | Each scenario = one path through the flowchart |
| Use Case steps | Sequence diagram | Each step = one interaction between participants |
| Architecture modules | Architecture diagram | Each module = one subgraph |
| User narratives | Sequence diagram | User types define the starting participants |
| Feature states | State diagram | Each UI/feature state = one node |

---

## Guardrails

- Do not create flowcharts with only the happy path — always include error/fallback branches
- Do not use generic labels ("Component A", "Module B") — use actual domain/class names
- Do not make diagrams that require explanation — they should be scannable in 30 seconds
- Do not mix flow directions within one diagram — choose top-to-bottom or left-to-right consistently
- Do not create diagrams that contradict the written requirements

## Verification

- [ ] Flowcharts include error/fallback branches for every decision
- [ ] Architecture diagrams use actual module/component names
- [ ] Sequence diagrams include alt/else blocks for error handling
- [ ] All diagram names match terms in BDD stories and use cases
- [ ] Dependencies flow in the correct direction (inward toward domain)
- [ ] Diagrams are scannable in 30 seconds
