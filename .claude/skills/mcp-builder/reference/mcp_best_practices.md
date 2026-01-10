# MCP Server Best Practices

## Tool Design

### Naming Convention

Use `{service}_{action}_{target}` pattern:

| Good | Bad |
|------|-----|
| `research_search_papers` | `searchPapers` |
| `vault_find_orphans` | `findOrphans` |
| `zotero_get_citations` | `getCitations` |

- Use snake_case
- Include service prefix to prevent conflicts
- Be action-oriented and specific
- Never include version numbers

### Tool Granularity

**Balance coverage vs specialization:**

| Approach | When to Use |
|----------|-------------|
| Fine-grained (one action per tool) | General-purpose APIs, unknown use cases |
| Coarse-grained (workflow tools) | Known workflows, reducing API calls |

When uncertain, prefer more granular tools - they're more composable.

### Tool Descriptions

Write descriptions that help Claude understand:
1. What the tool does
2. When to use it
3. What it returns

```python
@mcp.tool()
async def research_search_papers(params: SearchInput) -> str:
    """
    Search for academic papers across multiple sources.

    Use this when the user wants to find papers on a topic,
    gather literature for a review, or explore research areas.

    Returns paper metadata including title, authors, abstract,
    publication year, and citation count. Use the 'format' parameter
    to get JSON for processing or Markdown for display.
    """
```

## Response Design

### Dual Format Support

Always support both JSON and Markdown:

```python
format: Literal["json", "markdown"] = Field(
    default="markdown",
    description="json for structured data, markdown for display"
)
```

**JSON**: Complete data, machine-readable, for chaining tools
**Markdown**: Human-friendly, formatted timestamps, readable names

### Context Management

Return focused data, not everything:

```python
# Good - selective fields
fields: list[str] = Field(
    default=["title", "authors", "abstract", "year"],
    description="Fields to include in response"
)

# Good - reasonable defaults
limit: int = Field(default=20, le=100)
```

### Pagination

Required for list operations:

```python
class PaginatedResponse(BaseModel):
    items: list[Item]
    has_more: bool           # More results available?
    next_offset: int | None  # Offset for next page
    total_count: int         # Total matching items

# Never load all results into memory
# Default to 20-50 items
# Respect user-defined limits
```

## Error Handling

### Helpful Error Messages

Errors should guide toward solutions:

```python
# Bad
"Error: 404"

# Good
"Paper not found. The ID 'abc123' doesn't exist. Try searching for the paper by title instead."

# Bad
"API error"

# Good
"Rate limit exceeded (429). The Semantic Scholar API allows 100 requests per 5 minutes. Wait 30 seconds and try again."
```

### Error Categories

```python
def handle_error(e: Exception) -> str:
    if isinstance(e, HTTPError):
        return handle_http_error(e)
    if isinstance(e, ValidationError):
        return f"Invalid input: {e.message}. Check the parameter format."
    if isinstance(e, TimeoutError):
        return "Request timed out. The service may be slow. Try again or reduce the scope."
    return f"Unexpected error: {str(e)}"

def handle_http_error(e: HTTPError) -> str:
    messages = {
        400: "Bad request. Check parameter values.",
        401: "Authentication failed. Verify your API key.",
        403: "Access denied. You may lack permissions.",
        404: "Resource not found. Verify the ID exists.",
        429: "Rate limited. Wait and retry.",
        500: "Server error. Try again later.",
    }
    return messages.get(e.status_code, f"HTTP {e.status_code}: {e.message}")
```

## Tool Annotations

Provide hints about tool behavior:

```python
@mcp.tool(
    name="research_search_papers",
    annotations={
        "readOnlyHint": True,      # Doesn't modify data
        "destructiveHint": False,  # Doesn't delete anything
        "idempotentHint": True,    # Same result on repeat
        "openWorldHint": True      # Accesses external services
    }
)
```

| Annotation | When True |
|------------|-----------|
| `readOnlyHint` | Tool only reads, never writes |
| `destructiveHint` | Tool deletes or overwrites data |
| `idempotentHint` | Repeated calls produce same result |
| `openWorldHint` | Tool accesses external services |

## Security

### Authentication

```python
import os

# Always use environment variables
api_key = os.environ.get("SERVICE_API_KEY")
if not api_key:
    raise ValueError("SERVICE_API_KEY environment variable required")

# Never log or return API keys
# Use OAuth 2.1 for user-delegated access
```

### Input Sanitization

```python
from pydantic import Field, field_validator
import re

class FileInput(BaseModel):
    path: str = Field(..., description="File path")

    @field_validator("path")
    @classmethod
    def sanitize_path(cls, v: str) -> str:
        # Prevent path traversal
        if ".." in v or v.startswith("/"):
            raise ValueError("Invalid path: no traversal or absolute paths")
        # Normalize
        return v.strip()
```

### Rate Limiting

```python
import asyncio
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = timedelta(seconds=window_seconds)
        self.requests: list[datetime] = []

    async def acquire(self):
        now = datetime.now()
        # Remove old requests
        self.requests = [r for r in self.requests if now - r < self.window]
        if len(self.requests) >= self.max_requests:
            wait_time = (self.requests[0] + self.window - now).total_seconds()
            raise RateLimitError(f"Rate limited. Wait {wait_time:.0f} seconds.")
        self.requests.append(now)
```

## Code Quality

### No Duplication

```python
# Bad - copy-pasted logic
@mcp.tool()
async def get_paper(params: GetPaperInput) -> str:
    response = await client.get(f"/papers/{params.id}")
    if response.status_code == 404:
        return "Paper not found"
    return format_paper(response.json())

@mcp.tool()
async def get_author(params: GetAuthorInput) -> str:
    response = await client.get(f"/authors/{params.id}")
    if response.status_code == 404:
        return "Author not found"
    return format_author(response.json())

# Good - shared abstraction
async def get_resource(path: str, formatter: Callable) -> str:
    response = await client.get(path)
    if response.status_code == 404:
        return f"Resource not found at {path}"
    return formatter(response.json())

@mcp.tool()
async def get_paper(params: GetPaperInput) -> str:
    return await get_resource(f"/papers/{params.id}", format_paper)
```

### Async Everywhere

```python
# All I/O must be async
async def fetch_data() -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

# Use asyncio.gather for parallel requests
results = await asyncio.gather(
    fetch_papers(query1),
    fetch_papers(query2),
    fetch_papers(query3)
)
```

### Type Everything

```python
from typing import TypedDict, Literal

class Paper(TypedDict):
    id: str
    title: str
    authors: list[str]
    year: int
    abstract: str
    citation_count: int

async def search_papers(
    query: str,
    limit: int = 20
) -> list[Paper]:
    ...
```

## Testing

### MCP Inspector

```bash
# Install
npm install -g @modelcontextprotocol/inspector

# Run against your server
npx @modelcontextprotocol/inspector python -m my_mcp.server
```

### Unit Tests

```python
import pytest
from my_mcp.server import search_papers, SearchInput

@pytest.mark.asyncio
async def test_search_papers_returns_results():
    params = SearchInput(query="machine learning", limit=5)
    result = await search_papers(params)
    assert "papers" in result or "Found" in result

@pytest.mark.asyncio
async def test_search_papers_handles_empty_query():
    with pytest.raises(ValidationError):
        SearchInput(query="", limit=5)
```

### Integration Tests

```python
@pytest.mark.asyncio
async def test_full_workflow():
    # Search -> Get details -> Format
    search_result = await search_papers(SearchInput(query="transformers"))
    paper_id = extract_first_id(search_result)
    details = await get_paper(GetPaperInput(id=paper_id))
    assert "title" in details.lower()
```
