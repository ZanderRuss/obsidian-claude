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

If YES, guide them through these steps carefully:

---

#### Part A: Install and Enable the Plugin

1. **Open Obsidian Settings**
   - Click the gear icon (bottom-left corner of Obsidian)
   - Or press `Ctrl+,` (Windows) / `Cmd+,` (Mac)

2. **Enable Community Plugins** (if not already done)
   - In the left sidebar, click "Community plugins"
   - If you see "Restricted mode is ON", click "Turn on community plugins"
   - Click "Browse" to open the plugin browser

3. **Install Local REST API**
   - In the search box, type "Local REST API"
   - Find "Local REST API" by Adam Coddington
   - Click "Install"
   - After installation, click "Enable"

4. **Open Plugin Settings**
   - Still in Settings, scroll down the left sidebar to "Community plugins"
   - Find "Local REST API" in the list and click on it
   - You'll see the plugin settings page

---

#### Part B: Copy Your API Key

On the Local REST API settings page, you'll see:

```
Your API Key must be passed in requests via an authorization header:
┌─────────────────────────────────────────────────────────────┐
│ 72334a1f5f370d49009660863d24531738de73453ef47382f48aff...  │
└─────────────────────────────────────────────────────────────┘
```

**Copy this entire API key** - you'll need it in the next step.

**Important Settings to Check:**
- "Enable Encrypted (HTTPS) Server" should be ON (default)
- "Encrypted (HTTPS) Server Port" should be 27124 (default)

---

#### Part C: Choose Connection Method

There are TWO ways to connect. Choose ONE:

**Option 1: HTTPS (Recommended - More Secure)**
- Uses port 27124 (encrypted)
- Requires SSL verification bypass (we'll handle this)
- Best for: Most users

**Option 2: HTTP (Simpler - No SSL Issues)**
- Uses port 27123 (unencrypted)
- Only works locally (127.0.0.1)
- Best for: Users having certificate issues

For Option 2, enable "Enable Non-encrypted (HTTP) Server" in the plugin settings.

---

#### Part D: Configure Claude

Tell the user: "Now I need to add this to Claude's configuration. Here's exactly what to do:"

**Windows:**
1. Press `Win+R` to open Run dialog
2. Type `%APPDATA%\Claude` and press Enter
3. Look for `claude_desktop_config.json`
   - If it exists, open it with Notepad
   - If it doesn't exist, create a new text file with that exact name
4. Add this content (replace YOUR_API_KEY_HERE with the key you copied):

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "YOUR_API_KEY_HERE",
        "OBSIDIAN_HOST": "https://127.0.0.1:27124",
        "OBSIDIAN_VERIFY_SSL": "false"
      }
    }
  }
}
```

**If using HTTP (Option 2 above), use this instead:**
```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "YOUR_API_KEY_HERE",
        "OBSIDIAN_HOST": "http://127.0.0.1:27123"
      }
    }
  }
}
```

5. Save the file
6. **Completely restart Claude Code Desktop** (quit and reopen, not just close the window)

**Mac:**
1. Open Finder
2. Press `Cmd+Shift+G` (Go to Folder)
3. Type `~/Library/Application Support/Claude/` and press Enter
4. Open or create `claude_desktop_config.json`
5. Add the same content as Windows above
6. Save and restart Claude Code Desktop completely

**Linux:**
1. Open file manager or terminal
2. Navigate to `~/.config/Claude/`
3. Open or create `claude_desktop_config.json`
4. Add the same content as Windows above
5. Save and restart Claude Code Desktop completely

---

#### Part E: Verify Connection

After restarting Claude Code Desktop:

1. **Check Obsidian is running** - The Local REST API only works when Obsidian is open
2. **Test the connection** - Ask Claude: "Can you list the notes in my vault?"

If it works, you'll see a list of your notes!

---

#### Understanding the Settings

| Setting | What It Does |
|---------|--------------|
| `OBSIDIAN_API_KEY` | Your secret password to access the vault |
| `OBSIDIAN_HOST` | Where to find Obsidian (localhost on port 27124 or 27123) |
| `OBSIDIAN_VERIFY_SSL` | Set to "false" because the plugin uses a self-signed certificate |

**Why `OBSIDIAN_VERIFY_SSL: false`?**
The Local REST API plugin creates its own SSL certificate for security. Since this certificate isn't from a public authority (like Let's Encrypt), we tell Claude to trust it anyway. This is safe because:
- Everything runs locally on your computer (127.0.0.1)
- No data leaves your machine
- The API key still protects access

---

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

**Step-by-step diagnosis:**

1. **Is Obsidian running?**
   - The Local REST API only works when Obsidian is open
   - Open Obsidian and keep it running

2. **Is the plugin enabled?**
   - Go to Settings > Community plugins
   - Find "Local REST API" - it should show as enabled
   - If not, click the toggle to enable it

3. **Is the server running?**
   - In Obsidian, go to Settings > Community plugins > Local REST API
   - You should see the API URLs listed at the top
   - If you see errors, try clicking "Re-generate Certificates"

4. **Is your API key correct?**
   - Copy the API key fresh from the plugin settings
   - Paste it into your `claude_desktop_config.json`
   - Make sure there are no extra spaces or line breaks

5. **Are you using the right port?**
   - HTTPS uses port 27124
   - HTTP uses port 27123
   - Check your config matches what you enabled in the plugin

6. **Did you restart Claude Code Desktop?**
   - After changing `claude_desktop_config.json`, you must fully restart
   - Close the app completely (not just the window)
   - Reopen Claude Code Desktop

**Still not working? Try HTTP mode:**

If HTTPS keeps failing, switch to HTTP:

1. In Obsidian plugin settings, enable "Enable Non-encrypted (HTTP) Server"
2. Update your config to use `http://127.0.0.1:27123`
3. Remove the `OBSIDIAN_VERIFY_SSL` line
4. Restart Claude Code Desktop

**Check the API manually:**

Open a browser and go to: `http://127.0.0.1:27123/` (if HTTP enabled)

You should see a response (even if it's an error about authentication). If you see nothing, the server isn't running.

### Need More Help?
- Check README.md for detailed documentation
- Visit: https://github.com/ZanderRuss/obsidian-claude/issues
- Just ask Claude! Describe your problem and I'll help.
