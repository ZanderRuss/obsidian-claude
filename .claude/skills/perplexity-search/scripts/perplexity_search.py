#!/usr/bin/env python3
"""
Perplexity Search - Advanced API Integration

This script performs AI-powered web searches using Perplexity models with full support for:
  - Academic mode (search_mode: "academic") for scholarly sources
  - Pro Search (search_type: "pro") for multi-step reasoning
  - Date filtering (publication date, last updated, recency)
  - Domain filtering (allowlist/denylist, TLD filtering)
  - File attachments (PDF analysis)
  - Presets for common use cases (academic, technical, news)

Supports two backends:
  1. Direct Perplexity API (preferred) - uses PERPLEXITY_API_KEY
  2. OpenRouter fallback - uses OPENROUTER_API_KEY

Usage:
    python perplexity_search.py "search query" [options]

See .claude/docs/perplexity-best-practices.md for comprehensive documentation.

Requirements:
    - PERPLEXITY_API_KEY (direct API) OR OPENROUTER_API_KEY (via OpenRouter)
    - requests library: pip install requests
    - Optional: LiteLLM for OpenRouter backend: pip install litellm

Author: Scientific Skills
License: MIT
"""

import os
import sys
import json
import argparse
import base64
import re
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None


# =============================================================================
# Presets Configuration
# Based on: .claude/docs/perplexity-best-practices.md
# =============================================================================

PRESETS = {
    "academic": {
        "description": "Academic/scholarly search - prioritizes peer-reviewed sources",
        "search_mode": "academic",
        "search_domain_filter": [
            "nature.com", "science.org", "cell.com",
            "nih.gov", "ncbi.nlm.nih.gov", "pubmed.gov",
            "arxiv.org", "biorxiv.org", "medrxiv.org",
            "sciencedirect.com", "springer.com", "wiley.com", "plos.org"
        ],
        "search_context_size": "high"
    },
    "technical": {
        "description": "Technical documentation and code search",
        "search_domain_filter": [
            "github.com", "stackoverflow.com", "docs.python.org",
            "developer.mozilla.org", "docs.microsoft.com",
            "arxiv.org", "readthedocs.io"
        ],
        "search_type": "pro"
    },
    "news": {
        "description": "Recent news and current events",
        "search_recency_filter": "week",
        "search_domain_filter": [
            "-reddit.com", "-pinterest.com", "-quora.com",
            "-medium.com", "-linkedin.com"
        ]
    },
    "medical": {
        "description": "Medical and clinical research",
        "search_mode": "academic",
        "search_domain_filter": [
            "nih.gov", "ncbi.nlm.nih.gov", "pubmed.gov",
            "clinicaltrials.gov", "who.int", "cdc.gov",
            "nejm.org", "thelancet.com", "bmj.com"
        ],
        "search_context_size": "high"
    },
    "legal": {
        "description": "Legal and regulatory sources",
        "search_domain_filter": [
            ".gov", ".edu",
            "law.cornell.edu", "supremecourt.gov"
        ]
    }
}

# Domain lists for quick filtering
ACADEMIC_DOMAINS = [
    "nature.com", "science.org", "cell.com",
    "nih.gov", "ncbi.nlm.nih.gov", "pubmed.gov",
    "arxiv.org", "biorxiv.org", "medrxiv.org",
    "sciencedirect.com", "springer.com", "wiley.com", "plos.org",
    ".edu", ".gov"
]

EXCLUDE_SOCIAL = [
    "-reddit.com", "-quora.com", "-pinterest.com",
    "-medium.com", "-linkedin.com", "-facebook.com",
    "-twitter.com", "-youtube.com"
]


# =============================================================================
# Environment Loading
# =============================================================================

def _load_env_file():
    """Load .env file from current directory, parent directories, or project root.

    This allows API keys to be stored in a .env file instead of requiring
    manual 'export' commands. The function searches:
    1. Current working directory
    2. Parent directories (up to 5 levels)
    3. Script's parent directories (to find project root)

    Returns:
        bool: True if .env file was found and loaded, False otherwise
    """
    try:
        from dotenv import load_dotenv
    except ImportError:
        # python-dotenv not installed - that's okay, user can use env vars directly
        return False

    # Try current working directory first
    env_path = Path.cwd() / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path, override=False)
        return True

    # Try parent directories (up to 5 levels)
    cwd = Path.cwd()
    for _ in range(5):
        env_path = cwd / ".env"
        if env_path.exists():
            load_dotenv(dotenv_path=env_path, override=False)
            return True
        cwd = cwd.parent
        if cwd == cwd.parent:
            break

    # Try the script's parent directories (to find project root)
    script_dir = Path(__file__).resolve().parent
    for _ in range(5):
        env_path = script_dir / ".env"
        if env_path.exists():
            load_dotenv(dotenv_path=env_path, override=False)
            return True
        script_dir = script_dir.parent
        if script_dir == script_dir.parent:
            break

    return False


# Auto-load .env on import
_load_env_file()


# =============================================================================
# Date Validation
# Based on: .claude/docs/perplexity-best-practices.md - Date Filtering section
# =============================================================================

def validate_date_format(date_string: str) -> bool:
    """Validate date format matches Perplexity's required format: MM/DD/YYYY

    Args:
        date_string: Date string to validate

    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/[0-9]{4}$'
    return bool(re.match(pattern, date_string))


def parse_date_input(date_input: str) -> str:
    """Parse various date formats and convert to MM/DD/YYYY

    Accepts:
        - MM/DD/YYYY (pass through)
        - YYYY-MM-DD (ISO format)
        - "today", "yesterday", "last week", etc.

    Args:
        date_input: Date string in various formats

    Returns:
        str: Date in MM/DD/YYYY format

    Raises:
        ValueError: If date format is invalid
    """
    # Already in correct format
    if validate_date_format(date_input):
        return date_input

    # ISO format (YYYY-MM-DD)
    iso_pattern = r'^(\d{4})-(\d{2})-(\d{2})$'
    match = re.match(iso_pattern, date_input)
    if match:
        year, month, day = match.groups()
        return f"{int(month)}/{int(day)}/{year}"

    # Relative dates
    today = datetime.now()
    relative_dates = {
        "today": today,
        "yesterday": today.replace(day=today.day - 1) if today.day > 1 else today,
    }

    if date_input.lower() in relative_dates:
        dt = relative_dates[date_input.lower()]
        return f"{dt.month}/{dt.day}/{dt.year}"

    raise ValueError(f"Invalid date format: {date_input}. Use MM/DD/YYYY or YYYY-MM-DD")


# =============================================================================
# File Attachment Support
# Based on: .claude/docs/perplexity-best-practices.md - File Attachments section
# =============================================================================

def encode_file_to_base64(file_path: str) -> Tuple[str, str]:
    """Encode a file to base64 for API submission.

    Supported formats: PDF, DOC, DOCX, TXT, RTF
    Max size: 50MB

    Args:
        file_path: Path to file

    Returns:
        Tuple of (base64_content, filename)

    Raises:
        ValueError: If file type not supported or file too large
    """
    path = Path(file_path)

    if not path.exists():
        raise ValueError(f"File not found: {file_path}")

    # Check file size (50MB limit)
    file_size = path.stat().st_size
    max_size = 50 * 1024 * 1024  # 50MB
    if file_size > max_size:
        raise ValueError(f"File too large: {file_size / 1024 / 1024:.1f}MB (max 50MB)")

    # Check file extension
    supported_extensions = {'.pdf', '.doc', '.docx', '.txt', '.rtf'}
    if path.suffix.lower() not in supported_extensions:
        raise ValueError(f"Unsupported file type: {path.suffix}. Supported: {supported_extensions}")

    # Read and encode
    with open(path, 'rb') as f:
        content = base64.b64encode(f.read()).decode('utf-8')

    return content, path.name


def build_file_attachment_content(
    query: str,
    files: List[str]
) -> List[Dict[str, Any]]:
    """Build content array with file attachments for Perplexity API.

    Args:
        query: User question/query
        files: List of file paths to attach

    Returns:
        List of content objects for API request
    """
    content = [{"type": "text", "text": query}]

    for file_path in files:
        base64_content, filename = encode_file_to_base64(file_path)
        content.append({
            "type": "file_url",
            "file_url": {"url": base64_content},  # Note: No data: prefix for files!
            "file_name": filename
        })

    return content


# =============================================================================
# Dependency Checks & Backend Selection
# =============================================================================

def check_dependencies(backend: str = "auto") -> Tuple[bool, str]:
    """Check if required packages are installed for the given backend.

    Args:
        backend: "direct", "openrouter", or "auto" (try direct first)

    Returns:
        Tuple of (success, actual_backend_used)
    """
    if backend == "auto":
        # Try direct API first (requires requests)
        if requests is not None:
            perplexity_key = os.environ.get("PERPLEXITY_API_KEY")
            if perplexity_key:
                return True, "direct"

        # Fall back to OpenRouter (requires litellm)
        try:
            import litellm
            openrouter_key = os.environ.get("OPENROUTER_API_KEY")
            if openrouter_key:
                return True, "openrouter"
        except ImportError:
            pass

        # No valid backend found
        print("Error: No API key configured.", file=sys.stderr)
        print("\nOption 1 (Recommended): Direct Perplexity API", file=sys.stderr)
        print("  Set PERPLEXITY_API_KEY in .env or environment", file=sys.stderr)
        print("  Get key from: https://www.perplexity.ai/settings/api", file=sys.stderr)
        print("\nOption 2: Via OpenRouter", file=sys.stderr)
        print("  Set OPENROUTER_API_KEY in .env or environment", file=sys.stderr)
        print("  Get key from: https://openrouter.ai/keys", file=sys.stderr)
        return False, "none"

    elif backend == "direct":
        if requests is None:
            print("Error: requests library not installed.", file=sys.stderr)
            print("Install with: pip install requests", file=sys.stderr)
            return False, "none"
        return True, "direct"

    elif backend == "openrouter":
        try:
            import litellm
            return True, "openrouter"
        except ImportError:
            print("Error: LiteLLM is not installed.", file=sys.stderr)
            print("Install it with: pip install litellm", file=sys.stderr)
            return False, "none"

    return False, "none"


def get_api_key(backend: str) -> Optional[str]:
    """Get the API key for the specified backend."""
    if backend == "direct":
        api_key = os.environ.get("PERPLEXITY_API_KEY")
        if not api_key:
            print("Error: PERPLEXITY_API_KEY not set.", file=sys.stderr)
            print("Get key from: https://www.perplexity.ai/settings/api", file=sys.stderr)
            return None
        return api_key

    elif backend == "openrouter":
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            print("Error: OPENROUTER_API_KEY not set.", file=sys.stderr)
            print("Get key from: https://openrouter.ai/keys", file=sys.stderr)
            return None
        return api_key

    return None


# =============================================================================
# Direct Perplexity API (Enhanced)
# =============================================================================

def search_direct_api(
    query: str,
    api_key: str,
    model: str = "sonar-pro",
    max_tokens: int = 4000,
    temperature: float = 0.2,
    verbose: bool = False,
    # Advanced search options (from perplexity-best-practices.md)
    search_mode: Optional[str] = None,  # "academic" for scholarly sources
    search_type: Optional[str] = None,  # "pro", "fast", "auto"
    search_context_size: Optional[str] = None,  # "low", "medium", "high"
    search_after_date: Optional[str] = None,  # MM/DD/YYYY
    search_before_date: Optional[str] = None,  # MM/DD/YYYY
    search_recency_filter: Optional[str] = None,  # "day", "week", "month", "year"
    search_domain_filter: Optional[List[str]] = None,  # Domain allowlist/denylist
    files: Optional[List[str]] = None,  # File paths for attachment
    stream: bool = False  # Enable streaming (required for Pro Search)
) -> Dict[str, Any]:
    """
    Perform a search using the Direct Perplexity API with advanced options.

    Args:
        query: The search query
        api_key: Perplexity API key
        model: Model to use (default: sonar-pro)
        max_tokens: Maximum tokens in response
        temperature: Response temperature (0.0-1.0)
        verbose: Print detailed information

        # Advanced options (see .claude/docs/perplexity-best-practices.md)
        search_mode: "academic" for scholarly sources
        search_type: "pro" (multi-step), "fast" (default), "auto"
        search_context_size: Context depth - "low", "medium", "high"
        search_after_date: Only content published after this date (MM/DD/YYYY)
        search_before_date: Only content published before this date (MM/DD/YYYY)
        search_recency_filter: Quick filter - "day", "week", "month", "year"
        search_domain_filter: List of domains to include or exclude (prefix with -)
        files: List of file paths to attach for analysis
        stream: Enable streaming (required for Pro Search type)

    Returns:
        Dictionary containing the search results and metadata
    """
    if requests is None:
        return {"success": False, "error": "requests library not installed"}

    # Direct API endpoint
    url = "https://api.perplexity.ai/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Build message content (with or without file attachments)
    if files:
        try:
            message_content = build_file_attachment_content(query, files)
        except ValueError as e:
            return {"success": False, "error": str(e), "query": query}
    else:
        message_content = query

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": message_content}],
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    # Add search mode (academic)
    if search_mode:
        payload["search_mode"] = search_mode

    # Build web_search_options
    web_search_options = {}
    if search_type:
        web_search_options["search_type"] = search_type
        # Pro Search REQUIRES streaming
        if search_type == "pro":
            stream = True
    if search_context_size:
        web_search_options["search_context_size"] = search_context_size

    if web_search_options:
        payload["web_search_options"] = web_search_options

    # Add date filters (cannot combine recency with specific dates)
    if search_recency_filter:
        payload["search_recency_filter"] = search_recency_filter
    else:
        if search_after_date:
            payload["search_after_date_filter"] = search_after_date
        if search_before_date:
            payload["search_before_date_filter"] = search_before_date

    # Add domain filter
    if search_domain_filter:
        # Validate max 20 domains
        if len(search_domain_filter) > 20:
            return {"success": False, "error": "Maximum 20 domains allowed in filter"}
        payload["search_domain_filter"] = search_domain_filter

    # Enable streaming if needed
    if stream:
        payload["stream"] = True

    if verbose:
        print(f"Backend: Direct Perplexity API", file=sys.stderr)
        print(f"Model: {model}", file=sys.stderr)
        print(f"Query: {query[:100]}..." if len(query) > 100 else f"Query: {query}", file=sys.stderr)
        print(f"Max tokens: {max_tokens}", file=sys.stderr)
        print(f"Temperature: {temperature}", file=sys.stderr)
        if search_mode:
            print(f"Search mode: {search_mode}", file=sys.stderr)
        if search_type:
            print(f"Search type: {search_type}", file=sys.stderr)
        if search_context_size:
            print(f"Context size: {search_context_size}", file=sys.stderr)
        if search_domain_filter:
            print(f"Domain filter: {search_domain_filter}", file=sys.stderr)
        if search_recency_filter:
            print(f"Recency filter: {search_recency_filter}", file=sys.stderr)
        if files:
            print(f"Files attached: {len(files)}", file=sys.stderr)
        if stream:
            print(f"Streaming: enabled", file=sys.stderr)
        print("", file=sys.stderr)

    try:
        if stream:
            # Handle streaming response
            response = requests.post(url, headers=headers, json=payload, timeout=300, stream=True)

            if response.status_code != 200:
                error_json = response.json()
                error_msg = error_json.get("error", {}).get("message", str(error_json))
                return {"success": False, "error": f"API Error: {error_msg}", "query": query, "model": model}

            # Collect streamed response
            full_content = ""
            citations = []
            reasoning_steps = []
            usage = {}

            for line in response.iter_lines():
                if line:
                    line_str = line.decode('utf-8')
                    if line_str.startswith('data: '):
                        data_str = line_str[6:]
                        if data_str.strip() == '[DONE]':
                            break
                        try:
                            data = json.loads(data_str)
                            if 'choices' in data and len(data['choices']) > 0:
                                delta = data['choices'][0].get('delta', {})
                                if 'content' in delta:
                                    full_content += delta['content']
                                if 'reasoning_steps' in delta:
                                    reasoning_steps.extend(delta['reasoning_steps'])
                            if 'citations' in data:
                                citations = data['citations']
                            if 'usage' in data:
                                usage = data['usage']
                        except json.JSONDecodeError:
                            continue

            result = {
                "success": True,
                "backend": "direct",
                "query": query,
                "model": model,
                "answer": full_content,
                "usage": usage,
                "streaming": True
            }

            if citations:
                result["citations"] = citations
            if reasoning_steps:
                result["reasoning_steps"] = reasoning_steps

            return result
        else:
            # Non-streaming response
            response = requests.post(url, headers=headers, json=payload, timeout=120)
            response_json = response.json()

            if response.status_code != 200:
                error_msg = response_json.get("error", {}).get("message", str(response_json))
                return {"success": False, "error": f"API Error: {error_msg}", "query": query, "model": model}

            # Extract the response
            result = {
                "success": True,
                "backend": "direct",
                "query": query,
                "model": model,
                "answer": response_json["choices"][0]["message"]["content"],
                "usage": response_json.get("usage", {}),
                "streaming": False
            }

            # Check for citations
            if "citations" in response_json:
                result["citations"] = response_json["citations"]

            # Check for search results (contains URLs)
            if "search_results" in response_json:
                result["search_results"] = response_json["search_results"]

            return result

    except requests.exceptions.Timeout:
        return {"success": False, "error": "Request timed out", "query": query, "model": model}
    except Exception as e:
        return {"success": False, "error": str(e), "query": query, "model": model}


# =============================================================================
# OpenRouter Backend (Fallback) - Enhanced
# =============================================================================

def search_openrouter(
    query: str,
    model: str = "openrouter/perplexity/sonar-pro",
    max_tokens: int = 4000,
    temperature: float = 0.2,
    verbose: bool = False,
    # Note: OpenRouter may not support all advanced options
    files: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Perform a search using Perplexity models via LiteLLM and OpenRouter.

    Note: OpenRouter may not support all Perplexity-specific options like
    search_mode or web_search_options. Use direct API for full features.

    Args:
        query: The search query
        model: Model to use (default: sonar-pro)
        max_tokens: Maximum tokens in response
        temperature: Response temperature (0.0-1.0)
        verbose: Print detailed information
        files: File paths for attachment (limited support)

    Returns:
        Dictionary containing the search results and metadata
    """
    try:
        from litellm import completion
    except ImportError:
        return {"success": False, "error": "LiteLLM not installed. Run: pip install litellm"}

    api_key = get_api_key("openrouter")
    if not api_key:
        return {"success": False, "error": "OpenRouter API key not configured"}

    # Build message content
    if files:
        try:
            message_content = build_file_attachment_content(query, files)
        except ValueError as e:
            return {"success": False, "error": str(e), "query": query}
    else:
        message_content = query

    if verbose:
        print(f"Backend: OpenRouter", file=sys.stderr)
        print(f"Model: {model}", file=sys.stderr)
        print(f"Query: {query[:100]}..." if len(query) > 100 else f"Query: {query}", file=sys.stderr)
        print(f"Max tokens: {max_tokens}", file=sys.stderr)
        print(f"Temperature: {temperature}", file=sys.stderr)
        if files:
            print(f"Files attached: {len(files)}", file=sys.stderr)
        print("", file=sys.stderr)
        print("Note: Advanced options (academic mode, domain filter) require direct API", file=sys.stderr)
        print("", file=sys.stderr)

    try:
        response = completion(
            model=model,
            messages=[{"role": "user", "content": message_content}],
            max_tokens=max_tokens,
            temperature=temperature
        )

        result = {
            "success": True,
            "backend": "openrouter",
            "query": query,
            "model": model,
            "answer": response.choices[0].message.content,
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        }

        if hasattr(response.choices[0].message, 'citations'):
            result["citations"] = response.choices[0].message.citations

        return result

    except Exception as e:
        return {"success": False, "error": str(e), "query": query, "model": model}


# =============================================================================
# Unified Search Function (Enhanced)
# =============================================================================

def search_with_perplexity(
    query: str,
    model: str = "sonar-pro",
    max_tokens: int = 4000,
    temperature: float = 0.2,
    verbose: bool = False,
    backend: str = "auto",
    # Advanced options
    preset: Optional[str] = None,  # Use preset configuration
    academic: bool = False,  # Shortcut for search_mode="academic"
    pro: bool = False,  # Shortcut for search_type="pro"
    search_mode: Optional[str] = None,
    search_type: Optional[str] = None,
    search_context_size: Optional[str] = None,
    search_after_date: Optional[str] = None,
    search_before_date: Optional[str] = None,
    search_recency_filter: Optional[str] = None,
    search_domain_filter: Optional[List[str]] = None,
    files: Optional[List[str]] = None,
    stream: bool = False
) -> Dict[str, Any]:
    """
    Perform a search using Perplexity models with full feature support.

    Supports two backends:
    - direct: Uses PERPLEXITY_API_KEY for direct API access (full features)
    - openrouter: Uses OPENROUTER_API_KEY via LiteLLM (limited features)
    - auto: Try direct first, fall back to openrouter

    Args:
        query: The search query
        model: Model to use (default: sonar-pro)
        max_tokens: Maximum tokens in response
        temperature: Response temperature (0.0-1.0)
        verbose: Print detailed information
        backend: "direct", "openrouter", or "auto" (default)

        # Presets & Shortcuts
        preset: Use preset configuration ("academic", "technical", "news", "medical", "legal")
        academic: Shortcut for search_mode="academic"
        pro: Shortcut for search_type="pro"

        # Advanced options (see .claude/docs/perplexity-best-practices.md)
        search_mode: "academic" for scholarly sources
        search_type: "pro" (multi-step), "fast" (default), "auto"
        search_context_size: Context depth - "low", "medium", "high"
        search_after_date: Only content after this date (MM/DD/YYYY or YYYY-MM-DD)
        search_before_date: Only content before this date (MM/DD/YYYY or YYYY-MM-DD)
        search_recency_filter: Quick filter - "day", "week", "month", "year"
        search_domain_filter: List of domains to include or exclude (prefix with -)
        files: List of file paths to attach for analysis
        stream: Enable streaming (auto-enabled for Pro Search)

    Returns:
        Dictionary containing the search results and metadata
    """
    # Apply preset configuration if specified
    if preset:
        if preset not in PRESETS:
            return {"success": False, "error": f"Unknown preset: {preset}. Available: {list(PRESETS.keys())}"}

        preset_config = PRESETS[preset]
        if verbose:
            print(f"Using preset: {preset} - {preset_config.get('description', '')}", file=sys.stderr)

        # Apply preset values (don't override explicit arguments)
        if search_mode is None and "search_mode" in preset_config:
            search_mode = preset_config["search_mode"]
        if search_type is None and "search_type" in preset_config:
            search_type = preset_config["search_type"]
        if search_context_size is None and "search_context_size" in preset_config:
            search_context_size = preset_config["search_context_size"]
        if search_recency_filter is None and "search_recency_filter" in preset_config:
            search_recency_filter = preset_config["search_recency_filter"]
        if search_domain_filter is None and "search_domain_filter" in preset_config:
            search_domain_filter = preset_config["search_domain_filter"]

    # Apply shortcuts
    if academic and not search_mode:
        search_mode = "academic"
    if pro and not search_type:
        search_type = "pro"

    # Parse and validate dates
    if search_after_date:
        try:
            search_after_date = parse_date_input(search_after_date)
        except ValueError as e:
            return {"success": False, "error": str(e)}

    if search_before_date:
        try:
            search_before_date = parse_date_input(search_before_date)
        except ValueError as e:
            return {"success": False, "error": str(e)}

    # Validate recency filter
    if search_recency_filter and search_recency_filter not in ["day", "week", "month", "year"]:
        return {"success": False, "error": f"Invalid recency filter: {search_recency_filter}. Use: day, week, month, year"}

    # Check that recency filter is not used with specific dates
    if search_recency_filter and (search_after_date or search_before_date):
        return {"success": False, "error": "Cannot use recency filter with specific date filters"}

    # Determine which backend to use
    deps_ok, actual_backend = check_dependencies(backend)
    if not deps_ok:
        return {"success": False, "error": "No valid backend available"}

    if actual_backend == "direct":
        api_key = get_api_key("direct")
        if not api_key:
            return {"success": False, "error": "Perplexity API key not configured"}

        return search_direct_api(
            query=query,
            api_key=api_key,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            verbose=verbose,
            search_mode=search_mode,
            search_type=search_type,
            search_context_size=search_context_size,
            search_after_date=search_after_date,
            search_before_date=search_before_date,
            search_recency_filter=search_recency_filter,
            search_domain_filter=search_domain_filter,
            files=files,
            stream=stream
        )

    elif actual_backend == "openrouter":
        # OpenRouter has limited support for advanced features
        if search_mode or search_type or search_domain_filter:
            print("Warning: Advanced search options require direct Perplexity API", file=sys.stderr)
            print("Using OpenRouter - some features may not work", file=sys.stderr)

        # Format model name for OpenRouter
        openrouter_model = model
        if not model.startswith("openrouter/"):
            openrouter_model = f"openrouter/perplexity/{model}"

        return search_openrouter(
            query=query,
            model=openrouter_model,
            max_tokens=max_tokens,
            temperature=temperature,
            verbose=verbose,
            files=files
        )

    return {"success": False, "error": "No valid backend available"}


# =============================================================================
# CLI Main
# =============================================================================

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Perform AI-powered web searches using Perplexity with advanced options",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic search
  python perplexity_search.py "What are the latest developments in CRISPR?"

  # Academic mode (prioritizes scholarly sources)
  python perplexity_search.py "CRISPR clinical trials" --academic

  # Use academic preset (academic mode + curated domains)
  python perplexity_search.py "gene therapy for cancer" --preset academic

  # Pro Search for complex analysis (multi-step reasoning)
  python perplexity_search.py "Compare transformer architectures" --pro

  # Date filtering (recent papers only)
  python perplexity_search.py "COVID-19 variants" --date-after 01/01/2024

  # Recency filter (quick relative time)
  python perplexity_search.py "AI news" --recency week

  # Domain filtering (academic sources only)
  python perplexity_search.py "machine learning" --domains "arxiv.org,nature.com,.edu"

  # Exclude social media
  python perplexity_search.py "climate change" --domains "-reddit.com,-twitter.com,-medium.com"

  # Analyze a PDF
  python perplexity_search.py "What are the key findings?" --files paper.pdf

  # Medical research preset
  python perplexity_search.py "diabetes treatment" --preset medical

  # Save output to file
  python perplexity_search.py "quantum computing" --output results.json

Available Models:
  - sonar-pro (default): General-purpose search with good balance
  - sonar-pro-search: Most advanced agentic search with multi-step reasoning
  - sonar: Standard model for basic searches
  - sonar-reasoning-pro: Advanced reasoning capabilities
  - sonar-reasoning: Basic reasoning model
  - sonar-deep-research: Comprehensive deep research

Available Presets:
  - academic: Scholarly search with academic mode and journal domains
  - technical: Code/documentation search with tech domains
  - news: Recent news excluding social media
  - medical: Clinical/medical research sources
  - legal: Government and legal sources

See .claude/docs/perplexity-best-practices.md for detailed documentation.
        """
    )

    parser.add_argument(
        "query",
        help="The search query"
    )

    parser.add_argument(
        "--model",
        default="sonar-pro",
        choices=[
            "sonar-pro",
            "sonar-pro-search",
            "sonar",
            "sonar-reasoning-pro",
            "sonar-reasoning",
            "sonar-deep-research"
        ],
        help="Perplexity model to use (default: sonar-pro)"
    )

    parser.add_argument(
        "--backend",
        default="auto",
        choices=["auto", "direct", "openrouter"],
        help="API backend: auto (default), direct (Perplexity API), openrouter"
    )

    parser.add_argument(
        "--max-tokens",
        type=int,
        default=4000,
        help="Maximum tokens in response (default: 4000)"
    )

    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="Response temperature 0.0-1.0 (default: 0.2)"
    )

    # Preset and shortcuts
    parser.add_argument(
        "--preset",
        choices=list(PRESETS.keys()),
        help="Use preset configuration (academic, technical, news, medical, legal)"
    )

    parser.add_argument(
        "--academic",
        action="store_true",
        help="Enable academic mode (prioritizes scholarly sources)"
    )

    parser.add_argument(
        "--pro",
        action="store_true",
        help="Enable Pro Search (multi-step reasoning, requires streaming)"
    )

    # Advanced search options
    parser.add_argument(
        "--search-mode",
        choices=["academic"],
        help="Search mode: academic (prioritizes scholarly sources)"
    )

    parser.add_argument(
        "--search-type",
        choices=["fast", "pro", "auto"],
        help="Search type: fast (default), pro (multi-step), auto (classifier)"
    )

    parser.add_argument(
        "--context-size",
        choices=["low", "medium", "high"],
        help="Search context size (affects depth and cost)"
    )

    # Date filtering
    parser.add_argument(
        "--date-after",
        help="Only content published after this date (MM/DD/YYYY or YYYY-MM-DD)"
    )

    parser.add_argument(
        "--date-before",
        help="Only content published before this date (MM/DD/YYYY or YYYY-MM-DD)"
    )

    parser.add_argument(
        "--recency",
        choices=["day", "week", "month", "year"],
        help="Quick recency filter (cannot combine with specific dates)"
    )

    # Domain filtering
    parser.add_argument(
        "--domains",
        help="Comma-separated domain filter. Prefix with - to exclude. E.g.: 'arxiv.org,nature.com' or '-reddit.com,-quora.com'"
    )

    # File attachments
    parser.add_argument(
        "--files",
        help="Comma-separated file paths to attach (PDF, DOC, DOCX, TXT). Max 50MB each, 30 files total."
    )

    parser.add_argument(
        "--stream",
        action="store_true",
        help="Enable streaming (auto-enabled for Pro Search)"
    )

    parser.add_argument(
        "--output",
        help="Save results to JSON file"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed information"
    )

    parser.add_argument(
        "--check-setup",
        action="store_true",
        help="Check if dependencies and API key are configured"
    )

    parser.add_argument(
        "--list-presets",
        action="store_true",
        help="List available presets and their configurations"
    )

    args = parser.parse_args()

    # List presets if requested
    if args.list_presets:
        print("Available Presets:")
        print("="*60)
        for name, config in PRESETS.items():
            print(f"\n{name}:")
            print(f"  Description: {config.get('description', 'No description')}")
            for key, value in config.items():
                if key != 'description':
                    print(f"  {key}: {value}")
        return 0

    # Check setup if requested
    if args.check_setup:
        print("Checking setup...")
        print("\n--- Direct Perplexity API ---")
        direct_key = os.environ.get("PERPLEXITY_API_KEY")
        if direct_key:
            print(f"✓ PERPLEXITY_API_KEY: Set ({direct_key[:10]}...)")
        else:
            print("✗ PERPLEXITY_API_KEY: Not set")

        print("\n--- OpenRouter Backend ---")
        openrouter_key = os.environ.get("OPENROUTER_API_KEY")
        if openrouter_key:
            print(f"✓ OPENROUTER_API_KEY: Set ({openrouter_key[:10]}...)")
        else:
            print("✗ OPENROUTER_API_KEY: Not set")

        try:
            import litellm
            print("✓ LiteLLM: Installed")
        except ImportError:
            print("✗ LiteLLM: Not installed (needed for OpenRouter)")

        print("\n--- Requests Library ---")
        if requests is not None:
            print("✓ requests: Installed")
        else:
            print("✗ requests: Not installed (needed for direct API)")

        print("\n--- Best Practices Documentation ---")
        docs_path = Path(__file__).parent.parent.parent.parent / "docs" / "perplexity-best-practices.md"
        if docs_path.exists():
            print(f"✓ Best practices guide: {docs_path}")
        else:
            print("✗ Best practices guide: Not found")

        if direct_key or openrouter_key:
            print("\n✓ Setup complete! At least one backend is available.")
            return 0
        else:
            print("\n✗ Setup incomplete. Set at least one API key.")
            return 1

    # Parse domain filter
    search_domain_filter = None
    if args.domains:
        search_domain_filter = [d.strip() for d in args.domains.split(",")]

    # Parse files
    files = None
    if args.files:
        files = [f.strip() for f in args.files.split(",")]

    # Perform the search
    result = search_with_perplexity(
        query=args.query,
        model=args.model,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        verbose=args.verbose,
        backend=args.backend,
        preset=args.preset,
        academic=args.academic,
        pro=args.pro,
        search_mode=args.search_mode,
        search_type=args.search_type,
        search_context_size=args.context_size,
        search_after_date=args.date_after,
        search_before_date=args.date_before,
        search_recency_filter=args.recency,
        search_domain_filter=search_domain_filter,
        files=files,
        stream=args.stream
    )

    # Handle results
    if not result["success"]:
        print(f"Error: {result['error']}", file=sys.stderr)
        return 1

    # Print answer
    backend_used = result.get("backend", "unknown")
    streaming = " (streamed)" if result.get("streaming") else ""
    print("\n" + "="*80)
    print(f"ANSWER (via {backend_used} API{streaming})")
    print("="*80)
    print(result["answer"])
    print("="*80)

    # Print citations if available
    if result.get("citations"):
        print("\nCitations:")
        for i, citation in enumerate(result["citations"], 1):
            if isinstance(citation, dict):
                print(f"  [{i}] {citation.get('title', 'Unknown')} - {citation.get('url', '')}")
            else:
                print(f"  [{i}] {citation}")

    # Print reasoning steps if available (Pro Search)
    if result.get("reasoning_steps") and args.verbose:
        print("\nReasoning Steps:")
        for step in result["reasoning_steps"]:
            print(f"  - {step}")

    # Print usage stats if verbose
    if args.verbose and result.get("usage"):
        print(f"\nUsage:", file=sys.stderr)
        usage = result["usage"]
        if "prompt_tokens" in usage:
            print(f"  Prompt tokens: {usage['prompt_tokens']}", file=sys.stderr)
        if "completion_tokens" in usage:
            print(f"  Completion tokens: {usage['completion_tokens']}", file=sys.stderr)
        if "total_tokens" in usage:
            print(f"  Total tokens: {usage['total_tokens']}", file=sys.stderr)

    # Save to file if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\n✓ Results saved to {args.output}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
