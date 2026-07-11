from pathlib import Path
from json import dump

from .global_vars import Text
from ..data_storage import PageDB
from ..dataclasses import Page, PageJSON

__all__ = ["create_page", "delete_page", "list_pages", "display_page", "clear_data"]


class PageManager:
    def __init__(self) -> None:
        self.pagedb = PageDB()

    # Helpers
    # region
    def display_pages(self, pages: list[Page]) -> None:
        if not pages:
            Text.text("No pages to display.")
            return

        for i, page in enumerate(pages, 1):
            Text.text(f"{i}. {page.page_name} - ID: {page.page_id}")

    def display_page(self, page: str) -> None:
        Text.info("Will be implemented soon")

    def create_page_path(self, page_name: str, page_type: str, path: Path) -> None:
        p = PageJSON(page_name=page_name, page_type=page_type)

        with open(path, "w") as fp:
            dump(p.to_dict(), fp, indent = 4)

    def delete_page_path(self, path: Path) -> None:
        path.unlink(missing_ok=True)

    # endregion

    def create_page(self, name: str, is_checklist: bool, text_type: str) -> None:
        with Text.status("Creating Page...", style="bold cyan"):
            if is_checklist:
                page_id, path = self.pagedb.create_page(
                    page_name=name, page_type="checklist", text_type=text_type
                )
                self.create_page_path(name, "checklist", path)

            else:
                page_id, path = self.pagedb.create_page(
                    page_name=name, page_type="normal", text_type=text_type
                )
                self.create_page_path(name, "normal", path)

        Text.text(f"✓ Created Page {name}\n    - ID: {page_id}", style="bold cyan")

    def delete_page(self, value: str) -> None:
        with Text.status("Deleting Page...", style="bold cyan"):
            if value.isdigit():
                page = self.pagedb.delete_page(int(value))

                if page:
                    self.delete_page_path(Path(page))
                    Text.text("✓ Page removed.", style="bold cyan")

                else:
                    Text.error("Page not found")

                return

            r_value = self.pagedb.delete_page_by_name(value)

        if isinstance(r_value, list):
            Text.info("Couldn't remove page (multiple pages found). Please use the ID.")
            self.display_pages(r_value)

        elif isinstance(r_value, (str, Path)):
            self.delete_page_path(Path(r_value))
            Text.text("✓ Page removed.", style="bold cyan")

        else:
            Text.error("Page not found.")

    def get_all_pages(self) -> list[Page]:
        return self.pagedb.get_all()

    def clear_database(self) -> None:
        pages = self.pagedb.clear_data()

        for p in pages:
            self.delete_page_path(Path(p.file_path))


p = PageManager()


# Methods to use
def create_page(page_name: str, is_checklist: bool, text_type: str) -> None:
    p.create_page(name=page_name, is_checklist=is_checklist, text_type=text_type)


def delete_page(value: str) -> None:
    p.delete_page(value)


def list_pages() -> None:
    p.display_pages(p.get_all_pages())


def display_page(page: str) -> None:
    p.display_page(page=page)


def clear_data() -> None:
    p.clear_database()
