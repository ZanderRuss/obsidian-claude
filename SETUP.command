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
pip install --quiet -r .claude/skills/requirements.txt
if [ $? -ne 0 ]; then
    echo "[!] Could not install packages"
    echo "Please ask for help in the GitHub Issues."
    read -p "Press Enter to close..."
    exit 1
fi
echo "[OK] All packages installed"
echo ""

echo "============================================"
echo "     SETUP COMPLETE!"
echo "============================================"
echo ""
echo "WHAT TO DO NEXT:"
echo ""
echo "1. Open the Claude Desktop app"
echo ""
echo "2. Open the file 'Claude-Instructions.md'"
echo "   (it's in the same folder as this script)"
echo ""
echo "3. Copy ALL the text from that file"
echo ""
echo "4. Paste the text into Claude Desktop"
echo ""
echo "5. Claude will guide you through the rest!"
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
