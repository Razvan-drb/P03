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


@pytest.fixture
def new_four_players():
    """Generate 4 unique players"""

    players = []
    for _ in range(4):
        firstname = "Test" + secrets.token_hex(4)
        lastname = "TEST" + secrets.token_hex(4)
        player_id = "test" + secrets.token_hex(4)
        player = Player(firstname, lastname, player_id=player_id)
        player.create()
        logging.warning(f"Generated player: {player}")
        players.append(player)

    return players


@pytest.fixture
def last_four_players():
    """load 4 players"""

    p_list = Player.read_all()
    p_list = [i for i in p_list if i.firstname.startswith("Test")]
    p_list = p_list[-4:]

    assert len(p_list) >= 4
    assert isinstance(p_list[0], Player)
    return p_list


@pytest.fixture
def default_tournament():
    """create a tournament"""

    tournament_id = secrets.token_hex(4) + "_" + now()
    name = "TestTournament_" + tournament_id
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    t = Tournament(name, start_date, end_date, tournament_id=tournament_id)
    t.create()

    return t


@pytest.fixture
def last_tournament():
    """load a tournament"""

    tournament_list = Tournament.read_all()

    tournament_list = [
        i for i in tournament_list if i.name.startswith("TestTournament")
    ]
    tournament = tournament_list[-1]

    return tournament
