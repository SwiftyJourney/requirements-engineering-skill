# Requirements Engineering Agent Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agent Skills](https://img.shields.io/badge/Agent-Skills-blue)](https://agentskills.io)

Transform vague requirements into well-defined, testable specifications using BDD (Behavior-Driven Development), Use Cases, flowcharts, and architecture diagrams.

Based on the [Essential Developer](https://www.essentialdeveloper.com/) approach to requirements engineering as demonstrated in the [Feed Feature Case Study](https://github.com/essentialdevelopercom/essential-feed-case-study).

## Who This Is For

- **Product Managers** refining feature requirements
- **Software Teams** bridging business and technical requirements
- **Developers** documenting features before implementation
- **Technical Writers** creating comprehensive project documentation
- **Anyone** transforming "lousy requirements" into clear, actionable specifications

## What This Skill Does

This skill guides AI agents through a structured 6-step process:

1. **Identify vague requirements** → Recognize assumptions and gaps
2. **Ask clarifying questions** → Eliminate ambiguity
3. **Write BDD stories** → Multiple narratives with Given/When/Then scenarios
4. **Create use cases** → Step-by-step procedural documentation
5. **Generate diagrams** → Flowcharts, architecture, and sequence diagrams
6. **Document in README** → Complete structured project

## Installation

### Option A: Using skills CLI (Recommended)

```bash
npx skills add SwiftyJourney/requirements-engineering-skill
```

This automatically installs the skill for your AI agent tools.

### Option B: Manual Installation

#### For Claude.ai

1. Download `requirements-engineering.skill` from [Releases](https://github.com/SwiftyJourney/requirements-engineering-skill/releases)
2. Upload to your Claude project

#### For Cursor

```bash
git clone https://github.com/SwiftyJourney/requirements-engineering-skill.git
cp -r requirements-engineering-skill/requirements-engineering ~/Library/Application\ Support/Cursor/User/globalStorage/skills/
```

#### For Windsurf

```bash
git clone https://github.com/SwiftyJourney/requirements-engineering-skill.git
# Follow Windsurf's skills installation guide
```

See the [Installation Guide](docs/INSTALLATION.md) for detailed instructions.

## Quick Start

Try this prompt:

```plaintext
I need help refining this requirement:
"As a user, I want to see a feed so I can view content"
```

The agent will:

- Ask clarifying questions about user types, data sources, connectivity
- Create multiple BDD narratives (online/offline users)
- Write detailed use cases with error handling
- Generate flowcharts and architecture diagrams
- Structure everything for a README

## Example Output

When you use this skill, you get:

**BDD Stories:**

```gherkin
Story: Customer requests to see their image feed

Narrative #1
As an online customer
I want the app to automatically load my latest image feed
So I can always enjoy the newest images of my friends

Scenarios (Acceptance criteria)
Given the customer has connectivity
When the customer requests to see the feed
Then the app should display the latest feed from remote
And replace the cache with the new feed
```

**Use Cases:**

```plaintext
Load Feed Use Case

Data (Input):
- URL

Primary course (happy path):
1. Execute "Load Feed Items" command with above data
2. System downloads data from the URL
3. System validates downloaded data
4. System creates feed items from valid data
5. System delivers feed items

Invalid data – error course (sad path):
1. System delivers error
```

**Diagrams:** Mermaid flowcharts and architecture diagrams

**README:** Complete structured documentation

## What's Included

```plaintext
requirements-engineering/
├── SKILL.md                      # Main skill instructions (6-step process)
├── references/
│   ├── bdd_templates.md          # BDD story patterns and anti-patterns
│   ├── usecase_templates.md      # Use case templates (CRUD, caching, etc.)
│   └── diagram_guide.md          # Mermaid diagram generation guide
├── scripts/
│   └── generate_readme.py        # Automated README generation
└── assets/
    └── README_template.md        # Markdown template
```

## Key Features

### BDD Templates

- Multiple narrative patterns for different user types
- Given/When/Then scenario templates
- Error case handling patterns
- Anti-patterns to avoid

### Use Case Patterns

- CRUD operations (Create, Read, Update, Delete)
- Caching and fallback strategies
- Data fetching and validation
- Error handling workflows

### Diagram Generation

- Flowcharts for feature workflows
- Architecture diagrams for component structure
- Sequence diagrams for interactions
- State diagrams for feature states

### Automation

- Python script for README generation
- Templates for consistent documentation
- Structured approach for repeatability

## Usage Examples

### Example 1: Refining Vague Requirements

**Input:** "I need a feed feature"

**Output:**

- Clarifying questions asked
- BDD stories for online/offline users
- Use cases (Load, Cache, Save)
- Flowchart and architecture diagrams
- Complete README structure

### Example 2: Full Feature Documentation

**Input:** "Create requirements for a notification system"

**Output:**

- Multiple BDD narratives
- Complete use cases with error handling
- System architecture diagram
- Workflow flowchart
- README with all specifications

### Example 3: Converting Stories to Use Cases

**Input:** "Here are my BDD stories: [paste stories]"

**Output:**

- Extracted use cases from scenarios
- Additional error handling use cases
- Supporting diagrams
- Structured documentation

## Supported Agent Tools

This skill works with any tool supporting the [Agent Skills open format](https://agentskills.io):

- ✅ Claude.ai & Claude Code
- ✅ Cursor
- ✅ Windsurf
- ✅ Cline
- ✅ GitHub Copilot
- ✅ And many more

## Based On

This skill implements the Essential Developer's proven requirements engineering methodology:

- [Feed Feature Case Study](https://github.com/essentialdevelopercom/essential-feed-case-study)
- [Essential Developer Blog](https://www.essentialdeveloper.com/articles)
- Industry-standard BDD and use case practices

## Philosophy

> "Good architecture is a byproduct of good team processes"

This skill helps you:

- **Maximize understanding** through effective communication
- **Minimize assumptions** by asking the right questions
- **Bridge the gap** between technical and business requirements
- **Provide maximum value** to customers

## Documentation

- 📖 [Quick Start Guide](docs/QUICKSTART.md) - Get started in 5 minutes
- 🔧 [Installation Guide](docs/INSTALLATION.md) - Detailed install for all tools
- 🤝 [Contributing](docs/CONTRIBUTING.md) - How to contribute

## Contributing

Contributions are welcome! Whether you want to:

- Add new BDD patterns
- Improve use case templates
- Enhance diagram examples
- Fix documentation

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## License

This skill is open-source and available under the MIT License. See [LICENSE](LICENSE) for details.

## Author

Created by Juan Francisco Dorado Torres at SwiftyJourney, inspired by the Essential Developer's requirements engineering methodology.

## Acknowledgments

- [Essential Developer](https://www.essentialdeveloper.com/) for the requirements engineering methodology
- [Anthropic](https://www.anthropic.com/) for the Agent Skills format
- [Agent Skills community](https://agentskills.io) for the open standard

---

**Ready to transform your requirements?** Install the skill and start refining! ✨
