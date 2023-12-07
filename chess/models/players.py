import random
import secrets
import logging

from tinydb import TinyDB, Query


class Player:
    """players model class"""
    db = TinyDB('./data/players.json')

    def __init__(self,
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

        # TODO: implement init method
        pass

    def to_dict(self) -> dict:
        """convert player to dict"""
        return self.__dict__

        # TODO: implement to dict method
        pass

    def from_dict(self, player_dict):
        """convert dict to player"""
        return Player(**player_dict)

        # TODO: implement from dict method

    def create(self) -> None:
        """Create method for players"""
        self.db.insert(self.to_dict())

        # TODO: implement create method
        pass

    def read_one(self) -> None:
        """Read method for players"""
        # TODO: implement read one method
        pass

    def read_all(self) -> None:
        """Read all method for players"""
        # TODO: implement read all method
        pass

    def search_by(self, key: str, value) -> None:
        """Search method for players by key and value"""
        #  TODO: implement search by key and value

    pass

    def update(self) -> None:
        """Update method for players"""
        # not necessary
        raise NotImplementedError("not included in specs")

    def delete(self) -> None:
        """Delete method for players"""
        # not necessary
        raise NotImplementedError("not included in specs")
        pass

    def __repr__(self) -> str:
        """Player representation"""

        return f"Player(firstname={self.firstname}, lastname={self.lastname}, birthdate={self.birthdate}, " \
               f"player_id={self.player_id})"

    def delete_all(self):
        """delete all method for players"""
        pass

    def bootstrap(self):
        """create 100 players"""
        pass

    def reboot(self):
        """delete all players and create 100 players"""
        pass
