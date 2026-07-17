import json
from pathlib import Path

from ..dataclasses import PageJSON, Note
from ..paths import BASE_NOTE_PAGE
from .page_manager import PageManager
from .global_vars import Text

__all__ = ["add_note", "delete_note", "list_notes"]


class NoteManager:
    def __init__(self) -> None:
        self.page_manager = PageManager()

    # Helpers
    # region
    def load_data(self, file_path: Path) -> PageJSON:
        with open(file_path, "r") as f:
            data = json.load(f)
            return PageJSON.from_dict(data)

    def save_data(self, file_path: Path, data: PageJSON) -> None:
        with open(file_path, "w") as f:
            json.dump(data.to_dict(), f, indent=4)

    def get_note_by_name(self, name: str, data: PageJSON) -> list[(int, Note)] | None:
        notes = []

        for note_id, note in data.notes.items():
            if note.name == name:
                notes.append((note_id, note))

        return notes if notes else None

    def display_notes(self, note_data: PageJSON):
        if note_data.note_count == 0:
            Text.info("No notes created for this page!")
            return

        Text.info(f"Total Notes: {note_data.note_count}")
        Text.text("\n---\n")

        for ID, note in note_data.notes.items():
            Text.text(
                f"Note ID: {ID}\nNote Name: {note.name}\n Note Description: {note.description if note.description else 'None set.'}\n"
            )

        Text.text("\n---\n")

    # endregion

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
                        Text.error(
                            f"Multiple pages named {page}. Please select a page via ID"
                        )
                        Text.info("Use pynote page list to view current pages.")

                else:
                    Text.error("Page does not exist.")
                    return

        else:
            data: PageJSON = self.load_data(BASE_NOTE_PAGE)
            fp = BASE_NOTE_PAGE

        data.add_new_note(name, desc)

        self.save_data(fp, data)

        Text.success(f"Note created at {fp}.")

    def delete_note(self, name: str, page: str | None) -> None:
        if page:
            file_path = self.page_manager.get_page_by_name(page)

            if not file_path:
                Text.error("Page does not exist.")
                return

            elif len(file_path) > 1:
                Text.error(f"Multiple pages named {page}. Please use the id")
                return

            file_path = Path(file_path[0].file_path)

        else:
            file_path = BASE_NOTE_PAGE

        data = self.load_data(file_path)

        notes = self.get_note_by_name(name, data)

        if notes:
            if len(notes) > 1:
                Text.info(
                    f"Multiple notes with the name {name} have been found. Use [bold yellow]{f'pynote notes list --page {page}' if page else 'pynote notes list'}[/bold yellow]"
                )
                return

            else:
                del data.notes[notes[0][0]]
                self.save_data(file_path, data)

                Text.success("Note deleted!")
                return

        else:
            return

    def list_notes(self, page: str | None) -> None:
        file_path = BASE_NOTE_PAGE

        if page:
            pages = self.page_manager.get_page_by_name(page)

            if not pages:
                Text.error("Page does not exist.")
                return

            elif len(pages) > 1:
                Text.error("Multiple pages by that name exist. Please use the id.")
                return

            else:
                file_path = Path(pages[0].file_path)

        data = self.load_data(file_path)

        self.display_notes(data)


n = NoteManager()


def add_note(name: str, desc: str | None, page: str | None) -> None:
    n.add_note(name=name, desc=desc, page=page)


def delete_note(name: str, page: str | None) -> None:
    n.delete_note(name=name, page=page)


def list_notes(page: str | None) -> None:
    n.list_notes(page=page)
