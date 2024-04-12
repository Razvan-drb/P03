import logging
import secrets

import pytest

from chess.models.players import Player
from chess.models.rounds import Round
from chess.models.tournaments import Tournament


class TestTournamentBase:
    """Test Tournament model"""

    def test_init(self):
        """create a tournament"""

        token = "test_" + secrets.token_hex(2)

        t = Tournament(token, token, token, tournament_id=token)
        # logging.warning(t)

    def test_to_dict(self):
        """convert tournament to dict"""

        token = "test_" + secrets.token_hex(2)

        t = Tournament(token, token, token, tournament_id=token)
        # logging.warning(t.to_dict())

    def test_from_dict(self):
        """convert dict to tournament"""

        token = "test_" + secrets.token_hex(2)

        # logging.warning(t)
        t_dict = {
            "name": token,
            "start_date": token,
            "end_date": token,
            "tournament_id": token,
        }

        t = Tournament.from_dict(t_dict)
        # logging.warning(t)

    def test_create(self):
        """convert dict to tournament"""

        token = "test_" + secrets.token_hex(2)
        t = Tournament(token, token, token, tournament_id=token)

        # logging.warning(t.to_dict())
        t.create()
        # logging.warning(t)

    def test_search_by_tournament(self):
        """search method for tournaments by key and value"""

        token = "test_" + secrets.token_hex(2)
        t = Tournament(token, token, token, tournament_id=token)

        # logging.warning(t.to_dict())
        t.create()
        # logging.warning(t)

        del t

        result = Tournament.search_by("tournament_id", token)
        # logging.info(result)
        assert len(result) == 1

    def test_update(self):
        """update tournament"""

        token = "test_" + secrets.token_hex(2)
        t = Tournament(token, token, token, tournament_id=token)
        t.create()
        del t

        t_list = Tournament.search_by("tournament_id", token)
        t = t_list[0]
        t.name = "ON A CHANGé"
        t.update()
        del t

        t_list = Tournament.search_by("tournament_id", token)
        t = t_list[0]
        assert t.name == "ON A CHANGé"

    def test_get_score(self, last_four_players, last_tournament):
        """Test the get_score method"""

        # Iterate through each player
        for player in last_four_players:
            # Get the player's ID
            player_id = player.player_id

            # Call the get_score method for the current player
            player_score = last_tournament.get_score(player_id)

            # Log the player's ID and score
            logging.info(f"Player ID: {player_id}, Score: {player_score}")

            # Check if the actual score is an integer
            assert isinstance(player_score, int)
