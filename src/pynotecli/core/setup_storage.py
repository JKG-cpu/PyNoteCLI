import json
from pathlib import Path
import time

from ..paths import DATA_DIR, DATABASE_DIR, CONFIG_FILE, PAGES_DIR
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

    return DATA_DIR


def setup() -> None:
    with Text.status("Setting up data folders and files...", style="bold cyan"):
        data_dir = setup_storage()

    Text.text("✓ Setup complete!", style="bold cyan")

    Text.success(f"PyNote data setup at {data_dir}")
