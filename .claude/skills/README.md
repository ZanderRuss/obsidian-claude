# Claude Code Skills

This folder contains 18 skills that extend what Claude can do. Think of skills as specialized assistants - each one helps Claude do specific tasks better.

---

## How to Use Skills (The Easy Way)

**You don't need to install anything to use most skills.** Just type a command and Claude will help you.

### Step 1: Open Claude Code

Open your terminal or command prompt where Claude Code is running.

### Step 2: Type a Skill Command

Type a forward slash `/` followed by the skill name. For example:

```
/scientific-writing
```

Claude will then guide you through using that skill.

### Common Commands You Can Try Right Now

| Type This | What It Does |
|-----------|--------------|
| `/ai-search` | Search the web for current information |
| `/scientific-writing` | Help writing academic papers |
| `/literature-review` | Find and organize research papers |
| `/citation-management` | Create and format citations |
| `/statistical-analysis` | Help with statistics and data analysis |

---

## All Available Skills

### For Research & Academic Work

| Skill Name | What It Helps You Do |
|------------|---------------------|
| `/citation-management` | Find papers on Google Scholar and PubMed, create citations |
| `/literature-review` | Write systematic literature reviews |
| `/venue-templates` | Get templates for journals like Nature, IEEE, NeurIPS |
| `/scientific-writing` | Write better academic papers and manuscripts |
| `/scientific-slides` | Create presentation slides for talks |
| `/scientific-brainstorming` | Generate research ideas and hypotheses |
| `/scientific-critical-thinking` | Evaluate research methodology |

### For Data & Statistics

| Skill Name | What It Helps You Do |
|------------|---------------------|
| `/statistical-analysis` | Run statistical tests, regression, analysis |
| `/exploratory-data-analysis` | Explore and understand your data |
| `/seaborn` | Create statistical charts and graphs |
| `/plotly` | Create interactive visualizations |

### For Documents

| Skill Name | What It Helps You Do |
|------------|---------------------|
| `/docx` | Create and edit Word documents |
| `/xlsx` | Work with Excel spreadsheets |
| `/pdf-processing-pro` | Extract text from PDFs, fill forms |
| `/obsidian-markdown` | Write notes in Obsidian format |

### For Web Search

| Skill Name               | What It Helps You Do                                      |
|--------------------------|-----------------------------------------------------------|
| `/ai-search`             | Search the web using AI (works out of the box!)           |
| `/perplexity-search`     | AI-powered search with Perplexity models via OpenRouter   |

### For Developers

| Skill Name               | What It Helps You Do                                        |
|--------------------------|-------------------------------------------------------------|
| `/mcp-builder`           | Build MCP servers to connect Claude with external services |

---

## Web Search: How It Works

The easiest way to search the web is to just ask Claude:

> "Search the web for the latest research on CRISPR gene editing"

Claude will use its built-in web search - **no setup required**.

### Want to Use Your Own API?

If you have API keys from OpenAI, Google, or Anthropic, you can use those instead. See the detailed setup guide in:
```
.claude/skills/ai-search/references/provider_setup.md
```

---

## Advanced: Installing Python Tools (Optional)

Some skills have Python scripts that can do extra things (like searching PubMed directly). You only need to set this up if you want these advanced features.

### Do I Need This?

**No** - Most skills work without any installation. Only set this up if:
- You want to search PubMed/Google Scholar directly
- You want to validate citations automatically
- Claude specifically asks you to run a Python script

### Setup Steps (Windows)

1. **Open PowerShell** (search for "PowerShell" in Start menu)

2. **Navigate to your project folder:**
   ```powershell
   cd "d:\OneDrive\04_Projects\17_Obsidian-Claude"
   ```

3. **Activate the virtual environment:**
   ```powershell
   .\.venv\Scripts\activate
   ```
   You should see `(.venv)` appear at the start of your command line.

4. **Install the required packages:**
   ```powershell
   pip install -r .claude\skills\requirements.txt
   ```

5. **Done!** You can now use the Python scripts.

### Setup Steps (Mac/Linux)

1. **Open Terminal**

2. **Navigate to your project folder:**
   ```bash
   cd ~/path/to/17_Obsidian-Claude
   ```

3. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install the required packages:**
   ```bash
   pip install -r .claude/skills/requirements.txt
   ```

---

## Troubleshooting

### "Command not found" when typing a skill

Make sure you're typing the command in Claude Code, not in a regular terminal. The `/` commands only work when talking to Claude.

### Python script errors

If a Python script fails, make sure you:
1. Activated the virtual environment (see setup steps above)
2. Installed the requirements
3. Are running the command from the project folder

### Need more help?

Just ask Claude! Type something like:
> "Help me use the citation-management skill"

---

## Quick Reference Card

| I Want To... | Type This |
|--------------|-----------|
| Search the web | `/ai-search` or just ask Claude to search |
| Search with Perplexity | `/perplexity-search` |
| Write a paper | `/scientific-writing` |
| Find research papers | `/literature-review` or `/citation-management` |
| Create citations | `/citation-management` |
| Analyze data | `/statistical-analysis` |
| Make charts | `/seaborn` or `/plotly` |
| Work with Word docs | `/docx` |
| Work with Excel | `/xlsx` |
| Extract PDF text | `/pdf-processing-pro` |
| Write Obsidian notes | `/obsidian-markdown` |
| Build MCP servers | `/mcp-builder` |

---

## What's Installed

These Python packages are ready to use:
- **requests** - For connecting to websites
- **bibtexparser** - For working with citation files
- **biopython** - For searching PubMed medical database

You can install more packages later if needed - Claude will tell you when something extra is required.
