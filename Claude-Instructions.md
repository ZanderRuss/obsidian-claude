# Getting Started with Obsidian-Claude

Welcome! This guide helps you complete the setup. There are two paths depending on where you are:

---

## Path A: You're Reading This in Claude Code Desktop

**Great!** You're in the right place. Just paste the text below the line into the chat, and Claude will guide you through the rest.

---

## Path B: You're Reading This Outside Claude Code Desktop

You need to open this folder in Claude Code Desktop first. Here's how:

### Step 1: Open Claude Code Desktop

Download from [claude.ai/download](https://claude.ai/download) if you haven't already.

### Step 2: Open This Folder

1. In Claude Code Desktop, click **"Open Folder"** (or File > Open Folder)
2. Navigate to the folder containing this file (`Claude-Instructions.md`)
3. Select the folder and click "Open"

```
Your folder should look like this:
+-- obsidian-claude/
    +-- .claude/
    +-- Obsidian-Template-Vault/
    +-- SETUP.bat
    +-- SETUP.command
    +-- README.md
    +-- Claude-Instructions.md  <-- This file
```

### Step 3: Talk to Claude

Once the folder is open, type in the chat:
> "Help me complete the setup"

Or copy the text below and paste it into the chat.

---

## Copy Everything Below This Line

---

INSTRUCTIONS FOR CLAUDE

Hello Claude! A user wants to set up Obsidian-Claude. Please help them complete the setup with warm, encouraging guidance.

## Context

The user should have:
1. Downloaded and extracted the obsidian-claude project
2. Opened the project folder in Claude Code Desktop (you should be able to see SETUP.bat, README.md, etc.)

If they haven't done step 2, guide them:
- "First, let's make sure you've opened the project folder in Claude Code Desktop. Go to File > Open Folder and select the folder containing SETUP.bat and README.md."

## Setup Steps

### Step 1: Verify the Environment

Check if the Python environment exists by looking for:
- Windows: `.venv\Scripts\python.exe`
- Mac/Linux: `.venv/bin/python`

If it exists, say: "Your Python environment is ready!"

If it doesn't exist, help them run the setup script:
- Windows: `SETUP.bat`
- Mac/Linux: `SETUP.command`

Run the appropriate script for their OS. You can detect the OS from the environment.

### Step 2: Explain What They Have

Tell them (in simple terms):

"You now have access to 18 AI-powered skills:

**Research & Writing**
- Search the web for current information
- Find and organize research papers
- Help writing academic documents
- Manage citations

**Data & Analysis**
- Run statistical analyses
- Create charts and visualizations

**Documents**
- Create and edit Word documents
- Work with Excel spreadsheets
- Extract text from PDFs

You can use these by asking me naturally, like:
- 'Find papers about machine learning'
- 'Create a chart from this data'
- 'Help me write an introduction'"

### Step 3: Open Obsidian

Guide them to open the vault in Obsidian:

1. Open Obsidian (download from obsidian.md if needed)
2. Click "Open folder as vault"
3. Navigate to the `Obsidian-Template-Vault` folder inside this project
4. Click "Open"

Explain: "Now you have both apps working together:
- Claude Code Desktop: Where you talk to me
- Obsidian: Where your notes are stored

Keep both open while working!"

### Step 4: (Optional) Connect Claude to Obsidian

Ask: "Would you like me to be able to read and write notes directly in your vault? This is optional but very useful."

If YES:

1. **Install the plugin in Obsidian:**
   - Open Obsidian Settings (gear icon, bottom-left)
   - Go to Community plugins
   - Click "Browse"
   - Search for "Local REST API"
   - Click Install, then Enable
   - Go to the plugin settings and copy the API key

2. **Add the API key to your configuration:**

   Tell them: "Now I need to add this to Claude's configuration. I'll create a configuration file for you."

   Create or update the MCP configuration file. The location depends on OS:
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

   Since you may not have access to these folders, guide the user:

   "I can't access the Claude Desktop config folder directly. Here's what to do:

   **Windows:**
   1. Press Win+R, type `%APPDATA%\Claude` and press Enter
   2. Open or create `claude_desktop_config.json`
   3. Add this content (replace YOUR_API_KEY with the key you copied):

   ```json
   {
     "mcpServers": {
       "obsidian": {
         "command": "npx",
         "args": ["-y", "obsidian-mcp"],
         "env": {
           "OBSIDIAN_API_KEY": "YOUR_API_KEY"
         }
       }
     }
   }
   ```

   4. Save the file
   5. Restart Claude Code Desktop completely

   **Mac:**
   1. Open Finder, press Cmd+Shift+G
   2. Type `~/Library/Application Support/Claude/` and press Enter
   3. Open or create `claude_desktop_config.json`
   4. Add the same content as above
   5. Restart Claude Code Desktop"

If NO: "No problem! All the skills still work. You can set this up anytime later."

### Step 5: Quick Test

Say: "Let's try something! Ask me to search for something interesting, like 'Search for the latest news about AI agents'"

Celebrate when it works!

### Step 6: Share Quick Reference

```
QUICK REFERENCE

Research:
  "Search for [topic]"           - Web search
  "Find papers about [topic]"    - Academic papers
  "Create a citation for..."     - Citation help

Writing:
  "Help me write..."             - Writing assistance
  "Create a Word document..."    - .docx files

Data:
  "Analyze this data..."         - Statistics
  "Create a chart showing..."    - Visualizations

Documents:
  "Create a spreadsheet..."      - Excel files
  "Extract text from this PDF"   - PDF processing

Tip: Just describe what you need naturally!
```

### Step 7: Wrap Up

End with:
"You're all set! Here's what you can do now:

1. **Explore the vault** - Check out the Home.md file in Obsidian
2. **Try a search** - Ask me to find information on any topic
3. **Start writing** - Ask for help with any document

Both apps should stay open while you work:
- Ask me questions in Claude Code Desktop
- See your notes organized in Obsidian

If you need help anytime, just ask! Welcome to your AI-powered knowledge system!"

---

## Troubleshooting

### "I don't see the project files"
Make sure you opened the correct folder in Claude Code Desktop. Go to File > Open Folder and select the folder containing SETUP.bat and README.md.

### "Python not found"
Run the setup script again. If Python isn't installed, download it from python.org (it's free).

### "Skills not working"
1. Make sure you're using Claude Code Desktop (not the website)
2. Make sure the folder is open in Claude Code Desktop
3. Try running the setup script again

### "Can't connect to Obsidian"
1. Make sure Obsidian is running
2. Check that the Local REST API plugin is enabled
3. Verify the API key is correct in the config file
4. Restart Claude Code Desktop after making changes

### Need More Help?
- Check README.md for detailed documentation
- Visit: https://github.com/ZanderRuss/obsidian-claude/issues
- Just ask Claude! Describe your problem and I'll help.
