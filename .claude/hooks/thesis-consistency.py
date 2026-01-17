#!/usr/bin/env python3
"""
Hook: Thesis Consistency
Triggers on: PreToolUse (Write)
Purpose: Block thesis/paper files that have consistency issues

Consistency Checks:
- Terminology: Same term used consistently throughout
- Abbreviations: Defined on first use
- Tense: Appropriate for section type
- Style: Matches thesis requirements
"""

import json
import re
import sys
from pathlib import Path

# Trigger patterns for thesis/paper files
TRIGGER_PATTERNS = [
    r'.*Template - Thesis.*\.md$',
    r'.*Template - Paper.*\.md$',
    r'.*/thesis-draft/.*\.md$',
    r'.*/paper-draft/.*\.md$',
    r'.*/drafts/.*\.md$',
    r'.*\d{2}-.*Draft\.md$',  # Chapter drafts like "01-Introduction-Draft.md"
]

# Thesis-related frontmatter types
THESIS_TYPES = ['thesis', 'paper', 'chapter', 'section', 'thesis-chapter', 'thesis-project']


def should_trigger(file_path: str, content: str) -> bool:
    """Determine if this file should be checked for thesis consistency."""
    # Check file path patterns
    for pattern in TRIGGER_PATTERNS:
        if re.match(pattern, file_path, re.IGNORECASE):
            return True

    # Check frontmatter type
    type_match = re.search(r'^type:\s*(.+)$', content, re.MULTILINE)
    if type_match:
        file_type = type_match.group(1).strip().lower()
        if file_type in THESIS_TYPES:
            return True

    # Check tags
    tags_match = re.search(r'^tags:\s*\n((?:\s+-\s+.+\n)+)', content, re.MULTILINE)
    if tags_match:
        tags_str = tags_match.group(1)
        if 'thesis' in tags_str.lower() or 'paper' in tags_str.lower():
            return True

    return False


def check_terminology_consistency(content: str) -> tuple[bool, list[str]]:
    """Check for inconsistent terminology usage."""
    issues = []

    # Common inconsistency pairs
    term_pairs = [
        ('dataset', 'data set', 'data-set'),
        ('real-time', 'realtime', 'real time'),
        ('behavior', 'behaviour'),
        ('color', 'colour'),
        ('modeling', 'modelling'),
        ('center', 'centre'),
        ('optimization', 'optimisation'),
        ('utilize', 'utilise'),
        ('analyze', 'analyse'),
        ('labeled', 'labelled'),
    ]

    for variants in term_pairs:
        found_variants = []
        for variant in variants:
            # Case-insensitive search
            if re.search(r'\b' + re.escape(variant) + r'\b', content, re.IGNORECASE):
                found_variants.append(variant)

        if len(found_variants) > 1:
            issues.append(f"Inconsistent terminology: found both '{found_variants[0]}' and '{found_variants[1]}'. Standardize to one form.")

    return len(issues) == 0, issues


def check_abbreviation_definition(content: str) -> tuple[bool, list[str]]:
    """Check that abbreviations are defined on first use."""
    issues = []

    # Find all uppercase abbreviations (2+ letters)
    abbreviations = set(re.findall(r'\b([A-Z]{2,})\b', content))

    # Common abbreviations that don't need definition
    common_abbrevs = {'AI', 'ML', 'API', 'URL', 'HTML', 'CSS', 'SQL', 'GPU', 'CPU', 'RAM',
                      'USA', 'UK', 'PhD', 'MSc', 'BSc', 'ID', 'OK', 'DNA', 'RNA', 'PDF'}

    for abbrev in abbreviations:
        if abbrev in common_abbrevs:
            continue

        # Check if defined with full form: "Full Form (ABBREV)" or "(ABBREV)"
        definition_pattern = rf'\([^)]*\b{abbrev}\b[^)]*\)'
        full_form_pattern = rf'[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s*\({abbrev}\)'

        if not re.search(definition_pattern, content) and not re.search(full_form_pattern, content):
            # Count occurrences
            occurrences = len(re.findall(rf'\b{abbrev}\b', content))
            if occurrences > 1:
                issues.append(f"Abbreviation '{abbrev}' used {occurrences} times but not defined. Define on first use.")

    return len(issues) == 0, issues


def check_section_tense(content: str) -> tuple[bool, list[str]]:
    """Check for major tense issues in specific sections."""
    issues = []

    # Extract sections
    sections = re.split(r'^##\s+', content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue

        lines = section.split('\n')
        section_title = lines[0].strip().lower() if lines else ''
        section_content = '\n'.join(lines[1:])

        # Results section should use past tense predominantly
        if 'result' in section_title:
            # Check for present tense indicators where past expected
            present_indicators = re.findall(r'\b(shows?|demonstrates?|indicates?|achieves?)\b',
                                           section_content, re.IGNORECASE)
            past_indicators = re.findall(r'\b(showed|demonstrated|indicated|achieved)\b',
                                        section_content, re.IGNORECASE)

            if len(present_indicators) > len(past_indicators) * 2 and len(section_content) > 500:
                issues.append(f"Results section may have tense issues: predominantly present tense. Consider using past tense for reporting findings.")

    return len(issues) == 0, issues


def check_placeholder_markers(content: str) -> tuple[bool, list[str]]:
    """Check for unresolved placeholder markers."""
    issues = []

    placeholder_patterns = [
        (r'\[TODO[:\s].*?\]', 'TODO marker'),
        (r'\[PLACEHOLDER[:\s].*?\]', 'Placeholder marker'),
        (r'\[INSERT[:\s].*?\]', 'Insert marker'),
        (r'\[ADD[:\s].*?\]', 'Add marker'),
        (r'\[WRITE[:\s].*?\]', 'Write marker'),
        (r'XXX', 'XXX placeholder'),
        (r'\?\?\?', '??? placeholder'),
        (r'TBD\b', 'TBD marker'),
    ]

    for pattern, name in placeholder_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            issues.append(f"Found {len(matches)} {name}(s). Complete before saving final draft.")

    return len(issues) == 0, issues


def check_duplicate_phrases(content: str) -> tuple[bool, list[str]]:
    """Check for duplicate consecutive phrases (common in editing)."""
    issues = []

    # Find duplicated words
    duplicates = re.findall(r'\b(\w+)\s+\1\b', content, re.IGNORECASE)
    if len(duplicates) > 2:  # Allow a couple as they might be intentional
        issues.append(f"Found {len(duplicates)} duplicate consecutive words. Review: {', '.join(duplicates[:3])}...")

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

    # Check if this file should trigger consistency checks
    if not should_trigger(file_path, content):
        sys.exit(0)

    # Run all consistency checks
    all_issues = []

    checks = [
        ('Terminology', check_terminology_consistency),
        ('Abbreviations', check_abbreviation_definition),
        ('Tense', check_section_tense),
        ('Placeholders', check_placeholder_markers),
        ('Duplicates', check_duplicate_phrases),
    ]

    for check_name, check_func in checks:
        passed, issues = check_func(content)
        for issue in issues:
            all_issues.append(f"[{check_name}] {issue}")

    # Only block if there are critical issues (placeholders are critical)
    critical_issues = [i for i in all_issues if 'Placeholder' in i or 'TODO' in i]

    if critical_issues:
        result = {
            'decision': 'block',
            'reason': f"Thesis consistency check failed:\n" + "\n".join(f"- {i}" for i in critical_issues)
        }
        print(json.dumps(result))
        sys.exit(0)

    # Warn about non-critical issues but don't block
    if all_issues:
        result = {
            'decision': 'allow',
            'reason': f"Thesis consistency warnings (not blocking):\n" + "\n".join(f"- {i}" for i in all_issues)
        }
        print(json.dumps(result))
        sys.exit(0)

    # All checks passed
    sys.exit(0)


if __name__ == '__main__':
    main()
