---
tags:
  - content/prompt
  - type/reference
  - topics/development
type: prompt
category: Development
description: Thorough code review with security and quality focus
cover: ""
created: 2025-01-11
modified: 2025-01-11
status: active
---

# Code Review

## Purpose

Get a comprehensive code review covering correctness, security, performance, and maintainability.

## Prompt

```
Please review this code:

```{language}
{code}
```

Focus on:
1. **Correctness**: Logic errors, edge cases, potential bugs
2. **Security**: Vulnerabilities (injection, XSS, etc.)
3. **Performance**: Inefficiencies, optimization opportunities
4. **Maintainability**: Readability, naming, structure
5. **Best Practices**: Language idioms, patterns

Context: {context}
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{language}` | Programming language | "python" |
| `{code}` | The code to review | Your code here |
| `{context}` | What the code does | "API endpoint for user auth" |

## Usage Notes

- Include surrounding context when possible
- Mention what frameworks/libraries are being used
- Specify if there are particular concerns you have
- Great before merging PRs or after major changes

## Examples

### Example 1: Python Function Review

**Input:**
````
Please review this code:

```python
def process_user_input(data):
    query = f"SELECT * FROM users WHERE name = '{data['name']}'"
    result = db.execute(query)
    return result
```

Focus on:
1. **Correctness**: Logic errors, edge cases, potential bugs
2. **Security**: Vulnerabilities (injection, XSS, etc.)
3. **Performance**: Inefficiencies, optimization opportunities
4. **Maintainability**: Readability, naming, structure
5. **Best Practices**: Language idioms, patterns

Context: Handles user search in web application
````

**Output:**
Claude will identify the SQL injection vulnerability and suggest parameterized queries.

## Related Prompts

- [[Debug Assistant]]
- [[Refactoring Guide]]
