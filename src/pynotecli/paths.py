from pathlib import Path
from platformdirs import user_data_dir

__all__ = [
    "APP_NAME",
    "APP_AUTHOR",
    "DATA_DIR",
    "DATABASE_DIR",
    "PAGES_DIR",
    "CONFIG_FILE",
    "BASE_NOTE_PAGE",
]

APP_NAME = "PyNoteCLI"
APP_AUTHOR = "JKG"

DATA_DIR = Path(user_data_dir(APP_NAME, APP_AUTHOR))
DATABASE_DIR = DATA_DIR / "database"
PAGES_DIR = DATA_DIR / "pages"
BASE_NOTE_PAGE = PAGES_DIR / "base.json"
CONFIG_FILE = DATA_DIR / "config.json"
