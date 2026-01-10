---
tags:
  - reference
  - system
type: reference
created: 2025-01-10
---

# Vault Overview

## Folder Structure (PARA Method)

| Folder | Purpose | Examples |
|--------|---------|----------|
| `0. Inbox` | Temporary capture | Quick notes, ideas, unfiled items |
| `1. Projects` | Active initiatives with deadlines | Client work, launches, deliverables |
| `2. Areas (Ongoing)` | Ongoing responsibilities | Health, finances, relationships |
| `3. Resources (Dynamic)` | Reference materials | Research, how-tos, topic collections |
| `4. Archive (Supportive)` | Completed/inactive | Finished projects, old resources |
| `Images` | Attachments | Screenshots, diagrams, photos |
| `Templates` | Note templates | In Obsidian settings |
| `6. Metadata` | System files | Templates, workflows, reference |

## Available Claude Commands

### Knowledge Workflows

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/thinking-partner` | Explore ideas through dialogue | Complex problems, brainstorming |
| `/daily-review` | End-of-day reflection | Every evening |
| `/weekly-synthesis` | Weekly pattern recognition | Sunday/Monday |
| `/research-assistant` | Deep topic investigation | Learning new topics |
| `/inbox-processor` | Organize captured notes | Weekly or when backlog builds |

### Development & Git

| Command | Purpose |
|---------|---------|
| `/commit` | Create git commits |
| `/create-pr` | Create pull requests |
| `/pr-review` | Review pull requests |
| `/update-docs` | Update documentation |

## Installed Agents

### Obsidian Operations

- `vault-optimizer` - Performance and storage
- `moc-agent` - Maps of Content
- `tag-agent` - Tag taxonomy
- `content-curator` - Content organization
- `metadata-agent` - Frontmatter
- `connection-agent` - Links and relationships
- `review-agent` - Quality review

### Development

- `code-reviewer` - Code review
- `debugger` - Debug issues
- `technical-writer` - Documentation
- `security-auditor` - Security analysis

## Key Plugins

- **Smart Connections** - AI-powered linking
- **Dataview** - Query and display data
- **Templater** - Advanced templates
- **Local REST API** - External access

## Quick Reference

### Frontmatter Template

```yaml
---
tags:
  - category/subcategory
type: note
created: YYYY-MM-DD
status: active
---
```

### Link Syntax

- Wiki link: `[[Note Name]]`
- Alias: `[[Note Name|Display Text]]`
- Embed: `![[Note Name]]`
- Heading: `[[Note Name#Heading]]`
