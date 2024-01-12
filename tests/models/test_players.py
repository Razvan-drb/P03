import pytest
import logging
import secrets

from chess.models.players import Player


def test_init_player():
    """create a player"""

    firstname = "test" + secrets.token_hex(4)
    lastname = "test" + secrets.token_hex(4)

    p = Player(lastname, firstname)
    logging.warning(p)

    assert isinstance(p, Player)


def test_to_dict():
    """convert player to dict"""

    firstname = "test" + secrets.token_hex(4)
    lastname = "test" + secrets.token_hex(4)

    p = Player(lastname, firstname)
    logging.warning(p.to_dict())

    assert isinstance(p.to_dict(), dict)


def test_from_dict():
    """convert dict to player"""

    firstname = "test" + secrets.token_hex(4)
    lastname = "test" + secrets.token_hex(4)
    p_dict = {
        "firstname": firstname.capitalize(),
        "lastname": lastname.upper(),
    }

    p = Player.from_dict(p_dict)
    logging.warning(p)

    assert isinstance(p, Player)


def test_create():
    """convert dict to player"""

    firstname = "test" + secrets.token_hex(4)
    lastname = "test" + secrets.token_hex(4)

    # nb of players before creation
    list_player = Player.read_all()
    n0 = len(list_player)

    # create a player
    p = Player(firstname, lastname)
    p.create()
    logging.warning(p)

    # nb of players after creation
    list_player = Player.read_all()
    n1 = len(list_player)

    assert n1 == n0 + 1


def test_search_by():
    """search method for players by key and value"""
    firstname = "test" + "search"
    lastname = "test" + secrets.token_hex(4)

    p_dict = {
        "firstname": firstname.capitalize(),
        "lastname": lastname.upper(),
    }

    # reboot db
    Player.reboot(3)

    # create a player
    p = Player(**p_dict)
    p.create()

    # find one
    result = Player.search_by("firstname", firstname.capitalize())
    logging.info(result)

    # check result
    assert len(result) == 1