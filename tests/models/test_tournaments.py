import pytest
import logging
import secrets

from chess.models.tournaments import Tournament
from chess.models.players import Player


@pytest.fixture
def load_4_players():
    """load 4 players"""

    p_list = Player.read_all()
    p_list = [i for i in p_list if i.firstname.startswith("Test")]
    p_list = p_list[:4]
    assert len(p_list) == 4

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

    assert tournament.n_players == 4

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


class TestTournamentRun:
    """Test Tournament model"""

    def test_add_players(self, load_4_players, created_default_tournament):
        # create 4 players
        logging.info(load_4_players)

        # create tournament
        logging.info(created_default_tournament)

        # add players to tournament
        for player in load_4_players:
            created_default_tournament.add_player(player.player_id)

    def test_update_status(self, loaded_default_tournament):
        """update tournament status to "In Progress"""

        loaded_default_tournament.update_status("In Progress")

    # def test_add_results(self):
    #     # create 4 players

    #     # create tournament

    #     # add players to tournament

    #     # check players in tournament

    #     # update status to "running"

    #     # record scores for 1st round

    #     1 / 0

    # def test_run_complete_tournament(self):
    #     # create 4 players

    #     # create tournament

    #     # add players to tournament

    #     # check players in tournament

    #     # update status to "running"

    #     # record scores for 1st round

    #     # record all rounds

    #     # update status to "complete"

    #     # return  tournament results

    #     1 / 0
