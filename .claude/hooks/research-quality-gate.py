#!/usr/bin/env python3
"""
Hook: Research Quality Gate
Triggers on: PreToolUse (Write)
Purpose: Block research phase files that fail quality checks

Quality Checks:
- 30-synthesis.md: Must have citations, no "[citation needed]" markers
- 40-draft.md: Must pass synthesis, no unsupported claims flag
- Thesis chapters: Chapter-specific requirements (intro, lit review, methodology, etc.)
- Discussion sections: Argument quality, hedging, claim-evidence alignment
"""

import json
import re
import sys

# Files that require quality gate checks (research pipeline)
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

# Thesis chapter patterns and their required checks
THESIS_CHAPTER_PATTERNS = {
    'introduction': {
        'patterns': [r'introduction', r'ch.*1', r'chapter.*1'],
        'checks': ['has_research_questions', 'has_contributions', 'has_structure_outline']
    },
    'literature': {
        'patterns': [r'literature', r'related.*work', r'background', r'ch.*2', r'chapter.*2'],
        'checks': ['has_citations', 'has_synthesis', 'has_gap_identification']
    },
    'methodology': {
        'patterns': [r'methodology', r'methods?', r'approach', r'ch.*3', r'chapter.*3'],
        'checks': ['has_methodology_structure', 'has_justification']
    },
    'results': {
        'patterns': [r'results?', r'findings', r'experiments?', r'ch.*4', r'chapter.*4'],
        'checks': ['has_data_presentation', 'has_analysis']
    },
    'discussion': {
        'patterns': [r'discussion', r'ch.*5', r'chapter.*5'],
        'checks': ['has_interpretation', 'has_limitations', 'argument_quality']
    },
    'conclusion': {
        'patterns': [r'conclusion', r'summary', r'ch.*6', r'chapter.*6'],
        'checks': ['has_contributions_restated', 'has_future_work']
    }
}

# Thesis-related file patterns
THESIS_FILE_PATTERNS = [
    r'.*thesis.*chapter.*\.md$',
    r'.*thesis.*draft.*\.md$',
    r'.*chapter-\d+.*\.md$',
    r'.*\d{2}-.*chapter.*\.md$',
]

# Thesis-related frontmatter types
THESIS_TYPES = ['thesis', 'thesis-chapter', 'thesis-project', 'chapter', 'paper']

# Dataset file patterns
DATASET_FILE_PATTERNS = [
    r'.*8\.\s*Dataset Collection.*\.md$',
    r'.*Dataset Entry.*\.md$',
    r'.*dataset.*entry.*\.md$',
]


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


# --- Thesis Chapter Check Functions ---

def check_has_research_questions(content: str) -> tuple[bool, str]:
    """Check if introduction has research questions."""
    rq_patterns = [
        r'research\s+question',
        r'\bRQ\d+\b',
        r'we\s+(?:investigate|examine|explore|ask)',
        r'this\s+thesis\s+(?:addresses|investigates|examines)',
        r'## Research Questions',
        r'## Objectives',
    ]
    for pattern in rq_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True, ""
    return False, "Introduction should include research questions or objectives."


def check_has_contributions(content: str) -> tuple[bool, str]:
    """Check if introduction lists contributions."""
    contrib_patterns = [
        r'contribution',
        r'we\s+contribute',
        r'this\s+thesis\s+contributes',
        r'## Contributions',
        r'novel\s+approach',
        r'key\s+(?:contributions|findings)',
    ]
    for pattern in contrib_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True, ""
    return False, "Introduction should list thesis contributions."


def check_has_structure_outline(content: str) -> tuple[bool, str]:
    """Check if introduction outlines the thesis structure."""
    structure_patterns = [
        r'chapter\s+\d+',
        r'## Thesis Structure',
        r'## Outline',
        r'structured\s+as\s+follows',
        r'remainder\s+of\s+this',
        r'organized\s+as\s+follows',
    ]
    for pattern in structure_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True, ""
    return False, "Introduction should outline the thesis structure."


def check_has_synthesis(content: str) -> tuple[bool, str]:
    """Check if literature review synthesizes rather than just lists."""
    synthesis_patterns = [
        r'however',
        r'in\s+contrast',
        r'while\s+.+?,\s+.+',
        r'synthesis',
        r'together,\s+these',
        r'across\s+(?:these\s+)?studies',
        r'common\s+(?:theme|finding)',
    ]
    match_count = sum(1 for p in synthesis_patterns if re.search(p, content, re.IGNORECASE))
    if match_count >= 2:  # At least 2 synthesis indicators
        return True, ""
    return False, "Literature review should synthesize sources, not just list them."


def check_has_gap_identification(content: str) -> tuple[bool, str]:
    """Check if literature review identifies research gaps."""
    gap_patterns = [
        r'gap',
        r'lacks?',
        r'limited\s+(?:attention|research|work)',
        r'not\s+(?:yet\s+)?addressed',
        r'remains?\s+(?:unclear|open|unexplored)',
        r'few\s+studies',
        r'## Research Gap',
    ]
    for pattern in gap_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True, ""
    return False, "Literature review should identify research gaps."


def check_has_methodology_structure(content: str) -> tuple[bool, str]:
    """Check if methodology has proper structure."""
    required_sections = 0
    section_patterns = [
        r'## .*(?:Data|Dataset|Sample)',
        r'## .*(?:Method|Approach|Design)',
        r'## .*(?:Procedure|Process|Protocol)',
        r'## .*(?:Analysis|Evaluation|Metrics)',
    ]
    for pattern in section_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            required_sections += 1
    if required_sections >= 2:
        return True, ""
    return False, "Methodology should include data, methods, and analysis sections."


def check_has_justification(content: str) -> tuple[bool, str]:
    """Check if methodology justifies choices."""
    justification_patterns = [
        r'we\s+(?:chose|selected|used)\s+.+\s+because',
        r'this\s+approach\s+(?:allows|enables|is\s+appropriate)',
        r'justified\s+by',
        r'appropriate\s+for',
        r'suitable\s+for',
        r'following\s+.+\s+guidelines',
    ]
    for pattern in justification_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True, ""
    return False, "Methodology should justify methodological choices."


def check_has_data_presentation(content: str) -> tuple[bool, str]:
    """Check if results present data properly."""
    data_patterns = [
        r'\|.*\|.*\|',  # Table
        r'Figure\s+\d+',
        r'Table\s+\d+',
        r'\d+(?:\.\d+)?%',  # Percentages
        r'p\s*[<>=]\s*0\.\d+',  # P-values
        r'mean\s*=',
        r'n\s*=\s*\d+',
    ]
    match_count = sum(1 for p in data_patterns if re.search(p, content, re.IGNORECASE))
    if match_count >= 2:
        return True, ""
    return False, "Results should present data with tables, figures, or statistics."


def check_has_analysis(content: str) -> tuple[bool, str]:
    """Check if results include analysis."""
    analysis_patterns = [
        r'(?:show|indicate|demonstrate|reveal|suggest)s?\s+that',
        r'significant(?:ly)?',
        r'outperform',
        r'compared\s+to',
        r'increase|decrease',
        r'correlation',
    ]
    match_count = sum(1 for p in analysis_patterns if re.search(p, content, re.IGNORECASE))
    if match_count >= 2:
        return True, ""
    return False, "Results should include analysis of the data presented."


def check_has_interpretation(content: str) -> tuple[bool, str]:
    """Check if discussion interprets findings."""
    interpretation_patterns = [
        r'(?:this|these)\s+(?:finding|result)s?\s+(?:suggest|indicate|show)',
        r'implication',
        r'this\s+means',
        r'explain(?:ed|s)?\s+by',
        r'consistent\s+with',
        r'contrary\s+to',
    ]
    match_count = sum(1 for p in interpretation_patterns if re.search(p, content, re.IGNORECASE))
    if match_count >= 2:
        return True, ""
    return False, "Discussion should interpret findings, not just restate them."


def check_has_limitations(content: str) -> tuple[bool, str]:
    """Check if discussion acknowledges limitations."""
    limitation_patterns = [
        r'limitation',
        r'however',
        r'constraint',
        r'future\s+(?:work|research|studies)',
        r'could\s+not',
        r'did\s+not\s+(?:include|consider|address)',
        r'## Limitations',
    ]
    for pattern in limitation_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True, ""
    return False, "Discussion should acknowledge limitations."


def check_argument_quality(content: str) -> tuple[bool, str]:
    """Check argument quality in Discussion sections."""
    issues = []

    # Check for overclaiming (strong claims without hedging)
    overclaim_patterns = [
        (r'\b(?:prove|proven)\b', 'proves'),
        (r'\bdefinitely\b', 'definitely'),
        (r'\bwithout\s+doubt\b', 'without doubt'),
        (r'\bclearly\s+demonstrate\b', 'clearly demonstrate'),
    ]
    for pattern, term in overclaim_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append(f"Potential overclaiming: '{term}' - consider appropriate hedging")

    # Check hedging is present for claims
    hedging_patterns = [
        r'\bsuggest',
        r'\bindicate',
        r'\bmay\b',
        r'\bmight\b',
        r'\bpossibly\b',
        r'\blikely\b',
        r'\bappear\b',
    ]
    has_hedging = any(re.search(p, content, re.IGNORECASE) for p in hedging_patterns)

    # Only flag if there are strong claims but no hedging
    if issues and not has_hedging:
        return False, "Discussion contains strong claims but lacks hedging. Add appropriate qualifiers."

    # Check claim-evidence alignment (claims should reference results/data)
    claim_patterns = list(re.finditer(r'(?:we|this)\s+(?:show|demonstrate|find|conclude)\s+that', content, re.IGNORECASE))
    if claim_patterns:
        # For each claim, check if there's nearby evidence reference
        evidence_patterns = [r'Figure\s+\d+', r'Table\s+\d+', r'Section\s+\d+', r'(?:as\s+)?shown\s+(?:in|above|below)']
        has_evidence_refs = any(re.search(p, content, re.IGNORECASE) for p in evidence_patterns)
        if not has_evidence_refs:
            issues.append("Claims should reference supporting evidence (figures, tables, sections)")

    if len(issues) > 2:
        return False, "Argument quality issues:\n  - " + "\n  - ".join(issues[:3])

    return True, ""


def check_has_contributions_restated(content: str) -> tuple[bool, str]:
    """Check if conclusion restates contributions."""
    contrib_patterns = [
        r'contribution',
        r'we\s+have\s+(?:shown|demonstrated|presented)',
        r'this\s+thesis\s+has',
        r'key\s+(?:contribution|finding)',
        r'## Contributions',
    ]
    for pattern in contrib_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True, ""
    return False, "Conclusion should restate thesis contributions."


def check_has_future_work(content: str) -> tuple[bool, str]:
    """Check if conclusion suggests future work."""
    future_patterns = [
        r'future\s+(?:work|research|studies|direction)',
        r'could\s+be\s+(?:extended|improved|addressed)',
        r'## Future',
        r'open\s+question',
        r'further\s+(?:research|investigation)',
    ]
    for pattern in future_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True, ""
    return False, "Conclusion should suggest future research directions."


def check_citation_coverage(content: str) -> tuple[bool, str]:
    """Check citation coverage for dataset entries."""
    # Check if file has proper citations section
    has_references = ('## References' in content or
                      '## Sources' in content or
                      '## Bibliography' in content)

    if not has_references:
        return False, "Dataset entry must include ## References, ## Sources, or ## Bibliography section"

    # Look for citation keys (BibTeX style or other formats)
    citation_patterns = [
        r'\[@[\w-]+\]',  # BibTeX style [@key]
        r'\([A-Z][a-z]+,?\s*\d{4}\)',  # (Author, 2024)
        r'\[\d+\]',  # Numbered [1]
        r'\[\[.*?(?:Literature|Paper)',  # Obsidian literature note links
    ]

    citation_count = 0
    for pattern in citation_patterns:
        citation_count += len(re.findall(pattern, content))

    # Dataset entries should cite at least 1 source
    if citation_count < 1:
        return False, "Dataset entry must cite at least one source (manufacturer website, spec sheet, or research paper). Add inline citations like [@imby2024kits]"

    return True, ""


# --- Thesis file detection ---

def is_thesis_file(file_path: str, content: str) -> bool:
    """Check if file is a thesis-related file."""
    # Check file path patterns
    normalized = file_path.lower().replace(' ', '-')
    for pattern in THESIS_FILE_PATTERNS:
        if re.match(pattern, normalized, re.IGNORECASE):
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
        tags_str = tags_match.group(1).lower()
        if 'thesis' in tags_str or 'chapter' in tags_str:
            return True

    return False


def is_dataset_file(file_path: str) -> bool:
    """Check if file is a dataset entry requiring citation."""
    normalized = file_path.lower().replace(' ', '-').replace('_', '-')

    for pattern in DATASET_FILE_PATTERNS:
        if re.match(pattern, normalized, re.IGNORECASE):
            return True

    return False


def get_thesis_chapter_type(file_path: str, content: str) -> str | None:
    """Determine which type of thesis chapter this is."""
    combined = (file_path + ' ' + content[:1000]).lower()  # Check path + beginning of content

    for chapter_type, config in THESIS_CHAPTER_PATTERNS.items():
        for pattern in config['patterns']:
            if re.search(pattern, combined, re.IGNORECASE):
                return chapter_type

    return None


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

    # All available check functions
    check_functions = {
        # Research pipeline checks
        'has_citations': check_has_citations,
        'no_citation_needed': check_no_citation_needed,
        'no_unsupported_claims': check_no_unsupported_claims,
        'synthesis_passed': check_synthesis_passed,
        'citation_coverage': check_citation_coverage,
        # Thesis chapter checks
        'has_research_questions': check_has_research_questions,
        'has_contributions': check_has_contributions,
        'has_structure_outline': check_has_structure_outline,
        'has_synthesis': check_has_synthesis,
        'has_gap_identification': check_has_gap_identification,
        'has_methodology_structure': check_has_methodology_structure,
        'has_justification': check_has_justification,
        'has_data_presentation': check_has_data_presentation,
        'has_analysis': check_has_analysis,
        'has_interpretation': check_has_interpretation,
        'has_limitations': check_has_limitations,
        'argument_quality': check_argument_quality,
        'has_contributions_restated': check_has_contributions_restated,
        'has_future_work': check_has_future_work,
    }

    failures = []
    warnings = []
    check_type = None

    # Check if this is a research phase file
    phase = is_research_phase_file(file_path)
    if phase:
        check_type = f"research phase '{phase}'"
        checks = QUALITY_GATE_FILES[phase]['checks']
        for check_name in checks:
            if check_name in check_functions:
                passed, message = check_functions[check_name](content)
                if not passed:
                    failures.append(message)

    # Check if this is a dataset file
    elif is_dataset_file(file_path):
        check_type = "dataset entry"
        passed, message = check_citation_coverage(content)
        if not passed:
            failures.append(message)

    # Check if this is a thesis chapter file
    elif is_thesis_file(file_path, content):
        chapter_type = get_thesis_chapter_type(file_path, content)
        if chapter_type:
            check_type = f"thesis {chapter_type} chapter"
            checks = THESIS_CHAPTER_PATTERNS[chapter_type]['checks']
            for check_name in checks:
                if check_name in check_functions:
                    passed, message = check_functions[check_name](content)
                    if not passed:
                        # Argument quality issues are warnings for thesis, not blocks
                        if check_name == 'argument_quality':
                            warnings.append(message)
                        else:
                            failures.append(message)

    # No applicable checks
    if not check_type:
        sys.exit(0)

    # Block on critical failures
    if failures:
        result = {
            'decision': 'block',
            'reason': f"Quality gate failed for {check_type}:\n" + "\n".join(f"- {f}" for f in failures)
        }
        print(json.dumps(result))
        sys.exit(0)

    # Warn on non-critical issues but allow
    if warnings:
        result = {
            'decision': 'allow',
            'reason': f"Quality warnings for {check_type} (not blocking):\n" + "\n".join(f"- {w}" for w in warnings)
        }
        print(json.dumps(result))
        sys.exit(0)

    # All checks passed
    sys.exit(0)


if __name__ == '__main__':
    main()
