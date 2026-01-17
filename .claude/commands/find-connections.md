# Find Connections

You are a vault connection specialist. Analyze content and suggest links between related notes to strengthen the knowledge graph.

## Important: Use Specialized Agent

This command MUST use the `connection-agent` agent via the Task tool for comprehensive analysis:

```
Task tool with subagent_type="connection-agent"
```

## Connection Goals

A well-connected vault enables:
- Serendipitous discovery
- Stronger understanding through relationships
- Better navigation
- Emergent insights from linked ideas

## Analysis Process

The connection-agent will:

### 1. Semantic Analysis
- Identify concepts discussed in each note
- Find notes discussing similar concepts differently
- Detect implicit relationships not yet linked

### 2. Entity Matching
- People mentioned across notes
- Projects referenced in multiple places
- Tools, technologies, concepts appearing in different contexts

### 3. Structural Analysis
- Notes in same folder that should link
- Notes with same tags not linking
- Temporal relationships (notes from same period)

### 4. Gap Analysis
- Orphaned notes (no incoming links)
- Terminal notes (no outgoing links)
- Isolated clusters (groups not connected to main graph)

## Connection Types

| Type | Description | Example |
|------|-------------|---------|
| **Conceptual** | Same concept, different angle | Theory note ↔ Application note |
| **Sequential** | One follows/builds on another | Part 1 ↔ Part 2 |
| **Supportive** | Evidence or elaboration | Claim ↔ Research source |
| **Contrasting** | Opposing or alternative views | Approach A ↔ Approach B |
| **Hierarchical** | Parent/child relationship | MOC ↔ Individual notes |
| **Temporal** | Time-based relationship | Meeting ↔ Follow-up |

## Output Format

```markdown
# Connection Analysis Report

## Summary
- Notes analyzed: [X]
- Potential connections found: [Y]
- Orphan notes: [Z]
- Terminal notes: [N]

## High-Value Connections

Strong relationships that should definitely be linked:

| Note A | Note B | Relationship | Confidence |
|--------|--------|--------------|------------|
| [[Note 1]] | [[Note 2]] | Same project | High |
| [[Note 3]] | [[Note 4]] | Concept overlap | High |

**Why these matter**: [Explanation]

## Medium-Value Connections

Worth considering:

| Note A | Note B | Relationship | Confidence |
|--------|--------|--------------|------------|
| [[Note]] | [[Note]] | Related topic | Medium |

## Orphan Notes (No Incoming Links)

Notes nothing links to:

| Note | Topic | Suggested Link From |
|------|-------|---------------------|
| [[Orphan]] | Topic X | [[Related Note]], [[MOC - X]] |

## Terminal Notes (No Outgoing Links)

Notes that don't link to anything:

| Note | Topic | Suggested Link To |
|------|-------|-------------------|
| [[Terminal]] | Topic Y | [[Related]], [[Resource]] |

## Cluster Analysis

Groups of notes that should be interconnected:

### Cluster: [Topic Name]
```
[[Note A]] - - - [[Note B]]
     \           /
      \         /
       [[Note C]]
```
- Currently connected: A↔B
- Missing: A↔C, B↔C

## Entity Mentions

People/projects/tools mentioned in multiple notes:

| Entity | Mentioned In | Currently Linked |
|--------|--------------|------------------|
| "Project Alpha" | [[Note 1]], [[Note 2]], [[Note 3]] | Only 1↔2 |

## Recommended Actions

### Quick Wins (Add These Links)
1. [[Note A]] → [[Note B]]: [reason]
2. [[Note C]] → [[Note D]]: [reason]

### Create Hub Notes
- Topic X has 8 notes but no MOC
- Consider creating [[MOC - Topic X]]

### Review These Orphans
- [[Orphan 1]]: Valuable but disconnected
- [[Orphan 2]]: May be outdated, review content
```

## After Analysis

Offer to:
1. Add the high-confidence links automatically
2. Create backlinks where appropriate
3. Build MOCs for detected clusters
4. Add orphan notes to relevant MOCs
5. Enrich terminal notes with outgoing links

## Linking Best Practices

- **Link to the most relevant note**, not all related notes
- **Use contextual links** embedded in sentences
- **Create bidirectional links** when both directions add value
- **Group related links** in a "Related" section if many
- **Use aliases** for natural reading: `[[Technical Term|simple version]]`
