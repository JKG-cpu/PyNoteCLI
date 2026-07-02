from ..data_storage import PageDB
from .global_vars import Text

__all__ = [
    "create_page"
]

class PageManager:
    def __init__(self) -> None:
        self.pagedb = PageDB()

    def create_page(self, name: str, is_checklist: bool, text_type: str) -> None:
        Text.info("Creating Page...")
        
        if is_checklist:
            page_id = self.pagedb.create_page(
                page_name = name,
                page_type = "checklist",
                text_type = text_type,
                file_path = "N/A"
            )
            Text.success(f"Created page {name}. ID: {page_id}")
    
        else:
            page_id = self.pagedb.create_page(
                page_name = name,
                page_type = "normal",
                text_type = text_type,
                file_path = "N/A"
            )
            Text.success(f"Created page {name}. ID: {page_id}")

# Methods to use
def create_page(page_name: str, is_checklist: bool, text_type: str) -> None:
    PageManager().create_page(
        name = page_name,
        is_checklist = is_checklist,
        text_type = text_type
    )