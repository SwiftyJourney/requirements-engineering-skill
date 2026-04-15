# Requirements Engineering Skill

A Claude Code skill that transforms vague or incomplete requirements into well-defined, testable specifications using BDD, Use Cases, Model Specs, Payload Contracts, flowcharts, and architecture diagrams. Based on the [Essential Developer](https://www.essentialdeveloper.com) methodology.

## Who is this for?

Anyone who encounters vague requirements and needs to transform them into implementable specifications:

- Product Managers defining feature requirements
- Software Teams bridging business and technical needs
- Developers needing clear specs before writing code
- Technical Writers structuring project documentation

## Installation

Install via [skills.sh](https://skills.sh):

```bash
npx skills add SwiftyJourney/requirements-engineering-skill
```

## Compatible Agents

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- [Cursor](https://cursor.sh)
- [GitHub Copilot](https://github.com/features/copilot)
- [Windsurf](https://codeium.com/windsurf)
- Any agent supporting the `skills/` convention

## What the Skill Covers

### The 7 Feature Specification Artifacts

Every feature specification includes these artifacts:

1. **BDD Narrative** — Define who, what, why per user type
2. **Acceptance Criteria** — Given/When/Then scenarios
3. **Use Cases** — Step-by-step system behavior (Data/Primary/Error/Cancel)
4. **Model Specs** — Property/Type tables for domain entities
5. **Payload Contract** — HTTP method + path + response JSON
6. **Flowchart** — Decision flow with error branches
7. **Architecture Diagram** — Module dependency graph

### The 6-Step Process

1. **Identify** — Recognize vague requirements
2. **Clarify** — Ask Who/What/Where/When/Why/How
3. **Specify BDD** — Write narratives and acceptance criteria
4. **Define Use Cases** — Procedural steps with cancel courses
5. **Model & Contract** — Property/Type tables and JSON payloads
6. **Visualize & Document** — Diagrams and feature specification

### Key Patterns from Essential Developer

- **Cancel courses** — First-class cancellation requirements for async operations
- **Separation of concerns** — Extract focused use cases (Load vs Validate vs Cache)
- **Domain language alignment** — Consistent terminology across all artifacts
- **Incremental feature development** — Self-contained feature blocks
- **Living specification** — Requirements evolve with code

## Skill File Structure

```
requirements-engineering/
├── SKILL.md                             # Hub (~140 lines)
└── references/
    ├── _index.md                        # Navigation hub
    ├── bdd-narratives.md                # BDD stories, narratives, acceptance criteria
    ├── use-cases.md                     # Use case structure, courses, separation of concerns
    ├── model-specs-and-contracts.md     # Model specs, payload contracts, JSON examples
    ├── diagrams.md                      # Flowcharts, architecture, sequence, state diagrams
    ├── domain-language.md               # Terminology alignment, renaming patterns
    └── feature-specification-workflow.md # End-to-end workflow, traceability
```

## Related Skills

- [ios-architecture-expert](https://github.com/SwiftyJourney/ios-architecture-expert-skill) — Clean architecture, composition root, generic presenters

## Credits

Requirements methodology extracted from the [iOS Lead Essentials](https://www.essentialdeveloper.com/ios-lead-essentials) program by [Essential Developer](https://www.essentialdeveloper.com). The Essential Feed Case Study README demonstrates the canonical artifact format.

## License

MIT — see [LICENSE](LICENSE).
