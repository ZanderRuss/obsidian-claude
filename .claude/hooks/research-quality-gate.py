#!/usr/bin/env python3
"""
Hook: Research Quality Gate
Triggers on: PreToolUse (Write)
Purpose: Block research phase files that fail quality checks

Quality Checks:
- 30-synthesis.md: Must have citations, no "[citation needed]" markers
- 40-draft.md: Must pass synthesis, no unsupported claims flag
"""

import json
import re
import sys

# Files that require quality gate checks
QUALITY_GATE_FILES = {
    '30-synthesis': {
        'requires': ['10-sources', '20-notes'],
        'checks': ['has_citations', 'no_citation_needed']
    },
    '40-draft': {
        'requires': ['30-synthesis'],
        'checks': ['synthesis_passed', 'no_unsupported_claims']
    }
}


def check_has_citations(content: str) -> tuple[bool, str]:
    """Check if content has proper citations."""
    # Look for citation patterns: [@key], (Author, Year), [1], etc.
    citation_patterns = [
        r'\[@[\w-]+\]',  # BibTeX style
        r'\([A-Z][a-z]+,?\s*\d{4}\)',  # (Author, 2024)
        r'\[\d+\]',  # Numbered [1]
        r'\[\[Paper -',  # Obsidian literature links
        r'\[\[.*?Literature',  # Literature note links
        r'et al\.',  # Academic citation indicator
    ]

    for pattern in citation_patterns:
        if re.search(pattern, content):
            return True, ""

    return False, "No citations found. Research synthesis must cite sources."


def check_no_citation_needed(content: str) -> tuple[bool, str]:
    """Check for [citation needed] or similar markers."""
    markers = [
        r'\[citation needed\]',
        r'\[needs citation\]',
        r'\[cite\]',
        r'\[TODO:?\s*cite',
        r'\[source\?\]',
    ]

    for marker in markers:
        match = re.search(marker, content, re.IGNORECASE)
        if match:
            return False, f"Found '{match.group()}' - all claims must be cited before saving."

    return True, ""


def check_no_unsupported_claims(content: str) -> tuple[bool, str]:
    """Check for unsupported claim flags."""
    markers = [
        r'\[unsupported\]',
        r'\[unverified\]',
        r'\[needs verification\]',
        r'## Unsupported Claims\s*\n\s*[^#\n]',  # Non-empty unsupported section
    ]

    for marker in markers:
        if re.search(marker, content, re.IGNORECASE):
            return False, "Contains unsupported claims. Run fact-checker before saving."

    return True, ""


def check_synthesis_passed(content: str) -> tuple[bool, str]:
    """Check that synthesis quality markers are present."""
    # For drafts, we check that synthesis was completed properly
    # This is a lighter check - mainly ensuring the draft references synthesis
    if '## Sources' in content or '## References' in content or '## Bibliography' in content:
        return True, ""

    # Also accept if there are inline citations
    has_citations, _ = check_has_citations(content)
    if has_citations:
        return True, ""

    return False, "Draft must include sources/references section or inline citations."


def is_research_phase_file(file_path: str) -> str | None:
    """Check if file is a research phase file requiring quality gates."""
    # Normalize path for matching
    normalized = file_path.lower().replace(' ', '-').replace('_', '-')

    for phase in QUALITY_GATE_FILES:
        if phase in normalized:
            return phase
    return None


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

    # Check if this is a research phase file
    phase = is_research_phase_file(file_path)
    if not phase:
        sys.exit(0)

    # Run quality checks for this phase
    checks = QUALITY_GATE_FILES[phase]['checks']
    check_functions = {
        'has_citations': check_has_citations,
        'no_citation_needed': check_no_citation_needed,
        'no_unsupported_claims': check_no_unsupported_claims,
        'synthesis_passed': check_synthesis_passed,
    }

    failures = []
    for check_name in checks:
        if check_name in check_functions:
            passed, message = check_functions[check_name](content)
            if not passed:
                failures.append(message)

    if failures:
        result = {
            'decision': 'block',
            'reason': f"Quality gate failed for {phase}:\n" + "\n".join(f"- {f}" for f in failures)
        }
        print(json.dumps(result))
        sys.exit(0)

    # All checks passed
    sys.exit(0)


if __name__ == '__main__':
    main()
