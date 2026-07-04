from pathlib import Path

from .global_vars import Text
from ..data_storage import PageDB
from ..dataclasses import Page
from ..paths import PAGES_DIR

__all__ = ["create_page", "delete_page", "list_pages", "display_page"]


class PageManager:
    def __init__(self) -> None:
        self.pagedb = PageDB()

    # Helpers
    #region
    def display_pages(self, pages: list[Page]) -> None:
        if not pages:
            Text.text("No pages to display.")
            return

        for i, page in enumerate(pages, 1):
            Text.text(f"{i}. {page.page_name} - ID: {page.page_id}")

    def display_page(self, page: str) -> None:
        Text.info("Will be implemented soon")
    
    def create_page_path(self, path: Path) -> None:
        path.touch()
    
    def delete_page_path(self, path: Path) -> None:
        path.unlink(missing_ok = True)
    #endregion

    def create_page(self, name: str, is_checklist: bool, text_type: str) -> None:
        with Text.status("Creating Page...", style = "bold cyan"):
            if is_checklist:
                page_id, path = self.pagedb.create_page(
                    page_name=name,
                    page_type="checklist",
                    text_type=text_type
                )
                self.create_page_path(path)

            else:
                page_id, path = self.pagedb.create_page(
                    page_name=name, page_type="normal", text_type=text_type
                )
                self.create_page_path(path)

        Text.text(f"✓ Created Page {name}\n    - ID: {page_id}", style = "bold cyan")

    def delete_page(self, value: str) -> None:
        with Text.status("Deleting Page...", style = "bold cyan"):
            if value.isdigit():
                page = self.pagedb.delete_page(int(value))
                if page: self.delete_page_path(page)
                Text.text("✓ Page removed.", style = "bold cyan")
                return

            r_value = self.pagedb.delete_page_by_name(value)

        if r_value:
            Text.info(
                "Couldn't remove page (multiple pages found). Please use the ID."
            )
            self.display_pages(pages=r_value)

        else:
            Text.text("✓ Page removed.", style = "bold cyan")

    def get_all_pages(self) -> list[Page]:
        return self.pagedb.get_all()


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
