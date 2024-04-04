from __future__ import annotations

import logging
import secrets
from typing import List, Optional

from tinydb import Query, TinyDB, where

from .consts import ROUND_FILE


class Round:
    """Round model class"""

    db = TinyDB(ROUND_FILE)

    def __init__(
        self,
        round_number: int,
        matches: List[str],
        round_id: str | None = None,
    ) -> None:
        """Init method for rounds"""

        self.round_id = round_id if round_id else secrets.token_hex(4)
        self.round_number = round_number
        self.matches = matches

    def to_dict(self) -> dict:
        """Convert round to dict"""
        return self.__dict__

    @classmethod
    def from_dict(cls, round_dict):
        """Convert dict to round"""

        return Round(**round_dict)

    def create(self) -> None:
        """Create method for rounds"""

        self.db.insert(self.to_dict())

    @classmethod
    def read_one(cls, round_id: str) -> dict | None:
        """Read method for players (Read one)"""
        player = Query()
        result = cls.db.search(player.round_id == round_id)

        res = result[0] if result else None

        return Round.from_dict(res) if res else None

    @classmethod
    def read_all(cls) -> list[dict]:
        """Read all method for players"""

        res = cls.db.all()

        return [Round.from_dict(player) for player in res]

    @classmethod
    def search(cls, round_id: str) -> list[dict]:
        """Search for a player by round_id"""

        player_search = Query()
        result = cls.db.search(player_search.round_id == round_id)

        return [Round.from_dict(data) for data in result]

    @classmethod
    def search_by(cls, key: str, value) -> list[dict]:
        """Search method for players by key and value"""

        res = cls.db.search(where(key) == value)

        return [Round.from_dict(player) for player in res]

    def update(self):
        """Update method for round"""

    def update(self) -> None:
        """Update method for players"""

        self.db.update(self.to_dict(), where("round_id") == self.round_id)

        # logging.warning(f"Round {self.round_id} updated successfully.")

    def delete(self) -> None:
        """Delete method for players"""

        raise NotImplementedError("not included in specs")

    @classmethod
    def delete_all(cls) -> None:
        """delete all method for players"""

        cls.db.truncate()

    @classmethod
    def reboot(cls) -> None:
        """delete all players and create 100 players"""

        cls.delete_all()

    def __repr__(self) -> str:
        return f"{self.__dict__}"
