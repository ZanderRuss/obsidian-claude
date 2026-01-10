# First Time Setup for Mac Users

If you downloaded this as a ZIP file from GitHub, the setup script might not run when you double-click it. This is normal - GitHub ZIPs remove file permissions.

## Quick Fix (Choose One Method)

### Method 1: One Command (Recommended)

1. Open **Terminal** (search for "Terminal" in Spotlight or find it in Applications > Utilities)
2. Drag the folder you extracted onto the Terminal window (this types the path for you)
3. Delete whatever text appeared, then type:
   ```
   cd
   ```
4. Drag the folder again onto Terminal, then press Enter
5. Now type this command and press Enter:
   ```
   chmod +x SETUP.command && ./SETUP.command
   ```

### Method 2: Right-Click Method

1. Right-click on `SETUP.command`
2. Click "Open" (not double-click)
3. If asked, click "Open" again to confirm
4. The setup will run in Terminal

### Method 3: Run from Terminal

1. Open Terminal
2. Navigate to the folder:
   ```
   cd ~/Downloads/obsidian-claude-main
   ```
   (adjust the path if you extracted elsewhere)
3. Make the script executable:
   ```
   chmod +x SETUP.command
   ```
4. Run it:
   ```
   ./SETUP.command
   ```

## Why Does This Happen?

When you download a ZIP file from GitHub, it removes the "executable" permission from scripts for security reasons. The `chmod +x` command adds that permission back.

## Still Having Trouble?

Ask for help in the [GitHub Issues](https://github.com/ZanderRuss/obsidian-claude/issues) - we're happy to help!
