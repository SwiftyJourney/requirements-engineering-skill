# BDD Templates and Patterns

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

## Complete Example: Feed Feature

### Story: Customer requests to see their image feed

**Narrative #1**
As an online customer
I want the app to automatically load my latest image feed
So I can always enjoy the newest images of my friends

**Scenarios (Acceptance criteria)**
```
Given the customer has connectivity
When the customer requests to see the feed
Then the app should display the latest feed from remote
And replace the cache with the new feed
```

**Narrative #2**
As an offline customer
I want the app to show the latest saved version of my image feed
So I can always enjoy images of my friends

**Scenarios (Acceptance criteria)**
```
Given the customer doesn't have connectivity
And there's a cached version of the feed
When the customer requests to see the feed
Then the app should display the latest feed saved
```

```
Given the customer doesn't have connectivity
And the cache is empty
When the customer requests to see the feed
Then the app should display an error message
```

## Anti-Patterns to Avoid

### Vague Requirements
❌ BAD:
```
Story: As a user
I want the app to load the feed
So I can see the feed
```

✅ GOOD:
```
Story: Customer requests to see their image feed
As an online customer
I want the app to automatically load my latest image feed
So I can always enjoy the newest images of my friends
```

### Technical Implementation Details in Stories
❌ BAD:
```
As a developer
I want to implement a REST API endpoint
So I can fetch data from the database
```

✅ GOOD:
```
As a customer
I want to see real-time product availability
So I can make informed purchasing decisions
```

### Missing Acceptance Criteria
❌ BAD:
```
Story: User login
As a user I want to login
```

✅ GOOD:
```
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
