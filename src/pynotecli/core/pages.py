from ..data_storage import PageDB
from .global_vars import Text
from ..dataclasses import Page

__all__ = ["create_page", "delete_page", "list_pages", "display_page"]


class PageManager:
    def __init__(self) -> None:
        self.pagedb = PageDB()

    # Helpers
    def display_pages(self, pages: list[Page]) -> None:
        if not pages:
            Text.text("No pages to display.")
            return

        for i, page in enumerate(pages, 1):
            Text.text(f"{i}. {page.page_name} - ID: {page.page_id}")

    def display_page(self, page: str) -> None:
        Text.info("Will be implemented soon")

    def create_page(self, name: str, is_checklist: bool, text_type: str) -> None:
        Text.info("Creating Page...")

        if is_checklist:
            page_id = self.pagedb.create_page(
                page_name=name,
                page_type="checklist",
                text_type=text_type,
                file_path="N/A",
            )
            Text.success(f"Created page {name}. ID: {page_id}")

        else:
            page_id = self.pagedb.create_page(
                page_name=name, page_type="normal", text_type=text_type, file_path="N/A"
            )
            Text.success(f"Created page {name}. ID: {page_id}")

    def delete_page(self, value: str) -> None:
        Text.info(f"Removing Page...")

        if value.isdigit():
            self.pagedb.delete_page(int(value))
            Text.success("Page removed.")
            return

        else:
            r_value = self.pagedb.delete_page_by_name(value)

            if r_value:
                Text.info(
                    "Couldn't remove page (multiple pages found). Please use the ID."
                )
                self.display_pages(pages=r_value)

            else:
                Text.success("Page removed.")

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
