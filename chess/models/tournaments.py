import secrets
import random

from typing import List
from tinydb import TinyDB, Query, where


class Tournament:
    """Tournament model class"""
    db = TinyDB('./data/tournaments.json')

    def __init__(self,
                 name: str,
                 start_date: str,
                 end_date: str,
                 tournament_id: str | None = None,
                 rounds_id_list: List[str] = None,
                 player_id_list: List[str] = None,
                 current_round_number: int = 0,
                 status: str = "Created"
                 ) -> None:
        """Init method for tournaments"""

        self.status = status
        self.tournament_id = tournament_id if tournament_id else secrets.token_hex(4)
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_id_list = rounds_id_list if rounds_id_list else []
        self.player_id_list = player_id_list if player_id_list else []
        self.current_round_number = current_round_number

    def add_player(self, player_id: str) -> None:
        """ Add player to tournament"""

        # verify that current player number not higher than number of players (4)
        if len(self.player_id_list) > 4:
            raise AttributeError("Current player number is higher than number of players (4)")

        # verify that current player in not in player list
        if player_id in self.player_id_list:
            raise AttributeError("Current player is already in player list")

        # add player to player list
        self.player_id_list.append(player_id)

        self.update()

        # if len(self.player_id_list) == 4:
        #     self.status = "Launched"
        #     self.current_round_number = 0
        #     self.update()
        #

    def update_status(self):
        pass

    def update_current_round_number(self):
        pass

    def get_score(self):
        pass

    def to_dict(self) -> dict:
        """Convert tournament to dict"""
        return self.__dict__

    @classmethod
    def from_dict(cls, tournament_dict):
        """Convert dict to tournament"""
        return Tournament(**tournament_dict)

    def create(self) -> None:
        """Create method for tournaments"""
        self.db.insert(self.to_dict())

    @classmethod
    def read_one(cls, tournament_id: str) -> dict | None:
        """Read method for tournaments (Read one)"""
        tournament = Query()
        result = cls.db.search(tournament.tournament_id == tournament_id)
        return result[0] if result else None

    @classmethod
    def read_all(cls) -> list[dict]:
        """Read all method for tournaments"""
        return cls.db.all()

    @classmethod
    def search_by(cls, key: str, value) -> list[dict]:
        """Search method for tournaments by key and value"""
        return cls.db.search(where(key) == value)

    def update(self) -> None:
        """Update method for tournaments"""
        # Not necessary for now
        raise NotImplementedError("Not included in specs")

    def delete(self) -> None:
        """Delete method for tournaments"""
        # Not necessary for now
        raise NotImplementedError("Not included in specs")

    def __repr__(self) -> str:
        """Tournament representation"""
        return (f"Tournament(name={self.name}, start_date={self.start_date}, end_date={self.end_date}, "
                f"tournament_id={self.tournament_id}, matches={self.matches}, participants={self.participants})")

    @classmethod
    def delete_all(cls) -> None:
        """Delete all method for tournaments"""
        cls.db.truncate()

    @classmethod
    def bootstrap(cls, num_tournaments: int = 3) -> None:
        """Create method for tournaments (Bootstrap)"""
        for _ in range(num_tournaments):
            name = "Tournament" + secrets.token_hex(4)
            start_date = f"{random.randint(2023, 2025)}-01-01"
            end_date = f"{random.randint(2025, 2027)}-12-31"
            tournament_id = secrets.token_hex(4)
            matches = [f"Match{i}" for i in range(random.randint(10, 20))]
            participants = [f"Participant{i}" for i in range(random.randint(6, 10))]
            t = Tournament(name, start_date, end_date, tournament_id, matches, participants)
            t.create()

    @classmethod
    def reboot(cls, num_tournaments: int = 100) -> None:
        """Delete all tournaments and create 100 tournaments"""
        cls.delete_all()
        cls.bootstrap(num_tournaments)
