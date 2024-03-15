import logging
import secrets

import pytest

from chess.models.players import Player
from chess.models.rounds import Round
from chess.models.tournaments import Tournament


@pytest.fixture
def four_players():
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


class TestTournamentRun:
    """Test Tournament model"""

    def test_add_players(self, four_players, created_default_tournament):
        """test add 4 players"""

        # create 4 players
        logging.info(four_players)

        # create tournament
        logging.info(created_default_tournament)

        created_default_tournament.player_id_list = []

        # add players to tournament
        for player in four_players:
            created_default_tournament.add_player(player.player_id)

        assert created_default_tournament.n_players == 4

    def test_update_status(self, loaded_default_tournament):
        """update tournament status to "In Progress"""

        assert loaded_default_tournament.status == "Created"
        assert loaded_default_tournament.n_players == 4

        loaded_default_tournament.update_status("In Progress")

    def test_round_computed(self, loaded_default_tournament):
        """test if rounds had been computed"""

        logging.warning(f"id tournament: {loaded_default_tournament.tournament_id}")

        assert loaded_default_tournament.status == "In Progress"

        assert len(loaded_default_tournament.round_id_list) == 3

        # assert loaded_default_tournament.round == 0

    def test_get_results(self, four_players, loaded_default_tournament):
        """Test access to results"""

        # Get current round
        current_round = loaded_default_tournament.get_current_round()

        # Check if current_round is not None
        assert current_round is not None

        # Access match_list directly on the current_round instance
        assert isinstance(current_round.matches, list)

        # Get 1st match of the round
        first_match_of_the_list = current_round.matches[0]
        assert isinstance(first_match_of_the_list, list)

        # Get 1st player of the 1st match
        first_player_of_first_match = first_match_of_the_list[0]
        assert isinstance(first_player_of_first_match, list)

        # Extract id and score for this player
        first_player_of_first_match_id = first_player_of_first_match[0]
        first_player_of_first_match_score = first_player_of_first_match[1]

        # Check values
        assert first_player_of_first_match_id == four_players[0].player_id
        assert first_player_of_first_match_score == -1

    def test_add_1st_results(self, four_players, loaded_default_tournament):
        """add results for round 1"""

        # store current_round_number
        current_round_number = loaded_default_tournament.current_round_number

        # use random results for the first round
        new_res = [
            # 1st match
            (
                # player 1 of 1st match
                (four_players[0].player_id, 1),  # id, score
                # player 2 of 1st match
                (four_players[1].player_id, 0),  # id, score
            ),
            # 2nd match
            (
                # 1st player of 2nd match
                (four_players[2].player_id, 1),  # id, score
                # 2nd player of the 2nd match
                (four_players[3].player_id, 0),  # id, score
            ),
        ]

        # do update
        loaded_default_tournament.update_current_round(new_res)

        # next round
        loaded_default_tournament._next_round()

        # reload from the database the correct tournament
        tournament_id = loaded_default_tournament.tournament_id
        tournament = Tournament.search(tournament_id)

        # check current_round_number is OK
        if tournament is not None:
            assert (current_round_number + 1) == tournament.current_round_number
        else:
            logging.warning("Tournament is None")

    def test_add_3rd_results(self, four_players, loaded_default_tournament):
        """add results for round 1"""

        abcd_list = [(0, 2, 1, 3), (0, 3, 1, 2)]
        for a, b, c, d in abcd_list:

            # store current_round_number
            current_round_number = loaded_default_tournament.current_round_number

            # use random results for the first round
            new_res = [
                # 1st match
                (
                    # player 1 of 1st match
                    (four_players[a].player_id, 1),  # id, score
                    # player 2 of 1st match
                    (four_players[b].player_id, 0),  # id, score
                ),
                # 2nd match
                (
                    # 1st player of 2nd match
                    (four_players[c].player_id, 1),  # id, score
                    # 2nd player of the 2nd match
                    (four_players[d].player_id, 0),  # id, score
                ),
            ]

            # do update
            loaded_default_tournament.update_current_round(new_res)

            # next round
            loaded_default_tournament._next_round()

            #
            logging.critical(
                f"loaded_default_tournament.tournament_id: {loaded_default_tournament.tournament_id}"
            )
