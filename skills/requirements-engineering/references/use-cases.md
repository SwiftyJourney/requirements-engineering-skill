# Use Cases

Use this when:
- Creating procedural use cases from BDD scenarios
- Deciding how to separate use case responsibilities
- Adding cancel courses for cancellable operations
- Writing data fetching, caching, persistence, or CRUD use cases

Skip this file if:
- You need BDD narrative templates. Use `bdd-narratives.md`.
- You need data model definitions. Use `model-specs-and-contracts.md`.

Jump to:
- [Use Case Template](#use-case-template)
- [Course Types](#course-types)
- [Separation of Concerns](#separation-of-concerns)
- [Common Patterns](#common-use-case-patterns)
- [Complete Examples](#complete-examples)

---

## Use Case Template

```
### [Use Case Name]

#### Data:
- [Input 1]
- [Input 2]

#### Primary course (happy path):
1. Execute "[Command Name]" command with above data.
2. System [downloads/fetches/validates] data.
3. System [creates/transforms] [domain objects] from valid data.
4. System delivers [domain objects].

#### Cancel course:
1. System does not deliver [domain objects] nor error.

#### [Error Type] -- error course (sad path):
1. System delivers [specific error].
```

**Rules**:
- **Data section** lists ALL inputs — never omit parameters
- **Primary course** uses numbered steps with active voice ("System validates", not "Data is validated")
- **Cancel course** is required for any operation involving network or async work
- **Error courses** cover every way the operation can fail
- Steps are atomic — one action per step

---

## Course Types

| Course | When to include | Pattern |
|---|---|---|
| **Primary course** | Always | Numbered steps ending in "System delivers [output]" |
| **Cancel course** | Network/async operations | "System does not deliver [output] nor error" |
| **Error course** | Every failure mode | "System delivers [specific error]" |
| **Alternative course** | Valid alternative flow | Numbered steps with different outcome |

### Cancel course

The Cancel course is a **first-class requirement**, not an afterthought. Any operation the user can interrupt (navigating away, scrolling past, closing a screen) needs a Cancel course:

```
#### Cancel course:
1. System does not deliver image data nor error.
```

**Key principle**: On cancellation, the system delivers **nothing** — no data, no error. This prevents stale results from reaching the UI after the user has moved on.

---

## Separation of Concerns

Use cases should have a **single responsibility**. When a use case mixes multiple concerns, split it.

> **Command/Query Separation (CQS)** is the principle behind the most common split. A **query** returns data and has **no side effects** (Load). A **command** causes a side effect and returns nothing meaningful (Validate, which *deletes* the cache). The moment you catch a query mutating state — a Load step that deletes — that is the signal to extract the mutation into a separate command use case.

### Decision table

| Signal | Action |
|---|---|
| Use case has two distinct responsibilities (load + validate) | Split into two use cases |
| Data section mixes unrelated inputs | Split by input group |
| Error courses from one responsibility don't apply to the other | Split |
| Use case name has "and" in it | Likely should be split |
| One use case is used independently in multiple features | Extract as shared use case |

### Example: Extracting Validate Cache

**Before (mixed responsibilities):**
```
### Load Feed From Cache Use Case

#### Primary course:
1. Execute "Load Image Feed" command.
2. System retrieves feed data from cache.
3. System validates cache is less than seven days old.  <-- validation concern
4. System creates image feed from cached data.
5. System delivers image feed.
```

**After (separated):**

```
### Load Feed From Cache Use Case

#### Primary course:
1. Execute "Load Image Feed" command.
2. System retrieves feed data from cache.
3. System validates cache is less than seven days old.
4. System creates image feed from cached data.
5. System delivers image feed.

### Validate Feed Cache Use Case (extracted)

#### Primary course:
1. Execute "Validate Cache" command.
2. System retrieves feed data from cache.
3. System validates cache is less than seven days old.

#### Retrieval error course (sad path):
1. System deletes cache.

#### Expired cache course (sad path):
1. System deletes cache.
```

**Why separate**: Load is a side-effect-free **query**; deleting the cache is a **command**. They also have different triggers — loading happens on user request, validation runs in the background (e.g., when the app resigns active) — so they are different use cases (CQS).

> **How this actually evolved (a useful cautionary tale):** in the case study the deletion side-effect was first *added to* `Load Feed From Cache`'s retrieval-error course — the Load query started deleting. One revision later the team pulled it back out into a dedicated `Validate Feed Cache` use case, recognizing that delete-on-failure is a *command* that doesn't belong on the *read* path. Lesson: a query that mutates state is the smell; that is exactly when you extract.

---

## Common Use Case Patterns

### Data Fetching / Loading
```
Load [Resource] From Remote Use Case

Data:
- URL

Primary course (happy path):
1. Execute "Load [Resource]" command with above data.
2. System downloads data from the URL.
3. System validates downloaded data.
4. System creates [resource] from valid data.
5. System delivers [resource].

Cancel course:
1. System does not deliver [resource] nor error.

Invalid data -- error course (sad path):
1. System delivers invalid data error.

No connectivity -- error course (sad path):
1. System delivers connectivity error.
```

### Cache Loading
```
Load [Resource] From Cache Use Case

Primary course:
1. Execute "Load [Resource]" command.
2. System retrieves [resource] data from cache.
3. System validates cache is less than [max age].
4. System creates [resource] from cached data.
5. System delivers [resource].

Retrieval error course (sad path):
1. System delivers error.

Expired cache course (sad path):
1. System delivers no [resource].

Empty cache course (sad path):
1. System delivers no [resource].
```

> **Collection vs single keyed resource.** For a *collection* load (the feed), an empty or expired cache is an **empty success** — "System delivers no feed images", no error. For a *single keyed resource* (e.g. image data for one URL), an empty/missing cache is a **not-found error** — "System delivers not-found error", not an empty result. Same surface symptom ("nothing in the cache"), deliberately different modeling.

### Data Persistence / Caching
```
Cache [Resource] Use Case

Data:
- [Resource]

Primary course (happy path):
1. Execute "Save [Resource]" command with above data.
2. System deletes old cache data.
3. System encodes [resource].
4. System timestamps the new cache.
5. System saves new cache data.
6. System delivers success message.

Deleting error course (sad path):
1. System delivers error.

Saving error course (sad path):
1. System delivers error.
```

### Cache Validation
```
Validate [Resource] Cache Use Case

Primary course:
1. Execute "Validate Cache" command.
2. System retrieves [resource] data from cache.
3. System validates cache is less than [max age].

Retrieval error course (sad path):
1. System deletes cache.

Expired cache course (sad path):
1. System deletes cache.
```

### CRUD — Create
```
Create [Entity] Use Case

Data:
- [Entity properties]

Primary course:
1. Execute "Create [Entity]" command with data.
2. System validates required fields.
3. System checks for duplicates (if applicable).
4. System generates unique identifier.
5. System persists [entity].
6. System delivers created [entity] with ID.

Validation failed -- error course:
1. System delivers validation errors.

Duplicate detected -- error course:
1. System delivers conflict error.
```

### CRUD — Read / Update / Delete

Follow the same pattern: Data section -> Primary course -> Error courses. Read is a query (no side effects); Update and Delete are commands (each needs its own not-found / conflict error courses).

---

## Complete Examples

### Load Feed From Remote Use Case

#### Data:
- URL

#### Primary course (happy path):
1. Execute "Load Image Feed" command with above data.
2. System downloads data from the URL.
3. System validates downloaded data.
4. System creates image feed from valid data.
5. System delivers image feed.

#### Invalid data -- error course (sad path):
1. System delivers invalid data error.

#### No connectivity -- error course (sad path):
1. System delivers connectivity error.

---

### Load Feed Image Data From Remote Use Case

#### Data:
- URL

#### Primary course (happy path):
1. Execute "Load Image Data" command with above data.
2. System downloads data from the URL.
3. System validates downloaded data.
4. System delivers image data.

#### Cancel course:
1. System does not deliver image data nor error.

#### Invalid data -- error course (sad path):
1. System delivers invalid data error.

#### No connectivity -- error course (sad path):
1. System delivers connectivity error.

---

### Load Feed From Cache Use Case

#### Primary course:
1. Execute "Load Image Feed" command.
2. System retrieves feed data from cache.
3. System validates cache is less than seven days old.
4. System creates image feed from cached data.
5. System delivers image feed.

#### Retrieval error course (sad path):
1. System delivers error.

#### Expired cache course (sad path):
1. System delivers no feed images.

#### Empty cache course (sad path):
1. System delivers no feed images.

---

### Validate Feed Cache Use Case

#### Primary course:
1. Execute "Validate Cache" command.
2. System retrieves feed data from cache.
3. System validates cache is less than seven days old.

#### Retrieval error course (sad path):
1. System deletes cache.

#### Expired cache course (sad path):
1. System deletes cache.

---

### Cache Feed Use Case

#### Data:
- Image Feed

#### Primary course (happy path):
1. Execute "Save Image Feed" command with above data.
2. System deletes old cache data.
3. System encodes image feed.
4. System timestamps the new cache.
5. System saves new cache data.
6. System delivers success message.

#### Deleting error course (sad path):
1. System delivers error.

#### Saving error course (sad path):
1. System delivers error.

---

## Guardrails

- Do not omit the Data section — even if there are no inputs, state "None"
- Do not skip the Cancel course for network/async operations
- Do not combine "Load" and "Validate" into one use case — separate concerns
- Do not write "System does X and Y" — split into separate steps
- Do not use passive voice — "System validates", not "Data is validated"

## Verification

- [ ] Every use case has a Data section
- [ ] Every network/async use case has a Cancel course
- [ ] Every use case has at least one Error course
- [ ] Steps are atomic (one action per step)
- [ ] Active voice throughout ("System validates", "System delivers")
- [ ] No mixed responsibilities — each use case has a single purpose
- [ ] Domain language matches BDD narratives and model specs
