# Use Case Templates and Patterns

## Use Case Template

```
[Use Case Name]

Data (Input):
- [Input parameter 1]
- [Input parameter 2]

Primary course (happy path):
1. [First step]
2. [Second step]
3. [Third step]
4. System delivers [success output]

[Error Type] – error course (sad path):
1. System delivers [error output]

[Alternative Scenario] – alternative course:
1. [Alternative flow steps]
2. System delivers [alternative output]
```

## Common Use Case Patterns

### Data Fetching/Loading Pattern
```
Load [Resource] Use Case

Data (Input):
- URL/Identifier
- [Optional: Filters, limits, etc.]

Primary course (happy path):
1. Execute "Load [Resource]" command with above data
2. System downloads/fetches data from [source]
3. System validates downloaded data
4. System creates [resource objects] from valid data
5. System delivers [resource objects]

Invalid data – error course (sad path):
1. System delivers invalid data error

No connectivity – error course (sad path):
1. System delivers connectivity error

[Additional error cases as needed]
```

### Caching/Fallback Pattern
```
Load [Resource] Fallback (Cache) Use Case

Data (Input):
- Max age (optional)
- [Other cache parameters]

Primary course (happy path):
1. Execute "Retrieve [Resource]" command with above data
2. System fetches [resource] data from cache
3. System validates cache freshness (if max age provided)
4. System creates [resource objects] from cached data
5. System delivers [resource objects]

No cache – error course (sad path):
1. System delivers no [resource] found

Stale cache – alternative course:
1. System delivers stale cache warning
2. System delivers cached [resource objects]

Expired cache – error course:
1. System delivers cache expired error
```

### Data Persistence Pattern
```
Save [Resource] Use Case

Data (Input):
- [Resource objects/data]
- [Optional: Storage location, metadata]

Primary course (happy path):
1. Execute "Save [Resource]" command with above data
2. System validates [resource] data
3. System encodes [resource] for storage
4. System timestamps the new cache/storage
5. System replaces/updates existing data
6. System delivers success message

Invalid data – error course (sad path):
1. System delivers validation error

Storage full – error course (sad path):
1. System delivers storage error

Storage unavailable – error course (sad path):
1. System delivers unavailable error
```

### CRUD Operations Pattern

#### Create
```
Create [Entity] Use Case

Data (Input):
- [Entity properties]

Primary course:
1. Execute "Create [Entity]" command with data
2. System validates required fields
3. System checks for duplicates (if applicable)
4. System generates unique identifier
5. System persists [entity]
6. System delivers created [entity] with ID

Validation failed – error course:
1. System delivers validation errors

Duplicate detected – error course:
1. System delivers conflict error
```

#### Read
```
Get [Entity] Use Case

Data (Input):
- Entity ID/Identifier

Primary course:
1. Execute "Get [Entity]" command with ID
2. System fetches [entity] from storage
3. System delivers [entity] data

Not found – error course:
1. System delivers not found error
```

#### Update
```
Update [Entity] Use Case

Data (Input):
- Entity ID
- Updated properties

Primary course:
1. Execute "Update [Entity]" command with data
2. System validates entity exists
3. System validates updated properties
4. System applies updates to [entity]
5. System persists changes
6. System delivers updated [entity]

Not found – error course:
1. System delivers not found error

Validation failed – error course:
1. System delivers validation errors
```

#### Delete
```
Delete [Entity] Use Case

Data (Input):
- Entity ID

Primary course:
1. Execute "Delete [Entity]" command with ID
2. System validates entity exists
3. System removes [entity] from storage
4. System delivers success confirmation

Not found – error course:
1. System delivers not found error

Cannot delete (dependencies) – error course:
1. System delivers dependency conflict error
```

## Complete Example: Feed Feature Use Cases

### Load Feed Use Case
```
Data (Input):
- URL

Primary course (happy path):
1. Execute "Load Feed Items" command with above data
2. System downloads data from the URL
3. System validates downloaded data
4. System creates feed items from valid data
5. System delivers feed items

Invalid data – error course (sad path):
1. System delivers invalid data error

No connectivity – error course (sad path):
1. System delivers connectivity error
```

### Load Feed Fallback (Cache) Use Case
```
Data (Input):
- Max age

Primary course (happy path):
1. Execute "Retrieve Feed Items" command with above data
2. System fetches feed data from cache
3. System validates cache is within max age
4. System creates feed items from cached data
5. System delivers feed items

No cache – error course (sad path):
1. System delivers no feed items error

Expired cache – error course (sad path):
1. System delivers cache expired error
```

### Save Feed Items Use Case
```
Data (Input):
- Feed items

Primary course (happy path):
1. Execute "Save Feed Items" command with above data
2. System encodes feed items
3. System timestamps the new cache
4. System replaces the cache with new data
5. System delivers success message

Encoding failed – error course:
1. System delivers encoding error

Storage unavailable – error course:
1. System delivers storage error
```

## Tips for Writing Effective Use Cases

1. **Keep steps atomic**: Each step should represent a single, clear action
2. **Use active voice**: "System validates" not "Data is validated"
3. **Be specific about inputs**: List all required and optional parameters
4. **Cover all error cases**: Think through what can go wrong at each step
5. **Separate concerns**: One use case per major operation
6. **Name clearly**: Use case names should immediately convey their purpose
7. **Focus on behavior**: Describe what the system does, not how it does it
8. **Think user-first**: Even technical use cases should deliver value
