# /thesis-init

Initialize a PhD thesis project structure with chapters and templates.

## Usage

```
/thesis-init [project-name]
```

## Description

Creates a complete thesis project structure in the Obsidian vault, including:
- Chapter folders with section templates
- Research notes organization
- Bibliography management setup
- Progress tracking templates

## Process

1. **Gather Requirements**
   - Ask for thesis title (if not provided)
   - Ask for target institution (for formatting requirements)
   - Ask for expected chapter count (default: 7)
   - Ask for methodology type (experimental, analytical, empirical, theoretical, mixed)

2. **Create Folder Structure**

```
1. Projects/{project-name}/
├── 00-Overview/
│   ├── Thesis-Project.md          # Main project note
│   ├── Thesis-Context.md          # ThesisContext schema
│   └── Progress-Tracker.md        # Chapter completion tracking
├── 01-Introduction/
│   ├── Introduction-Draft.md
│   └── notes/
├── 02-Literature-Review/
│   ├── Literature-Review-Draft.md
│   └── notes/
├── 03-Methodology/
│   ├── Methodology-Draft.md
│   └── notes/
├── 04-Results/
│   ├── Results-Draft.md
│   └── notes/
├── 05-Discussion/
│   ├── Discussion-Draft.md
│   └── notes/
├── 06-Conclusion/
│   ├── Conclusion-Draft.md
│   └── notes/
├── Appendices/
│   └── Appendix-A.md
├── drafts/
│   └── thesis-draft.md            # Combined document
├── exports/
│   └── .gitkeep
└── bibliography/
    └── thesis-refs.bib
```

3. **Create Initial Files**
   - Use thesis templates from `6. Metadata/Templates/Thesis/`
   - Initialize ThesisContext with collected metadata
   - Link to existing research project if applicable

4. **Setup Integration**
   - Connect to Zotero collection if specified
   - Create dataview queries for progress tracking
   - Set up daily/weekly check-in reminders

## Output

- Project folder structure created in vault
- All template files initialized
- ThesisContext populated with initial values
- Progress tracker ready for use

## Related Commands

- `/thesis-write` - Write thesis using multi-agent pipeline
- `/chapter-write` - Write individual chapters
- `/research-project-init` - Initialize research project (may precede thesis)

## Example

```
User: /thesis-init "Efficient Attention Mechanisms"

Claude:
- Created thesis project: "Efficient Attention Mechanisms"
- Chapter structure: 7 chapters (standard IMRAD)
- Institution: Stanford University
- Methodology: Experimental
- Zotero collection: "PhD-Thesis"
- Location: 1. Projects/Efficient Attention Mechanisms Thesis/
```

## Agent Integration

This command coordinates with:
- Uses thesis templates from `6. Metadata/Templates/Thesis/`
- Sets up context for thesis-orchestrator
- Prepares structure for chapter-coordinator
