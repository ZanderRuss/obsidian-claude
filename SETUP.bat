@echo off
title Obsidian-Claude Setup
color 0A

echo.
echo  ============================================
echo       OBSIDIAN-CLAUDE SETUP
echo  ============================================
echo.
echo  This will prepare your computer to use
echo  Claude with your Obsidian vault.
echo.
echo  Please wait while we set things up...
echo.
echo  ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo  [!] Python is not installed on your computer.
    echo.
    echo  Python is a free program that some features need.
    echo  Don't worry - it's easy to install!
    echo.
    echo  I'm opening the download page for you now...
    echo.
    start https://www.python.org/downloads/
    echo.
    echo  INSTALLATION STEPS:
    echo  1. Click the big yellow "Download Python" button
    echo  2. Run the downloaded file
    echo  3. IMPORTANT: Check the box "Add Python to PATH"
    echo  4. Click "Install Now"
    echo  5. When done, come back here and press any key
    echo.
    pause
    echo.
    echo  Checking if Python installed correctly...
    python --version >nul 2>&1
    if errorlevel 1 (
        echo  [!] Python still not detected.
        echo  You may need to restart your computer and try again.
        pause
        exit /b 1
    )
    echo  [OK] Python is now installed! Continuing setup...
)

echo  [OK] Python is installed
echo.

REM Check if venv already exists
if exist ".venv" (
    echo  [OK] Virtual environment already exists
) else (
    echo  Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo  [!] Could not create virtual environment
        echo  Please ask for help in the GitHub Issues.
        pause
        exit /b 1
    )
    echo  [OK] Virtual environment created
)
echo.

REM Activate and install packages
echo  Installing required packages...
echo  (This may take 1-2 minutes)
echo.
call .venv\Scripts\activate.bat
python -m pip install --quiet --upgrade pip 2>nul

REM Install UV for MCP tools
echo  Installing UV (for MCP server)...
pip install --quiet uv 2>nul
if errorlevel 1 (
    echo  [!] Warning: Could not install UV. MCP features may not work.
) else (
    echo  [OK] UV installed
)

REM Install skills requirements
pip install --quiet -r .claude\skills\requirements.txt 2>nul
if errorlevel 1 (
    echo  [!] Could not install some packages
    echo  Some skills may not work, but you can continue.
)
echo  [OK] Packages installed
echo.

REM Create mcp.json from example if it doesn't exist
if not exist ".claude\mcp.json" (
    if exist ".claude\mcp.json.example" (
        copy ".claude\mcp.json.example" ".claude\mcp.json" >nul
        echo  [OK] Created MCP configuration file
        echo.
        echo  ============================================
        echo       IMPORTANT: API KEY NEEDED
        echo  ============================================
        echo.
        echo  To connect Claude to Obsidian, you need an API key:
        echo.
        echo  1. Open Obsidian
        echo  2. Go to Settings ^> Community Plugins
        echo  3. Search for "Local REST API" and install it
        echo  4. Enable the plugin
        echo  5. Go to the plugin settings
        echo  6. Copy the API key shown there
        echo.
        echo  Then edit this file and paste your key:
        echo  %~dp0.claude\mcp.json
        echo.
        echo  Replace "YOUR_API_KEY_HERE" with your actual key.
        echo.
    )
) else (
    echo  [OK] MCP configuration already exists
)

echo  ============================================
echo       SETUP COMPLETE!
echo  ============================================
echo.
echo  WHAT TO DO NEXT:
echo.
echo  1. Open Obsidian and install "Local REST API" plugin
echo     (if you haven't already)
echo.
echo  2. Copy your API key from the plugin settings
echo.
echo  3. Edit .claude\mcp.json and add your API key
echo.
echo  4. Open this folder in Claude Code Desktop
echo.
echo  5. Ask Claude: "Help me verify the setup"
echo.
echo  ============================================
echo.
echo  Opening the Claude-Instructions file now...
echo.

start notepad "%~dp0Claude-Instructions.md"

echo  Press any key to close this window...
pause >nul
