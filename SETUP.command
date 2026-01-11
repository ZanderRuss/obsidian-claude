#!/bin/bash

# Change to the directory where this script is located
cd "$(dirname "$0")"

clear
echo ""
echo "============================================"
echo "     OBSIDIAN-CLAUDE SETUP"
echo "============================================"
echo ""
echo "This will prepare your computer to use"
echo "Claude with your Obsidian vault."
echo ""
echo "Please wait while we set things up..."
echo ""
echo "============================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "[!] Python 3 is not installed on your computer."
    echo ""
    echo "TO FIX THIS:"
    echo "1. Go to: https://www.python.org/downloads/"
    echo "2. Download Python for Mac"
    echo "3. Run the installer"
    echo "4. After installing, run this setup again"
    echo ""
    read -p "Press Enter to close..."
    exit 1
fi

echo "[OK] Python is installed"
echo ""

# Check if venv already exists
if [ -d ".venv" ]; then
    echo "[OK] Virtual environment already exists"
else
    echo "Creating virtual environment..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "[!] Could not create virtual environment"
        echo "Please ask for help in the GitHub Issues."
        read -p "Press Enter to close..."
        exit 1
    fi
    echo "[OK] Virtual environment created"
fi
echo ""

# Activate and install packages
echo "Installing required packages..."
echo "(This may take 1-2 minutes)"
echo ""
source .venv/bin/activate
pip install --quiet --upgrade pip

# Install UV for MCP tools
echo "Installing UV (for MCP server)..."
pip install --quiet uv
if [ $? -eq 0 ]; then
    echo "[OK] UV installed"
else
    echo "[!] Warning: Could not install UV. MCP features may not work."
fi

# Install skills requirements
pip install --quiet -r .claude/skills/requirements.txt
if [ $? -ne 0 ]; then
    echo "[!] Could not install some packages"
    echo "Some skills may not work, but you can continue."
fi
echo "[OK] Packages installed"
echo ""

# Create mcp.json from example if it doesn't exist
if [ ! -f ".claude/mcp.json" ]; then
    if [ -f ".claude/mcp.json.example" ]; then
        cp ".claude/mcp.json.example" ".claude/mcp.json"
        echo "[OK] Created MCP configuration file"
        echo ""
        echo "============================================"
        echo "     IMPORTANT: API KEY NEEDED"
        echo "============================================"
        echo ""
        echo "To connect Claude to Obsidian, you need an API key:"
        echo ""
        echo "1. Open Obsidian"
        echo "2. Go to Settings > Community Plugins"
        echo "3. Search for 'Local REST API' and install it"
        echo "4. Enable the plugin"
        echo "5. Go to the plugin settings"
        echo "6. Copy the API key shown there"
        echo ""
        echo "Then edit this file and paste your key:"
        echo "$(pwd)/.claude/mcp.json"
        echo ""
        echo "Replace 'YOUR_API_KEY_HERE' with your actual key."
        echo ""
    fi
else
    echo "[OK] MCP configuration already exists"
fi

echo "============================================"
echo "     SETUP COMPLETE!"
echo "============================================"
echo ""
echo "WHAT TO DO NEXT:"
echo ""
echo "1. Open Obsidian and install 'Local REST API' plugin"
echo "   (if you haven't already)"
echo ""
echo "2. Copy your API key from the plugin settings"
echo ""
echo "3. Edit .claude/mcp.json and add your API key"
echo ""
echo "4. Open this folder in Claude Code Desktop"
echo ""
echo "5. Ask Claude: 'Help me verify the setup'"
echo ""
echo "============================================"
echo ""

# Try to open the instructions file
if command -v open &> /dev/null; then
    open "Claude-Instructions.md"
elif command -v xdg-open &> /dev/null; then
    xdg-open "Claude-Instructions.md"
fi

read -p "Press Enter to close this window..."
