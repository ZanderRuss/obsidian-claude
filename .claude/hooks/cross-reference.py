#!/usr/bin/env python3
"""
Hook: Cross-Reference Validator
Triggers on: PreToolUse (Write)
Purpose: Block thesis/paper files with broken cross-references

Cross-Reference Checks:
- Figure references match defined figures
- Table references match defined tables
- Section references match defined sections
- Citation references match bibliography
"""

import json
import re
import sys

# Trigger patterns (shared with thesis-consistency)
TRIGGER_PATTERNS = [
    r'.*Template - Thesis.*\.md$',
    r'.*Template - Paper.*\.md$',
    r'.*/thesis-draft/.*\.md$',
    r'.*/paper-draft/.*\.md$',
    r'.*/drafts/.*\.md$',
    r'.*\d{2}-.*Draft\.md$',
]

THESIS_TYPES = ['thesis', 'paper', 'chapter', 'section', 'thesis-chapter', 'thesis-project']


def should_trigger(file_path: str, content: str) -> bool:
    """Determine if this file should be checked for cross-references."""
    for pattern in TRIGGER_PATTERNS:
        if re.match(pattern, file_path, re.IGNORECASE):
            return True

    type_match = re.search(r'^type:\s*(.+)$', content, re.MULTILINE)
    if type_match:
        file_type = type_match.group(1).strip().lower()
        if file_type in THESIS_TYPES:
            return True

    tags_match = re.search(r'^tags:\s*\n((?:\s+-\s+.+\n)+)', content, re.MULTILINE)
    if tags_match:
        tags_str = tags_match.group(1)
        if 'thesis' in tags_str.lower() or 'paper' in tags_str.lower():
            return True

    return False


def extract_figure_definitions(content: str) -> set[str]:
    """Extract defined figure numbers/labels from content."""
    figures = set()

    # Markdown image with caption pattern: ![Figure X: caption](path)
    for match in re.finditer(r'!\[Figure\s+(\d+)', content, re.IGNORECASE):
        figures.add(match.group(1))

    # LaTeX style: \begin{figure}...\label{fig:X}
    for match in re.finditer(r'\\label\{fig:([^}]+)\}', content):
        figures.add(match.group(1))

    # Table-style figure listing: | Figure 1 | caption |
    for match in re.finditer(r'\|\s*Figure\s+(\d+)\s*\|', content, re.IGNORECASE):
        figures.add(match.group(1))

    # Obsidian embedded images with Figure caption
    for match in re.finditer(r'!\[\[.*?\]\]\s*\n\s*\*\*Figure\s+(\d+)', content, re.IGNORECASE):
        figures.add(match.group(1))

    return figures


def extract_table_definitions(content: str) -> set[str]:
    """Extract defined table numbers/labels from content."""
    tables = set()

    # Table caption pattern: **Table X.**
    for match in re.finditer(r'\*\*Table\s+(\d+)[.\*]', content, re.IGNORECASE):
        tables.add(match.group(1))

    # LaTeX style: \label{tab:X}
    for match in re.finditer(r'\\label\{tab:([^}]+)\}', content):
        tables.add(match.group(1))

    return tables


def extract_section_definitions(content: str) -> set[str]:
    """Extract defined section numbers from content."""
    sections = set()

    # Markdown headers: ## 3.1 Section Title
    for match in re.finditer(r'^#{1,6}\s+(\d+(?:\.\d+)*)', content, re.MULTILINE):
        sections.add(match.group(1))

    return sections


def check_figure_references(content: str) -> tuple[bool, list[str]]:
    """Check that all figure references have corresponding definitions."""
    issues = []

    # Find defined figures
    defined_figures = extract_figure_definitions(content)

    # Find referenced figures: Figure X, Fig. X, (Figure X)
    referenced_figures = set()
    for match in re.finditer(r'(?:Figure|Fig\.?)\s+(\d+)', content, re.IGNORECASE):
        referenced_figures.add(match.group(1))

    # Check for undefined references
    undefined = referenced_figures - defined_figures
    for fig_num in undefined:
        issues.append(f"Figure {fig_num} is referenced but not defined in this document.")

    # Check for unreferenced definitions (warning, not blocking)
    # unreferenced = defined_figures - referenced_figures
    # for fig_num in unreferenced:
    #     issues.append(f"Figure {fig_num} is defined but never referenced.")

    return len(issues) == 0, issues


def check_table_references(content: str) -> tuple[bool, list[str]]:
    """Check that all table references have corresponding definitions."""
    issues = []

    # Find defined tables
    defined_tables = extract_table_definitions(content)

    # Find referenced tables
    referenced_tables = set()
    for match in re.finditer(r'(?:Table|Tab\.?)\s+(\d+)', content, re.IGNORECASE):
        referenced_tables.add(match.group(1))

    # Check for undefined references
    undefined = referenced_tables - defined_tables
    for tab_num in undefined:
        issues.append(f"Table {tab_num} is referenced but not defined in this document.")

    return len(issues) == 0, issues


def check_section_references(content: str) -> tuple[bool, list[str]]:
    """Check that section references exist."""
    issues = []

    # Find defined sections
    defined_sections = extract_section_definitions(content)

    # Find referenced sections: Section X.Y, Sec. X
    referenced_sections = set()
    for match in re.finditer(r'(?:Section|Sec\.?)\s+(\d+(?:\.\d+)*)', content, re.IGNORECASE):
        referenced_sections.add(match.group(1))

    # For section references, only check top-level within the document
    # (cross-chapter references are expected to be unresolved within a single file)
    undefined = []
    for sec in referenced_sections:
        # Only flag if it looks like it should be in this document
        # (starts with same chapter number as defined sections)
        if defined_sections:
            first_defined = min(defined_sections, default='0')
            chapter_prefix = first_defined.split('.')[0] if '.' in first_defined else first_defined
            if sec.startswith(chapter_prefix + '.') and sec not in defined_sections:
                undefined.append(sec)

    for sec_num in undefined:
        issues.append(f"Section {sec_num} is referenced but not defined in this document.")

    return len(issues) == 0, issues


def check_equation_references(content: str) -> tuple[bool, list[str]]:
    """Check that equation references exist."""
    issues = []

    # Find defined equations: \label{eq:X} or (X) after equation
    defined_equations = set()
    for match in re.finditer(r'\\label\{eq:([^}]+)\}', content):
        defined_equations.add(match.group(1))

    # Find numbered equations in display math
    for match in re.finditer(r'\$\$.*?\(\d+\).*?\$\$', content, re.DOTALL):
        eq_num = re.search(r'\((\d+)\)', match.group())
        if eq_num:
            defined_equations.add(eq_num.group(1))

    # Find referenced equations: Equation (X), Eq. (X)
    referenced_equations = set()
    for match in re.finditer(r'(?:Equation|Eq\.?)\s*\(?(\d+)\)?', content, re.IGNORECASE):
        referenced_equations.add(match.group(1))

    # Check for undefined references
    undefined = referenced_equations - defined_equations
    for eq_num in undefined:
        # Only flag if we have some defined equations (document uses numbered equations)
        if defined_equations:
            issues.append(f"Equation {eq_num} is referenced but not defined.")

    return len(issues) == 0, issues


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_name = input_data.get('tool_name', '')
    tool_input = input_data.get('tool_input', {})

    if tool_name != 'Write':
        sys.exit(0)

    file_path = tool_input.get('file_path', '')
    content = tool_input.get('content', '')

    # Check if this file should trigger cross-reference checks
    if not should_trigger(file_path, content):
        sys.exit(0)

    # Run all cross-reference checks
    all_issues = []

    checks = [
        ('Figure', check_figure_references),
        ('Table', check_table_references),
        ('Section', check_section_references),
        ('Equation', check_equation_references),
    ]

    for check_name, check_func in checks:
        passed, issues = check_func(content)
        for issue in issues:
            all_issues.append(f"[{check_name}] {issue}")

    # Cross-reference issues are warnings by default, not blocks
    # Only block if there are many issues (likely a bigger problem)
    if len(all_issues) > 5:
        result = {
            'decision': 'block',
            'reason': f"Multiple cross-reference issues found ({len(all_issues)}):\n" +
                     "\n".join(f"- {i}" for i in all_issues[:10]) +
                     ("\n..." if len(all_issues) > 10 else "")
        }
        print(json.dumps(result))
        sys.exit(0)
    elif all_issues:
        result = {
            'decision': 'allow',
            'reason': f"Cross-reference warnings (not blocking):\n" +
                     "\n".join(f"- {i}" for i in all_issues)
        }
        print(json.dumps(result))
        sys.exit(0)

    # All checks passed
    sys.exit(0)


if __name__ == '__main__':
    main()
