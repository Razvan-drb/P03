import logging
import secrets

from chess.models.players import Player
from chess.models.rounds import Round
from chess.models.tournaments import Tournament

# import pytest
# from ...chess.models.players import Player
# from ...chess.models.rounds import Round
# from ...chess.models.tournaments import Tournament


# from ..conftest import new_four_players


class TestTournamentRun:
    """Test Tournament model"""

    def test_reboot(self):
        """Reboot all players and tournaments"""

        Player.reboot()
        Tournament.reboot()

    def test_create_player(self, last_four_players):

        for p in last_four_players:
            assert isinstance(p, Player)

    def test_add_players(self, last_four_players, last_tournament):
        """test add 4 players"""

        assert last_tournament.n_players == 0

        assert last_tournament.player_id_list == []

        # add players to tournament
        for player in last_four_players:
            last_tournament.add_player(player.player_id)

        assert last_tournament.n_players == 4
        last_tournament.update()

        # just reload the tournament from db to check update OK in db
        id_tournament = last_tournament.tournament_id
        tournament = Tournament.search(id_tournament)[0]
        assert tournament.n_players == 4

    def test_update_status(self, last_tournament):
        """update tournament status to "In Progress"""

        assert last_tournament.status == "Created"
        assert last_tournament.n_players == 4

        last_tournament.update_status("In Progress")

    def test_round_computed(self, last_tournament):
        """test if rounds had been computed"""

        logging.warning(f"id tournament: {last_tournament.tournament_id}")

        assert last_tournament.status == "In Progress"

        assert len(last_tournament.round_id_list) == 3

        assert last_tournament.current_round_number == 0

        logging.critical(
            f"last_tournament.round_id_list is {last_tournament.round_id_list}"
        )

    def test_add_1st_results(self, last_tournament):
        """add results for round 1"""

        # use random results for the first round
        new_res = [
            # 1st match
            (
                # player 1 of 1st match
                (last_tournament.player_id_list[0], 1),  # id, score
                # player 2 of 1st match
                (last_tournament.player_id_list[1], 0),  # id, score
            ),
            # 2nd match
            (
                # 1st player of 2nd match
                (last_tournament.player_id_list[2], 1),  # id, score
                # 2nd player of the 2nd match
                (last_tournament.player_id_list[3], 0),  # id, score
            ),
        ]

        # do update
        last_tournament.update_current_round(new_res)
        logging.critical(
            f"last_tournament.round_id_list is {last_tournament.round_id_list}"
        )
        logging.critical(
            f"last_tournament.current_round_number is {last_tournament.current_round_number}"
        )
        logging.critical(
            f"last_tournament.current_round is {last_tournament.current_round}"
        )

    def test_1st_round_updated_in_db(self, last_tournament):

        # reload from the database the correct tournament
        tournament_id = last_tournament.tournament_id
        tournaments = Tournament.search(tournament_id)
        tournament = tournaments[0]

        assert tournament.current_round_number == 1
        assert tournament.status == "In Progress"

        id_1st_round = tournament.round_id_list[0]
        round_1st = Round.search(id_1st_round)[0]
        match_0 = round_1st.matches[0]

        p0 = match_0[0]
        assert p0[1] != -1

    def test_add_3rd_results(self, last_tournament):
        """add results for round 1"""

        round_1 = [
            [
                (last_tournament.player_id_list[0], 1),  # P0 (id, score)
                (last_tournament.player_id_list[2], 0),  # P2 (id, score)
            ],  # 1er match
            [
                (last_tournament.player_id_list[1], 1),
                (last_tournament.player_id_list[3], 0),
            ],  # 2eme match
        ]

        round_2 = [
            [
                (last_tournament.player_id_list[0], 1),
                (last_tournament.player_id_list[3], 0),
            ],  # 1er match
            [
                (last_tournament.player_id_list[1], 0.5),
                (last_tournament.player_id_list[2], 0.5),
            ],  # 2eme match
        ]

        last_tournament.update_current_round(round_1)
        last_tournament.update_current_round(round_2)

        assert last_tournament.status == "Completed"

    # def test_get_score(self, last_four_players, last_tournament):
    #     """Test the get_score method"""
    #
    #     # Iterate through each player
    #     for player in last_four_players:
    #         # Get the player's ID
    #         player_id = player.player_id
    #
    #         # Call the get_score method for the current player
    #         player_score = last_tournament.get_score(player_id)
    #
    #         # Log the player's ID and score
    #         logging.info(f"Player ID: {player_id}, Score: {player_score}")
    #
    #         # Check if the actual score is an integer
    #         assert isinstance(player_score, int)

    # def test_get_results(self, new_four_players, last_tournament):
    #     """Test access to results"""

    #     # Get current round
    #     current_round = last_tournament.get_current_round()

    #     # Check if current_round is not None
    #     assert current_round is not None

    #     # Access match_list directly on the current_round instance
    #     assert isinstance(current_round.matches, list)

    #     # Get 1st match of the round
    #     first_match_of_the_list = current_round.matches[0]
    #     assert isinstance(first_match_of_the_list, list)

    #     # Get 1st player of the 1st match
    #     first_player_of_first_match = first_match_of_the_list[0]
    #     assert isinstance(first_player_of_first_match, list)

    #     # Extract id and score for this player
    #     first_player_of_first_match_id = first_player_of_first_match[0]
    #     first_player_of_first_match_score = first_player_of_first_match[1]

    #     # Check values
    #     # player_ids = [player.player_id for player in new_four_players]
    #     # assert first_player_of_first_match_id in player_ids
    #     # assert first_player_of_first_match_score in [0, 1]
