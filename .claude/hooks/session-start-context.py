#!/usr/bin/env python3
"""
Hook: Session Start Context
Triggers on: SessionStart
Purpose: Output vault structure and status at session start

This hook provides immediate context about the Obsidian vault when
a Claude Code session begins, helping agents orient quickly without
needing to explore the filesystem first.
"""

import json
import sys
from pathlib import Path


# Relative to project root where Claude Code runs
VAULT_PATH = Path("Obsidian-Vault-Live")


def get_folder_structure() -> str:
    """Generate concise folder overview with note counts."""
    if not VAULT_PATH.exists():
        return "  (Vault not found at expected path)"

    structure = []
    for item in sorted(VAULT_PATH.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            # Count markdown files recursively
            count = len(list(item.rglob("*.md")))
            structure.append(f"  {item.name}/ ({count} notes)")

    return "\n".join(structure) if structure else "  (No folders found)"


def count_inbox_items() -> int:
    """Count items in inbox folder, excluding template files."""
    inbox_path = VAULT_PATH / "0. Inbox"
    if not inbox_path.exists():
        return 0

    # Exclude known template/placeholder files
    exclude = {"Daily Note.md", "Welcome to Your Inbox.md"}
    items = [f for f in inbox_path.glob("*.md") if f.name not in exclude]
    return len(items)


def get_moc_count() -> int:
    """Count MOC files in vault."""
    if not VAULT_PATH.exists():
        return 0
    return len(list(VAULT_PATH.rglob("MOC - *.md")))


def get_recent_changes(days: int = 7) -> int:
    """Count files modified in the last N days."""
    if not VAULT_PATH.exists():
        return 0

    import time
    cutoff = time.time() - (days * 24 * 60 * 60)

    count = 0
    for f in VAULT_PATH.rglob("*.md"):
        try:
            if f.stat().st_mtime > cutoff:
                count += 1
        except (OSError, PermissionError):
            continue

    return count


def main():
    # Read hook input from stdin
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        # No valid input, exit silently
        sys.exit(0)

    # Generate context message
    inbox_count = count_inbox_items()
    moc_count = get_moc_count()
    recent_count = get_recent_changes(7)

    # Build status indicators
    inbox_status = f"{inbox_count} items"
    if inbox_count > 10:
        inbox_status += " ⚠️ (needs processing)"
    elif inbox_count == 0:
        inbox_status += " ✓"

    context = f"""
📁 **Vault Structure**
{get_folder_structure()}

📊 **Status**
- Inbox: {inbox_status}
- MOCs: {moc_count} Maps of Content
- Recent: {recent_count} files modified (7 days)
- Index: [[VAULT-INDEX]] for quick reference

💡 **Quick Start**
- PARA: Inbox → Projects/Areas/Resources → Archive
- Key commands: /thinking-partner, /research-assistant, /vault-review
- See CLAUDE.md for full documentation
""".strip()

    # Return allow decision with context message
    result = {
        'decision': 'allow',
        'message': context
    }
    print(json.dumps(result))
    sys.exit(0)


if __name__ == '__main__':
    main()
