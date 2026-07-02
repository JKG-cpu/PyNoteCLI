import sqlite3
from pathlib import Path
from dataclasses import dataclass

from ..dataclasses import Page


__all__ = ["PageDB"]


class PageDB:
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parents[1]
        self.db_path = self.base_dir / "database" / "pages.db"

        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init_db(self) -> None:
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            page_id INTEGER PRIMARY KEY AUTOINCREMENT,
            page_name TEXT NOT NULL,
            page_type TEXT NOT NULL,
            text_type TEXT NOT NULL,
            file_path TEXT NOT NULL
        )
        """)

        conn.commit()
        conn.close()

    def create_page(
        self, page_name: str, page_type: str, text_type: str, file_path: str
    ) -> int:
        conn = self._connect()
        cur = conn.cursor()

        cur.execute(
            """
        INSERT INTO pages (page_name, page_type, text_type, file_path)
        VALUES (?, ?, ?, ?)
        """,
            (page_name, page_type, text_type, file_path),
        )

        conn.commit()
        page_id = cur.lastrowid
        conn.close()

        return page_id

    def get_page_by_id(self, page_id: int) -> Page | None:
        conn = self._connect()
        cur = conn.cursor()

        cur.execute(
            """
        SELECT page_id, page_name, page_type, text_type, file_path
        FROM pages
        WHERE page_id = ?
        """,
            (page_id,),
        )

        row = cur.fetchone()
        conn.close()

        if not row:
            return None

        return Page(
            page_id=row[0],
            page_name=row[1],
            page_type=row[2],
            text_type=row[3],
            file_path=row[4],
        )

    def get_page_by_name(self, page_name: str) -> list[Page]:
        conn = self._connect()
        cur = conn.cursor()

        cur.execute(
            """
        SELECT page_id, page_name, page_type, text_type, file_path
        FROM pages
        WHERE page_name = ?
        """,
            (page_name,),
        )

        rows = cur.fetchall()
        conn.close()

        return [
            Page(
                page_id=r[0],
                page_name=r[1],
                page_type=r[2],
                text_type=r[3],
                file_path=r[4],
            )
            for r in rows
        ]

    def get_all(self) -> list[Page]:
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
        SELECT page_id, page_name, page_type, text_type, file_path
        FROM pages
        """)

        rows = cur.fetchall()
        conn.close()

        return [
            Page(
                page_id=r[0],
                page_name=r[1],
                page_type=r[2],
                text_type=r[3],
                file_path=r[4],
            )
            for r in rows
        ]

    def delete_page(self, page_id: int) -> None:
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("DELETE FROM pages WHERE page_id = ?", (page_id,))

        conn.commit()
        conn.close()

    def delete_page_by_name(self, page_name: str) -> int:
        pages = self.get_page_by_name(page_name)

        conn = self._connect()
        cur = conn.cursor()

        for page in pages:
            cur.execute("DELETE FROM pages WHERE page_id = ?", (page.page_id,))

        conn.commit()
        conn.close()

        return len(pages)
