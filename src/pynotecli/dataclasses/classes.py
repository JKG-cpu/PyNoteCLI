from dataclasses import dataclass

__all__ = ["Page"]


@dataclass
class Page:
    page_id: int
    page_name: str
    page_type: str
    text_type: str
    file_path: str
