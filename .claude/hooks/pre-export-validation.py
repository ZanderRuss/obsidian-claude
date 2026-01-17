#!/usr/bin/env python3
"""
Hook: Pre-Export Citation Validation
Triggers on: PreToolUse (Write, Bash)
Purpose: Block exports with missing or broken citations

Validates:
- All [@key] citations exist in library.bib
- All {citationID} citations exist in library.bib
- BibTeX file is accessible and parseable
- Warns about empty bibliography

This is the FINAL safety net before paper submission.
"""

import json
import re
import sys
from pathlib import Path
from typing import Set, Tuple, List

# File patterns that indicate export operations
EXPORT_FILE_PATTERNS = [
    r'.*\.tex$',  # LaTeX files
    r'.*final.*report.*\.md$',  # Final report drafts
    r'.*submission.*\.md$',  # Submission drafts
    r'.*export.*\.md$',  # Export staging files
    r'.*10\.\s*Final Report.*\.md$',  # WSU final report folder
    r'.*paper.*final.*\.md$',  # Final paper versions
]

# Bash commands that indicate export
EXPORT_BASH_PATTERNS = [
    r'/export-paper',
    r'pdflatex',
    r'xelatex',
    r'lualatex',
    r'pandoc.*--to.*latex',
    r'pandoc.*--to.*pdf',
]

# Expected location of library.bib (relative to project root)
LIBRARY_BIB_PATHS = [
    'Obsidian-Vault-Live/6. Metadata/References/library.bib',
    '6. Metadata/References/library.bib',
]


def extract_citation_keys_from_content(content: str) -> Set[str]:
    """Extract all citation keys from content using multiple syntax patterns."""
    citation_keys = set()

    # Pattern 1: [@key] - BibTeX Scholar / Pandoc style
    bibtex_citations = re.findall(r'\[@([\w-]+)\]', content)
    citation_keys.update(bibtex_citations)

    # Pattern 2: {citationID} - Paper-writing agent style
    agent_citations = re.findall(r'\{([\w-]+)\}', content)
    # Filter to likely citation keys (heuristic: contains year or academic pattern)
    for key in agent_citations:
        if re.search(r'\d{4}|^[a-z]+\d{4}', key):  # Has year or starts with author+year
            citation_keys.add(key)

    # Pattern 3: \cite{key} - LaTeX style (for .tex files)
    latex_citations = re.findall(r'\\cite(?:\w*)?{([\w-]+)}', content)
    citation_keys.update(latex_citations)

    # Pattern 4: [@key1; @key2] - Multiple citations
    multi_citations = re.findall(r'\[@([\w-]+)(?:;\s*@[\w-]+)*\]', content)
    citation_keys.update(multi_citations)

    return citation_keys


def parse_bibtex_keys(bibtex_content: str) -> Set[str]:
    """Extract all BibTeX keys from library.bib content."""
    # Match @type{key, ... }
    keys = re.findall(r'@\w+\s*{\s*([\w-]+)\s*,', bibtex_content)
    return set(keys)


def find_library_bib(file_path: str) -> str | None:
    """Find library.bib relative to the file being written or project root."""
    # Try to find project root (look for .claude folder)
    current = Path(file_path).resolve().parent

    for _ in range(10):  # Search up to 10 levels
        if (current / '.claude').exists():
            # Found project root
            for bib_path in LIBRARY_BIB_PATHS:
                full_path = current / bib_path
                if full_path.exists():
                    return str(full_path)

        if current.parent == current:
            break  # Reached filesystem root
        current = current.parent

    return None


def validate_citations(content: str, library_bib_path: str) -> Tuple[bool, List[str], Set[str], Set[str]]:
    """
    Validate all citations in content against library.bib.

    Returns:
        (is_valid, error_messages, cited_keys, available_keys)
    """
    errors = []

    # Read library.bib
    try:
        with open(library_bib_path, 'r', encoding='utf-8') as f:
            bib_content = f.read()
    except Exception as e:
        errors.append(f"Cannot read library.bib: {e}")
        return False, errors, set(), set()

    # Parse available citation keys
    available_keys = parse_bibtex_keys(bib_content)

    if not available_keys:
        errors.append("library.bib is empty or has no valid entries. Add citations before exporting.")
        return False, errors, set(), available_keys

    # Extract cited keys from content
    cited_keys = extract_citation_keys_from_content(content)

    if not cited_keys:
        # No citations found - this might be intentional (e.g., abstract-only file)
        # Don't block, but warn
        return True, ["Warning: No citations found in document. This may be intentional."], cited_keys, available_keys

    # Find missing citations
    missing_keys = cited_keys - available_keys

    if missing_keys:
        errors.append(
            f"Missing citations in library.bib ({len(missing_keys)} broken):\n" +
            "\n".join(f"  - [@{key}] or {{{key}}}" for key in sorted(missing_keys))
        )
        errors.append(
            f"\nAvailable citations ({len(available_keys)} total):\n" +
            "  " + ", ".join(sorted(list(available_keys)[:10])) +
            (f" ... and {len(available_keys) - 10} more" if len(available_keys) > 10 else "")
        )
        errors.append(
            "\nTo fix:\n" +
            "1. Check citation key spelling matches library.bib\n" +
            "2. Add missing entries to library.bib or pending-imports.bib\n" +
            "3. Import pending-imports.bib to Zotero if needed"
        )
        return False, errors, cited_keys, available_keys

    # All citations valid
    return True, [], cited_keys, available_keys


def is_export_file(file_path: str) -> bool:
    """Check if file is an export-related file."""
    normalized = file_path.lower().replace(' ', '-').replace('\\', '/')

    for pattern in EXPORT_FILE_PATTERNS:
        if re.match(pattern, normalized, re.IGNORECASE):
            return True

    return False


def is_export_bash_command(command: str) -> bool:
    """Check if bash command is an export operation."""
    for pattern in EXPORT_BASH_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return True

    return False


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_name = input_data.get('tool_name', '')
    tool_input = input_data.get('tool_input', {})

    # Check Write operations (LaTeX files, final reports)
    if tool_name == 'Write':
        file_path = tool_input.get('file_path', '')
        content = tool_input.get('content', '')

        if not is_export_file(file_path):
            sys.exit(0)  # Not an export file

        # Find library.bib
        library_bib_path = find_library_bib(file_path)
        if not library_bib_path:
            # Can't find library.bib - warn but don't block
            result = {
                'decision': 'allow',
                'reason': 'Warning: Could not locate library.bib. Citation validation skipped.'
            }
            print(json.dumps(result))
            sys.exit(0)

        # Validate citations
        is_valid, errors, cited_keys, available_keys = validate_citations(content, library_bib_path)

        if not is_valid:
            result = {
                'decision': 'block',
                'reason': f"Export validation failed:\n" + "\n".join(errors)
            }
            print(json.dumps(result))
            sys.exit(0)

        # Valid but with warnings
        if errors:
            result = {
                'decision': 'allow',
                'reason': "\n".join(errors)
            }
            print(json.dumps(result))
            sys.exit(0)

        # All checks passed - allow silently with info message
        result = {
            'decision': 'allow',
            'reason': f"✓ Citation validation passed: {len(cited_keys)} citations, all valid."
        }
        print(json.dumps(result))
        sys.exit(0)

    # Check Bash operations (pdflatex, pandoc, /export-paper)
    elif tool_name == 'Bash':
        command = tool_input.get('command', '')

        if not is_export_bash_command(command):
            sys.exit(0)  # Not an export command

        # For bash commands, we can't easily check content
        # Just ensure library.bib exists and is not empty

        # Find library.bib from current working directory
        library_bib_path = None
        for bib_path in LIBRARY_BIB_PATHS:
            if Path(bib_path).exists():
                library_bib_path = bib_path
                break

        if not library_bib_path:
            result = {
                'decision': 'block',
                'reason': (
                    f"Export command detected but library.bib not found.\n"
                    f"Command: {command[:80]}...\n"
                    f"Searched: {', '.join(LIBRARY_BIB_PATHS)}"
                )
            }
            print(json.dumps(result))
            sys.exit(0)

        # Check library.bib is not empty
        try:
            with open(library_bib_path, 'r', encoding='utf-8') as f:
                bib_content = f.read()

            available_keys = parse_bibtex_keys(bib_content)

            if not available_keys:
                result = {
                    'decision': 'block',
                    'reason': (
                        f"Export command detected but library.bib is empty.\n"
                        f"Command: {command[:80]}...\n"
                        f"Add citations to {library_bib_path} before exporting."
                    )
                }
                print(json.dumps(result))
                sys.exit(0)

            # Library exists and has entries - allow with info
            result = {
                'decision': 'allow',
                'reason': f"✓ library.bib found with {len(available_keys)} citations. Export allowed."
            }
            print(json.dumps(result))
            sys.exit(0)

        except Exception as e:
            result = {
                'decision': 'block',
                'reason': f"Cannot read library.bib: {e}"
            }
            print(json.dumps(result))
            sys.exit(0)

    # Other tools - not relevant
    sys.exit(0)


if __name__ == '__main__':
    main()
