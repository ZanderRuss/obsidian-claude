# Python MCP Server Implementation Guide

## Framework: FastMCP

Use FastMCP from the official MCP Python SDK. It provides:
- Automatic schema generation from function signatures
- Pydantic model integration for input validation
- Decorator-based tool registration

## Project Structure

```text
my_mcp_server/
├── pyproject.toml
├── .env.example
├── README.md
├── src/
│   └── my_mcp/
│       ├── __init__.py
│       ├── server.py          # FastMCP server + tool definitions
│       ├── api_client.py      # External API wrapper
│       ├── models.py          # Pydantic input/output models
│       ├── formatters.py      # Response formatting (JSON/Markdown)
│       └── utils.py           # Shared utilities
└── tests/
    └── test_server.py
```

## Server Initialization

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Name follows {service}_mcp pattern
mcp = FastMCP("research_mcp")
```

## Tool Definition Pattern

```python
from pydantic import BaseModel, Field
from typing import Literal

class SearchPapersInput(BaseModel):
    """Input model with Pydantic v2 features."""

    model_config = {"extra": "forbid"}  # Reject unknown fields

    query: str = Field(
        ...,  # Required
        description="Search query for papers",
        min_length=1,
        max_length=500
    )
    sources: list[Literal["arxiv", "semantic_scholar", "web"]] = Field(
        default=["arxiv", "semantic_scholar"],
        description="Sources to search"
    )
    limit: int = Field(
        default=20,
        ge=1,
        le=100,
        description="Maximum number of results"
    )
    offset: int = Field(
        default=0,
        ge=0,
        description="Offset for pagination"
    )
    format: Literal["json", "markdown"] = Field(
        default="markdown",
        description="Response format"
    )


@mcp.tool(
    name="research_search_papers",
    annotations={
        "readOnlyHint": True,
        "openWorldHint": True
    }
)
async def search_papers(params: SearchPapersInput) -> str:
    """
    Search for academic papers across multiple sources.

    Returns papers matching the query with title, authors,
    abstract, and citation count.
    """
    try:
        results = await api_client.search(
            query=params.query,
            sources=params.sources,
            limit=params.limit,
            offset=params.offset
        )
        return format_response(results, params.format)
    except APIError as e:
        return handle_error(e)
```

## Input Validation with Pydantic v2

```python
from pydantic import BaseModel, Field, field_validator
from typing import Annotated

class CreateNoteInput(BaseModel):
    model_config = {"extra": "forbid"}

    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    folder: str = Field(default="0. Inbox")
    tags: list[str] = Field(default_factory=list)

    @field_validator("folder")
    @classmethod
    def validate_folder(cls, v: str) -> str:
        valid_folders = ["0. Inbox", "1. Projects", "2. Areas", "3. Resources"]
        if v not in valid_folders:
            raise ValueError(f"Invalid folder. Choose from: {valid_folders}")
        return v

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, v: list[str]) -> list[str]:
        return [tag.lower().replace(" ", "-") for tag in v]
```

## Response Formatting

```python
# formatters.py
import json
from datetime import datetime
from typing import Any

def format_response(data: dict, format: str = "markdown") -> str:
    """Format response as JSON or Markdown."""
    if format == "json":
        return json.dumps(data, indent=2, default=str)
    return format_as_markdown(data)

def format_as_markdown(data: dict) -> str:
    """Human-readable markdown formatting."""
    lines = []

    if "papers" in data:
        lines.append(f"## Found {len(data['papers'])} papers\n")
        for i, paper in enumerate(data["papers"], 1):
            lines.append(f"### {i}. {paper['title']}")
            lines.append(f"**Authors**: {', '.join(paper['authors'])}")
            lines.append(f"**Year**: {paper['year']}")
            lines.append(f"**Citations**: {paper['citation_count']}")
            lines.append(f"\n{paper['abstract'][:300]}...\n")

    if data.get("has_more"):
        lines.append(f"\n*{data['total_count'] - len(data['papers'])} more results available*")

    return "\n".join(lines)

def format_timestamp(ts: str | datetime) -> str:
    """Convert timestamp to readable format."""
    if isinstance(ts, str):
        ts = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    return ts.strftime("%B %d, %Y at %I:%M %p")
```

## Pagination Pattern

```python
from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    has_more: bool
    next_offset: int | None
    total_count: int

    @classmethod
    def from_results(
        cls,
        items: list[T],
        offset: int,
        limit: int,
        total: int
    ) -> "PaginatedResponse[T]":
        has_more = offset + len(items) < total
        return cls(
            items=items,
            has_more=has_more,
            next_offset=offset + limit if has_more else None,
            total_count=total
        )
```

## Error Handling

```python
# utils.py
from typing import Any

class MCPError(Exception):
    """Base error with helpful message."""
    def __init__(self, message: str, suggestion: str = None):
        self.message = message
        self.suggestion = suggestion
        super().__init__(message)

def handle_error(e: Exception) -> str:
    """Convert exceptions to helpful error messages."""
    if isinstance(e, MCPError):
        msg = f"Error: {e.message}"
        if e.suggestion:
            msg += f"\n\nSuggestion: {e.suggestion}"
        return msg

    if hasattr(e, "status_code"):
        status = e.status_code
        if status == 401:
            return "Authentication failed. Check your API key."
        if status == 403:
            return "Access denied. You may not have permission for this resource."
        if status == 404:
            return "Resource not found. Verify the ID or path exists."
        if status == 429:
            return "Rate limit exceeded. Wait a moment and try again."
        return f"API error ({status}): {str(e)}"

    return f"Unexpected error: {str(e)}"
```

## API Client Pattern

```python
# api_client.py
import httpx
from typing import Any

class APIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0
        )

    async def get(self, path: str, params: dict = None) -> dict:
        response = await self.client.get(path, params=params)
        response.raise_for_status()
        return response.json()

    async def post(self, path: str, data: dict) -> dict:
        response = await self.client.post(path, json=data)
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
```

## Context Injection (Optional)

```python
from mcp.server.fastmcp import FastMCP, Context

@mcp.tool()
async def long_running_task(params: TaskInput, ctx: Context) -> str:
    """Tool with progress reporting."""
    await ctx.report_progress(0, 100, "Starting...")

    for i, item in enumerate(params.items):
        await process_item(item)
        await ctx.report_progress(i + 1, len(params.items), f"Processing {item}")

    return "Complete"
```

## Running the Server

```python
# server.py (bottom of file)
if __name__ == "__main__":
    mcp.run()
```

```bash
# For Claude Desktop (stdio transport)
python -m my_mcp.server

# Or via uv
uv run python -m my_mcp.server
```

## pyproject.toml

```toml
[project]
name = "research-mcp"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "mcp>=1.0.0",
    "httpx>=0.27.0",
    "pydantic>=2.0.0",
]

[project.scripts]
research-mcp = "research_mcp.server:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## Claude Desktop Configuration

```json
{
  "mcpServers": {
    "research": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/research-mcp", "research-mcp"],
      "env": {
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}"
      }
    }
  }
}
```
