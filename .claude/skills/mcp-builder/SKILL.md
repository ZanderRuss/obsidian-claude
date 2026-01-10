# MCP Server Builder Skill

Build Model Context Protocol (MCP) servers that enable Claude to interact with external services through well-designed tools.

## When to Use

Use this skill when:
- Building a new MCP server for Claude Desktop integration
- Adding tools to an existing MCP server
- Reviewing MCP implementation for best practices

## Four-Phase Development Process

### Phase 1: Research & Planning

1. **Understand the API/Service**
   - Document available endpoints and capabilities
   - Identify authentication requirements
   - Map rate limits and pagination patterns

2. **Design Tool Surface**
   - Balance comprehensive coverage vs specialized workflows
   - Use action-oriented names with service prefix: `research_search_papers`
   - Plan context management (filtering, pagination)

3. **Choose Framework**
   - **Python**: Use FastMCP from official SDK
   - **TypeScript**: Use @modelcontextprotocol/sdk
   - **Transport**: stdio for local (Claude Desktop), HTTP for remote

### Phase 2: Implementation

Read reference docs before implementing:
- `reference/python_mcp_server.md` - Python patterns
- `reference/mcp_best_practices.md` - Design guidelines

Key patterns:
```python
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("research_mcp")

class SearchInput(BaseModel):
    query: str = Field(..., description="Search query")
    limit: int = Field(20, ge=1, le=100, description="Max results")

@mcp.tool(
    name="research_search_papers",
    annotations={"readOnlyHint": True}
)
async def search_papers(params: SearchInput) -> str:
    """Search for academic papers across multiple sources."""
    # Implementation
    pass
```

### Phase 3: Testing

1. Run syntax/type checks
2. Test with MCP Inspector: `npx @modelcontextprotocol/inspector`
3. Verify in Claude Desktop

### Phase 4: Evaluation

Create 10 test questions that:
- Require multiple tool calls
- Are independent and read-only
- Have verifiable answers

## Quick Reference

### Tool Naming
```
{service}_{action}_{target}
research_search_papers
research_get_citations
vault_find_orphans
```

### Tool Annotations
```python
annotations={
    "readOnlyHint": True,      # Doesn't modify state
    "destructiveHint": False,  # Doesn't delete data
    "idempotentHint": True,    # Same result on repeat
    "openWorldHint": True      # Interacts with external world
}
```

### Response Format
Support both JSON (structured) and Markdown (human-readable):
```python
def format_response(data: dict, format: str = "markdown") -> str:
    if format == "json":
        return json.dumps(data, indent=2)
    return format_as_markdown(data)
```

### Pagination
```python
class PaginatedResponse(BaseModel):
    items: list[Item]
    has_more: bool
    next_offset: int | None
    total_count: int
```

### Error Handling
```python
def handle_api_error(e: Exception) -> str:
    if isinstance(e, HTTPError):
        return f"API error {e.status_code}: {e.message}. Try: {suggestion}"
    return f"Unexpected error: {str(e)}"
```

## Resources

- MCP Specification: https://modelcontextprotocol.io
- Python SDK: https://github.com/modelcontextprotocol/python-sdk
- TypeScript SDK: https://github.com/modelcontextprotocol/typescript-sdk
- Official skills: https://github.com/anthropics/skills
