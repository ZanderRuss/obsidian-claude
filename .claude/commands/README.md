# Claude Code Commands

This folder contains 37 commands that help you work with your Obsidian vault and manage your knowledge. Think of commands as workflows - each one guides Claude through a specific process to help you accomplish common tasks.

---

## How to Use Commands (The Easy Way)

**You don't need to do anything special.** Just type a command and Claude will guide you through the workflow.

### Step 1: Open Claude Code

Open your terminal or command prompt where Claude Code is running.

### Step 2: Type a Command

Type a forward slash `/` followed by the command name. For example:

```
/thinking-partner
```

Claude will then start the workflow and guide you through the process.

### Common Commands You Can Try Right Now

| Type This | What It Does |
|-----------|--------------|
| `/thinking-partner` | Explore ideas through questioning |
| `/daily-review` | End-of-day reflection and planning |
| `/inbox-processor` | Organize captured notes using PARA |
| `/research-ideate` | Generate and refine research ideas |
| `/smart-link` | Find connections between notes |

---

## All Available Commands

### Knowledge Workflows

| Command Name | What It Helps You Do | When to Use |
|--------------|---------------------|-------------|
| `/thinking-partner` | Explore ideas through Socratic dialogue | Complex problems, brainstorming |
| `/daily-review` | End-of-day reflection and capture | Every evening (5-10 min) |
| `/weekly-synthesis` | Identify patterns across the week | Sunday or Monday (30-60 min) |
| `/research-assistant` | Deep topical investigation | Learning new topics |
| `/inbox-processor` | Organize captured notes via PARA | Weekly or when backlog builds |

### Advanced Analysis

| Command Name | What It Helps You Do | When to Use |
|--------------|---------------------|-------------|
| `/smart-link` | AI-powered connection suggestions | After creating notes, finding orphans |
| `/graph-analysis` | Analyze knowledge graph health | Monthly vault maintenance |
| `/extract-todos` | Find and consolidate scattered tasks | Weekly task review |
| `/summarize-project` | Create project executive summary | Project check-ins, handoffs |

### Content Transformation

| Command Name | What It Helps You Do | When to Use |
|--------------|---------------------|-------------|
| `/flashcards` | Generate spaced repetition cards | Learning/studying topics |
| `/note-to-blog` | Transform notes into publishable content | Content creation |
| `/voice-process` | Structure voice transcriptions | After voice capture |
| `/web-clip` | Save web articles as markdown | Research, bookmarking |

### Academic Research Workflow

| Command Name | What It Helps You Do | When to Use |
|--------------|---------------------|-------------|
| `/research-ideate` | Socratic exploration of research ideas | Starting new research, brainstorming |
| `/quick-research` | Rapid 5-10 source investigation | Exploration, background research |
| `/research-project-init` | Create phased research folder structure | Starting major research projects |
| `/research-progress` | Check research phase completion status | Progress tracking, gap analysis |
| `/lit-search` | Literature search across Zotero + web | Finding relevant papers |
| `/deep-research` | Comprehensive multi-source investigation | Background research, surveys |
| `/evidence-qa` | Evidence-grounded Q&A over your PDFs | Answering specific research questions |
| `/lit-review` | Generate structured literature review | Writing related work sections |
| `/paper-outline` | Create paper structure for venue | Starting paper writing |
| `/paper-draft` | Draft specific paper sections | Writing methodology, experiments |
| `/paper-review` | Simulate peer review feedback | Before submission |
| `/paper-polish` | Grammar, style, consistency | Final editing pass |
| `/export-paper` | Export to LaTeX/PDF/Word | Submission preparation |

### Thesis & Paper Writing (Multi-Agent Pipeline)

| Command Name | What It Helps You Do | When to Use |
|--------------|---------------------|-------------|
| `/thesis-init` | Initialize thesis project with templates | Starting PhD thesis, large documents |
| `/thesis-write` | Write complete thesis (90k+ words) | Full thesis production with quality gates |
| `/chapter-write` | Write a single thesis chapter | Individual chapter drafting |
| `/paper-write` | Write conference/journal paper | Academic paper submissions |
| `/quality-check` | Run all quality control agents | Before submission, after revisions |
| `/paper-revise` | Handle reviewer feedback systematically | Post-review revision process |

### Git & Documentation

| Command Name | What It Helps You Do | When to Use |
|--------------|---------------------|-------------|
| `/commit` | Create well-formatted git commits | After making code changes |
| `/create-pr` | Create pull requests | Ready to merge changes |
| `/pr-review` | Review pull requests | Code review process |
| `/update-docs` | Update documentation | After implementation changes |
| `/create-architecture-documentation` | Generate architecture docs with diagrams | Documenting system design |

---

## Command Workflows Explained

### Knowledge Management Flow

The knowledge management commands work together as a system:

```
Daily Work → /daily-review → /inbox-processor → /weekly-synthesis
                ↓                    ↓                    ↓
          Capture wins         Organize notes      Find patterns
```

**Recommended cadence:**
- `/daily-review`: Every evening (5-10 minutes)
- `/inbox-processor`: Weekly or when inbox has 10+ items
- `/weekly-synthesis`: Sunday evening or Monday morning (30-60 minutes)

### Research Pipeline Flow

The academic research commands follow a structured pipeline:

```
Idea → /research-ideate → /lit-search → /deep-research
           ↓                   ↓              ↓
     Research questions    Find papers    Deep analysis
           ↓                   ↓              ↓
    /evidence-qa → /lit-review → /paper-outline → /paper-draft
           ↓                   ↓              ↓              ↓
     Answer questions   Synthesize    Structure paper   Write sections
           ↓
    /paper-review → /paper-polish → /export-paper
           ↓              ↓              ↓
     Peer review    Final edits    Submit ready
```

**Full pipeline:**
1. `/research-ideate` - Generate research questions & hypotheses
2. `/lit-search` - Find relevant papers in Zotero + web
3. `/deep-research` - Comprehensive background investigation
4. `/evidence-qa` - Ground claims in your PDF corpus
5. `/lit-review` - Synthesize into literature review
6. `/paper-outline` - Structure for target venue
7. `/paper-draft` - Write sections with citations
8. `/paper-review` - Simulate peer review
9. `/paper-polish` - Final editing pass
10. `/export-paper` - LaTeX/PDF for submission

### Content Creation Flow

Transform and publish your knowledge:

```
Voice Recording → /voice-process → /thinking-partner → /note-to-blog
      ↓                 ↓                   ↓              ↓
  Quick capture    Structured note    Deep thinking   Publishable
```

Or for web research:

```
Web Article → /web-clip → /research-assistant → /note-to-blog
      ↓            ↓              ↓                  ↓
   Raw HTML    Clean markdown  Synthesize        Publish
```

### Vault Maintenance Flow

Keep your vault healthy and connected:

```
Weekly Check → /extract-todos → /graph-analysis → /smart-link
      ↓              ↓                 ↓              ↓
  Review vault   Find tasks      Health check   Add connections
```

**Recommended cadence:**
- `/extract-todos`: Weekly task consolidation
- `/graph-analysis`: Monthly vault health check
- `/smart-link`: After creating 5+ new notes

---

## Quick Reference Card

| I Want To... | Type This |
|--------------|-----------|
| Explore an idea deeply | `/thinking-partner` |
| Review my day | `/daily-review` |
| Review my week | `/weekly-synthesis` |
| Organize my inbox | `/inbox-processor` |
| Find connections | `/smart-link` |
| Check vault health | `/graph-analysis` |
| Find all my tasks | `/extract-todos` |
| Generate research ideas | `/research-ideate` |
| Quick exploration research | `/quick-research` |
| Start a major research project | `/research-project-init` |
| Check research progress | `/research-progress` |
| Search for papers | `/lit-search` |
| Write a literature review | `/lit-review` |
| Structure a paper | `/paper-outline` |
| Draft a paper section | `/paper-draft` |
| Get peer review feedback | `/paper-review` |
| Polish my writing | `/paper-polish` |
| Export to LaTeX/PDF | `/export-paper` |
| Start a thesis project | `/thesis-init` |
| Write a complete thesis | `/thesis-write` |
| Write a thesis chapter | `/chapter-write` |
| Write a conference paper | `/paper-write` |
| Run quality checks | `/quality-check` |
| Handle reviewer comments | `/paper-revise` |
| Create flashcards | `/flashcards` |
| Process voice memos | `/voice-process` |
| Save web articles | `/web-clip` |
| Write a blog post | `/note-to-blog` |
| Create git commit | `/commit` |
| Create pull request | `/create-pr` |
| Review a PR | `/pr-review` |

---

## Understanding Command Types

### Thinking Commands (Exploration)

These commands help you explore and develop ideas:
- **Philosophy**: Questions before answers
- **Output**: Thinking logs, insights
- **Duration**: 15-30 minutes
- **Examples**: `/thinking-partner`, `/research-ideate`

### Review Commands (Reflection)

These commands help you reflect and synthesize:
- **Philosophy**: Look back to learn, look forward to prepare
- **Output**: Review notes, patterns, action items
- **Duration**: 5-60 minutes depending on scope
- **Examples**: `/daily-review`, `/weekly-synthesis`

### Processing Commands (Organization)

These commands help you organize and structure:
- **Philosophy**: Everything in its place (PARA method)
- **Output**: Organized notes, updated structure
- **Duration**: 10-30 minutes
- **Examples**: `/inbox-processor`, `/smart-link`

### Analysis Commands (Insight)

These commands help you analyze and understand:
- **Philosophy**: Data-driven insights
- **Output**: Reports, visualizations, summaries
- **Duration**: 10-20 minutes
- **Examples**: `/graph-analysis`, `/extract-todos`, `/summarize-project`

### Creation Commands (Production)

These commands help you create content:
- **Philosophy**: Transform knowledge into artifacts
- **Output**: Publishable content, flashcards, structured documents
- **Duration**: 20-60 minutes
- **Examples**: `/note-to-blog`, `/flashcards`, `/paper-draft`

### Research Commands (Academic)

These commands support academic research workflows:
- **Philosophy**: Rigorous, evidence-based, systematic
- **Output**: Literature reviews, paper sections, citations
- **Duration**: 30-120 minutes depending on scope
- **Examples**: All `/paper-*` and `/lit-*` commands

---

## Daily Workflow Examples

### Morning Routine (5 minutes)

1. Review yesterday's `/daily-review` note
2. Check top 3 priorities
3. Quick scan of `/inbox-processor` output

### During the Day

1. Capture quick notes to `0. Inbox/`
2. Use `/thinking-partner` for complex problems
3. Use `/web-clip` for interesting articles
4. Use `/voice-process` for voice memos

### Evening Routine (10 minutes)

1. Run `/daily-review`
2. Process voice memos if any
3. Quick inbox triage
4. Set tomorrow's focus

### Weekly Routine (60 minutes)

1. Run `/weekly-synthesis`
2. Full `/inbox-processor` pass
3. Run `/extract-todos` for task consolidation
4. Run `/graph-analysis` for vault health
5. Run `/smart-link` to connect new notes
6. Archive completed work

---

## Integration with Skills

Commands and skills work together. Commands invoke skills automatically when needed:

### Command Uses Skill

| Command | Uses These Skills |
|---------|-------------------|
| `/lit-search` | `citation-management` |
| `/lit-review` | `literature-review`, `scientific-writing` |
| `/paper-outline` | `venue-templates`, `scientific-writing` |
| `/paper-draft` | `scientific-writing` |
| `/paper-polish` | `scientific-writing` |
| `/export-paper` | `docx`, `pdf-processing-pro` |
| `/flashcards` | (built-in) |
| `/voice-process` | (built-in) |
| `/web-clip` | (built-in) |
| `/graph-analysis` | (built-in) |

**You don't need to call skills directly** - commands handle this for you.

---

## Tips for Success

### Start Small

Don't try to use all commands at once. Start with:
1. `/daily-review` - Build reflection habit
2. `/inbox-processor` - Keep vault organized
3. `/thinking-partner` - Explore one idea deeply

Then expand as needed.

### Create Habits

Commands work best as regular habits:
- **Daily**: `/daily-review`
- **Weekly**: `/inbox-processor`, `/weekly-synthesis`
- **Monthly**: `/graph-analysis`
- **As needed**: Everything else

### Combine Commands

Commands are designed to work together:
```
/thinking-partner → /daily-review → /inbox-processor → /smart-link
```

Each builds on the previous one.

### Customize Workflows

Feel free to adapt commands to your workflow:
- Skip sections that don't apply
- Add your own templates
- Adjust frequency to your needs

---

## Troubleshooting

### "Command not found"

Make sure you're typing the command in Claude Code, not in a regular terminal. The `/` commands only work when talking to Claude.

### Commands feel overwhelming

Start with just `/daily-review`. Build one habit before adding more. Quality over quantity.

### Not seeing results

Commands work best with consistency:
- `/daily-review` needs daily practice
- `/inbox-processor` needs weekly rhythm
- `/smart-link` needs notes to connect

Give it 2-3 weeks to see patterns emerge.

### Need more help?

Just ask Claude! Type something like:
> "Help me understand how to use /weekly-synthesis"

---

## Command Philosophy

### AI as Thinking Partner

> "AI amplifies thinking, not just writing."

Commands embody this philosophy:
- **Questions before answers** - Clarify understanding first
- **Exploration before production** - Think deeply before creating
- **Connections over content** - Link ideas, find patterns
- **Iteration over perfection** - Build understanding incrementally

### PARA Method Integration

Commands respect the PARA method:
- **Projects** (1. Projects/) - Active work with deadlines
- **Areas** (2. Areas (Ongoing)/) - Ongoing responsibilities
- **Resources** (3. Resources (Dynamic)/) - Reference materials
- **Archive** (4. Archive (Supportive)/) - Completed items

### Evidence-Based Workflows

Academic commands follow best practices:
- Systematic literature search
- Evidence grounding
- Peer review simulation
- Proper citation management
- Venue-specific formatting

---

## What's Next?

After mastering commands, explore:

1. **Skills** - Lower-level capabilities commands build on
   - See `.claude/skills/README.md` for details

2. **Agents** - Specialized assistants for specific tasks
   - Check CLAUDE.md for agent descriptions

3. **MCP Integration** - Direct vault access via API
   - See `6. Metadata/Reference/Local REST API Setup.md`

4. **Custom Commands** - Create your own workflows
   - Copy an existing command and adapt it

---

## Summary

**37 commands organized into 7 categories:**

- 5 Knowledge Workflows
- 4 Advanced Analysis
- 4 Content Transformation
- 13 Academic Research
- 6 Thesis & Paper Writing (Multi-Agent Pipeline)
- 5 Git & Documentation

**Start with these 3:**
1. `/daily-review` - Build reflection habit
2. `/inbox-processor` - Stay organized
3. `/thinking-partner` - Explore ideas deeply

**Remember:**
- Commands are workflows, not just features
- Consistency beats intensity
- Start small, build habits, expand gradually
- Quality of exploration > speed of production

Ready to begin? Try `/thinking-partner` and explore your first idea!
