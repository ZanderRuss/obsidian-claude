# Research Agent SDK Implementation Plan

## Overview

Build a Python Agent SDK application that provides autonomous research capabilities to Claude Desktop users via MCP. The system will integrate with existing Obsidian vault, Zotero library, and PaperQA2 for comprehensive research automation.

**Target Users**: PhD researchers using Claude Desktop + Obsidian + MCP

**Goal**: Create intelligent agents that automate literature search, knowledge graph management, and paper writing assistance.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      Claude Desktop                              │
│                   (User's chat interface)                        │
└────────────────────────────┬────────────────────────────────────┘
                             │ MCP Protocol
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              Research Agent MCP Server                           │
│                 (Python Agent SDK)                               │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                   Agent Orchestrator                      │   │
│  │            (Routes requests to specialized agents)        │   │
│  └──────────────────────────────────────────────────────────┘   │
│                             │                                    │
│     ┌───────────────────────┼───────────────────────┐           │
│     │                       │                       │           │
│     ▼                       ▼                       ▼           │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────────┐   │
│  │  Literature │     │  Knowledge  │     │  Paper Writing  │   │
│  │    Agent    │     │ Graph Agent │     │      Agent      │   │
│  └──────┬──────┘     └──────┬──────┘     └────────┬────────┘   │
│         │                   │                      │            │
└─────────┼───────────────────┼──────────────────────┼────────────┘
          │                   │                      │
          ▼                   ▼                      ▼
    ┌──────────┐       ┌──────────┐          ┌──────────┐
    │ External │       │ Obsidian │          │  Local   │
    │   APIs   │       │ REST API │          │  Files   │
    ├──────────┤       └──────────┘          └──────────┘
    │ Zotero   │
    │ Semantic │
    │ Scholar  │
    │ arXiv    │
    │ PaperQA2 │
    └──────────┘
```

---

## Project Structure

```
research-agents/
├── pyproject.toml              # Project config & dependencies
├── requirements.txt            # Pip requirements
├── .env.example                # Environment template
├── .gitignore
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── main.py                 # MCP server entry point
│   ├── config.py               # Configuration management
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py             # Base agent class
│   │   ├── orchestrator.py     # Agent coordinator
│   │   ├── literature.py       # Literature Agent
│   │   ├── knowledge_graph.py  # Knowledge Graph Agent
│   │   └── paper_writing.py    # Paper Writing Agent (Phase 3)
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── zotero.py           # Zotero integration
│   │   ├── semantic_scholar.py # Semantic Scholar API
│   │   ├── arxiv.py            # arXiv API
│   │   ├── paperqa.py          # PaperQA2 wrapper
│   │   ├── obsidian.py         # Obsidian REST API
│   │   └── embeddings.py       # Embedding generation
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── paper.py            # Paper data model
│   │   ├── note.py             # Note data model
│   │   └── graph.py            # Knowledge graph model
│   │
│   └── utils/
│       ├── __init__.py
│       ├── markdown.py         # Markdown generation
│       └── cache.py            # Caching utilities (JSON-based)
│
├── tests/
│   ├── __init__.py
│   ├── test_literature.py
│   ├── test_knowledge_graph.py
│   └── test_tools.py
│
└── examples/
    ├── basic_search.py
    └── full_workflow.py
```

---

## Phase 1: Literature Agent

### Overview

An autonomous agent that searches, retrieves, and processes academic literature, creating structured notes in Obsidian.

### Capabilities

| Capability | Description | Tools Used |
|------------|-------------|------------|
| **Search** | Find papers across multiple sources | Zotero, Semantic Scholar, arXiv |
| **Retrieve** | Get full paper metadata and PDFs | Zotero, API downloads |
| **Process** | Extract key information from papers | PaperQA2 |
| **Summarize** | Generate structured literature notes | Claude Agent SDK |
| **Store** | Create notes in Obsidian vault | Obsidian REST API |

### MCP Tools Exposed

```python
@mcp_tool
def search_literature(
    query: str,
    sources: list[str] = ["zotero", "semantic_scholar", "arxiv"],
    limit: int = 20,
    date_range: str = "last_5_years"
) -> list[PaperResult]:
    """Search for papers across multiple sources."""

@mcp_tool
def get_paper_details(paper_id: str, source: str) -> PaperMetadata:
    """Get full metadata for a specific paper."""

@mcp_tool
def process_paper(
    paper_id: str,
    extract: list[str] = ["summary", "methods", "findings"]
) -> PaperAnalysis:
    """Process a paper and extract key information using PaperQA2."""

@mcp_tool
def create_literature_note(
    paper_id: str,
    template: str = "Template - Literature Note"
) -> str:
    """Create a literature note in Obsidian from paper analysis."""

@mcp_tool
def batch_process_papers(
    query: str,
    max_papers: int = 10,
    auto_create_notes: bool = True
) -> BatchResult:
    """Search, process, and create notes for multiple papers."""

@mcp_tool
def find_related_papers(
    paper_id: str,
    relationship: str = "citations",
    limit: int = 10
) -> list[PaperResult]:
    """Find papers related to a given paper."""
```

### Implementation Highlights

#### Zotero Integration
```python
class ZoteroTool:
    """Wrapper for existing Zotero MCP."""
    async def search(self, query: str, limit: int = 20) -> list[dict]
    async def get_item(self, item_id: str) -> dict
    async def get_pdf_path(self, item_id: str) -> Path
```

#### Semantic Scholar API
```python
class SemanticScholarTool:
    """Semantic Scholar API integration."""
    BASE_URL = "https://api.semanticscholar.org/graph/v1"
    async def search(self, query: str, limit: int = 20) -> list[dict]
    async def get_citations(self, paper_id: str) -> list[dict]
```

#### PaperQA2 Wrapper
```python
class PaperQATool:
    """PaperQA2 integration for paper analysis."""
    async def add_paper(self, pdf_path: Path) -> str
    async def ask(self, question: str) -> dict
    async def summarize_paper(self, pdf_path: Path) -> dict
```

---

## Phase 2: Knowledge Graph Agent

### Overview

An agent that monitors the Obsidian vault, analyzes note relationships, suggests connections, and maintains Maps of Content (MOCs).

### Capabilities

| Capability | Description | Tools Used |
|------------|-------------|------------|
| **Analyze** | Understand vault structure and content | Obsidian REST API |
| **Embed** | Generate embeddings for semantic search | Sentence Transformers |
| **Connect** | Find and suggest note connections | Embeddings + Claude |
| **Maintain** | Update MOCs and fix broken links | Obsidian REST API |

### MCP Tools Exposed

```python
@mcp_tool
def analyze_vault(focus_folders: list[str] = None) -> VaultAnalysis:
    """Analyze vault structure, orphans, and connection density."""

@mcp_tool
def find_connections(
    note_path: str,
    threshold: float = 0.7,
    limit: int = 10
) -> list[ConnectionSuggestion]:
    """Find semantically similar notes that should be linked."""

@mcp_tool
def update_moc(moc_path: str, auto_add: bool = False) -> MOCUpdate:
    """Analyze and update a Map of Content."""

@mcp_tool
def find_orphans(folder: str = None, min_age_days: int = 7) -> list[OrphanNote]:
    """Find notes with no incoming or outgoing links."""

@mcp_tool
def generate_moc(topic: str, source_folders: list[str] = None) -> str:
    """Generate a new Map of Content for a topic."""

@mcp_tool
def fix_broken_links(folder: str = None, auto_fix: bool = False) -> list[BrokenLink]:
    """Find and optionally fix broken wiki links."""
```

### Embeddings Cache (JSON-based for security)

```python
import json
import numpy as np
from pathlib import Path

class EmbeddingCache:
    """JSON-based embedding cache (safe serialization)."""

    def __init__(self, cache_path: Path):
        self.cache_path = cache_path
        self.cache = self._load()

    def _load(self) -> dict:
        if self.cache_path.exists():
            with open(self.cache_path, "r") as f:
                data = json.load(f)
                # Convert lists back to numpy arrays
                return {k: np.array(v) for k, v in data.items()}
        return {}

    def _save(self):
        # Convert numpy arrays to lists for JSON serialization
        data = {k: v.tolist() for k, v in self.cache.items()}
        with open(self.cache_path, "w") as f:
            json.dump(data, f)

    def get(self, key: str) -> np.ndarray | None:
        return self.cache.get(key)

    def set(self, key: str, embedding: np.ndarray):
        self.cache[key] = embedding
        self._save()
```

---

## Integration with Existing Setup

### MCP Configuration

Add to `.claude/mcp.json`:

```json
{
  "mcpServers": {
    "obsidian": { ... },
    "zotero": { ... },
    "research-agents": {
      "command": "python",
      "args": ["-m", "research_agents.main"],
      "env": {
        "OBSIDIAN_API_KEY": "your-api-key",
        "ANTHROPIC_API_KEY": "your-anthropic-key"
      }
    }
  }
}
```

---

## Development Timeline

### Phase 1: Literature Agent (Week 1-2)

| Task | Effort |
|------|--------|
| Project setup with Agent SDK | 2h |
| Zotero + Semantic Scholar tools | 8h |
| PaperQA2 wrapper | 6h |
| Literature Agent implementation | 8h |
| Obsidian note creation | 4h |
| MCP server setup | 4h |
| Testing & docs | 8h |

### Phase 2: Knowledge Graph Agent (Week 3-4)

| Task | Effort |
|------|--------|
| Obsidian API wrapper | 4h |
| Embedding tool (JSON cache) | 6h |
| Vault analysis | 6h |
| Connection suggestions | 8h |
| MOC generation | 6h |
| Testing & docs | 6h |

---

## Success Metrics

- [ ] Literature search across 3+ sources in <5 seconds
- [ ] Properly formatted literature notes created
- [ ] PaperQA2 answers with source citations
- [ ] Vault analysis completes in <30 seconds
- [ ] Connection suggestions with >70% relevance
- [ ] Works reliably via Claude Desktop

---

## Next Steps

1. [ ] Review and approve this plan
2. [ ] Set up development environment
3. [ ] Create project scaffold with `/new-sdk-app`
4. [ ] Implement Phase 1
5. [ ] Test with real vault
6. [ ] Implement Phase 2
7. [ ] Document and deploy
