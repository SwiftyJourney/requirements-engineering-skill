# Installation Guide

Complete installation instructions for different AI agent tools.

## skills CLI (Recommended)

```bash
npx skills add SwiftyJourney/requirements-engineering-skill
```

This works with Claude, Cursor, Windsurf, Cline, and other compatible tools.

## Claude.ai

1. Download `requirements-engineering.skill` from [Releases](https://github.com/SwiftyJourney/requirements-engineering-skill/releases)
2. Open Claude.ai and go to your Project
3. Click "Add Skills" or upload the `.skill` file
4. The skill is now available in your project

## Cursor

```bash
# Clone the repository
git clone https://github.com/SwiftyJourney/requirements-engineering-skill.git

# Copy to Cursor skills directory
# macOS:
cp -r requirements-engineering-skill/requirements-engineering ~/Library/Application\ Support/Cursor/User/globalStorage/skills/

# Linux:
cp -r requirements-engineering-skill/requirements-engineering ~/.config/Cursor/User/globalStorage/skills/

# Windows:
# Copy to %APPDATA%\Cursor\User\globalStorage\skills\
```

Restart Cursor and enable the skill in Settings → Features → Skills.

## Windsurf

```bash
git clone https://github.com/SwiftyJourney/requirements-engineering-skill.git
# Follow Windsurf's skills installation guide
# Copy requirements-engineering/ folder to Windsurf's skills directory
```

## Cline (VS Code Extension)

```bash
git clone https://github.com/SwiftyJourney/requirements-engineering-skill.git
# In VS Code: Settings → Extensions → Cline → Skills Directory
# Copy requirements-engineering/ folder to configured directory
```

## Verification

Test the skill is working:

```plaintext
I need help refining this requirement: "Users should see a dashboard"
```

The agent should ask clarifying questions and create BDD stories.

## Troubleshooting

**Skill not found:** Ensure the folder is named exactly `requirements-engineering` and contains `SKILL.md`

**Not triggering:** Try explicitly: "Use the requirements-engineering skill to help me..."

**Permission issues:** Use `sudo` on macOS/Linux or run as Administrator on Windows

For more help, see [GitHub Issues](https://github.com/SwiftyJourney/requirements-engineering-skill/issues).
