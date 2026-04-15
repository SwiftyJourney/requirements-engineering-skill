# BDD Narratives & Acceptance Criteria

Use this when:
- Writing BDD stories from vague requirements
- Creating acceptance criteria for a feature
- Reviewing existing BDD specs for completeness
- Splitting a single narrative into multiple user-type-specific narratives

Skip this file if:
- You need use case procedural steps. Use `use-cases.md`.
- You need model specs or payload contracts. Use `model-specs-and-contracts.md`.

Jump to:
- [User Story Template](#user-story-template)
- [Narrative Patterns](#common-narrative-patterns)
- [Scenario Patterns](#scenario-patterns)
- [Cache-Specific Criteria](#cache-specific-acceptance-criteria)
- [Single vs Multiple Narratives](#single-vs-multiple-narratives)
- [Complete Examples](#complete-examples)
- [Anti-Patterns](#anti-patterns)

---

## User Story Template

```
Story: [Clear, user-focused title describing the goal]

Narrative #[N]
As a [type of user/customer]
I want [specific feature/functionality]
So I can/that [business value/benefit]

Scenarios (Acceptance Criteria)
Given [initial context/preconditions]
And [additional preconditions if needed]
When [user action/trigger]
Then [expected outcome]
And [additional expected outcomes]
```

---

## Common Narrative Patterns

### Online/Connected Users
```
As an online customer
I want the app to automatically [action]
So I can [benefit]
```

### Offline/Disconnected Users
```
As an offline customer
I want the app to [fallback behavior]
So I can [benefit despite lack of connectivity]
```

### Power Users/Advanced Features
```
As an experienced user
I want to [advanced capability]
So I can [efficiency/productivity gain]
```

### New Users/Onboarding
```
As a new user
I want [guided experience]
So I can [learn/get started quickly]
```

---

## Scenario Patterns

### Happy Path (Primary Course)
```
Given the customer has connectivity
And [any other prerequisites]
When the customer requests to [action]
Then the app should [expected behavior]
And [secondary outcomes like caching, updates]
```

### Error Handling (Sad Path)
```
Given the customer doesn't have connectivity
And [specific error condition]
When the customer requests to [action]
Then the app should display [error message/fallback behavior]
```

### Edge Cases
```
Given [unusual but valid condition]
When [action]
Then [graceful handling]
```

### Data Validation
```
Given [data in specific state]
When the system validates [data]
Then the system should [accept/reject with reason]
```

---

## Cache-Specific Acceptance Criteria

When a feature involves caching, acceptance criteria must specify time-based validation rules explicitly:

```
Given the customer doesn't have connectivity
  And there's a cached version of the feed
  And the cache is less than seven days old
 When the customer requests to see the feed
 Then the app should display the latest feed saved

Given the customer doesn't have connectivity
  And there's a cached version of the feed
  And the cache is seven days old or more
 When the customer requests to see the feed
 Then the app should display an error message

Given the customer doesn't have connectivity
  And the cache is empty
 When the customer requests to see the feed
 Then the app should display an error message
```

**Key details**:
- Cache age threshold is explicit ("seven days"), not vague ("recent")
- Three scenarios cover all cache states: valid cache, expired cache, empty cache
- Each scenario results in a distinct behavior

---

## Single vs Multiple Narratives

### Multiple narratives — when different user types have different needs

**Example: Feed Feature** (2 narratives)

Online customers need fresh data from the server. Offline customers need cached data. These are distinct needs requiring separate narratives:

```
Narrative #1
As an online customer
I want the app to automatically load my latest image feed
So I can always enjoy the newest images of my friends

Narrative #2
As an offline customer
I want the app to show the latest saved version of my image feed
So I can always enjoy images of my friends
```

### Single narrative — when only one user type matters

**Example: Image Comments Feature** (1 narrative)

Comments only make sense with connectivity (no offline cache needed). A single narrative suffices:

```
Narrative
As an online customer
I want the app to load image comments
So I can see how people are engaging with images in my feed
```

**Decision rule**: If the same feature behaves differently for different user types or contexts, write multiple narratives. If the feature has a single mode of operation, one narrative is enough.

---

## Complete Examples

### Example 1: Image Feed Feature (from Essential Developer)

**Story: Customer requests to see their image feed**

**Narrative #1**
```
As an online customer
I want the app to automatically load my latest image feed
So I can always enjoy the newest images of my friends
```

**Scenarios (Acceptance criteria)**
```
Given the customer has connectivity
 When the customer requests to see their feed
 Then the app should display the latest feed from remote
  And replace the cache with the new feed
```

**Narrative #2**
```
As an offline customer
I want the app to show the latest saved version of my image feed
So I can always enjoy images of my friends
```

**Scenarios (Acceptance criteria)**
```
Given the customer doesn't have connectivity
  And there's a cached version of the feed
  And the cache is less than seven days old
 When the customer requests to see the feed
 Then the app should display the latest feed saved

Given the customer doesn't have connectivity
  And there's a cached version of the feed
  And the cache is seven days old or more
 When the customer requests to see the feed
 Then the app should display an error message

Given the customer doesn't have connectivity
  And the cache is empty
 When the customer requests to see the feed
 Then the app should display an error message
```

### Example 2: Image Comments Feature (from Essential Developer)

**Story: Customer requests to see image comments**

**Narrative**
```
As an online customer
I want the app to load image comments
So I can see how people are engaging with images in my feed
```

**Scenarios (Acceptance criteria)**
```
Given the customer has connectivity
 When the customer requests to see comments on an image
 Then the app should display all comments for that image

Given the customer doesn't have connectivity
 When the customer requests to see comments on an image
 Then the app should display an error message
```

---

## Anti-Patterns

### Vague user type
```
INCORRECT:
As a user
I want the app to load the feed
So I can see the feed

CORRECT:
As an online customer
I want the app to automatically load my latest image feed
So I can always enjoy the newest images of my friends
```

### Implementation details in narratives
```
INCORRECT:
As a developer
I want to implement a REST API endpoint
So I can fetch data from the database

CORRECT:
As a customer
I want to see real-time product availability
So I can make informed purchasing decisions
```

### Missing acceptance criteria
```
INCORRECT:
Story: User login
As a user I want to login

CORRECT:
Story: Secure user authentication

Given a registered user with valid credentials
When they enter their username and password
Then they should be logged in successfully
And redirected to their dashboard

Given a user enters invalid credentials
When they attempt to login
Then they should see an error message
And remain on the login screen
```

### Vague conditions
```
INCORRECT:
Given the cache is recent
When the user opens the app
Then show cached data

CORRECT:
Given the cache is less than seven days old
When the customer requests to see the feed
Then the app should display the latest feed saved
```

---

## Guardrails

- Do not write "As a user" — always specify a concrete user type
- Do not omit offline/error scenarios — think through what can go wrong
- Do not use vague time references ("recent", "old") — use specific thresholds
- Do not combine multiple user types into one narrative — separate them
- Do not include implementation details — keep narratives behavioral

## Verification

- [ ] Every narrative specifies a concrete user type
- [ ] Every scenario has Given/When/Then with specific preconditions
- [ ] Offline scenarios cover: valid cache, expired cache, empty cache
- [ ] No vague terms ("recent", "old", "good") — all thresholds are explicit
- [ ] Story title is user-focused, not implementation-focused
