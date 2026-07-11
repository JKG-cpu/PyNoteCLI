from dataclasses import dataclass, asdict, field
from typing import Literal
from collections import deque

__all__ = ["Page", "PageJSON", "Note"]


@dataclass
class Page:
    page_id: int
    page_name: str
    page_type: str
    text_type: str
    file_path: str


@dataclass
class Note:
    name: str
    description: str

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Note":
        return cls(**data)


@dataclass
class PageJSON:
    page_name: str
    page_type: Literal["checklist", "normal"]
    page_tag: str = ""
    note_count: int = 0
    deleted_ids: deque[int] = field(default_factory=deque)
    notes: dict[int, Note] = field(default_factory=dict)

    # Get
    def get_available_id(self) -> int:
        if self.deleted_ids:
            return self.deleted_ids.popleft()

        return max(self.notes, default=0) + 1

    def get_notes_by_name(self, name: str) -> list[Note]:
        pass

    # Adding Notes
    def add_new_note(self, name: str, desc: str) -> None:
        self.notes[self.get_available_id()] = Note(name=name, description=desc)

    # Delete Notes
    def delete_note(self, id: int) -> None:
        self.deleted_ids.append(id)
        del self.notes[id]

    def delete_note_by_name(self, name: str) -> None | list[tuple[int, Note]]:
        pass

    # Json Serialization Methods
    def to_dict(self) -> dict:
        return {
            "page_name": self.page_name,
            "page_tag": self.page_tag,
            "page_type": self.page_type,
            "note_count": self.note_count,
            "deleted_ids": list(self.deleted_ids),
            "notes": {note: self.notes[note].to_dict() for note in self.notes},
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PageJSON":
        return cls(
            page_name=data["page_name"],
            page_tag=data["page_tag"],
            page_type=data["page_type"],
            note_count=data["note_count"],
            deleted_ids=deque(data["deleted_ids"]),
            notes={
                note_id: Note.from_dict(note_data)
                for note_id, note_data in data["notes"].items()
            },
        )
