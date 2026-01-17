#!/usr/bin/env python3
"""
Perplexity Academic Search - Specialized scholarly research search.

A wrapper around perplexity_search.py with academic mode pre-configured.
Optimized for peer-reviewed sources, literature searches, and research discovery.

Usage:
    python perplexity_academic.py "CRISPR gene editing" --recent 2023
    python perplexity_academic.py "transformer architectures" --domain cs --pro
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any

# Add parent directory to path to import from perplexity-search skill
SKILL_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(SKILL_ROOT / "perplexity-search" / "scripts"))

try:
    from perplexity_search import search_with_perplexity, check_setup
except ImportError:
    print("Error: Could not import perplexity_search module.")
    print("Ensure perplexity-search skill is installed.")
    sys.exit(1)


# =============================================================================
# Domain Presets - Curated academic domain lists
# =============================================================================

DOMAIN_PRESETS: Dict[str, Dict[str, Any]] = {
    "general": {
        "description": "Broad academic search across all scholarly domains",
        "domains": [
            "arxiv.org",
            "nature.com",
            "science.org",
            "cell.com",
            "nih.gov",
            "pubmed.gov",
            "ncbi.nlm.nih.gov",
            "pnas.org",
            "sciencedirect.com",
            "springer.com",
            "wiley.com",
            "plos.org",
            "biorxiv.org",
            "medrxiv.org",
            ".edu",
            ".gov"
        ]
    },
    "medical": {
        "description": "Medical and clinical research sources",
        "domains": [
            "nih.gov",
            "pubmed.gov",
            "ncbi.nlm.nih.gov",
            "nejm.org",
            "thelancet.com",
            "bmj.com",
            "jamanetwork.com",
            "annals.org",
            "cochranelibrary.com",
            "clinicaltrials.gov"
        ]
    },
    "biomedical": {
        "description": "Life sciences and biomedical research",
        "domains": [
            "nature.com",
            "cell.com",
            "pnas.org",
            "ncbi.nlm.nih.gov",
            "pubmed.gov",
            "biorxiv.org",
            "medrxiv.org",
            "elifesciences.org",
            "plos.org",
            "sciencedirect.com"
        ]
    },
    "cs": {
        "description": "Computer science and AI research",
        "domains": [
            "arxiv.org",
            "acm.org",
            "ieee.org",
            "proceedings.neurips.cc",
            "openreview.net",
            "aclanthology.org",
            "jmlr.org",
            "proceedings.mlr.press"
        ]
    },
    "physics": {
        "description": "Physics and astronomy research",
        "domains": [
            "arxiv.org",
            "aps.org",
            "iop.org",
            "nature.com/nphys",
            "journals.aps.org",
            "aip.org"
        ]
    },
    "chemistry": {
        "description": "Chemistry and materials science",
        "domains": [
            "pubs.acs.org",
            "rsc.org",
            "nature.com/nchem",
            "wiley.com",
            "sciencedirect.com",
            "chemrxiv.org"
        ]
    },
    "social": {
        "description": "Social sciences and humanities",
        "domains": [
            ".edu",
            "jstor.org",
            "ssrn.com",
            "tandfonline.com",
            "sagepub.com",
            "cambridge.org",
            "oxfordjournals.org"
        ]
    }
}


def academic_search(
    query: str,
    domain_preset: str = "general",
    recent_year: Optional[int] = None,
    date_after: Optional[str] = None,
    date_before: Optional[str] = None,
    pro: bool = False,
    verbose: bool = False,
    citations_only: bool = False
) -> Dict[str, Any]:
    """
    Perform an academic search with pre-configured scholarly settings.

    Args:
        query: Search query (academic topic)
        domain_preset: Domain preset name (general, medical, biomedical, cs, physics, chemistry, social)
        recent_year: Only include papers from this year onwards (e.g., 2023)
        date_after: Specific start date in YYYY-MM-DD format
        date_before: Specific end date in YYYY-MM-DD format
        pro: Enable Pro Search for multi-step reasoning
        verbose: Print detailed progress information
        citations_only: Return only citation information

    Returns:
        Dict with search results including answer, citations, and metadata
    """
    # Get domain list from preset
    if domain_preset not in DOMAIN_PRESETS:
        return {
            "success": False,
            "error": f"Unknown domain preset: {domain_preset}. Valid options: {', '.join(DOMAIN_PRESETS.keys())}"
        }

    domains = DOMAIN_PRESETS[domain_preset]["domains"]

    # Handle date filtering
    search_after = None
    if recent_year:
        search_after = f"01/01/{recent_year}"
    elif date_after:
        # Convert YYYY-MM-DD to MM/DD/YYYY if needed
        if "-" in date_after and len(date_after) == 10:
            parts = date_after.split("-")
            search_after = f"{parts[1]}/{parts[2]}/{parts[0]}"
        else:
            search_after = date_after

    search_before = None
    if date_before:
        if "-" in date_before and len(date_before) == 10:
            parts = date_before.split("-")
            search_before = f"{parts[1]}/{parts[2]}/{parts[0]}"
        else:
            search_before = date_before

    if verbose:
        print(f"Academic search: {query}")
        print(f"Domain preset: {domain_preset}")
        print(f"Domains: {', '.join(domains[:5])}...")
        if search_after:
            print(f"Date filter: after {search_after}")
        if pro:
            print("Pro Search: enabled")

    # Call the main search function with academic settings hardcoded
    result = search_with_perplexity(
        query=query,
        model="sonar-pro",
        max_tokens=4000,
        temperature=0.2,
        # Academic mode settings
        academic=True,
        search_context_size="high",
        # Domain filtering
        search_domain_filter=domains,
        # Date filtering
        search_after_date=search_after,
        search_before_date=search_before,
        # Pro Search
        pro=pro,
        stream=pro,  # Streaming required for Pro Search
        verbose=verbose
    )

    # Add metadata about academic search
    if result.get("success"):
        result["search_mode"] = "academic"
        result["domain_preset"] = domain_preset
        result["domains_used"] = domains

        # If citations_only, simplify output
        if citations_only and result.get("citations"):
            return {
                "success": True,
                "query": query,
                "citations": result.get("citations", []),
                "citation_count": len(result.get("citations", []))
            }

    return result


def list_presets() -> None:
    """Print available domain presets."""
    print("\nAvailable Domain Presets:")
    print("=" * 60)
    for name, config in DOMAIN_PRESETS.items():
        print(f"\n{name}:")
        print(f"  Description: {config['description']}")
        print(f"  Domains: {', '.join(config['domains'][:5])}...")
    print()


def main():
    """CLI entry point for academic search."""
    parser = argparse.ArgumentParser(
        description="Perplexity Academic Search - Scholarly research with peer-reviewed sources",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "CRISPR gene editing" --recent 2023
  %(prog)s "transformer architectures" --domain cs
  %(prog)s "clinical trials diabetes" --domain medical --pro
  %(prog)s "machine learning" --citations-only --output refs.json
        """
    )

    parser.add_argument(
        "query",
        nargs="?",
        help="Academic search query"
    )

    # Domain preset
    parser.add_argument(
        "--domain", "-d",
        default="general",
        choices=list(DOMAIN_PRESETS.keys()),
        help="Domain preset (default: general)"
    )

    # Date filtering
    parser.add_argument(
        "--recent",
        type=int,
        metavar="YEAR",
        help="Only papers from this year onwards (e.g., 2023)"
    )
    parser.add_argument(
        "--date-after",
        metavar="DATE",
        help="Start date (YYYY-MM-DD format)"
    )
    parser.add_argument(
        "--date-before",
        metavar="DATE",
        help="End date (YYYY-MM-DD format)"
    )

    # Search mode
    parser.add_argument(
        "--pro",
        action="store_true",
        help="Enable Pro Search (multi-step reasoning)"
    )

    # Output options
    parser.add_argument(
        "--output", "-o",
        metavar="FILE",
        help="Save results to JSON file"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed progress"
    )
    parser.add_argument(
        "--citations-only",
        action="store_true",
        help="Output only citations"
    )

    # Utility options
    parser.add_argument(
        "--list-presets",
        action="store_true",
        help="Show available domain presets"
    )
    parser.add_argument(
        "--check-setup",
        action="store_true",
        help="Verify API key and dependencies"
    )

    args = parser.parse_args()

    # Handle utility commands
    if args.list_presets:
        list_presets()
        return 0

    if args.check_setup:
        return check_setup()

    # Require query for search
    if not args.query:
        parser.print_help()
        return 1

    # Perform search
    result = academic_search(
        query=args.query,
        domain_preset=args.domain,
        recent_year=args.recent,
        date_after=args.date_after,
        date_before=args.date_before,
        pro=args.pro,
        verbose=args.verbose,
        citations_only=args.citations_only
    )

    # Handle output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        print(f"Results saved to: {args.output}")
    else:
        if result.get("success"):
            if args.citations_only:
                print(f"\nFound {result.get('citation_count', 0)} citations:\n")
                for citation in result.get("citations", []):
                    if isinstance(citation, dict):
                        print(f"  [{citation.get('number', '?')}] {citation.get('url', 'N/A')}")
                    else:
                        print(f"  - {citation}")
            else:
                print(f"\n{result.get('answer', 'No answer')}\n")
                if result.get("citations"):
                    print("\nCitations:")
                    for citation in result["citations"]:
                        if isinstance(citation, dict):
                            print(f"  [{citation.get('number', '?')}] {citation.get('url', 'N/A')}")
                        else:
                            print(f"  - {citation}")
        else:
            print(f"Error: {result.get('error', 'Unknown error')}")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
