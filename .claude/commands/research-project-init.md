# Initialize Research Project

Creates a complete research project folder with all phase templates for the Complete Research Track.

## Input

- Project name: $ARGUMENTS

## Process

### 1. Confirm Research Track

Ask the user to confirm they want the Complete Research Track (6 phases, quality gates).

For quick exploration, recommend `/quick-research` instead.

### 2. Create Project Folder

Create folder structure at:
`Obsidian-Template-Vault/3. Resources (Dynamic)/Research/[Project Name]/`

### 3. Generate Phase Files

Create the following files from templates:

| File | Template Source |
|------|-----------------|
| `00 - Brief - [Name].md` | Template - Research Brief (00) |
| `10 - Sources - [Name].md` | Template - Research Sources (10) |
| `20 - Notes - [Name].md` | Template - Research Notes (20) |
| `30 - Synthesis - [Name].md` | Template - Research Synthesis (30) |
| `40 - Draft - [Name].md` | Template - Research Draft (40) |
| `99 - Bibliography - [Name].md` | Template - Research Bibliography (99) |

### 4. Create Project MOC

Create a Map of Content for the project:
`MOC - [Name] Research.md`

### 5. Update Cross-References

Ensure all phase files link to each other correctly.

## Output

### Folder Structure Created

```
3. Resources (Dynamic)/Research/[Project Name]/
├── 00 - Brief - [Name].md
├── 10 - Sources - [Name].md
├── 20 - Notes - [Name].md
├── 30 - Synthesis - [Name].md
├── 40 - Draft - [Name].md
├── 99 - Bibliography - [Name].md
└── MOC - [Name] Research.md
```

### Confirmation Message

Provide:

1. Links to all created files
2. Reminder about quality gates (Phase 30 and 40)
3. Suggested first step: "Start by completing the Brief (00)"
4. Link to `/research-progress` for tracking

## Example Usage

```
/research-project-init Transformer Efficiency Methods
```

Creates:
- `3. Resources (Dynamic)/Research/Transformer Efficiency Methods/`
- All 6 phase files + MOC
- Ready for Complete Research Track workflow

## Related Commands

| Command | Purpose |
|---------|---------|
| `/quick-research` | Lightweight single-file research |
| `/research-progress` | Check phase completion status |
| `/deep-research` | Comprehensive investigation (uses these templates) |

## Notes

- Project names should be descriptive but concise
- Avoid special characters that cause file system issues
- The Brief (00) should be completed first to define scope
- Quality gates are enforced on Synthesis (30) and Draft (40)
