#!/bin/bash
# Obsidian-Claude Setup Script for Linux/macOS
# Run this script to set up the Claude Code integration for your Obsidian vault

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Options
VAULT_PATH=""
SKIP_PYTHON=false
SKIP_OBSIDIAN_PLUGINS=false

print_header() {
    echo -e "\n${CYAN}========================================"
    echo -e "  $1"
    echo -e "========================================${NC}\n"
}

print_step() {
    echo -e "${GREEN}[+] $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}[!] $1${NC}"
}

print_error() {
    echo -e "${RED}[X] $1${NC}"
}

show_help() {
    cat << EOF
Obsidian-Claude Setup Script

USAGE:
    ./setup.sh [-v <vault_path>] [-p] [-o]

OPTIONS:
    -v, --vault      Path to your Obsidian vault (will prompt if not provided)
    -p, --skip-python    Skip Python tool installation (Zotero MCP, PaperQA2)
    -o, --skip-obsidian  Skip Obsidian plugin reminders
    -h, --help       Show this help message

EXAMPLES:
    ./setup.sh
    ./setup.sh -v ~/Documents/MyVault
    ./setup.sh --skip-python
EOF
    exit 0
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--vault)
            VAULT_PATH="$2"
            shift 2
            ;;
        -p|--skip-python)
            SKIP_PYTHON=true
            shift
            ;;
        -o|--skip-obsidian)
            SKIP_OBSIDIAN_PLUGINS=true
            shift
            ;;
        -h|--help)
            show_help
            ;;
        *)
            shift
            ;;
    esac
done

print_header "Obsidian-Claude Setup"

# Check prerequisites
print_step "Checking prerequisites..."

# Check for Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    print_step "Node.js: $NODE_VERSION"
else
    print_error "Node.js not found. Please install from https://nodejs.org"
    exit 1
fi

# Check for Python
if [ "$SKIP_PYTHON" = false ]; then
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        print_step "Python: $PYTHON_VERSION"
    elif command -v python &> /dev/null; then
        PYTHON_VERSION=$(python --version)
        print_step "Python: $PYTHON_VERSION"
    else
        print_warning "Python not found. Skipping Python tools."
        SKIP_PYTHON=true
    fi
fi

# Check for Claude Code
if command -v claude &> /dev/null; then
    print_step "Claude Code: Installed"
else
    print_error "Claude Code not found. Install from https://claude.ai/code"
    exit 1
fi

# Get vault path
if [ -z "$VAULT_PATH" ]; then
    echo -e "\nEnter the path to your Obsidian vault:"
    read -r VAULT_PATH
fi

# Expand tilde
VAULT_PATH="${VAULT_PATH/#\~/$HOME}"

if [ ! -d "$VAULT_PATH" ]; then
    print_error "Vault path not found: $VAULT_PATH"
    exit 1
fi

print_step "Vault path: $VAULT_PATH"

# Create .claude directory structure
print_header "Setting up Claude Code configuration"

CLAUDE_DIR="$VAULT_PATH/.claude"
mkdir -p "$CLAUDE_DIR/commands"
mkdir -p "$CLAUDE_DIR/agents/research-team"
mkdir -p "$CLAUDE_DIR/hooks"

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_ROOT="$(dirname "$SCRIPT_DIR")"
SOURCE_CLAUDE_DIR="$SOURCE_ROOT/.claude"

if [ -d "$SOURCE_CLAUDE_DIR" ]; then
    print_step "Copying Claude Code configuration..."

    # Copy commands
    if [ -d "$SOURCE_CLAUDE_DIR/commands" ]; then
        cp -r "$SOURCE_CLAUDE_DIR/commands/"* "$CLAUDE_DIR/commands/" 2>/dev/null || true
        CMD_COUNT=$(find "$CLAUDE_DIR/commands" -name "*.md" 2>/dev/null | wc -l)
        print_step "Copied $CMD_COUNT commands"
    fi

    # Copy agents
    if [ -d "$SOURCE_CLAUDE_DIR/agents" ]; then
        cp -r "$SOURCE_CLAUDE_DIR/agents/"* "$CLAUDE_DIR/agents/" 2>/dev/null || true
        AGENT_COUNT=$(find "$CLAUDE_DIR/agents" -name "*.md" 2>/dev/null | wc -l)
        print_step "Copied $AGENT_COUNT agents"
    fi

    # Copy mcp.json.example
    if [ -f "$SOURCE_CLAUDE_DIR/mcp.json.example" ]; then
        cp "$SOURCE_CLAUDE_DIR/mcp.json.example" "$CLAUDE_DIR/mcp.json.example"
        print_step "Copied MCP configuration template"
    fi

    # Create mcp.json from example if it doesn't exist
    if [ ! -f "$CLAUDE_DIR/mcp.json" ] && [ -f "$CLAUDE_DIR/mcp.json.example" ]; then
        cp "$CLAUDE_DIR/mcp.json.example" "$CLAUDE_DIR/mcp.json"
        print_step "Created mcp.json from template"
        print_warning "Edit $CLAUDE_DIR/mcp.json and add your Obsidian API key"
    fi
fi

# Copy CLAUDE.md
if [ -f "$SOURCE_ROOT/CLAUDE.md" ]; then
    cp "$SOURCE_ROOT/CLAUDE.md" "$VAULT_PATH/CLAUDE.md"
    print_step "Copied CLAUDE.md"
fi

# Create PARA structure
print_header "Checking PARA structure"

PARA_FOLDERS=(
    "0. Inbox"
    "1. Projects"
    "2. Areas (Ongoing)"
    "3. Resources (Dynamic)"
    "4. Archive (Supportive)"
    "6. Metadata"
    "6. Metadata/Templates"
    "6. Metadata/Workflows"
    "6. Metadata/Reference"
)

for folder in "${PARA_FOLDERS[@]}"; do
    FOLDER_PATH="$VAULT_PATH/$folder"
    if [ ! -d "$FOLDER_PATH" ]; then
        mkdir -p "$FOLDER_PATH"
        print_step "Created PARA folder: $folder"
    fi
done

# Copy templates
SOURCE_TEMPLATES="$SOURCE_ROOT/Obsidian-Vault-Live/6. Metadata/Templates"
DEST_TEMPLATES="$VAULT_PATH/6. Metadata/Templates"
if [ -d "$SOURCE_TEMPLATES" ]; then
    cp -r "$SOURCE_TEMPLATES/"* "$DEST_TEMPLATES/" 2>/dev/null || true
    TEMPLATE_COUNT=$(find "$DEST_TEMPLATES" -name "*.md" 2>/dev/null | wc -l)
    print_step "Copied $TEMPLATE_COUNT templates"
fi

# Install Python tools
if [ "$SKIP_PYTHON" = false ]; then
    print_header "Installing Python tools"

    print_step "Installing uv..."
    pip install uv 2>/dev/null || pip3 install uv 2>/dev/null || true

    print_step "Installing Zotero MCP..."
    uv tool install "git+https://github.com/54yyyu/zotero-mcp.git" 2>/dev/null || true

    print_step "Installing PaperQA2..."
    pip install "paper-qa>=5" 2>/dev/null || pip3 install "paper-qa>=5" 2>/dev/null || true

    print_step "Python tools installed"
fi

# Obsidian plugin reminders
if [ "$SKIP_OBSIDIAN_PLUGINS" = false ]; then
    print_header "Obsidian Plugin Setup"
    cat << EOF
Please install these Obsidian plugins:

REQUIRED:
  - Local REST API (for Claude Code integration)
    Settings: Enable HTTPS, Port 27124

RECOMMENDED:
  - Dataview (for querying notes)
  - Smart Connections (AI-powered linking)
  - Templater (advanced templates)

After installing Local REST API:
  1. Copy the API key from plugin settings
  2. Paste it in: $CLAUDE_DIR/mcp.json
EOF
fi

# Final instructions
print_header "Setup Complete!"

cat << EOF
Next steps:

1. Open your vault in Obsidian
2. Install the Local REST API plugin
3. Copy your API key to: $CLAUDE_DIR/mcp.json
4. Run Claude Code in your vault:

   cd "$VAULT_PATH"
   claude

5. Try a command:
   /thinking-partner
   /daily-review
   /research-ideate

For research tools (if Zotero is installed):
   zotero-mcp setup
   zotero-mcp update-db --fulltext

Documentation: $VAULT_PATH/CLAUDE.md
EOF
