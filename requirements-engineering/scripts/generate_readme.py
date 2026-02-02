#!/usr/bin/env python3
"""
Generate a comprehensive README.md from structured requirements.

This script helps convert BDD stories, use cases, and architecture descriptions
into a well-formatted README.md file suitable for project documentation.
"""

import sys
from datetime import datetime
from typing import List, Dict, Optional


def generate_header(project_name: str, description: str) -> str:
    """Generate README header section."""
    return f"""# {project_name}

{description}

---

## Table of Contents
- [Use Cases](#use-cases)
- [Flowchart](#flowchart)
- [Architecture](#architecture)
- [BDD Specs](#bdd-specs)

---

"""


def generate_use_case_section(use_cases: List[Dict]) -> str:
    """Generate use cases section."""
    section = "## Use Cases\n\n"
    
    for uc in use_cases:
        section += f"### {uc['name']}\n\n"
        
        if 'data' in uc and uc['data']:
            section += "#### Data:\n"
            for item in uc['data']:
                section += f"- {item}\n"
            section += "\n"
        
        if 'primary_course' in uc:
            section += "#### Primary course (happy path):\n"
            for i, step in enumerate(uc['primary_course'], 1):
                section += f"{i}. {step}\n"
            section += "\n"
        
        if 'error_courses' in uc:
            for error in uc['error_courses']:
                section += f"#### {error['name']} – error course (sad path):\n"
                for i, step in enumerate(error['steps'], 1):
                    section += f"{i}. {step}\n"
                section += "\n"
        
        section += "---\n\n"
    
    return section


def generate_flowchart_section(flowchart_description: Optional[str] = None) -> str:
    """Generate flowchart section with placeholder."""
    section = "## Flowchart\n\n"
    
    if flowchart_description:
        section += f"{flowchart_description}\n\n"
    else:
        section += "*[Insert flowchart diagram here - Use Mermaid, PlantUML, or image]*\n\n"
    
    section += "---\n\n"
    return section


def generate_architecture_section(architecture_description: Optional[str] = None) -> str:
    """Generate architecture section."""
    section = "## Architecture\n\n"
    
    if architecture_description:
        section += f"{architecture_description}\n\n"
    else:
        section += "*[Insert architecture diagram here - Show component relationships]*\n\n"
    
    section += "---\n\n"
    return section


def generate_bdd_section(stories: List[Dict]) -> str:
    """Generate BDD specifications section."""
    section = "## BDD Specs\n\n"
    
    for story in stories:
        section += f"### Story: {story['title']}\n\n"
        
        if 'narratives' in story:
            for i, narrative in enumerate(story['narratives'], 1):
                section += f"#### Narrative #{i}\n\n"
                section += f"```gherkin\n"
                section += f"As a {narrative['actor']}\n"
                section += f"I want {narrative['action']}\n"
                section += f"So {narrative['benefit']}\n"
                section += f"```\n\n"
                
                if 'scenarios' in narrative:
                    section += "#### Scenarios (Acceptance criteria)\n\n"
                    for scenario in narrative['scenarios']:
                        section += f"```gherkin\n"
                        section += scenario
                        section += f"\n```\n\n"
        
        section += "---\n\n"
    
    return section


def generate_readme(
    project_name: str,
    description: str,
    use_cases: List[Dict],
    stories: List[Dict],
    flowchart_desc: Optional[str] = None,
    architecture_desc: Optional[str] = None
) -> str:
    """Generate complete README content."""
    readme = generate_header(project_name, description)
    readme += generate_use_case_section(use_cases)
    readme += generate_flowchart_section(flowchart_desc)
    readme += generate_architecture_section(architecture_desc)
    readme += generate_bdd_section(stories)
    
    return readme


# Example usage template
if __name__ == "__main__":
    # Example data structure
    example_use_cases = [
        {
            "name": "Load Feed Use Case",
            "data": ["URL"],
            "primary_course": [
                'Execute "Load Feed Items" command with above data',
                "System downloads data from the URL",
                "System validates downloaded data",
                "System creates feed items from valid data",
                "System delivers feed items"
            ],
            "error_courses": [
                {
                    "name": "Invalid data",
                    "steps": ["System delivers error"]
                },
                {
                    "name": "No connectivity",
                    "steps": ["System delivers error"]
                }
            ]
        }
    ]
    
    example_stories = [
        {
            "title": "Customer requests to see their image feed",
            "narratives": [
                {
                    "actor": "an online customer",
                    "action": "the app to automatically load my latest image feed",
                    "benefit": "I can always enjoy the newest images of my friends",
                    "scenarios": [
                        "Given the customer has connectivity\nWhen the customer requests to see the feed\nThen the app should display the latest feed from remote\nAnd replace the cache with the new feed"
                    ]
                }
            ]
        }
    ]
    
    readme_content = generate_readme(
        project_name="Feed Feature Case Study",
        description="A robust feed loading system with offline support",
        use_cases=example_use_cases,
        stories=example_stories,
        flowchart_desc="See flowchart.png for the complete feature workflow",
        architecture_desc="See architecture.png for system component design"
    )
    
    print(readme_content)
