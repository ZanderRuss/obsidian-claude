# Claude Code Hooks

Hooks are Python scripts that run automatically in response to Claude's actions. They provide validation, transformation, and enforcement without manual intervention.

## Available Hooks (3)

| Hook | Trigger | Purpose |
|------|---------|---------|
| `obsidian-markdown.py` | Write tool | Convert standard markdown to Obsidian format |
| `conventional-commits.py` | Bash (git commit) | Validate commit message format |
| `research-quality-gate.py` | Write tool | Enforce citation requirements |

---

## Obsidian Markdown Converter

**File:** `obsidian-markdown.py`

**Trigger:** Runs on every `Write` tool call to vault files

**What it does:**

Automatically converts standard markdown to Obsidian Flavored Markdown:

| Standard Markdown | Obsidian Markdown |
|-------------------|-------------------|
| `[text](file.md)` | `[[file\|text]]` |
| `![alt](image.png)` | `![[image.png]]` |
| `> Note:` | `> [!note]` |
| (missing frontmatter) | Adds tags, type, created, status |

**Path patterns:**

Only processes files in these locations:

- `Obsidian-Vault-Live`
- `0. Inbox`
- `1. Projects`
- `2. Areas`
- `3. Resources`
- `4. Archive`
- `6. Metadata`

**Usage:** Automatic - paste research in any format and it auto-converts.

---

## Conventional Commits

**File:** `conventional-commits.py`

**Trigger:** Runs on `Bash` tool calls containing `git commit`

**What it does:**

Validates commit messages follow conventional commit format:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Allowed types:**

| Type | Purpose |
|------|---------|
| `feat` | New features |
| `fix` | Bug fixes |
| `docs` | Documentation changes |
| `style` | Formatting, whitespace |
| `refactor` | Code restructuring |
| `perf` | Performance improvements |
| `test` | Adding or updating tests |
| `build` | Build system changes |
| `ci` | CI/CD configuration |
| `chore` | Maintenance tasks |
| `revert` | Reverting previous commits |

**Example valid commits:**

```bash
git commit -m "feat: add user authentication"
git commit -m "fix(api): resolve rate limiting bug"
git commit -m "docs: update installation guide"
```

---

## Research Quality Gate

**File:** `research-quality-gate.py`

**Trigger:** Runs on `Write` tool calls to research phase files

**What it does:**

Enforces academic quality standards for Complete Research Track files:

### Phase 3: Synthesis (`30-synthesis`)

**Requirements:**

- Must contain at least one citation
- Cannot contain `[citation needed]` markers

**Recognized citation formats:**

- `[@citekey]` — BibTeX style
- `(Author, 2024)` — APA-like
- `[1]` — Numbered references
- `[[Paper - ...]]` — Obsidian literature links
- `et al.` — Academic citation indicator

### Phase 4: Draft (`40-draft`)

**Requirements:**

- Must have a References section
- Cannot contain `[unsupported]` markers

### Bypassing Quality Gates

If you need to save work-in-progress that fails gates:

1. **Rename the file** — Save as `30-synthesis-WIP.md` instead
2. Quality gates only apply to standard phase file names
3. Rename back when ready for final version

---

## How Hooks Work

Hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/obsidian-markdown.py"
          },
          {
            "type": "command",
            "command": "python .claude/hooks/research-quality-gate.py"
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/conventional-commits.py"
          }
        ]
      }
    ]
  }
}
```

### Hook Lifecycle

1. Claude decides to use a tool (Write, Bash, etc.)
2. `PreToolUse` hooks run with tool input as stdin
3. Hook can:
   - **Pass silently** — Return `{"result": "continue"}`
   - **Block action** — Return `{"result": "block", "reason": "..."}`
   - **Modify input** — Return modified tool input
4. Tool executes (if not blocked)
5. `PostToolUse` hooks run with result

### Creating New Hooks

1. Create a Python file in `.claude/hooks/`
2. Read JSON input from stdin
3. Process and return JSON result
4. Register in `.claude/settings.json`

**Template:**

```python
#!/usr/bin/env python3
import json
import sys

def main():
    try:
        input_data = json.loads(sys.stdin.read())
        tool_input = input_data.get("tool_input", {})

        # Your validation/transformation logic here

        # Pass through
        print(json.dumps({"result": "continue"}))

        # Or block
        # print(json.dumps({"result": "block", "reason": "Why it was blocked"}))

        # Or modify
        # print(json.dumps(tool_input))

    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

## Troubleshooting

### Hook not running

1. Check file path matches pattern in settings.json
2. Verify Python is available in PATH
3. Check hook file has no syntax errors: `python -m py_compile hookfile.py`
4. Restart Claude Code after config changes

### Quality gate blocking valid content

1. Verify citation format matches recognized patterns
2. Check for hidden `[citation needed]` text
3. Use WIP filename to bypass temporarily

### Obsidian conversion not working

1. Verify file path includes vault folder name
2. Check file ends with `.md`
3. Look for conversion errors in hook output

---

## Files

```text
.claude/hooks/
├── README.md                    # This file
├── conventional-commits.py      # Commit message validation
├── obsidian-markdown.py         # Markdown format conversion
└── research-quality-gate.py     # Research citation enforcement
```
