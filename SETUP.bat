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
pip install --quiet --upgrade pip
pip install --quiet -r .claude\skills\requirements.txt
if errorlevel 1 (
    echo  [!] Could not install packages
    echo  Please ask for help in the GitHub Issues.
    pause
    exit /b 1
)
echo  [OK] All packages installed
echo.

echo  ============================================
echo       SETUP COMPLETE!
echo  ============================================
echo.
echo  WHAT TO DO NEXT:
echo.
echo  1. Open the Claude Desktop app
echo.
echo  2. A file called "Claude-Instructions.md" will
echo     open in Notepad. Copy ALL the text.
echo.
echo  3. Paste the text into Claude Desktop
echo.
echo  4. Claude will guide you through the rest!
echo.
echo  ============================================
echo.
echo  Opening the instructions file now...
echo.

start notepad "%~dp0Claude-Instructions.md"

echo  Press any key to close this window...
pause >nul
