## Idea
A Python CLI application that holds all your notes. There will be 
-  Different Formats (text, markdown)
-  A simple command
-  TUI

You will be able to
-  Create new notes
-  Create temporary notes
-  Remove old notes
-  Set reminders
-  Create notes with specific tags
	- So some notes are for this project, others are for other projects, etc
-  Export notes
---
## Commands
```bash
pynote
pynote --help
pynote tui # Opens TUI (textual + rich?)

# Config / Settings
pynote config show

pynote config edit

pynote config reset

# Page Management
pynote page create "Todo"
pynote page create "Shopping" --checklist

pynote page delete "Todo"

pynote page rename "Todo" "Tasks"

pynote page list

pynote page show "Todo" # Display page

pynote page edit "Todo" # In CLI Text editor

# Note Management
pynote note add "Buy milk"

pynote note add "Buy milk" --page "Shopping"

# Edit, delete, move by ID
pynote note edit 12

pynote note delete 12

pynote note move 12 --page "Archive"

pynote note list

pynote note list --page "Shopping"

# Checklist
pynote check complete 5

pynote check uncomplete 5

pynote check toggle 5

# Search
pynote search "python"

pynote search "pygame"

pynote search --page "Ideas" "game"

# Tags
pynote tag add 12 "Python"

pynote tag remove 12 "Python"

pynote tag list

pynote tag show "Python"

# Export / Import (DECIDING)
pynote export ...
pynote import ...

# Stats???
pynote stats
---
Pages: 12
Notes: 156
Checklist Items: 43
Completed: 31
---

# Quick Capture
pynote quick "Remember to update my program"

# Daily Notes
pynote today # Opens a note with today's date

```

---
## Setup
Will be using `Python` as the language, and `SQLite` for the data management. Use `platformdirs` for setting up the data paths.
```python
from pathlib import Path
from platformdirs import user_data_dir

# Base Path
DATA_DIR = Path(user_data_dir("PyNoteCLI"))
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Notes Directory
NOTES_DIR = DATA_DIR / "notes"
NOTES_DIR.mkdir(exist_ok=True)
```

Gonna use `textual` + `rich` for the TUI. Gonna use `Typer` for the CLI.

---
## Todo
1.  Create basic file setup
2.  Learn how to use Typer
3.  Setup the entry point
	1. Include 1 - 3 commands