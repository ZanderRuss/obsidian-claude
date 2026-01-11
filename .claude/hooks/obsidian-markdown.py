#!/usr/bin/env python3
"""
Hook: Obsidian Markdown Converter
Triggers on: PreToolUse (Edit, Write, MultiEdit)
Purpose: Auto-convert standard markdown to Obsidian Flavored Markdown

Conversions:
- [text](file.md) → [[file|text]]
- Standard blockquotes → Callouts where appropriate
- Ensures frontmatter exists
"""

import json
import re
import sys
from datetime import date


def convert_markdown_links_to_wikilinks(text: str) -> str:
    """Convert [text](file.md) to [[file|text]] for internal links."""
    # Match markdown links to .md files (not external URLs)
    # Pattern: [display text](filename.md) or [display text](path/to/file.md)
    pattern = r'\[([^\]]+)\]\((?!https?://)([^)]+\.md)(?:#[^)]*)?\)'

    def replace_link(match):
        display = match.group(1)
        filepath = match.group(2)
        # Remove .md extension and path
        filename = filepath.replace('.md', '').split('/')[-1]

        if display == filename:
            return f'[[{filename}]]'
        else:
            return f'[[{filename}|{display}]]'

    return re.sub(pattern, replace_link, text)


def convert_image_embeds(text: str) -> str:
    """Convert ![alt](image.png) to ![[image.png]] for local images."""
    # Match markdown images (not external URLs)
    pattern = r'!\[([^\]]*)\]\((?!https?://)([^)]+)\)'

    def replace_image(match):
        alt = match.group(1)
        filepath = match.group(2)
        filename = filepath.split('/')[-1]

        # Check if there's a size specification in alt text like "alt|300"
        if '|' in alt:
            return f'![[{filename}|{alt.split("|")[1]}]]'
        return f'![[{filename}]]'

    return re.sub(pattern, replace_image, text)


def ensure_frontmatter(text: str) -> str:
    """Ensure note has frontmatter with required fields."""
    # Check if frontmatter exists
    if text.startswith('---'):
        # Frontmatter exists, check if it has required fields
        end_match = re.search(r'^---\s*$', text[3:], re.MULTILINE)
        if end_match:
            frontmatter_end = end_match.start() + 3
            frontmatter = text[3:frontmatter_end]

            # Check for missing fields
            missing = []
            if 'tags:' not in frontmatter:
                missing.append('tags:\n  - uncategorized')
            if 'type:' not in frontmatter:
                missing.append('type: note')
            if 'created:' not in frontmatter:
                missing.append(f'created: {date.today().isoformat()}')
            if 'status:' not in frontmatter:
                missing.append('status: draft')

            if missing:
                # Insert missing fields before closing ---
                insert_pos = frontmatter_end
                insert_text = '\n'.join(missing) + '\n'
                text = text[:insert_pos] + insert_text + text[insert_pos:]

        return text

    # No frontmatter, add it
    frontmatter = f"""---
tags:
  - uncategorized
type: note
created: {date.today().isoformat()}
status: draft
---

"""
    return frontmatter + text


def convert_blockquotes_to_callouts(text: str) -> str:
    """Convert plain blockquotes that look like notes/warnings to callouts.

    Only converts blockquotes that start with common indicator words.
    """
    # Pattern for blockquotes starting with Note:, Warning:, Tip:, etc.
    indicators = {
        r'^>\s*\*?\*?Note\*?\*?:?\s*': '> [!note]\n> ',
        r'^>\s*\*?\*?Warning\*?\*?:?\s*': '> [!warning]\n> ',
        r'^>\s*\*?\*?Tip\*?\*?:?\s*': '> [!tip]\n> ',
        r'^>\s*\*?\*?Important\*?\*?:?\s*': '> [!important]\n> ',
        r'^>\s*\*?\*?Caution\*?\*?:?\s*': '> [!caution]\n> ',
        r'^>\s*\*?\*?Info\*?\*?:?\s*': '> [!info]\n> ',
        r'^>\s*\*?\*?Example\*?\*?:?\s*': '> [!example]\n> ',
    }

    for pattern, replacement in indicators.items():
        text = re.sub(pattern, replacement, text, flags=re.MULTILINE | re.IGNORECASE)

    return text


def process_content(content: str) -> str:
    """Apply all Obsidian markdown conversions."""
    content = convert_markdown_links_to_wikilinks(content)
    content = convert_image_embeds(content)
    content = convert_blockquotes_to_callouts(content)
    content = ensure_frontmatter(content)
    return content


# Paths that should receive Obsidian Markdown processing
VAULT_PATH_PATTERNS = [
    'Obsidian-Template-Vault',
    '3. Resources',
    '1. Projects',
    '2. Areas',
    '0. Inbox',
    '4. Archive',
    '6. Metadata'
]


def is_vault_file(file_path: str) -> bool:
    """Check if file is in an Obsidian vault location."""
    if not file_path.endswith('.md'):
        return False
    return any(pattern in file_path for pattern in VAULT_PATH_PATTERNS)


def main():
    # Read hook input from stdin
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        # No valid JSON input, pass through
        sys.exit(0)

    # Check if this is a file operation on the vault
    tool_name = input_data.get('tool_name', '')
    tool_input = input_data.get('tool_input', {})

    if tool_name not in ['Edit', 'Write', 'MultiEdit']:
        # Not a file write operation, pass through
        sys.exit(0)

    # Get file path
    file_path = tool_input.get('file_path', '')

    # Only process .md files in Obsidian vault locations
    if not is_vault_file(file_path):
        sys.exit(0)

    # For Write tool, process the content
    if tool_name == 'Write':
        content = tool_input.get('content', '')
        if content:
            new_content = process_content(content)
            if new_content != content:
                # Content was modified, output the modified tool input
                tool_input['content'] = new_content
                result = {
                    'decision': 'modify',
                    'modified_tool_input': tool_input
                }
                print(json.dumps(result))
                sys.exit(0)

    # For Edit tool, process the new_string
    elif tool_name == 'Edit':
        new_string = tool_input.get('new_string', '')
        if new_string:
            new_content = convert_markdown_links_to_wikilinks(new_string)
            new_content = convert_image_embeds(new_content)
            new_content = convert_blockquotes_to_callouts(new_content)
            if new_content != new_string:
                tool_input['new_string'] = new_content
                result = {
                    'decision': 'modify',
                    'modified_tool_input': tool_input
                }
                print(json.dumps(result))
                sys.exit(0)

    # For MultiEdit tool, process each edit's new_string
    elif tool_name == 'MultiEdit':
        edits = tool_input.get('edits', [])
        modified = False
        for edit in edits:
            new_string = edit.get('new_string', '')
            if new_string:
                new_content = convert_markdown_links_to_wikilinks(new_string)
                new_content = convert_image_embeds(new_content)
                new_content = convert_blockquotes_to_callouts(new_content)
                if new_content != new_string:
                    edit['new_string'] = new_content
                    modified = True

        if modified:
            tool_input['edits'] = edits
            result = {
                'decision': 'modify',
                'modified_tool_input': tool_input
            }
            print(json.dumps(result))
            sys.exit(0)

    # No modifications needed
    sys.exit(0)


if __name__ == '__main__':
    main()
