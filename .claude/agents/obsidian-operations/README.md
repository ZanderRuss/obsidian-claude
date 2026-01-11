# Obsidian Operations Team

This directory contains specialized agents for maintaining, optimizing, and organizing your Obsidian vault using the PARA method.

## Agent Categories

### 📊 Content Organization

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **moc-agent** | Map of Content creation | Missing MOCs, orphaned content, navigation structure |
| **tag-agent** | Tag taxonomy standardization | Inconsistent tags, duplicates, hierarchy cleanup |
| **metadata-agent** | Frontmatter management | Missing metadata, standardization |
| **content-curator** | Content quality & organization | Consolidation, quality review, content improvement |

### 🔗 Vault Maintenance

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **connection-agent** | Link analysis & suggestions | Finding orphans, suggesting connections |
| **vault-optimizer** | Performance optimization | Large files, slow search, storage cleanup |
| **review-agent** | Quality assurance | Cross-checking work, validation |

## Detailed Agent Profiles

### moc-agent (Sonnet)
**Map of Content specialist**

**Core Responsibilities:**
- Identify directories needing MOCs
- Generate new MOCs from templates
- Organize orphaned images into galleries
- Update existing MOCs with new content
- Maintain MOC network and cross-links

**Use When:**
- New content areas need navigation hubs
- Images without links need organization
- MOC structure needs updating
- Directories lack clear entry points

**Deliverables:**
- MOC files following naming convention (`MOC - [Topic].md`)
- Gallery notes for orphaned images
- Updated Master_Index with new MOCs
- Proper frontmatter and hierarchical structure

**Key Standards:**
- Store in `/map-of-content/` directory
- Include frontmatter with `type: "moc"`
- Link to sub-MOCs and related content
- Clear hierarchical structure

---

### tag-agent (Sonnet)
**Tag taxonomy and standardization specialist**

**Core Responsibilities:**
- Normalize technology names (e.g., "langchain" → "LangChain")
- Apply hierarchical tag structure (`ai/agents`, `business/client-work`)
- Consolidate duplicate tags
- Generate tag usage analysis reports
- Maintain master Tag Taxonomy document

**Use When:**
- Tags are inconsistent across vault
- Multiple variations of same tag exist
- Need hierarchical organization
- New tag categories emerge

**Deliverables:**
- Standardized tags following taxonomy
- Tag analysis reports
- Updated Tag Taxonomy document
- Hierarchical tag structure (max 3 levels)

**Standardization Rules:**
```
Technology Names:
- LangChain (not langchain)
- OpenAI (not openai)
- PostgreSQL (not postgres)

Hierarchical Paths:
- Use forward slashes: ai/agents
- No trailing slashes
- Maximum 3 levels deep

Naming Conventions:
- Lowercase for categories
- Proper case for product names
- Hyphens for multi-word: client-work
```

---

### metadata-agent (Sonnet)
**Frontmatter and metadata management**

**Core Responsibilities:**
- Add standardized frontmatter to files
- Extract creation dates from filesystem
- Generate tags based on directory/content
- Determine appropriate file types
- Ensure consistency across vault

**Use When:**
- Files missing frontmatter
- Inconsistent metadata fields
- Need bulk metadata updates
- Standardizing new imports

**Deliverables:**
- Complete frontmatter for all files
- Consistent metadata structure
- Creation/modification timestamps
- Proper type and status fields

**Metadata Standards:**
```yaml
---
tags:
  - category/subcategory
type: note|reference|moc|daily-note|template|system
created: YYYY-MM-DD
modified: YYYY-MM-DD
status: active|archive|draft
---
```

---

### content-curator (Sonnet)
**Content quality and organization specialist**

**Core Responsibilities:**
- Identify outdated or redundant content
- Suggest content improvements
- Consolidate similar notes
- Maintain content quality standards
- Archive inactive content

**Use When:**
- Vault has duplicate content
- Content quality review needed
- Old content needs archiving
- Similar notes should be merged

**Deliverables:**
- Content consolidation recommendations
- Quality improvement suggestions
- Archive candidates list
- Merged/improved notes

---

### connection-agent (Sonnet)
**Link analysis and relationship management**

**Core Responsibilities:**
- Analyze vault knowledge graph
- Identify orphaned notes (no incoming links)
- Suggest relevant connections between notes
- Find broken links
- Recommend bidirectional linking

**Use When:**
- Notes lack connections
- Finding related content
- Identifying isolated notes
- Building knowledge graph
- Linking new notes to existing content

**Deliverables:**
- Orphaned note lists
- Connection suggestions with rationale
- Broken link reports
- Graph analysis insights
- Bidirectional link recommendations

---

### vault-optimizer (Sonnet)
**Performance and storage optimization**

**Core Responsibilities:**
- Analyze vault performance metrics
- Identify oversized files (>1MB markdown)
- Compress and optimize images
- Remove unused attachments
- Improve search indexing
- Calculate storage usage

**Use When:**
- Vault feels slow
- Search performance degrades
- Storage cleanup needed
- Large file management
- Monthly maintenance

**Deliverables:**
- Performance audit reports
- Storage usage breakdown
- Optimization recommendations
- Compressed images (85% JPEG quality)
- Removed orphaned attachments

**Optimization Standards:**
- Maximum markdown file: 1MB
- Image compression: 85% quality (JPEG)
- PNG: Lossless compression
- Archive content older than 2 years
- Maintain 90%+ search performance

---

### review-agent (Sonnet)
**Quality assurance and validation**

**Core Responsibilities:**
- Cross-check enhancement work
- Validate consistency across vault
- Ensure quality standards met
- Review agent outputs
- Verify link integrity

**Use When:**
- After bulk operations
- Validating other agent work
- Ensuring quality standards
- Final review before completion

**Deliverables:**
- Quality assurance reports
- Inconsistency identification
- Validation checklists
- Error detection

## Common Workflows

### New Content Organization
```
moc-agent → tag-agent → metadata-agent → connection-agent
```
1. Create MOCs for new content areas
2. Standardize tags
3. Add/update frontmatter
4. Suggest connections to existing notes

### Monthly Vault Maintenance
```
vault-optimizer → tag-agent → metadata-agent → review-agent
```
1. Performance audit and cleanup
2. Tag standardization
3. Metadata consistency check
4. Final quality review

### Knowledge Graph Enhancement
```
connection-agent → content-curator → moc-agent
```
1. Identify orphans and suggest links
2. Consolidate similar content
3. Create MOCs for new clusters

### Content Import Workflow
```
metadata-agent → tag-agent → connection-agent → moc-agent
```
1. Add frontmatter to imported files
2. Standardize tags
3. Link to existing content
4. Create/update relevant MOCs

### Quarterly Deep Clean
```
vault-optimizer → content-curator → tag-agent → metadata-agent → review-agent
```
1. Storage and performance optimization
2. Archive old/consolidate content
3. Clean up tag taxonomy
4. Ensure metadata consistency
5. Final validation

## Integration with Vault

### PARA Method Support
These agents help maintain PARA organization:
- **moc-agent**: Creates MOCs for each PARA category
- **tag-agent**: Ensures tags align with PARA structure
- **content-curator**: Moves content between PARA folders as needed
- **metadata-agent**: Sets proper `type` field for categorization

### Obsidian Plugin Integration
Works with installed plugins:
- **Smart Connections**: Uses graph data for connection-agent
- **Dataview**: Queries enhanced by proper metadata-agent frontmatter
- **Local REST API**: Enables programmatic vault access
- **Graph Analysis**: Powered by connection-agent insights

### Automation Scripts
Some agents reference Python scripts (from VAULT01 system):
- `moc_generator.py` - MOC creation automation
- `tag_standardizer.py` - Tag normalization
- `metadata_adder.py` - Bulk frontmatter addition

**Note**: Script paths may need adjustment for your vault location.

## Best Practices

### 1. Regular Maintenance Schedule
- **Daily**: Quick review-agent check after changes
- **Weekly**: tag-agent + metadata-agent standardization
- **Monthly**: Full vault-optimizer performance review
- **Quarterly**: Deep clean with content-curator

### 2. Order of Operations
Run agents in this sequence for best results:
1. **vault-optimizer** - Clean foundation
2. **metadata-agent** - Ensure all files have frontmatter
3. **tag-agent** - Standardize taxonomy
4. **connection-agent** - Build relationships
5. **moc-agent** - Create navigation
6. **content-curator** - Quality improvements
7. **review-agent** - Final validation

### 3. Backup Before Bulk Operations
Always backup before running:
- vault-optimizer (file deletions)
- tag-agent (bulk tag changes)
- metadata-agent (frontmatter modifications)
- content-curator (content merging)

### 4. Incremental Changes
- Start with `--dry-run` or `--report` modes
- Review outputs before applying
- Test on small sections first
- Monitor impact on vault performance

### 5. Preserve User Organization
Agents respect:
- Existing folder structure
- User-created links
- Manual categorization choices
- Custom frontmatter fields

## Agent Selection Guide

| I want to... | Use this agent |
|--------------|----------------|
| Create navigation hubs | `moc-agent` |
| Organize orphaned images | `moc-agent` |
| Fix inconsistent tags | `tag-agent` |
| Add missing frontmatter | `metadata-agent` |
| Find related notes | `connection-agent` |
| Identify orphaned content | `connection-agent` |
| Speed up slow vault | `vault-optimizer` |
| Reduce storage usage | `vault-optimizer` |
| Consolidate similar notes | `content-curator` |
| Archive old content | `content-curator` |
| Validate recent changes | `review-agent` |
| Clean up after imports | `metadata-agent` → `tag-agent` |
| Monthly maintenance | Run all in sequence |

## Performance Notes

All agents use **Sonnet model** for:
- Cost efficiency on bulk operations
- Fast execution for maintenance tasks
- Sufficient reasoning for organizational decisions

## Directory Structure

```
obsidian-operations/
├── README.md                # This file
├── connection-agent.md      # Link analysis & suggestions
├── content-curator.md       # Content quality & organization
├── metadata-agent.md        # Frontmatter management
├── moc-agent.md            # Map of Content creation
├── review-agent.md         # Quality assurance
├── tag-agent.md            # Tag taxonomy standardization
└── vault-optimizer.md      # Performance optimization
```

## Contributing

When adding new Obsidian operation agents:

1. Use YAML frontmatter: `name`, `description`, `tools`, `model: sonnet`
2. Include "Use PROACTIVELY" if agent should auto-suggest
3. Document integration with existing agents
4. Specify when to use vs similar agents
5. Update this README.md
6. Update parent `.claude/agents/README.md`

---

**Note**: This README serves as human documentation. Individual agent files (e.g., `moc-agent.md`) are automatically loaded by the Claude Agent SDK.
