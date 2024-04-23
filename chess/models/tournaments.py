from __future__ import annotations

import logging
import random
import secrets
from typing import List

from tinydb import Query, TinyDB, where

from chess.helpers import now
from chess.models.consts import TOURNAMENT_FILE
from chess.models.players import Player
from chess.models.rounds import Round


class Tournament:
    """Tournament model class

    Positionnal args:
        name - str - name of the tournament
        start_date - str - start date of the tournament
        end_date - str - end date of the tournament

    Optional args:
        description - str - description of the tournament - default = "" (empty string)
        location - str - location of the tournament - default = "" (empty string)
        tournament_id - str - id of the tournament - default = None
        round_id_list - List[str] - list of rounds id - default = None
        player_id_list - List[str] - list of players id - default = None
        current_round_number - int - current round number - default = -1
        status - str - status of the tournament - default = "Created"
    """

    db = TinyDB(TOURNAMENT_FILE)

    N_PLAYERS = 4
    N_ROUNDS = 3
    N_MATCHES_PER_ROUND = 2
    AUTHORISED_STATUS = ["Created", "In Progress", "Completed"]

    def __init__(
        self,
        name: str,
        start_date: str,
        end_date: str,
        description: str = "",
        location: str = "",
        tournament_id: str | None = None,
        round_id_list: List[str] | None = None,
        player_id_list: List[str] | None = None,
        current_round_number: int = -1,
        status: str = "Created",
    ):
        """Init method for tournaments"""

        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.location = location

        self.tournament_id = tournament_id if tournament_id else secrets.token_hex(4)
        self.round_id_list = round_id_list if round_id_list else []
        self.player_id_list = player_id_list if player_id_list else []
        self.current_round_number = current_round_number
        self.status = status

    @property
    def current_round_id(self) -> str:
        try:
            return self.round_id_list[self.current_round_number]
        except Exception as e:
            logging.error(f"Error getting current round id: {e}")
            return None

    @property
    def current_round(self):
        """Get the current round number for the tournament."""

        if not self.round_id_list:
            logging.warning("No rounds have been computed yet.")
            return None

        # try to get current round data
        current_round_ = Round.search_by("round_id", self.current_round_id)
        print("***********************", current_round_)
        assert len(current_round_) == 1
        current_round_ = current_round_[0]

        if not current_round_:
            logging.warning(f"No data found for Round ID: {self.current_round_id}")
            return None

        return current_round_

    @property
    def n_players(self) -> int:
        """Return number of players"""

        return len(self.player_id_list)

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
        res = result[0] if result else None

        return Tournament.from_dict(res) if res else None

    @classmethod
    def read_all(cls) -> list[dict]:
        """Read all method for tournaments"""

        res = cls.db.all()
        return [Tournament.from_dict(tournament) for tournament in res]

    @classmethod
    def search(cls, tournament_id):
        """Search for a tournament by tournament_id"""

        tournament = Query()
        result = cls.db.search(tournament.tournament_id == tournament_id)
        res = result[0] if result else None
        t = Tournament.from_dict(res) if res else None

        return [t]

    @classmethod
    def search_by(cls, key: str, value) -> list[dict]:
        """Search method for tournaments by key and value"""

        res = cls.db.search(where(key) == value)
        return [Tournament.from_dict(tournament) for tournament in res]

    def update(self) -> None:
        """Update method for tournaments"""

        self.db.update(self.to_dict(), where("tournament_id") == self.tournament_id)

    def delete(self) -> None:
        """Delete method for tournaments"""

        raise NotImplementedError("Not included in specs")

    @classmethod
    def delete_all(cls) -> None:
        """Delete all method for tournaments"""

        cls.db.truncate()

    def add_player(self, player_id: str) -> None:
        """Add player to tournament"""

        # TODO : add verification that the player is not already in the tournament
        # TODO : add verification that the player is not already in the Player DB Table

        if player_id in self.player_id_list:
            raise ValueError("Le jouer existe deja dans le tournament.")

        if player_id not in Player.all_ids():
            raise ValueError("Le jouer n'existe pas dans Player DB Table.")

        if self.status != "Created":
            raise ValueError(
                "Impossible d'ajouter un joueur après le début du tournoi."
            )

        # verify that current player number not higher than number of players (4)
        if len(self.player_id_list) > self.N_PLAYERS:
            raise AttributeError(
                f"Current player number is higher than the number of players ({self.N_PLAYERS})"
            )

        # add player to the player list
        self.player_id_list.append(player_id)

        self.update()  # for now it is useless?

    def _add_round(self, round_number: int, matches: List[str]) -> str:
        """Add a round to the tournament."""

        # init and create a new round
        round_id = f"{self.tournament_id}_round_{round_number}"
        new_round = Round(round_number, matches, round_id=round_id)
        new_round.create()

        # Add the round to the list of rounds
        self.round_id_list.append(new_round.round_id)

        # save the tournament
        self.update()

        return new_round.round_id

    def update_status(self, new_status: str):
        """Update the status of the tournament."""

        # Check if the new status is authorised
        if new_status not in self.AUTHORISED_STATUS:
            raise ValueError(
                f"Invalid tournament status should be in {self.AUTHORISED_STATUS} recieved {new_status}."
            )

        if self.status == "Created" and new_status == "In Progress":
            # Check if there are enough players
            if self.n_players != self.N_PLAYERS:
                raise ValueError(
                    f"Impossible de passer à 'In Progress' sans {self.N_PLAYERS} joueurs, for now on en a {self.n_players}."
                )

            # on calcule les rounds
            round_0 = [
                # 1er match du round 0
                [
                    (self.player_id_list[0], -1),  # Player 0, (son id, son score)
                    (self.player_id_list[1], -1),  # Player 1, (son id, son score)
                ],
                # 2eme match du round 0
                [
                    (self.player_id_list[2], -1),  # Player 2,son id son score
                    (self.player_id_list[3], -1),  # Player 3, son id son score
                ],
            ]

            round_1 = [
                [
                    (self.player_id_list[0], -1),  # P0 (id, score)
                    (self.player_id_list[2], -1),  # P2 (id, score)
                ],  # 1er match
                [
                    (self.player_id_list[1], -1),
                    (self.player_id_list[3], -1),
                ],  # 2eme match
            ]

            round_2 = [
                [
                    (self.player_id_list[0], -1),
                    (self.player_id_list[3], -1),
                ],  # 1er match
                [
                    (self.player_id_list[1], -1),
                    (self.player_id_list[2], -1),
                ],  # 2eme match
            ]

            # match list
            match_list = [round_0, round_1, round_2]

            # Add rounds to database
            for i, round_matches in enumerate(match_list):
                _ = self._add_round(i, round_matches)

            # Update status to 'In Progress' and save
            self.status = "In Progress"
            self.current_round_number = 0
            self.update()

        elif self.status == "In Progress" and new_status == "Completed":
            # Check if all rounds are played
            if self.current_round_number + 1 != self.N_ROUNDS:
                raise ValueError(
                    "Impossible de terminer le tournoi sans que tous les rounds soient finis."
                )
            self.status = "Completed"
            self.update()

        else:
            raise ValueError(
                f"Statut invalide. Impossible de changer le statut de {self.status} à {new_status}."
            )

    def _next_round(self):
        """change the round +=1"""

        # Check si toutes le rounds sont finished
        if self.current_round_number == self.N_ROUNDS - 1:
            # Update status et save
            self.status = "Completed"

        else:
            # On continue les rounds
            self.current_round_number += 1

        self.update()

    def get_current_round(self):

        c = self.current_round
        return Round.from_dict(c.to_dict())

    def update_current_round(self, match_list=None):
        """Update the current round number for the tournament."""

        if not match_list:
            raise ValueError("Match list is empty")

        # update current round with match list
        current_round = self.get_current_round()
        current_round.matches = match_list

        logging.critical(f"Current Round: {self.current_round}")
        current_round.update()

        # next round
        self._next_round()

        # update
        self.update()

    def get_score(self, player_id):
        player_score = 0

        # Iterate through rounds
        for round_id in self.round_id_list:
            round_data = Round.search_by("round_id", round_id)

            if round_data:
                for match in round_data.matches:
                    # Iterate matches to find player's score
                    for player_tuple in match:
                        if player_tuple[0] == player_id:
                            player_score += player_tuple[1]

        return player_score

    @classmethod
    def bootstrap(cls, num_tournaments: int = 3) -> None:
        """Create method for tournaments (Bootstrap)"""

        for _ in range(num_tournaments):
            token = "test_" + secrets.token_hex(3) + "_" + now()

            t = Tournament(
                token + "_" + now(),
                token,
                token,
                tournament_id=token + "_" + now(),
            )
            t.create()

    @classmethod
    def bootstrap(cls, num_tournament: int = 4) -> None:
        """Create method for players (Bootstrap)"""

        for _ in range(num_tournament):
            token = "test_" + secrets.token_hex(3)

            p = Tournament(token, token, token, tournament_id=token)
            p.create()

    @classmethod
    def reboot(cls, num_tournament: int = 4) -> None:
        """delete all players and create 100 players"""

        cls.delete_all()
        cls.bootstrap(num_tournament)

    def __repr__(self) -> str:
        return f"{self.__dict__}"
