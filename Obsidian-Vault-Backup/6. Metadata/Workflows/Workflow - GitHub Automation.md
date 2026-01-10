---
tags:
  - workflow
  - automation
  - github
type: workflow
created: 2025-01-10
---

# GitHub Automation Workflow

Use GitHub Issues and Actions to trigger Claude work even when away from computer.

## Overview

```
Create Issue (mobile) → GitHub Action triggers → Claude processes → Commits result → Syncs to vault
```

## Setup

### Step 1: Connect Vault to GitHub

```bash
cd "D:\OneDrive\04_Projects\17_Obsidian-Claude"
git init
git add .
git commit -m "Initial vault commit"
git remote add origin https://github.com/YOUR_USERNAME/obsidian-vault.git
git push -u origin main
```

### Step 2: Create GitHub Action

Create `.github/workflows/claude-processor.yml`:

```yaml
name: Claude Vault Processor

on:
  issues:
    types: [opened, labeled]

jobs:
  process:
    if: contains(github.event.issue.labels.*.name, 'claude-task')
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Process Request
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          # Extract task from issue body
          TASK="${{ github.event.issue.body }}"

          # Run Claude with the task
          claude --print "$TASK" > result.md

          # Move result to appropriate location
          TIMESTAMP=$(date +%Y-%m-%d-%H%M)
          mv result.md "Obsidian-Vault-Backup/0. Inbox/GitHub-Task-$TIMESTAMP.md"

      - name: Commit Results
        run: |
          git config user.name "Claude Bot"
          git config user.email "claude@bot.local"
          git add .
          git commit -m "Claude processed: ${{ github.event.issue.title }}"
          git push

      - name: Close Issue
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '✅ Task processed! Check your vault for results.'
            });
            github.rest.issues.update({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'closed'
            });
```

### Step 3: Add Secrets

In GitHub repo settings, add:
- `ANTHROPIC_API_KEY`: Your Claude API key

### Step 4: Create Issue Templates

Create `.github/ISSUE_TEMPLATE/claude-task.yml`:

```yaml
name: Claude Task
description: Request Claude to process something in your vault
labels: ["claude-task"]
body:
  - type: dropdown
    id: task-type
    attributes:
      label: Task Type
      options:
        - Research a topic
        - Summarize notes
        - Create connections
        - Process inbox
        - Generate content
        - Other
    validations:
      required: true

  - type: textarea
    id: task-description
    attributes:
      label: Task Description
      description: What should Claude do?
      placeholder: "Research the topic of X and create a summary note..."
    validations:
      required: true

  - type: textarea
    id: context
    attributes:
      label: Additional Context
      description: Any specific notes or areas to focus on?
```

## Usage

### From Mobile

1. Open GitHub app
2. Go to your vault repo
3. Create new Issue using "Claude Task" template
4. Fill in the task
5. Submit
6. Wait for Action to complete
7. Pull/sync vault to see results

### Task Examples

**Research Request:**
```
Task: Research the topic of "knowledge graphs" and create a
summary note with key concepts, tools, and how it relates
to my existing notes on AI and data management.

Focus on: 3. Resources (Dynamic)/Technology/
```

**Inbox Processing:**
```
Task: Process all notes in 0. Inbox/ that are older than
3 days. Categorize them using PARA and suggest connections.
```

**Content Generation:**
```
Task: Based on my notes in 1. Projects/Blog Ideas/,
create a draft blog post outline about productivity systems.
```

## Advanced: Scheduled Tasks

Add scheduled processing with cron:

```yaml
on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM UTC

jobs:
  daily-process:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Daily Vault Maintenance
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude --print "Run /inbox-processor on all items
          in 0. Inbox/ older than 24 hours"
```

## Security Notes

- Keep vault repo private
- Use GitHub Secrets for API keys
- Review Action logs for sensitive data exposure
- Consider .gitignore for personal/sensitive notes

## Sync Considerations

- Use branch protection if multiple sync sources
- Pull before making local changes
- Consider automated conflict resolution
