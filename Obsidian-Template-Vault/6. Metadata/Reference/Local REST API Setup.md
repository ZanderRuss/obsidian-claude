---
tags:
  - type/reference
  - topics/setup
  - topics/integration
type: reference
created: 2025-01-11
modified: 2025-01-11
status: active
---

# Local REST API Setup Guide

Complete guide for connecting Claude to your Obsidian vault using the Local REST API plugin.

## Overview

The Local REST API plugin allows external applications (like Claude) to read and write notes in your Obsidian vault. This enables Claude to:

- Read your existing notes for context
- Create new notes directly in your vault
- Search across your vault content
- Update and organize your notes

## Quick Start

### Step 1: Install the Plugin

1. Open Obsidian
2. Click the **gear icon** (bottom-left) to open Settings
3. Go to **Community plugins** in the left sidebar
4. If you see "Restricted mode is ON", click **Turn on community plugins**
5. Click **Browse**
6. Search for **"Local REST API"**
7. Click **Install** on "Local REST API" by Adam Coddington
8. Click **Enable**

### Step 2: Get Your API Key

1. Still in Settings, scroll down the left sidebar
2. Under "Community plugins", click on **Local REST API**
3. You'll see the settings page with your API key displayed:

```
Your API Key must be passed in requests via an authorization header:
┌─────────────────────────────────────────────────────────────┐
│ 72334a1f5f370d49009660863d24531738de73453ef47382f48aff...  │
└─────────────────────────────────────────────────────────────┘
```

4. **Copy this entire API key** - you'll need it for configuration

### Step 3: Choose Your Connection Method

There are two ways to connect:

| Method | Port | Security | Best For |
|--------|------|----------|----------|
| HTTPS | 27124 | Encrypted, self-signed cert | Most users (recommended) |
| HTTP | 27123 | Unencrypted | Users with certificate issues |

**For HTTP**, you need to enable it:
- In plugin settings, toggle ON **"Enable Non-encrypted (HTTP) Server"**

### Step 4: Configure Claude

Add the following to your MCP configuration:

**For HTTPS (Recommended):**

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "paste-your-api-key-here",
        "OBSIDIAN_HOST": "https://127.0.0.1:27124",
        "OBSIDIAN_VERIFY_SSL": "false"
      }
    }
  }
}
```

**For HTTP:**

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "mcp-obsidian"],
      "env": {
        "OBSIDIAN_API_KEY": "paste-your-api-key-here",
        "OBSIDIAN_HOST": "http://127.0.0.1:27123"
      }
    }
  }
}
```

**Config file locations:**

| OS | Location |
|----|----------|
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| Mac | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

### Step 5: Restart and Test

1. **Save** your configuration file
2. **Completely quit** Claude Code Desktop (not just close the window)
3. **Reopen** Claude Code Desktop
4. **Keep Obsidian running** (the API only works when Obsidian is open)
5. Ask Claude: "Can you list the notes in my vault?"

---

## Configuration Settings Explained

| Setting | Value | Purpose |
|---------|-------|---------|
| `OBSIDIAN_API_KEY` | Your key from plugin | Authentication - proves you're authorized |
| `OBSIDIAN_HOST` | `https://127.0.0.1:27124` | Where to find Obsidian (HTTPS) |
| `OBSIDIAN_HOST` | `http://127.0.0.1:27123` | Where to find Obsidian (HTTP) |
| `OBSIDIAN_VERIFY_SSL` | `"false"` | Trust the self-signed certificate |

### Why `OBSIDIAN_VERIFY_SSL: false`?

The Local REST API plugin creates its own SSL certificate for encryption. Since this certificate isn't from a public certificate authority (like Let's Encrypt), most systems won't trust it by default.

Setting `OBSIDIAN_VERIFY_SSL` to `"false"` tells Claude to trust it anyway.

**Is this safe?** Yes, because:

- Everything runs locally on your computer (`127.0.0.1` = localhost)
- No data leaves your machine
- The API key still protects against unauthorized access
- Only applications with your API key can access the vault

---

## Plugin Settings Reference

### Main Settings

| Setting | Default | Description |
|---------|---------|-------------|
| Enable Encrypted (HTTPS) Server | ON | Run HTTPS server on port 27124 |
| Enable Non-encrypted (HTTP) Server | OFF | Run HTTP server on port 27123 |
| Encrypted (HTTPS) Server Port | 27124 | Port for HTTPS connections |
| Non-encrypted (HTTP) Server Port | 27123 | Port for HTTP connections |

### Advanced Settings

| Setting | Default | Description |
|---------|---------|-------------|
| Certificate Hostnames | (empty) | Additional hostnames for the certificate |
| Binding Host | 127.0.0.1 | IP address to bind to (localhost only) |
| Authorization Header | Authorization | HTTP header name for API key |

### Buttons

| Button | What It Does |
|--------|--------------|
| Re-generate Certificates | Creates new SSL certificates (use if having cert issues) |
| Reset All Crypto | Regenerates certificates AND creates new API key |
| Restore Default Settings | Resets everything to defaults |

---

## Troubleshooting

### "Connection refused" or "Cannot connect"

**Check these in order:**

1. **Is Obsidian running?**
   - The API only works when Obsidian is open
   - Open Obsidian and keep it running

2. **Is the plugin enabled?**
   - Settings > Community plugins
   - Find "Local REST API" - toggle should be ON

3. **Is the server running?**
   - Settings > Community plugins > Local REST API
   - You should see the API URLs at the top
   - If there are errors, click "Re-generate Certificates"

4. **Is your API key correct?**
   - Copy fresh from plugin settings
   - Paste into config (no extra spaces or line breaks)

5. **Are you using the right port?**
   - HTTPS = port 27124
   - HTTP = port 27123
   - Make sure config matches what you enabled

6. **Did you restart Claude?**
   - After changing config, fully restart Claude Code Desktop
   - Close the app completely, then reopen

### "SSL Certificate Error" or "Certificate Invalid"

**Option 1: Use the bypass setting**

Add to your config:
```json
"OBSIDIAN_VERIFY_SSL": "false"
```

**Option 2: Switch to HTTP**

1. Enable HTTP in plugin settings
2. Change config to use `http://127.0.0.1:27123`
3. Remove `OBSIDIAN_VERIFY_SSL` line

**Option 3: Regenerate certificates**

1. In plugin settings, click "Re-generate Certificates"
2. Restart Obsidian
3. Restart Claude

### "401 Unauthorized" or "Invalid API Key"

- Copy the API key again from plugin settings
- Make sure there are no extra spaces
- Check for hidden characters (copy to plain text first)
- Verify you're using the correct config file

### Test the API Manually

Open a web browser and go to:

- HTTP: `http://127.0.0.1:27123/`
- HTTPS: `https://127.0.0.1:27124/` (may show certificate warning)

You should see a response. Even an error like "Unauthorized" means the server is working.

---

## Security Considerations

### What's Protected

- **API Key**: Only applications with your key can access the vault
- **Localhost Only**: By default, only your computer can connect (127.0.0.1)
- **HTTPS**: Data is encrypted (even with self-signed certificate)

### Best Practices

1. **Don't share your API key** - treat it like a password
2. **Keep Binding Host as 127.0.0.1** - don't expose to network
3. **Use HTTPS when possible** - even with self-signed certs
4. **Regenerate key if compromised** - click "Reset All Crypto"

### What to Avoid

- Don't expose the API to the internet
- Don't commit your API key to git repositories
- Don't share config files containing your key

---

## API Endpoints Reference

The plugin provides these REST endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/vault/` | GET | List all files |
| `/vault/{path}` | GET | Read a file |
| `/vault/{path}` | PUT | Create/update a file |
| `/vault/{path}` | DELETE | Delete a file |
| `/vault/{path}` | PATCH | Insert content into a file |
| `/periodic/daily` | GET/POST | Daily note operations |
| `/commands/` | GET | List available commands |
| `/commands/{id}` | POST | Execute a command |
| `/search/simple/` | POST | Search vault content |

For full API documentation, see: https://coddingtonbear.github.io/obsidian-local-rest-api/

---

## Related

- [[Vault Overview]]
- [[Research Tools Setup]]

---

## External Resources

- [Local REST API Plugin](https://github.com/coddingtonbear/obsidian-local-rest-api) - GitHub repository
- [Interactive API Docs](https://coddingtonbear.github.io/obsidian-local-rest-api/) - Swagger documentation
- [MCP Obsidian](https://github.com/smithery-ai/mcp-obsidian) - MCP server for Claude integration
