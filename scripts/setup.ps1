# Obsidian-Claude Setup Script for Windows
# Run this script to set up the Claude Code integration for your Obsidian vault

param(
    [string]$VaultPath = "",
    [switch]$SkipPython,
    [switch]$SkipObsidianPlugins,
    [switch]$Help
)

$ErrorActionPreference = "Stop"

function Write-Header {
    param([string]$Text)
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "  $Text" -ForegroundColor Cyan
    Write-Host "========================================`n" -ForegroundColor Cyan
}

function Write-Step {
    param([string]$Text)
    Write-Host "[+] $Text" -ForegroundColor Green
}

function Write-Warning {
    param([string]$Text)
    Write-Host "[!] $Text" -ForegroundColor Yellow
}

function Write-Error {
    param([string]$Text)
    Write-Host "[X] $Text" -ForegroundColor Red
}

if ($Help) {
    Write-Host @"
Obsidian-Claude Setup Script

USAGE:
    .\setup.ps1 [-VaultPath <path>] [-SkipPython] [-SkipObsidianPlugins]

OPTIONS:
    -VaultPath              Path to your Obsidian vault (will prompt if not provided)
    -SkipPython            Skip Python tool installation (Zotero MCP, PaperQA2)
    -SkipObsidianPlugins   Skip Obsidian plugin reminders
    -Help                  Show this help message

EXAMPLES:
    .\setup.ps1
    .\setup.ps1 -VaultPath "C:\Users\Me\Documents\MyVault"
    .\setup.ps1 -SkipPython
"@
    exit 0
}

Write-Header "Obsidian-Claude Setup"

# Check prerequisites
Write-Step "Checking prerequisites..."

# Check for Node.js
try {
    $nodeVersion = node --version 2>$null
    Write-Step "Node.js: $nodeVersion"
} catch {
    Write-Error "Node.js not found. Please install from https://nodejs.org"
    exit 1
}

# Check for Python
if (-not $SkipPython) {
    try {
        $pythonVersion = python --version 2>$null
        Write-Step "Python: $pythonVersion"
    } catch {
        Write-Warning "Python not found. Skipping Python tools."
        $SkipPython = $true
    }
}

# Check for Claude Code
try {
    $claudeVersion = claude --version 2>$null
    Write-Step "Claude Code: Installed"
} catch {
    Write-Error "Claude Code not found. Install from https://claude.ai/code"
    exit 1
}

# Get vault path
if (-not $VaultPath) {
    Write-Host "`nEnter the path to your Obsidian vault:" -ForegroundColor White
    $VaultPath = Read-Host
}

if (-not (Test-Path $VaultPath)) {
    Write-Error "Vault path not found: $VaultPath"
    exit 1
}

Write-Step "Vault path: $VaultPath"

# Create .claude directory structure
Write-Header "Setting up Claude Code configuration"

$claudeDir = Join-Path $VaultPath ".claude"
$dirs = @(
    "$claudeDir\commands",
    "$claudeDir\agents",
    "$claudeDir\agents\research-team",
    "$claudeDir\hooks"
)

foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Step "Created: $dir"
    }
}

# Copy configuration files
$scriptRoot = Split-Path -Parent $PSScriptRoot
$sourceClaudeDir = Join-Path $scriptRoot ".claude"

if (Test-Path $sourceClaudeDir) {
    Write-Step "Copying Claude Code configuration..."

    # Copy commands
    $sourceCommands = Join-Path $sourceClaudeDir "commands"
    $destCommands = Join-Path $claudeDir "commands"
    if (Test-Path $sourceCommands) {
        Copy-Item -Path "$sourceCommands\*" -Destination $destCommands -Recurse -Force
        $cmdCount = (Get-ChildItem $destCommands -Filter "*.md").Count
        Write-Step "Copied $cmdCount commands"
    }

    # Copy agents
    $sourceAgents = Join-Path $sourceClaudeDir "agents"
    $destAgents = Join-Path $claudeDir "agents"
    if (Test-Path $sourceAgents) {
        Copy-Item -Path "$sourceAgents\*" -Destination $destAgents -Recurse -Force
        $agentCount = (Get-ChildItem $destAgents -Filter "*.md" -Recurse).Count
        Write-Step "Copied $agentCount agents"
    }

    # Copy mcp.json (but don't overwrite API keys)
    $sourceMcp = Join-Path $sourceClaudeDir "mcp.json"
    $destMcp = Join-Path $claudeDir "mcp.json"
    if ((Test-Path $sourceMcp) -and (-not (Test-Path $destMcp))) {
        Copy-Item -Path $sourceMcp -Destination $destMcp
        Write-Step "Copied MCP configuration"
        Write-Warning "Edit $destMcp and add your Obsidian API key"
    }
}

# Copy CLAUDE.md
$sourceClaude = Join-Path $scriptRoot "CLAUDE.md"
$destClaude = Join-Path $VaultPath "CLAUDE.md"
if (Test-Path $sourceClaude) {
    Copy-Item -Path $sourceClaude -Destination $destClaude -Force
    Write-Step "Copied CLAUDE.md"
}

# Create PARA structure if it doesn't exist
Write-Header "Checking PARA structure"

$paraFolders = @(
    "0. Inbox",
    "1. Projects",
    "2. Areas (Ongoing)",
    "3. Resources (Dynamic)",
    "4. Archive (Supportive)",
    "6. Metadata",
    "6. Metadata\Templates",
    "6. Metadata\Workflows",
    "6. Metadata\Reference"
)

foreach ($folder in $paraFolders) {
    $folderPath = Join-Path $VaultPath $folder
    if (-not (Test-Path $folderPath)) {
        New-Item -ItemType Directory -Path $folderPath -Force | Out-Null
        Write-Step "Created PARA folder: $folder"
    }
}

# Copy templates
$sourceTemplates = Join-Path $scriptRoot "Obsidian-Vault-Backup\6. Metadata\Templates"
$destTemplates = Join-Path $VaultPath "6. Metadata\Templates"
if (Test-Path $sourceTemplates) {
    Copy-Item -Path "$sourceTemplates\*" -Destination $destTemplates -Recurse -Force
    $templateCount = (Get-ChildItem $destTemplates -Filter "*.md" -ErrorAction SilentlyContinue).Count
    Write-Step "Copied $templateCount templates"
}

# Install Python tools
if (-not $SkipPython) {
    Write-Header "Installing Python tools"

    Write-Step "Installing uv..."
    pip install uv 2>$null

    Write-Step "Installing Zotero MCP..."
    uv tool install "git+https://github.com/54yyyu/zotero-mcp.git" 2>$null

    Write-Step "Installing PaperQA2..."
    pip install "paper-qa>=5" 2>$null

    Write-Step "Python tools installed"
}

# Obsidian plugin reminders
if (-not $SkipObsidianPlugins) {
    Write-Header "Obsidian Plugin Setup"
    Write-Host @"
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
  2. Paste it in: $claudeDir\mcp.json
"@ -ForegroundColor White
}

# Final instructions
Write-Header "Setup Complete!"

Write-Host @"
Next steps:

1. Open your vault in Obsidian
2. Install the Local REST API plugin
3. Copy your API key to: $claudeDir\mcp.json
4. Run Claude Code in your vault:

   cd "$VaultPath"
   claude

5. Try a command:
   /thinking-partner
   /daily-review
   /research-ideate

For research tools (if Zotero is installed):
   zotero-mcp setup
   zotero-mcp update-db --fulltext

Documentation: $VaultPath\CLAUDE.md
"@ -ForegroundColor Green
