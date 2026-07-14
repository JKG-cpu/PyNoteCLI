import json
from pathlib import Path

from ..paths import DATA_DIR, DATABASE_DIR, CONFIG_FILE, PAGES_DIR, BASE_NOTE_PAGE
from ..dataclasses import PageJSON
from .global_vars import CONFIG, Text

__all__ = ["setup"]


def setup_storage() -> Path:
    # Create Directories
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Generate config
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text(json.dumps(CONFIG, indent=4), encoding="utf-8")

    if not BASE_NOTE_PAGE.exists():
        BASE_NOTE_PAGE.write_text(
            json.dumps(
                PageJSON(page_name="Base Notes", page_type="normal").to_dict(), indent=4
            )
        )

    return DATA_DIR


def setup() -> None:
    with Text.status("Setting up data folders and files...", style="bold cyan"):
        data_dir = setup_storage()

    Text.text("✓ Setup complete!", style="bold cyan")

    Text.success(f"PyNote data setup at {data_dir}")
