#!/usr/bin/env python3
"""
AI Search - Model-Agnostic Web Search

Perform AI-powered web searches using your preferred provider:
- OpenAI (GPT-4o with web browsing)
- Anthropic (Claude with tools)
- Google Gemini (with Search grounding)
- Perplexity (via OpenRouter)

For Claude's built-in WebSearch, no script is needed - just ask Claude directly.

Usage:
    python ai_search.py "search query" --provider openai
    python ai_search.py "search query" --provider gemini --verbose
    python ai_search.py "search query" --provider perplexity --output results.json

Author: Obsidian-Claude
License: MIT
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod


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
# Provider Base Class
# =============================================================================

class SearchProvider(ABC):
    """Abstract base class for search providers."""

    name: str = "base"

    @abstractmethod
    def search(self, query: str, **kwargs) -> Dict[str, Any]:
        """Perform a search and return results."""
        pass

    @abstractmethod
    def check_setup(self) -> bool:
        """Check if provider is properly configured."""
        pass

    def get_api_key_env(self) -> str:
        """Get the environment variable name for API key."""
        return ""


# =============================================================================
# OpenAI Provider
# =============================================================================

class OpenAIProvider(SearchProvider):
    """Search using OpenAI's API."""

    name = "openai"

    def __init__(self, model: str = "gpt-4o"):
        self.model = model
        self.api_key = os.environ.get("OPENAI_API_KEY")

    def get_api_key_env(self) -> str:
        return "OPENAI_API_KEY"

    def check_setup(self) -> bool:
        if not self.api_key:
            print(f"Error: {self.get_api_key_env()} not set", file=sys.stderr)
            print("Get your API key from: https://platform.openai.com/api-keys", file=sys.stderr)
            return False

        try:
            import openai
            return True
        except ImportError:
            print("Error: openai package not installed", file=sys.stderr)
            print("Install with: pip install openai", file=sys.stderr)
            return False

    def search(self, query: str, max_tokens: int = 4000, temperature: float = 0.2, **kwargs) -> Dict[str, Any]:
        if not self.check_setup():
            return {"success": False, "error": "Setup incomplete"}

        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)

            # Create a web search prompt
            system_prompt = """You are a helpful research assistant with access to current web information.
When answering questions:
1. Provide accurate, up-to-date information
2. Cite your sources where possible
3. Be specific and detailed
4. Acknowledge uncertainty when appropriate"""

            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Please search and provide current information on: {query}"}
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )

            return {
                "success": True,
                "provider": self.name,
                "model": self.model,
                "query": query,
                "answer": response.choices[0].message.content,
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens
                }
            }

        except Exception as e:
            return {"success": False, "error": str(e), "provider": self.name}


# =============================================================================
# Anthropic Provider
# =============================================================================

class AnthropicProvider(SearchProvider):
    """Search using Anthropic's Claude API with web search tool."""

    name = "anthropic"

    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        self.model = model
        self.api_key = os.environ.get("ANTHROPIC_API_KEY")

    def get_api_key_env(self) -> str:
        return "ANTHROPIC_API_KEY"

    def check_setup(self) -> bool:
        if not self.api_key:
            print(f"Error: {self.get_api_key_env()} not set", file=sys.stderr)
            print("Get your API key from: https://console.anthropic.com", file=sys.stderr)
            return False

        try:
            import anthropic
            return True
        except ImportError:
            print("Error: anthropic package not installed", file=sys.stderr)
            print("Install with: pip install anthropic", file=sys.stderr)
            return False

    def search(self, query: str, max_tokens: int = 4000, temperature: float = 0.2, **kwargs) -> Dict[str, Any]:
        if not self.check_setup():
            return {"success": False, "error": "Setup incomplete"}

        try:
            import anthropic
            client = anthropic.Anthropic(api_key=self.api_key)

            # Use web_search tool if available (Claude 3.5+)
            response = client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                tools=[{
                    "type": "web_search_20250305",
                    "name": "web_search",
                    "max_uses": 5
                }],
                messages=[{
                    "role": "user",
                    "content": f"Please search for current information on: {query}"
                }]
            )

            # Extract text content
            answer = ""
            for block in response.content:
                if hasattr(block, 'text'):
                    answer += block.text

            return {
                "success": True,
                "provider": self.name,
                "model": self.model,
                "query": query,
                "answer": answer,
                "usage": {
                    "input_tokens": response.usage.input_tokens,
                    "output_tokens": response.usage.output_tokens
                }
            }

        except Exception as e:
            return {"success": False, "error": str(e), "provider": self.name}


# =============================================================================
# Google Gemini Provider
# =============================================================================

class GeminiProvider(SearchProvider):
    """Search using Google Gemini with Search grounding."""

    name = "gemini"

    def __init__(self, model: str = "gemini-2.0-flash"):
        self.model = model
        self.api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")

    def get_api_key_env(self) -> str:
        return "GEMINI_API_KEY"

    def check_setup(self) -> bool:
        if not self.api_key:
            print(f"Error: {self.get_api_key_env()} or GOOGLE_API_KEY not set", file=sys.stderr)
            print("Get your API key from: https://aistudio.google.com/apikey", file=sys.stderr)
            return False

        try:
            import google.generativeai
            return True
        except ImportError:
            print("Error: google-generativeai package not installed", file=sys.stderr)
            print("Install with: pip install google-generativeai", file=sys.stderr)
            return False

    def search(self, query: str, max_tokens: int = 4000, temperature: float = 0.2, **kwargs) -> Dict[str, Any]:
        if not self.check_setup():
            return {"success": False, "error": "Setup incomplete"}

        try:
            import google.generativeai as genai
            from google.generativeai.types import Tool

            genai.configure(api_key=self.api_key)

            # Enable Google Search grounding
            model = genai.GenerativeModel(
                model_name=self.model,
                tools=[Tool(google_search={})]
            )

            response = model.generate_content(
                f"Please search for current information on: {query}",
                generation_config=genai.GenerationConfig(
                    max_output_tokens=max_tokens,
                    temperature=temperature
                )
            )

            return {
                "success": True,
                "provider": self.name,
                "model": self.model,
                "query": query,
                "answer": response.text,
                "grounding_metadata": getattr(response, 'grounding_metadata', None)
            }

        except Exception as e:
            return {"success": False, "error": str(e), "provider": self.name}


# =============================================================================
# Perplexity Provider (via OpenRouter)
# =============================================================================

class PerplexityProvider(SearchProvider):
    """Search using Perplexity via OpenRouter."""

    name = "perplexity"

    def __init__(self, model: str = "sonar-pro"):
        self.model = model
        self.api_key = os.environ.get("OPENROUTER_API_KEY")

    def get_api_key_env(self) -> str:
        return "OPENROUTER_API_KEY"

    def check_setup(self) -> bool:
        if not self.api_key:
            print(f"Error: {self.get_api_key_env()} not set", file=sys.stderr)
            print("Get your API key from: https://openrouter.ai/keys", file=sys.stderr)
            return False

        try:
            import litellm
            return True
        except ImportError:
            print("Error: litellm package not installed", file=sys.stderr)
            print("Install with: pip install litellm", file=sys.stderr)
            return False

    def search(self, query: str, max_tokens: int = 4000, temperature: float = 0.2, **kwargs) -> Dict[str, Any]:
        if not self.check_setup():
            return {"success": False, "error": "Setup incomplete"}

        try:
            from litellm import completion

            # Format model name for OpenRouter
            model = self.model
            if not model.startswith("openrouter/"):
                model = f"openrouter/perplexity/{model}"

            response = completion(
                model=model,
                messages=[{"role": "user", "content": query}],
                max_tokens=max_tokens,
                temperature=temperature
            )

            result = {
                "success": True,
                "provider": self.name,
                "model": self.model,
                "query": query,
                "answer": response.choices[0].message.content,
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens
                }
            }

            # Include citations if available
            if hasattr(response.choices[0].message, 'citations'):
                result["citations"] = response.choices[0].message.citations

            return result

        except Exception as e:
            return {"success": False, "error": str(e), "provider": self.name}


# =============================================================================
# Provider Factory
# =============================================================================

PROVIDERS = {
    "openai": OpenAIProvider,
    "anthropic": AnthropicProvider,
    "gemini": GeminiProvider,
    "perplexity": PerplexityProvider
}

def get_provider(name: str, **kwargs) -> SearchProvider:
    """Get a search provider by name."""
    if name not in PROVIDERS:
        raise ValueError(f"Unknown provider: {name}. Available: {list(PROVIDERS.keys())}")
    return PROVIDERS[name](**kwargs)


# =============================================================================
# Main CLI
# =============================================================================

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="AI-powered web search with multiple providers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # OpenAI
  python ai_search.py "CRISPR developments 2024" --provider openai

  # Google Gemini
  python ai_search.py "AlphaFold 3 improvements" --provider gemini

  # Anthropic
  python ai_search.py "mRNA vaccine research" --provider anthropic

  # Perplexity (via OpenRouter)
  python ai_search.py "machine learning trends" --provider perplexity --model sonar-pro-search

  # Save to file
  python ai_search.py "query" --provider openai --output results.json

For Claude's built-in WebSearch (recommended), no script is needed - just ask Claude directly.
        """
    )

    parser.add_argument("query", help="Search query")

    parser.add_argument(
        "--provider", "-p",
        choices=list(PROVIDERS.keys()),
        required=True,
        help="Search provider to use"
    )

    parser.add_argument(
        "--model", "-m",
        help="Model to use (provider-specific)"
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

    parser.add_argument(
        "--output", "-o",
        help="Save results to JSON file"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print detailed information"
    )

    parser.add_argument(
        "--check-setup",
        action="store_true",
        help="Check if provider is configured"
    )

    args = parser.parse_args()

    # Build provider kwargs
    provider_kwargs = {}
    if args.model:
        provider_kwargs["model"] = args.model

    # Get provider
    try:
        provider = get_provider(args.provider, **provider_kwargs)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Check setup if requested
    if args.check_setup:
        print(f"Checking {args.provider} setup...")
        if provider.check_setup():
            print(f"\n[OK] {args.provider} is configured and ready.")
            return 0
        else:
            print(f"\n[FAIL] {args.provider} setup incomplete.")
            return 1

    if args.verbose:
        print(f"Provider: {args.provider}", file=sys.stderr)
        print(f"Query: {args.query}", file=sys.stderr)
        print(f"Max tokens: {args.max_tokens}", file=sys.stderr)
        print(f"Temperature: {args.temperature}", file=sys.stderr)
        print("", file=sys.stderr)

    # Perform search
    result = provider.search(
        args.query,
        max_tokens=args.max_tokens,
        temperature=args.temperature
    )

    # Handle results
    if not result.get("success"):
        print(f"Error: {result.get('error', 'Unknown error')}", file=sys.stderr)
        return 1

    # Print answer
    print("\n" + "=" * 80)
    print(f"ANSWER (via {args.provider})")
    print("=" * 80)
    print(result.get("answer", "No answer"))
    print("=" * 80)

    # Print usage stats if verbose
    if args.verbose and result.get("usage"):
        print(f"\nUsage:", file=sys.stderr)
        for key, value in result["usage"].items():
            print(f"  {key}: {value}", file=sys.stderr)

    # Save to file if requested
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to {args.output}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
