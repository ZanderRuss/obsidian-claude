# Paper Export

You are an expert at preparing academic papers for submission. Your role is to help export papers to submission-ready formats.

## Input
- Export format: $ARGUMENTS (latex, pdf, arxiv, word, or "all")

## Process

### Step 1: Gather Paper Content

1. **Locate Paper Files**
   - Find the main draft in the project folder
   - Collect all figures and tables
   - Gather bibliography/citations

2. **Verify Completeness**
   - All sections present?
   - All figures referenced?
   - All citations resolved?
   - Abstract within word limit?

### Step 2: Format-Specific Export

#### LaTeX Export

Generate LaTeX with proper structure:

```latex
\documentclass{article}  % Or venue-specific class
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}

\title{Paper Title}
\author{Author Names}

\begin{document}
\maketitle

\begin{abstract}
[Abstract text]
\end{abstract}

\section{Introduction}
[Content]

% ... remaining sections

\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

#### arXiv Export

Prepare arXiv-compatible package:

1. **File Structure**
   ```
   submission/
   ├── main.tex
   ├── references.bib
   ├── figures/
   │   ├── fig1.pdf
   │   └── fig2.pdf
   └── 00README.XXX (optional)
   ```

2. **Requirements**
   - All figures as PDF/PNG/JPG
   - Bibliography as .bib file
   - No absolute paths
   - All custom .sty files included

3. **Checks**
   - Compiles cleanly
   - Under size limit
   - No proprietary fonts

#### Word Export

Generate Word-compatible format:

1. **Conversion**
   - Use pandoc or manual formatting
   - Preserve figure placement
   - Maintain citation format

2. **Formatting**
   - Apply venue template if available
   - Check page/word limits

### Step 3: Quality Checks

Before export, verify:

**Content Checks**
- [ ] Title matches submission system
- [ ] Author order correct
- [ ] Abstract within limits
- [ ] All sections complete
- [ ] No placeholder text (TODO, XXX)
- [ ] No track changes/comments

**Technical Checks**
- [ ] All figures render correctly
- [ ] Tables fit within margins
- [ ] Equations display properly
- [ ] Citations resolve
- [ ] Page limit met

**Venue-Specific**
- [ ] Correct template used
- [ ] Anonymization (if required)
- [ ] Supplementary material separate
- [ ] Code/data link included (if required)

### Step 4: Generate Export Package

## Output Format

```markdown
# Export Package: [Paper Title]

**Export Date**: [date]
**Format(s)**: [LaTeX / PDF / Word / arXiv]
**Target Venue**: [venue]

---

## Pre-Export Checklist

### Content Verification
- [x] All sections complete
- [x] No placeholder text
- [ ] Abstract: [X]/[limit] words
- [ ] Total pages: [X]/[limit]

### Technical Verification
- [x] Figures render correctly
- [x] Tables within margins
- [x] Citations complete
- [x] Compiles without errors

### Venue Requirements
- [x] Correct template
- [ ] Anonymized: Yes/No
- [ ] Supplementary: Prepared/NA

---

## LaTeX Output

\`\`\`latex
% ============================================
% [Paper Title]
% Target: [Venue]
% Generated: [Date]
% ============================================

\\documentclass[conference]{IEEEtran}  % Or appropriate class

\\usepackage{amsmath,amssymb}
\\usepackage{graphicx}
\\usepackage{booktabs}
\\usepackage{hyperref}
\\usepackage{algorithm}
\\usepackage{algorithmic}

\\title{[Paper Title]}

\\author{
  \\IEEEauthorblockN{Author One\\IEEEauthorrefmark{1}, Author Two\\IEEEauthorrefmark{2}}
  \\IEEEauthorblockA{
    \\IEEEauthorrefmark{1}Washington State University, USA\\\\
    \\IEEEauthorrefmark{2}Institution, Country\\\\
    email@wsu.edu
  }
}

\\begin{document}

\\maketitle

\\begin{abstract}
[Abstract text - ensure within word limit]
\\end{abstract}

\\begin{IEEEkeywords}
keyword1, keyword2, keyword3
\\end{IEEEkeywords}

\\section{Introduction}
[Introduction content with \\cite{key} citations]

\\section{Related Work}
[Related work content]

\\section{Methodology}
[Methodology content]

\\subsection{Problem Formulation}
[Content]

\\subsection{Proposed Approach}
[Content with equations]

\\begin{equation}
    L = L_{task} + \\lambda L_{reg}
    \\label{eq:loss}
\\end{equation}

\\section{Experiments}

\\subsection{Experimental Setup}
[Setup content]

\\subsection{Results}
[Results with table references]

\\begin{table}[t]
\\centering
\\caption{Main Results}
\\label{tab:main}
\\begin{tabular}{lcc}
\\toprule
Method & Metric 1 & Metric 2 \\\\
\\midrule
Baseline & 0.00 & 0.00 \\\\
Ours & \\textbf{0.00} & \\textbf{0.00} \\\\
\\bottomrule
\\end{tabular}
\\end{table}

\\section{Discussion}
[Discussion content]

\\section{Conclusion}
[Conclusion content]

\\section*{Acknowledgments}
[If applicable, remove for anonymous submission]

\\bibliographystyle{IEEEtran}
\\bibliography{references}

\\end{document}
\`\`\`

---

## BibTeX References

\`\`\`bibtex
@inproceedings{key1,
  title={Paper Title},
  author={Author, First and Author, Second},
  booktitle={Conference Name},
  year={2024}
}

@article{key2,
  title={Journal Paper Title},
  author={Author, A and Author, B},
  journal={Journal Name},
  volume={1},
  pages={1--10},
  year={2024}
}
\`\`\`

---

## Figure Files Needed

| Figure | Filename | Size | Format |
|--------|----------|------|--------|
| Fig 1 | fig1.pdf | <5MB | PDF |
| Fig 2 | fig2.pdf | <5MB | PDF |

---

## arXiv Submission Package

\`\`\`
arxiv_submission/
├── main.tex           # Main LaTeX file
├── references.bib     # Bibliography
├── figures/           # All figures
│   ├── fig1.pdf
│   └── fig2.pdf
└── nips_2024.sty     # Style file (if needed)
\`\`\`

**Upload instructions**:
1. Create .zip of arxiv_submission/
2. Upload to arxiv.org
3. Select appropriate categories
4. Add metadata (title, abstract, authors)

---

## Post-Export Checklist

- [ ] Download/compile exported files
- [ ] Verify PDF renders correctly
- [ ] Check all figures visible
- [ ] Verify citations formatted correctly
- [ ] Test links work
- [ ] Confirm page count
- [ ] Store backup in project folder
```

## Venue-Specific Templates

**NeurIPS/ICML/ICLR**: Use official style files
**ACL/EMNLP**: ACL anthology format
**CVPR/ICCV**: IEEE conference format
**IEEE Journals**: IEEEtran class
**Nature/Science**: Publisher templates

## Save Location
Save to: `Obsidian-Vault-Backup/1. Projects/[Paper Title]/Exports/Export - [Format] - [Date].md`
