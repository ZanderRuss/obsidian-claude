# Provider Setup Guide

Complete setup instructions for each AI search provider.

## Claude WebSearch (Default)

**Setup**: None required. Claude's built-in WebSearch is available automatically.

**Usage**: Simply ask Claude to search for information.

**Cost**: Included with Claude Code subscription.

---

## OpenAI

### Get API Key

1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-`)

### Configure

```bash
# macOS/Linux
export OPENAI_API_KEY='sk-...'

# Windows PowerShell
$env:OPENAI_API_KEY = 'sk-...'

# Windows CMD
set OPENAI_API_KEY=sk-...
```

### Install Package

```bash
pip install openai
```

### Available Models

- `gpt-4o` (recommended) - Latest, most capable
- `gpt-4o-mini` - Faster, cheaper
- `gpt-4-turbo` - Previous generation

### Test Setup

```bash
python scripts/ai_search.py "test query" --provider openai --check-setup
```

---

## Anthropic

### Get API Key

1. Go to https://console.anthropic.com
2. Navigate to "API Keys"
3. Click "Create Key"
4. Copy the key (starts with `sk-ant-`)

### Configure

```bash
# macOS/Linux
export ANTHROPIC_API_KEY='sk-ant-...'

# Windows PowerShell
$env:ANTHROPIC_API_KEY = 'sk-ant-...'

# Windows CMD
set ANTHROPIC_API_KEY=sk-ant-...
```

### Install Package

```bash
pip install anthropic
```

### Available Models

- `claude-sonnet-4-20250514` (recommended) - Best balance
- `claude-opus-4-20250514` - Most capable
- `claude-haiku-3-20240307` - Fastest, cheapest

### Test Setup

```bash
python scripts/ai_search.py "test query" --provider anthropic --check-setup
```

---

## Google Gemini

### Get API Key

1. Go to https://aistudio.google.com/apikey
2. Click "Create API Key"
3. Copy the key

### Configure

```bash
# macOS/Linux
export GEMINI_API_KEY='...'
# or
export GOOGLE_API_KEY='...'

# Windows PowerShell
$env:GEMINI_API_KEY = '...'

# Windows CMD
set GEMINI_API_KEY=...
```

### Install Package

```bash
pip install google-generativeai
```

### Available Models

- `gemini-2.0-flash` (recommended) - Fast with grounding
- `gemini-1.5-pro` - More capable
- `gemini-1.5-flash` - Fastest

### Test Setup

```bash
python scripts/ai_search.py "test query" --provider gemini --check-setup
```

---

## Perplexity (via OpenRouter)

### Get API Key

1. Go to https://openrouter.ai/keys
2. Create an account if needed
3. Click "Create Key"
4. Add credits ($5 minimum recommended)

### Configure

```bash
# macOS/Linux
export OPENROUTER_API_KEY='sk-or-v1-...'

# Windows PowerShell
$env:OPENROUTER_API_KEY = 'sk-or-v1-...'

# Windows CMD
set OPENROUTER_API_KEY=sk-or-v1-...
```

### Install Package

```bash
pip install litellm
```

### Available Models

- `sonar-pro` (recommended) - General-purpose search
- `sonar-pro-search` - Deep agentic search
- `sonar` - Basic, cheapest
- `sonar-reasoning-pro` - Advanced reasoning
- `sonar-reasoning` - Basic reasoning

### Test Setup

```bash
python scripts/ai_search.py "test query" --provider perplexity --check-setup
```

---

## Troubleshooting

### API Key Not Found

**Error**: `OPENAI_API_KEY not set`

**Solution**: Ensure the environment variable is exported in your current shell session. For permanent setup, add to your shell profile (`.bashrc`, `.zshrc`, etc.) or use a `.env` file.

### Package Not Installed

**Error**: `openai package not installed`

**Solution**: Install the required package:
```bash
pip install openai anthropic google-generativeai litellm
```

### Invalid API Key

**Error**: `Invalid API key`

**Solution**: Double-check your API key is correct and hasn't expired. Regenerate if needed.

### Rate Limiting

**Error**: `Rate limit exceeded`

**Solution**: Wait a few seconds and retry. Consider upgrading your API tier for higher limits.

### Insufficient Credits

**Error**: `Insufficient credits` (OpenRouter/Perplexity)

**Solution**: Add credits at https://openrouter.ai/account

---

## Security Best Practices

1. **Never commit API keys** to version control
2. **Use environment variables** instead of hardcoding
3. **Set spending limits** in provider dashboards
4. **Rotate keys periodically**
5. **Use separate keys** for development and production
