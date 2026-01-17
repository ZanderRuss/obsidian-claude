# Claude Code Skills

This folder contains **18 specialized skills** that extend Claude's capabilities for research, writing, data analysis, and document processing. Think of skills as expert assistants - each one helps Claude excel at specific tasks.

---

## Quick Start

### How to Use Skills

**You don't need to install anything to use most skills.** Just type a command and Claude will help you.

1. **Open Claude Code** in your terminal
2. **Type a skill command** with a forward slash `/`
3. **Follow Claude's guidance** to use the skill

**Example:**
```
/scientific-writing
```

Claude will guide you through using the skill for your specific task.

---

## All Skills by Category

### 📚 Research & Academic Writing

#### `/scientific-writing`

**Core skill for academic manuscripts.** Write research papers in IMRAD structure with proper citations (APA/AMA/Vancouver), figures/tables, and reporting guidelines (CONSORT/STROBE/PRISMA). Always outputs full paragraphs with flowing prose, never bullet points.


**Use when:**


- Writing journal articles, manuscripts, or papers
- Drafting sections: abstract, introduction, methods, results, discussion
- Following specific reporting guidelines (CONSORT, STROBE, PRISMA)
- Need verified citations from literature databases


**Features:**


- Two-stage process: outline with research-lookup, then flowing prose
- IMRAD structure (Introduction, Methods, Results, Discussion)
- Multiple citation formats (APA, AMA, Vancouver)
- Integration with research databases for verified citations

---

#### `/literature-review`
**Conduct systematic, comprehensive literature reviews.** Search multiple databases (PubMed, arXiv, bioRxiv, Semantic Scholar), synthesize findings thematically, verify citations, and generate professional markdown/PDF output.


**Use when:**

- Conducting systematic literature reviews for research or publication
- Writing meta-analyses or research synthesis
- Comprehensive literature searches across multiple domains
- Need professionally formatted output with verified citations


**Features:**

- Multi-database search (PubMed, arXiv, bioRxiv, Semantic Scholar)
- Citation verification and aggregation
- Thematic synthesis of findings
- Professional markdown and PDF output
- Multiple citation styles (APA, Nature, Vancouver)

---

#### `/citation-management`
**Find papers and manage citations.** Search Google Scholar and PubMed, extract metadata, validate citations, and generate BibTeX entries. Ensures citation accuracy and reproducibility.


**Use when:**

- Searching for specific papers on Google Scholar or PubMed
- Converting DOIs, PMIDs, or arXiv IDs to BibTeX
- Verifying citation accuracy before submission
- Building bibliography for manuscripts
- Need properly formatted BibTeX entries


**Features:**

- Google Scholar and PubMed search
- Metadata extraction from CrossRef, PubMed, arXiv
- DOI/PMID/arXiv ID to BibTeX conversion
- Citation validation and verification
- Integration with literature-review skill

---

#### `/venue-templates`
**Get LaTeX templates for major journals and conferences.** Access formatting requirements and submission guidelines for Nature, Science, PLOS, IEEE, ACM, NeurIPS, ICML, CVPR, CHI, and more.


**Use when:**

- Preparing manuscript for specific journal (Nature, Science, PLOS, IEEE)
- Writing conference paper (NeurIPS, ICML, CHI, CVPR)
- Creating research posters for conferences
- Writing grant proposals (NSF, NIH, DOE, DARPA)
- Need venue-specific formatting requirements


**Features:**

- Ready-to-use LaTeX templates
- Journal-specific formatting requirements
- Conference paper templates
- Grant proposal templates
- Submission guideline summaries

---

#### `/scientific-slides`
**Build presentation decks for research talks.** Create PowerPoint or LaTeX Beamer presentations with proper structure, visual design, timing guidance, and evidence-based content.


**Use when:**

- Preparing conference presentations or seminar talks
- Creating thesis defense slides
- Building research presentations for professional audiences
- Need visually engaging, research-backed slides


**Features:**

- PowerPoint and LaTeX Beamer support
- Modern, visually engaging design templates
- Timing guidance and delivery preparation
- Research-backed content with proper citations
- Avoids text-heavy bullet points (visual-first approach)

---

#### `/scientific-brainstorming`
**Research ideation partner.** Generate hypotheses, explore interdisciplinary connections, challenge assumptions, develop methodologies, and identify research gaps.


**Use when:**

- Generating novel research ideas or directions
- Exploring interdisciplinary connections and analogies
- Challenging assumptions in existing frameworks
- Developing new methodological approaches
- Identifying research gaps or opportunities
- Overcoming creative blocks in problem-solving


**Features:**

- Hypothesis generation
- Interdisciplinary exploration
- Assumption challenging
- Methodology development
- Research gap identification

---

#### `/scientific-critical-thinking`
**Evaluate research rigor.** Assess methodology, experimental design, statistical validity, biases, confounding, and evidence quality using GRADE and Cochrane ROB frameworks.


**Use when:**

- Evaluating research methodology and experimental design
- Assessing statistical validity and evidence quality
- Identifying biases and confounding in studies
- Reviewing scientific claims and conclusions
- Conducting systematic reviews or meta-analyses
- Peer review preparation


**Features:**

- Methodology assessment
- Experimental design evaluation
- Statistical validity checks
- Bias and confounding identification
- GRADE and Cochrane ROB frameworks
- Evidence quality assessment

---

### 📊 Data Analysis & Statistics

#### `/statistical-analysis`
**Comprehensive statistical toolkit.** Conduct hypothesis tests (t-test, ANOVA, chi-square), regression, correlation, Bayesian analysis, power analysis, assumption checks, and APA reporting.


**Use when:**

- Conducting hypothesis tests (t-tests, ANOVA, chi-square)
- Performing regression or correlation analyses
- Running Bayesian statistical analyses
- Checking statistical assumptions and diagnostics
- Calculating effect sizes and conducting power analyses
- Reporting results in APA format for publications


**Features:**

- Hypothesis testing (t-test, ANOVA, chi-square, etc.)
- Regression and correlation analysis
- Bayesian statistics
- Power analysis
- Assumption validation
- APA-format reporting

---

#### `/exploratory-data-analysis`
**Analyze scientific data files across 200+ formats.** Automatic file type detection, format-specific analysis, data quality assessment, and comprehensive markdown reports. Covers chemistry, bioinformatics, microscopy, spectroscopy, proteomics, metabolomics.


**Use when:**

- Analyzing any scientific data file to understand structure and content
- Need format-specific metadata extraction
- Data quality and integrity assessment required
- Want statistical summaries and distributions
- Need visualization and analysis recommendations


**Features:**

- 200+ scientific file format support
- Automatic file type detection
- Format-specific metadata extraction
- Data quality assessment
- Statistical summaries
- Visualization recommendations
- Markdown report generation

---

#### `/seaborn`
**Statistical visualization library.** Create scatter, box, violin, heatmaps, pair plots, regression, correlation matrices, KDE, and faceted plots for exploratory analysis and publication figures.


**Use when:**

- Creating publication-quality statistical graphics
- Exploratory data analysis with visualizations
- Multi-panel figures with complex layouts
- Need automatic statistical estimation (confidence intervals, etc.)
- Dataset-oriented plotting with Pandas DataFrames


**Features:**

- Dataset-oriented plotting (works with DataFrames)
- Automatic statistical estimation
- Publication-ready themes and color palettes
- Matplotlib integration for customization
- Complex multi-panel figures

---

#### `/plotly`
**Interactive scientific visualization.** Create scatter plots, line charts, bar charts, heatmaps, 3D plots, geographic maps, statistical distributions, financial charts, and dashboards. Outputs interactive HTML or static images (PNG, PDF, SVG).


**Use when:**

- Creating interactive visualizations for web or notebooks
- Need 3D plots or geographic maps
- Building interactive dashboards
- Want both quick visualizations (Plotly Express) and fine-grained control (graph objects)
- Need exportable static images (PNG, PDF, SVG)


**Features:**

- 40+ chart types
- Interactive HTML output
- Static image export (PNG, PDF, SVG)
- Plotly Express (high-level API) and graph objects (low-level control)
- 3D plots and geographic maps
- Dashboard support

---

### 📄 Document Processing

#### `/docx`
**Work with Word documents.** Create, edit, and analyze .docx files with support for tracked changes, comments, formatting preservation, and text extraction.


**Use when:**

- Creating new Word documents programmatically
- Modifying or editing existing .docx files
- Working with tracked changes and comments
- Extracting text from Word documents
- Need professional document formatting


**Features:**

- Document creation and editing
- Tracked changes support
- Comment management
- Formatting preservation
- Text extraction and analysis

---

#### `/xlsx`
**Work with Excel spreadsheets.** Create, edit, and analyze spreadsheets (.xlsx, .xlsm, .csv, .tsv) with formulas, formatting, data analysis, and visualization. Zero formula errors guaranteed.


**Use when:**

- Creating new spreadsheets with formulas and formatting
- Reading or analyzing spreadsheet data
- Modifying existing spreadsheets while preserving formulas
- Data analysis and visualization in spreadsheets
- Recalculating formulas


**Features:**

- Formula creation and preservation
- Data analysis and visualization
- Multiple format support (.xlsx, .xlsm, .csv, .tsv)
- Zero formula errors guarantee
- Template preservation

---

#### `/pdf-processing-pro`
**Production-ready PDF processing.** Extract text, fill forms, extract tables, OCR, validate, and batch process PDFs with comprehensive error handling.


**Use when:**

- Extracting text from PDF documents
- Filling PDF forms programmatically
- Extracting tables from PDFs
- OCR (text from scanned documents)
- Batch processing large volumes of PDFs
- Need robust error handling and validation


**Features:**

- Text extraction with pdfplumber
- Form filling
- Table extraction
- OCR support
- Batch processing
- Comprehensive error handling

---

#### `/obsidian-markdown`
**Write Obsidian Flavored Markdown.** Create notes with wikilinks, embeds, callouts, properties (frontmatter), tags, and other Obsidian-specific syntax.


**Use when:**

- Creating or editing notes in Obsidian vault
- Need wikilinks, embeds, or callouts
- Adding frontmatter/properties to notes
- Working with Obsidian-specific syntax
- Building knowledge management notes


**Features:**

- Wikilinks: `[[Note Name]]` and `[[Note|Alias]]`
- Embeds: `![[Note]]` or `![[image.png]]`
- Callouts: `> [!note]`, `> [!warning]`, etc.
- YAML frontmatter (properties)
- Block references and transclusion
- Tags and metadata

---

### 🌐 Web Search

#### `/ai-search`
**Model-agnostic AI-powered web search.** Use Claude's built-in WebSearch (no setup required) or plug in your own API from OpenAI, Anthropic, Google Gemini, or Perplexity. Real-time web search with source citations.


**Use when:**

- Searching for current information beyond Claude's knowledge cutoff
- Research, fact-checking, or accessing recent information
- Want flexibility to use different AI providers
- Need source citations for web information


**Default:** Uses Claude's built-in WebSearch - **no API key needed!**


**Optional:** Configure API keys for OpenAI, Anthropic, Google Gemini, or Perplexity.


**Features:**

- Model-agnostic (works with multiple providers)
- Real-time web search
- Source citations
- No setup required (default mode)
- Optional API integration for advanced features

---

#### `/perplexity-search`
**AI-powered search with Perplexity models.** Search using Perplexity via LiteLLM and OpenRouter. Access Sonar Pro, Sonar Pro Search (advanced agentic search), and Sonar Reasoning Pro models with a single API key.


**Use when:**

- Searching for current information or recent developments (2024+)
- Finding latest scientific publications and research
- Getting real-time answers grounded in web sources
- Verifying facts with source citations
- Want Perplexity-specific models (Sonar Pro, Sonar Reasoning)


**Requires:** OpenRouter API key (single key for all Perplexity models)


**Features:**

- Multiple Perplexity models (Sonar Pro, Sonar Pro Search, Sonar Reasoning Pro)
- Real-time web grounding
- Source citations
- Scientific literature search
- Single API key setup (OpenRouter)

---

### 🛠️ Developer Tools

#### `/mcp-builder`
**Build MCP servers.** Create Model Context Protocol (MCP) servers to connect Claude with external services through well-designed tools.


**Use when:**

- Building new MCP server for Claude Desktop integration
- Adding tools to existing MCP server
- Reviewing MCP implementation for best practices
- Connecting Claude to external APIs or services


**Features:**

- Four-phase development process (Research, Plan, Build, Test)
- API integration best practices
- Authentication and rate limiting
- Tool design patterns
- Testing and validation

---

## Installation & Setup

### No Installation Required (Most Skills)

Most skills work immediately without any installation. Just use the `/skill-name` command and Claude will guide you.

### Optional: Python Tools Setup

Some skills have Python scripts for advanced features (e.g., PubMed search, citation validation). Only set this up if:
- You want to search PubMed/Google Scholar directly
- You want to validate citations automatically
- Claude specifically asks you to run a Python script

#### Windows Setup

1. **Open PowerShell** (search "PowerShell" in Start menu)
2. **Navigate to project folder:**
   ```powershell
   cd "d:\OneDrive\04_Projects\17_Obsidian-Claude"
   ```
3. **Activate virtual environment:**
   ```powershell
   .\.venv\Scripts\activate
   ```
   You should see `(.venv)` at the start of your command line.
4. **Install requirements:**
   ```powershell
   pip install -r .claude\skills\requirements.txt
   ```

#### Mac/Linux Setup

1. **Open Terminal**
2. **Navigate to project folder:**
   ```bash
   cd ~/path/to/17_Obsidian-Claude
   ```
3. **Activate virtual environment:**
   ```bash
   source .venv/bin/activate
   ```
4. **Install requirements:**
   ```bash
   pip install -r .claude/skills/requirements.txt
   ```

### What Gets Installed

These Python packages are included:
- **requests** - Web API connections
- **bibtexparser** - Citation file processing
- **biopython** - PubMed database access

Additional packages may be installed by specific skills as needed.

---

## Configuration

### Web Search Setup

#### Default (No Setup)
Just ask Claude to search the web - uses built-in WebSearch.

#### Advanced (Optional API Keys)
To use your own API from OpenAI, Google, Anthropic, or Perplexity:

See detailed guide: `.claude/skills/ai-search/references/provider_setup.md`

### Perplexity Search Setup

Requires OpenRouter API key. Get yours at: <https://openrouter.ai/>

See skill documentation: `.claude/skills/perplexity-search/SKILL.md`

---

## Quick Reference Card

| I Want To... | Use This Skill |
|--------------|----------------|
| **Research & Writing** | |
| Write a research paper | `/scientific-writing` |
| Conduct literature review | `/literature-review` |
| Find and cite papers | `/citation-management` |
| Get journal templates | `/venue-templates` |
| Create presentation slides | `/scientific-slides` |
| Generate research ideas | `/scientific-brainstorming` |
| Evaluate research rigor | `/scientific-critical-thinking` |
| **Data & Statistics** | |
| Analyze data statistically | `/statistical-analysis` |
| Explore scientific data files | `/exploratory-data-analysis` |
| Create statistical plots | `/seaborn` |
| Create interactive visualizations | `/plotly` |
| **Documents** | |
| Work with Word docs | `/docx` |
| Work with Excel spreadsheets | `/xlsx` |
| Process PDF files | `/pdf-processing-pro` |
| Write Obsidian notes | `/obsidian-markdown` |
| **Web Search** | |
| Search the web (default) | `/ai-search` or just ask Claude |
| Search with Perplexity | `/perplexity-search` |
| **Development** | |
| Build MCP servers | `/mcp-builder` |

---

## Troubleshooting

### "Command not found" when typing a skill

Make sure you're typing the command **in Claude Code**, not in a regular terminal. The `/` commands only work when talking to Claude.

### Python script errors

If a Python script fails:
1. Activate the virtual environment (see setup steps above)
2. Install the requirements
3. Run the command from the project folder
4. Check that you're in the correct directory

### Web search not working

**Default mode:** Just ask Claude to search - no setup needed.

**API mode:** If using custom API keys, check:
- API key is set correctly in environment variables
- API key has sufficient credits
- Provider is spelled correctly in config

### Skill not responding as expected

Just ask Claude for help:
> "Help me use the [skill-name] skill"

Claude will guide you through the specific skill's usage.

---

## Skill Development

Each skill follows a standard structure:

```text
skill-name/
├── SKILL.md           # Main skill documentation
├── README.md          # User-facing guide (optional)
├── scripts/           # Python scripts (optional)
├── templates/         # Templates (optional)
└── references/        # Reference materials (optional)
```

When skills reference other skills or tools not available in this installation, Claude will use available alternatives (WebSearch, WebFetch, or direct API access via included Python scripts).

---

## Need Help?

Just ask Claude! Type something like:
> "Help me use the scientific-writing skill to draft a paper"

Claude will guide you through using any skill for your specific needs.
