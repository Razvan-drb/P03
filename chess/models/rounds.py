from __future__ import annotations

import secrets

from typing import List
from tinydb import TinyDB, Query, where


class Round:
    """Round model class"""

    db = TinyDB("./data/rounds.json")

    def __init__(
        self,
        round_number: int,
        matches: List[str],
        round_id: str | None = None,
        status: str = "Created",
    ) -> None:
        """Init method for rounds"""

        self.round_id = round_id if round_id else secrets.token_hex(4)
        self.round_number = round_number
        self.matches = matches
        self.status = status

    def to_dict(self) -> dict:
        """Convert round to dict"""
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        """Convert dict to round"""

        return Round(**data)

    def create(self) -> None:
        """Create method for rounds"""
        self.db.insert(self.to_dict())

    def search(self, round_id: str) -> list[dict]:
        """Search for a round by round_id"""

        round_search = Query()
        result = self.db.search(round_search.round_id == round_id)

        return [Round.from_dict(data) for data in result]

    @classmethod
    def search_by(cls, key: str, value) -> list[dict]:
        """Search method for rounds by key and value"""
        res = cls.db.search(Query()[key] == value)
        return res  # Return the list of matching rounds

    def update(self):
        """Update method for round"""

        self.db.update(self.to_dict(), where('round_id') == self.round_id)

        print(f"Round {self.round_id} updated successfully.")

