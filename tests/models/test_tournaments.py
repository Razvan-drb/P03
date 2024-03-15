import logging
import secrets

import pytest

from chess.models.players import Player
from chess.models.rounds import Round
from chess.models.tournaments import Tournament


@pytest.fixture
def load_4_players():
    """load 4 players"""

    p_list = Player.read_all()
    p_list = [i for i in p_list if i.firstname.startswith("Test")]
    p_list = p_list[:4]

    assert len(p_list) >= 4
    assert isinstance(p_list[0], Player)
    return p_list


@pytest.fixture
def created_default_tournament():
    """create a tournament"""

    name = "TestTournament" + secrets.token_hex(4)
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    t = Tournament(name, start_date, end_date)
    t.create()

    return t


@pytest.fixture
def loaded_default_tournament():
    """load a tournament"""

    tournament_list = Tournament.read_all()

    tournament_list = [
        i for i in tournament_list if i.name.startswith("TestTournament")
    ]
    tournament = tournament_list[-1]

    return tournament


class TestTournamentBase:
    """Test Tournament model"""

    def test_init(self):
        """create a tournament"""

        name = "Tournament" + secrets.token_hex(4)
        start_date = "2023-01-01"
        end_date = "2023-12-31"

        t = Tournament(name, start_date, end_date)
        logging.warning(t)

    def test_to_dict(self):
        """convert tournament to dict"""

        name = "Tournament" + secrets.token_hex(4)
        start_date = "2023-01-01"
        end_date = "2023-12-31"

        t = Tournament(name, start_date, end_date)
        logging.warning(t.to_dict())

    def test_from_dict(self):
        """convert dict to tournament"""

        name = "Tournament" + secrets.token_hex(4)
        start_date = "2023-01-01"
        end_date = "2023-12-31"
        t_dict = {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
        }

        t = Tournament.from_dict(t_dict)
        logging.warning(t)

    def test_create(self):
        """convert dict to tournament"""

        name = "Tournament" + secrets.token_hex(4)
        start_date = "2023-01-01"
        end_date = "2023-12-31"

        t = Tournament(name, start_date, end_date)
        t.create()
        logging.warning(t)

    def test_search_by_tournament(self):
        """search method for tournaments by key and value"""

        name = "Tournament" + "search"
        start_date = "2023-01-01"
        end_date = "2023-12-31"
        t_dict = {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
        }
        Tournament.reboot(3)

        t = Tournament(**t_dict)
        t.create()
        result = Tournament.search_by("name", name)
        logging.info(result)
        assert len(result) == 1

    def test_update(self, created_default_tournament):
        """update tournament"""

        # load mon default tournament
        created_default_tournament

        # recup valeur à la con location
        # store cette  valeur
        old_location = created_default_tournament.location

        # # changer à la main
        new_location = "Fake_Loc_" + str(secrets.token_hex(4))
        created_default_tournament.location = new_location

        # updante
        created_default_tournament.update()

        # store id tournois
        id_tournament = created_default_tournament.tournament_id

        # reoard à la main le tournois sur base id
        same_tournament = Tournament.read_one(id_tournament)

        # assert
        assert same_tournament.location != old_location
        assert same_tournament.location == new_location
