from __future__ import annotations

import secrets

from tinydb import Query, TinyDB, where

from .consts import PLAYER_FILE


class Player:
    """
    Player class to interact with player data in  database.

    """

    db = TinyDB(PLAYER_FILE)

    def __init__(
            self,
            firstname: str,
            lastname: str,
            birthdate: str = "1970-01-01",
            player_id: int | None = None,
    ) -> None:
        """Init method for players"""

        self.player_id = player_id if player_id else secrets.token_hex(4)
        self.firstname = firstname.capitalize()
        self.lastname = lastname.upper()
        self.birthdate = birthdate

    def to_dict(self) -> dict:
        """convert player to dict"""

        return self.__dict__

    @classmethod
    def from_dict(cls, player_dict):
        """convert dict to player"""

        return Player(**player_dict)

    def create(self) -> None:
        """Create method for players"""

        self.db.insert(self.to_dict())

    @classmethod
    def read_one(cls, player_id: str) -> 'Player' | None:
        """Read method for players (Read one)"""
        player = Query()
        result = cls.db.search(player.player_id == player_id)

        if result:
            return Player.from_dict(result[0])
        else:
            return None

    @classmethod
    def read_all(cls) -> list[dict]:
        """Read all method for players"""

        res = cls.db.all()

        return [Player.from_dict(player) for player in res]

    @classmethod
    def all_ids(cls) -> list[str]:
        """return all player ids"""

        return [player.player_id for player in cls.read_all()]

    @classmethod
    def search(cls, player_id: str) -> list[Player]:
        """Search for a player by player_id"""

        player_search = Query()
        result = cls.db.search(player_search.player_id == player_id)

        return [Player.from_dict(data) for data in result]

    @classmethod
    def search_by(cls, key: str, value) -> list[Player]:
        """Search method for players by key and value"""

        res = cls.db.search(where(key) == value)

        return [Player.from_dict(player) for player in res]

    def update(self) -> None:
        """Update method for players"""

        self.db.update(self.to_dict(), where("player_id") == self.player_id)

        # print(f"Player {self.player_id} updated successfully.")

    def delete(self) -> None:
        """Delete method for players"""

        raise NotImplementedError("not included in specs")

    @classmethod
    def delete_all(cls) -> None:
        """delete all method for players"""

        cls.db.truncate()

    @classmethod
    def bootstrap(cls, num_players: int = 5) -> None:
        """Create method for players (Bootstrap)"""

        for _ in range(num_players):
            token = "test_" + secrets.token_hex(3)
            p = Player(token, token, token, player_id=token)
            p.create()

    @classmethod
    def reboot(cls, num_players: int = 5) -> None:
        """delete all players and create 100 players"""

        cls.delete_all()
        cls.bootstrap(num_players)

    def __repr__(self) -> str:
        return f"{self.__dict__}"
