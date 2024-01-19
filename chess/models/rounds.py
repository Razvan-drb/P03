import secrets
from typing import List
from tinydb import TinyDB, Query


class Round:
    """Round model class"""
    db = TinyDB('./data/rounds.json')

    def __init__(self,
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

    def from_dict(self) -> dict:
        """Convert dict to round"""
        return self.__dict__

    def create(self) -> None:
        """Create method for rounds"""
        self.db.insert(self.to_dict())

    # TODO def search
    def search(self, round_id: str) -> list[dict]:
        """Search for a round by round_id"""

        round_search = Query()
        result = self.db.search(round_search.round_id == round_id)

        return [Round.from_dict(round_id) for round_id in result]
