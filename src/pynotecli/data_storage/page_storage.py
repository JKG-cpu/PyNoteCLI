import sqlite3
from pathlib import Path

from ..dataclasses import Page
from ..paths import DATABASE_DIR, PAGES_DIR


__all__ = ["PageDB"]


class PageDB:
    def __init__(self):
        self.base_dir = DATABASE_DIR
        self.db_path = self.base_dir / "pages.db"

        self.db_path.touch(exist_ok=True)

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
        self, page_name: str, page_type: str, text_type: str
    ) -> tuple[int, Path]:
        conn = self._connect()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO pages (page_name, page_type, text_type, file_path)
            VALUES (?, ?, ?, ?)
            """,
            (page_name, page_type, text_type, ""),  # temp placeholder
        )

        conn.commit()

        page_id = cur.lastrowid

        file_path = PAGES_DIR / f"{page_name}_{page_id}.json"

        cur.execute(
            "UPDATE pages SET file_path = ? WHERE page_id = ?",
            (str(file_path), page_id),
        )

        conn.commit()
        conn.close()

        return page_id, file_path

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

    def delete_page(self, page_id: int) -> Path | None:
        # Get Page Filepath to return
        p = self.get_page_by_id(page_id)

        conn = self._connect()
        cur = conn.cursor()

        cur.execute("DELETE FROM pages WHERE page_id = ?", (page_id,))

        conn.commit()
        conn.close()

        if p:
            return p.file_path

    def delete_page_by_name(self, page_name: str) -> list[Page] | Path | None:
        pages = self.get_page_by_name(page_name)

        if not pages:
            return None

        if len(pages) != 1:
            return pages

        return self.delete_page(pages[0].page_id)

    # Clear Data
    def clear_data(self) -> list[Page]:
        pages = self.get_all()

        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            DROP TABLE IF EXISTS pages
        """)

        conn.commit()
        conn.close()

        return pages

    def clear_file(self) -> None:
        with open(self.db_path, "wb"):
            pass
