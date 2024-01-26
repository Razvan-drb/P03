import os
import logging
import secrets
import random

from typing import List
from tinydb import TinyDB, Query, where

from chess.models.rounds import Round


class Tournament:
    """Tournament model class"""

    db = TinyDB("./data/tournaments.json")

    N_PLAYERS = 4
    N_ROUNDS = 3
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
        """Init method for tournaments

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

        # handly written args by user
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

    def to_dict(self) -> dict:
        """Convert tournament to dict"""
        return self.__dict__

    @property
    def n_players(self) -> int:
        """Return number of players"""

        return len(self.player_id_list)

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
    def search_by(cls, key: str, value) -> list[dict]:
        """Search method for tournaments by key and value"""

        res = cls.db.search(where(key) == value)
        return [Tournament.from_dict(tournament) for tournament in res]

    def update(self) -> None:
        """Update method for tournaments"""

        self.db.update(self.to_dict(), where('tournament_id') == self.tournament_id)

        print(f"Tournament {self.tournament_id} updated successfully.")

    def delete(self) -> None:
        """Delete method for tournaments"""
        # Not necessary for now
        raise NotImplementedError("Not included in specs")

    def add_player(self, player_id: str) -> None:  # !!!!!!!!!!
        """Add player to tournament"""

        # TODO : add verification that the player is not already in the tournament
        # TODO : add verification that the player is not already in the Player DB Table

        if player_id in self.player_id_list:
            raise ValueError("Le jouer existe deja dans le tournament.")

        # TODO: Add verification that the player is not already in the Player DB Table
        # if self._player_exists_in_db(player_id):  # a implementer
        #     raise ValueError("Le jouer existe deja dans Player DB Table .")

        # si status != created => trop tard mon coco :)

        # verify that current player number not higher than number of players (4)
        if len(self.player_id_list) > self.N_PLAYERS:
            raise AttributeError(
                "Current player number is higher than the number of players (4)"
            )

        # verify that the current player is not in the player list
        if player_id in self.player_id_list:
            raise AttributeError("Current player is already in the player list")

        # add player to the player list
        self.player_id_list.append(player_id)

        self.update()  # for now it is useless   !!!!!

    def update_status(self, new_status: str):
        """ """

        #     # on passe de created à en cours, on passe de en cours à terminé

        #     # quand on passe de created à en cours :
        #     #  - il faut calucler d'un coup toutes les rondes / tous les match
        #     # round 0 = player 0 vs player 1, player 2 vs player 3
        #     # round 1 = player 0 vs player 2, player 1 vs player 3
        #     # round 2 = player 0 vs player 3, player 1 vs player 2

        #     # c'est ici que on va use self._add_round(blabla bla)

        #     # enregistrer les rounds dans la db

        #     # MAJ la rounds_id_list de la clas
        #     # update le numéro de la ronde en cours
        #     # save notre new  tournois

        #     # interdire de passer de terminé à en cours ou terminé à created !!!!

        #     # pas le droit de passer en created à en cours si pas 4 joeurs

        #     # quand on passe de en cours à terminé ??? que se passe t'il ?

        # check if new status is authorised
        if new_status not in self.AUTHORISED_STATUS:
            raise ValueError("Invalid tournament status.")

        # manage created
        if self.status == "Created" and new_status == "In Progress":
            # if not good n players
            if len(self.player_id_list) != self.N_PLAYERS:
                raise ValueError(
                    "Pas possible de passer a 'In Progress' sans 4 jouers."
                )

            # Calculate rounds and matches
            round_0 = [
                [self.player_id_list[0], self.player_id_list[1]],  # 1er match
                [self.player_id_list[2], self.player_id_list[3]],  # 2eme match
            ]

            round_1 = [
                [self.player_id_list[0], self.player_id_list[2]],  # 1er match
                [self.player_id_list[1], self.player_id_list[3]],  # 2eme match
            ]

            round_2 = [
                [self.player_id_list[0], self.player_id_list[3]],  # 1er match
                [self.player_id_list[1], self.player_id_list[2]],  # 2eme match
            ]

            # match list
            match_list = [round_0, round_1, round_2]

            for i, match_list in enumerate(match_list):
                # add round id db
                round_id = self._add_round(i, match_list)
                # update round id list wuth new roud created
                self.round_id_list.append(round_id)

            # Save rounds to DB
            self.status = "In Progress"
            self.update()

        elif self.status == "In Progress" and new_status == "Completed":
            # Check if all rounds have been played

            if len(self.round_id_list) < self.N_PLAYERS - 1:
                raise ValueError(
                    "Impossible de terminer le tournoi sans que tout les rounds sois finis."
                )

        else:
            raise ValueError(
                f"Status invalid. Impossible de changer le status de {self.status} a {new_status}"
            )

    def next_round(self):
        """change the round +=1"""

        # Check si toutes le rounds sont finished
        if self.current_round_number == self.N_ROUNDS - 1:
            # Update status et save
            self.status = "Completed"
            self.update()

        else:
            # On continue les rounds
            self.current_round_number += 1
            self.update()

    def get_current_round(self):
        """Get the current round number for the tournament."""
        if not self.round_id_list:
            print("No rounds have been computed yet.")
            return None

        current_round_id = self.round_id_list[-1]
        print(f"Current Round ID: {current_round_id}")

        # Print the result of Round.search_by
        current_round_data = Round.search_by('round_id', current_round_id)
        print(f"Current Round Data: {current_round_data}")

        if current_round_data:
            current_round = current_round_data[0]
            print(f"Current Round: {current_round}")
            return current_round

        print("No current round found.")
        return None

    def update_current_round(self, match_list=None):
        """Update the current round number for the tournament."""

        # find the round instance of the current round
        # update the round
        # save round updated

        #
        # if self.current_round_number >= 0:
        #     # Increment round number
        #     if self.current_round_number < self.N_ROUNDS - 1:
        #         self.current_round_number += 1
        #
        #         match_list = match_list[self.current_round_number]
        #         new_round_number = self._add_round(
        #             self.current_round_number, match_list
        #         )  # ajout a la DB
        #         self.round_id_list.append(
        #             new_round_number
        #         )  # ajout new round number a la round id list
        #
        #     else:
        #         self.status = "Completed"
        #
        #     self.update()


    def get_score(self):
        # UN DES TRUC QUON FERRA A LA TOUTE FIN !!!
        pass

    def _add_round(self, round_number: int, matches: List[str]) -> None:
        """Add a round to the tournament."""

        round_id = f"{self.tournament_id}_round_{round_number}"
        new_round = Round(round_id, matches)

        # Add the round to the list of rounds
        self.round_id_list.append(new_round.round_id)

        self.update()

        return new_round.round_id

    def __repr__(self) -> str:
        """Tournament representation"""

        return (
            f"Tournament(name={self.name}, start_date={self.start_date}, end_date={self.end_date}, "
            f"tournament_id={self.tournament_id}, description={self.description},location={self.location}, "
            f"matches={self.round_id_list}, participants={self.player_id_list})"
        )

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
            tournament_id = "boot_" + secrets.token_hex(4)
            # matches = [f"Match{i}" for i in range(random.randint(10, 20))]
            # participants = [f"Participant{i}" for i in range(random.randint(6, 10))]
            description = "Description for " + name
            location = [f"Location{i}" for i in range(random.randint(3, 5))]
            t = Tournament(
                name,
                start_date,
                end_date,
                description=description,
                location=location,
                tournament_id=tournament_id,
            )
            t.create()

    @classmethod
    def reboot(cls, num_tournaments: int = 100) -> None:
        """Delete all tournaments and create 100 tournaments"""

        cls.delete_all()
        cls.bootstrap(num_tournaments)
