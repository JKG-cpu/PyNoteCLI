import json
from pathlib import Path

from ..dataclasses import PageJSON
from ..paths import BASE_NOTE_PAGE
from .page_manager import PageManager
from .global_vars import Text

__all__ = ["add_note", "delete_note", "edit_note", "list_notes"]


class NoteManager:
    def __init__(self) -> None:
        self.page_manager = PageManager()

    def load_data(self, file_path: Path) -> PageJSON:
        with open(file_path, "r") as f:
            data = json.load(f)
            return PageJSON.from_dict(data)

    def save_data(self, file_path: Path, data: PageJSON) -> None:
        with open(file_path, "w") as f:
            json.dump(data.to_dict(), f, indent = 4)

    def add_note(self, name: str, desc: str | None, page: str | None) -> None:
        if page:
            if page.isdigit():
                p = self.page_manager.get_page_by_id(int(page))

                if p:
                    data: PageJSON = self.load_data(Path(p.file_path))
                    fp = Path(p.file_path)

                else:
                    Text.error("Page does not exist.")
                    return

            else:
                pages = self.page_manager.get_page_by_name(page)

                if pages:
                    if len(pages) == 1:
                        data: PageJSON = self.load_data(Path(pages[0].file_path))
                        fp = Path(pages[0].file_path)

                    else:
                        Text.error(f"Multiple pages named {page}. Please select a page via ID")
                        Text.info("Use pynote page list to view current pages.")

                else:
                    Text.error("Page does not exist.")
                    return

        else:
            data: PageJSON = self.load_data(BASE_NOTE_PAGE)
            fp = BASE_NOTE_PAGE

        data.add_new_note(name, desc)

        self.save_data(fp, data)

    def edit(self, name: str, page: str | None) -> None:
        pass

    def delete_note(self, name: str, page: str | None) -> None:
        pass

    def list_notes(self, page: str | None) -> None:
        pass


n = NoteManager()


def add_note(name: str, desc: str | None, page: str | None) -> None:
    n.add_note(name=name, desc=desc, page=page)


def edit_note(name: str, page: str | None) -> None:
    n.edit(name=name, page=page)


def delete_note(name: str, page: str | None) -> None:
    n.delete_note(name=name, page=page)


def list_notes(page: str | None) -> None:
    n.list_notes(page=page)
