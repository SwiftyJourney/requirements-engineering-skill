# Model Specs & Payload Contracts

Use this when:
- Defining domain model properties and types
- Specifying API payload contracts (request/response JSON)
- Documenting optional fields and nested objects
- Establishing the data contract between frontend and backend

Skip this file if:
- You need BDD narratives or acceptance criteria. Use `bdd-narratives.md`.
- You need use case procedural steps. Use `use-cases.md`.

Jump to:
- [Model Spec Template](#model-spec-template)
- [Type Conventions](#type-conventions)
- [Payload Contract Template](#payload-contract-template)
- [Optional Fields](#optional-fields)
- [Nested Objects](#nested-objects)
- [Complete Examples](#complete-examples)

---

## Model Spec Template

Model Specs define the **requirements contract** for domain entities. They specify what the system must store, transfer, and display.

```
### [Entity Name]

| Property      | Type                |
|---------------|---------------------|
| `id`          | `UUID`              |
| `name`        | `String`            |
| `description` | `String` (optional) |
| `url`         | `URL`               |
| `createdAt`   | `Date` (ISO8601)    |
```

**Rules**:
- Every domain entity gets its own table
- Optional fields are explicitly marked as `(optional)`
- Use domain-specific types (`UUID`, `URL`, `Date`) not implementation types (`String` for everything)
- Nested objects get their own table with a cross-reference

```
INCORRECT: Describing model as prose
"The feed item has an id, maybe a description, maybe a location, and a URL for the image"

CORRECT: Property/Type table
| Property      | Type                |
|---------------|---------------------|
| `id`          | `UUID`              |
| `description` | `String` (optional) |
| `location`    | `String` (optional) |
| `url`         | `URL`               |
```

---

## Type Conventions

| Type | Meaning | Example |
|---|---|---|
| `UUID` | Universally unique identifier | `"a5b4c3d2-e1f0-..."` |
| `String` | Required text | `"A description"` |
| `String` (optional) | Text that may be absent | Field omitted from some JSON items |
| `URL` | Web address | `"https://example.com/image.png"` |
| `Date` (ISO8601 String) | Timestamp as ISO8601 string | `"2020-05-20T11:24:59+0000"` |
| `Int` | Whole number | `42` |
| `Bool` | True/False | `true` |
| `[Entity]` | Array of related entities | Array of child objects |
| `EntityObject` | Nested object — see its own table | `{ "username": "..." }` |

---

## Payload Contract Template

Payload Contracts define the **exact HTTP interface** between client and server.

```
### Payload contract

GET /[resource]

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

**Rules**:
- Show HTTP method and path
- Show the expected status code (`200 RESPONSE` for exact, `2xx RESPONSE` for any success)
- Include example JSON with realistic values
- Demonstrate optional fields by **omission** — show some items with the field, some without
- Nested objects must match their Model Spec table

---

## Optional Fields

Optional fields are demonstrated by **omission** in the JSON payload — some items include the field, others do not:

```
GET /feed

200 RESPONSE

{
    "items": [
        {
            "id": "a UUID",
            "description": "a description",
            "location": "a location",
            "image": "https://a-image.url"
        },
        {
            "id": "another UUID",
            "description": "another description",
            "image": "https://another-image.url"
        },
        {
            "id": "even another UUID",
            "location": "even another location",
            "image": "https://even-another-image.url"
        },
        {
            "id": "yet another UUID",
            "image": "https://yet-another-image.url"
        }
    ]
}
```

Notice how `description` and `location` are present in some items and absent in others. This communicates optionality more clearly than any prose description.

---

## Nested Objects

When a model contains nested objects, define both the parent and child as separate Model Spec tables:

```
### Image Comment

| Property      | Type                    |
|---------------|-------------------------|
| `id`          | `UUID`                  |
| `message`     | `String`                |
| `created_at`  | `Date` (ISO8601 String) |
| `author`      | `CommentAuthorObject`   |

### Image Comment Author

| Property      | Type                |
|---------------|---------------------|
| `username`    | `String`            |
```

The payload contract mirrors this nesting:

```
GET /image/{image-id}/comments

2xx RESPONSE

{
    "items": [
        {
            "id": "a UUID",
            "message": "a message",
            "created_at": "2020-05-20T11:24:59+0000",
            "author": {
                "username": "a username"
            }
        }
    ]
}
```

---

## Status Code Conventions

| Convention | Meaning | When to use |
|---|---|---|
| `200 RESPONSE` | Exact status code required | When the API always returns 200 on success |
| `2xx RESPONSE` | Any success status acceptable | When the API may return 200, 201, 204, etc. |
| `404 RESPONSE` | Resource not found | Document in Error courses of use cases |

---

## Complete Examples

### Example 1: Feed Image

**Model Spec:**

| Property      | Type                |
|---------------|---------------------|
| `id`          | `UUID`              |
| `description` | `String` (optional) |
| `location`    | `String` (optional) |
| `url`         | `URL`               |

**Payload Contract:**

```
GET /feed

200 RESPONSE

{
    "items": [
        {
            "id": "a UUID",
            "description": "a description",
            "location": "a location",
            "image": "https://a-image.url"
        },
        {
            "id": "another UUID",
            "description": "another description",
            "image": "https://another-image.url"
        },
        {
            "id": "even another UUID",
            "location": "even another location",
            "image": "https://even-another-image.url"
        },
        {
            "id": "yet another UUID",
            "image": "https://yet-another-image.url"
        }
    ]
}
```

### Example 2: Image Comment (with nested object)

**Model Spec:**

| Property      | Type                    |
|---------------|-------------------------|
| `id`          | `UUID`                  |
| `message`     | `String`                |
| `created_at`  | `Date` (ISO8601 String) |
| `author`      | `CommentAuthorObject`   |

| Property      | Type                |
|---------------|---------------------|
| `username`    | `String`            |

**Payload Contract:**

```
GET /image/{image-id}/comments

2xx RESPONSE

{
    "items": [
        {
            "id": "a UUID",
            "message": "a message",
            "created_at": "2020-05-20T11:24:59+0000",
            "author": {
                "username": "a username"
            }
        },
        {
            "id": "another UUID",
            "message": "another message",
            "created_at": "2020-05-19T14:23:53+0000",
            "author": {
                "username": "another username"
            }
        }
    ]
}
```

---

## Guardrails

- Do not describe models in prose — always use Property/Type tables
- Do not omit optional field markers — every optional must be `(optional)` in the table
- Do not show payload contracts without an HTTP method and path
- Do not hide optional fields — demonstrate them by omission in JSON examples
- Do not mix JSON property names with model property names when they differ (e.g., JSON `"image"` maps to model `url`)

## Verification

- [ ] Every domain entity has a Property/Type table
- [ ] Optional fields are marked `(optional)` in the table AND demonstrated by omission in JSON
- [ ] Nested objects have their own table with a cross-reference
- [ ] Payload contracts show HTTP method, path, and status code
- [ ] JSON examples use realistic, descriptive placeholder values
- [ ] Property names in model tables are consistent with domain language
