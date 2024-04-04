"""
Find here all shared fixtures used by all tests
"""

import logging
import secrets

import pytest

from chess.models.players import Player
from chess.models.rounds import Round
from chess.models.tournaments import Tournament

from chess.helpers import now


# @pytest.fixture(autouse=False)
# def run_before_tests():
#     """Fixture to execute asserts before and after a test is run"""

#     logging.warning("Starting tests")

#     Player.reboot()
#     Tournament.reboot()


# @pytest.fixture
# def new_four_players():
#     """Generate 4 unique players"""

#     logging.warning("Generating 4 players")

#     players = []
#     for _ in range(4):
#         token = "test_" + secrets.token_hex(3)
#         player = Player(token, token, player_id=token)
#         player.create()
#         # logging.warning(f"Generated player: {player}")
#         players.append(player)

#     return players


@pytest.fixture
def last_four_players():
    """load 4 players"""

    logging.warning("Loading 4 players")

    p_list = Player.read_all()
    p_list = [i for i in p_list if i.player_id.startswith("test_")]
    p_list = p_list[-4:]

    assert len(p_list) == 4
    assert isinstance(p_list[0], Player)

    return p_list


# @pytest.fixture
# def default_tournament():
#     """create a tournament"""

#     logging.warning("Generating a tournament")

#     token = "test_" + secrets.token_hex(3) + "_" + now()
#     start_date = "2023-01-01"
#     end_date = "2023-12-31"

#     t = Tournament(token, start_date, end_date, tournament_id=token)
#     t.create()

#     return t


@pytest.fixture
def last_tournament():
    """load a tournament"""

    logging.warning("Loading last tournament")
    tournament_list = Tournament.read_all()

    tournament_list = [i for i in tournament_list if i.tournament_id.startswith("test")]
    tournament = tournament_list[-1]

    return tournament
