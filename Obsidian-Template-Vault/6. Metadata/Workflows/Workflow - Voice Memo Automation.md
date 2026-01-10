---
tags:
  - workflow
  - automation
  - voice
type: workflow
created: 2025-01-10
---

# Voice Memo Automation Workflow

Capture thoughts on mobile, have them processed automatically into structured notes.

## Overview

```
Voice Recording → Transcription → Sync to Vault → Claude Processing → Structured Note
```

## Setup Options

### Option 1: Apple Shortcuts (iOS)

**Requirements:**
- iPhone/iPad
- Obsidian mobile app
- Whisper API or on-device transcription

**Shortcut Flow:**
1. Record voice memo
2. Transcribe using Whisper (via API or Shortcuts ML)
3. Create markdown file with transcription
4. Save to Obsidian vault's `0. Inbox/` folder
5. File syncs to desktop via iCloud/Obsidian Sync

**Shortcut Template:**
```
1. Record Audio
2. Transcribe Audio (Whisper API)
3. Text: Create markdown template
   ---
   tags: voice-memo, unprocessed
   type: voice-raw
   created: [Current Date]
   ---
   # Voice Memo - [Current Date Time]

   [Transcription]
4. Save File to: Obsidian/Vault/0. Inbox/Voice-[Date].md
```

### Option 2: Obsidian + Local Whisper

**Requirements:**
- Whisper.cpp or similar local setup
- Watch folder script

**Script (PowerShell):**
```powershell
# watch-voice-memos.ps1
$watchFolder = "C:\VoiceMemos"
$vaultInbox = "D:\OneDrive\04_Projects\17_Obsidian-Claude\Obsidian-Vault-Backup\0. Inbox"

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $watchFolder
$watcher.Filter = "*.m4a"
$watcher.EnableRaisingEvents = $true

Register-ObjectEvent $watcher "Created" -Action {
    $file = $Event.SourceEventArgs.FullPath
    $name = [System.IO.Path]::GetFileNameWithoutExtension($file)

    # Transcribe with Whisper
    whisper $file --output_format txt --output_dir $watchFolder

    # Create markdown note
    $transcription = Get-Content "$watchFolder\$name.txt"
    $date = Get-Date -Format "yyyy-MM-dd HH:mm"

    $content = @"
---
tags:
  - voice-memo
  - unprocessed
type: voice-raw
created: $date
---

# Voice Memo - $date

$transcription
"@

    $content | Out-File "$vaultInbox\Voice-$name.md" -Encoding UTF8
}
```

### Option 3: Android + Tasker

**Requirements:**
- Tasker app
- AutoVoice or similar
- Sync solution (Syncthing, Dropsync)

**Tasker Profile:**
1. Trigger: New audio file in recording folder
2. Task: Transcribe (via API call to Whisper)
3. Task: Create markdown file
4. Task: Move to synced vault folder

## Processing with Claude

Once voice memos land in `0. Inbox/`:

1. Run `/voice-process` command
2. Claude cleans and structures the transcription
3. Extracts tasks, insights, and connections
4. Files to appropriate location

## Recommended Naming Convention

```
Voice-YYYY-MM-DD-HHMM.md
Voice-2025-01-10-1430.md
```

## Tags for Voice Memos

- `voice-memo` - All voice captures
- `unprocessed` - Not yet run through Claude
- `processed` - Cleaned and structured
- `meeting` - Meeting recordings
- `brainstorm` - Idea dumps
- `journal` - Personal reflections

## Best Practices

1. **Keep recordings short** (2-5 minutes ideal)
2. **State context at start** ("This is about project X...")
3. **Speak clearly** for better transcription
4. **Process daily** - don't let backlog build
5. **Review processed notes** - add connections manually

## Integration with Daily Review

Add to `/daily-review`:
- Check for new voice memos in Inbox
- Process any unprocessed recordings
- Link insights to relevant projects
