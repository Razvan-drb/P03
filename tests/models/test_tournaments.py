import pytest
import logging
import secrets

from chess.models.tournaments import Tournament


def test_init_tournament():
    """create a tournament"""
    name = "Tournament" + secrets.token_hex(4)
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    t = Tournament(name, start_date, end_date)
    logging.warning(t)


def test_to_dict_tournament():
    """convert tournament to dict"""
    name = "Tournament" + secrets.token_hex(4)
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    t = Tournament(name, start_date, end_date)
    logging.warning(t.to_dict())


def test_from_dict_tournament():
    """convert dict to tournament"""
    name = "Tournament" + secrets.token_hex(4)
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    t_dict = {
        'name': name,
        'start_date': start_date,
        'end_date': end_date,
    }

    t = Tournament.from_dict(t_dict)
    logging.warning(t)


def test_create_tournament():
    """convert dict to tournament"""
    name = "Tournament" + secrets.token_hex(4)
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    t = Tournament(name, start_date, end_date)
    t.create()
    logging.warning(t)


def test_search_by_tournament():
    """search method for tournaments by key and value"""
    name = "Tournament" + "search"
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    t_dict = {
        'name': name,
        'start_date': start_date,
        'end_date': end_date,
    }
    Tournament.reboot(3)

    t = Tournament(**t_dict)
    t.create()
    result = Tournament.search_by('name', name)
    logging.info(result)
    assert len(result) == 1
