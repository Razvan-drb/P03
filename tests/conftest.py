"""
Find here all shared fixtures used by all tests
"""

import logging

import pytest

from chess.models.players import Player
from chess.models.tournaments import Tournament


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


@pytest.fixture
def last_tournament():
    """load a tournament"""

    logging.warning("Loading last tournament")
    tournament_list = Tournament.read_all()

    tournament_list = [i for i in tournament_list if i.tournament_id.startswith("test")]
    tournament = tournament_list[-1]

    return tournament
