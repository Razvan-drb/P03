import logging
import secrets

# import pytest
# from ...chess.models.players import Player
# from ...chess.models.rounds import Round
# from ...chess.models.tournaments import Tournament

from chess.models.players import Player
from chess.models.rounds import Round
from chess.models.tournaments import Tournament

# from ..conftest import new_four_players


class TestTournamentRun:
    """Test Tournament model"""

    def test_create_player(self, new_four_players):

        for p in new_four_players:
            assert isinstance(p, Player)

    def test_add_players(self, new_four_players, default_tournament):
        """test add 4 players"""

        assert default_tournament.n_players == 0

        # # create 4 players
        # logging.info(new_four_players)

        # # create tournament
        # logging.info(default_tournament)

        assert default_tournament.player_id_list == []

        # add players to tournament
        for player in new_four_players:
            default_tournament.add_player(player.player_id)

        assert default_tournament.n_players == 4
        default_tournament.update()

        # just reload the tournament from db to check update OK in db
        id_tournament = default_tournament.tournament_id
        tournament = Tournament.search(id_tournament)
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

        round_objects = [
            Round(round_number=1, matches=[], round_id=i)
            for i in last_tournament.round_id_list
        ]

        id_tournament = last_tournament.tournament_id

        for round_ in round_objects:
            assert id_tournament in round_.round_id

    def test_get_results(self, new_four_players, last_tournament):
        """Test access to results"""

        # Get current round
        current_round = last_tournament.get_current_round()

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
        # player_ids = [player.player_id for player in new_four_players]
        # assert first_player_of_first_match_id in player_ids
        # assert first_player_of_first_match_score in [0, 1]

    def test_add_1st_results(self, new_four_players, last_tournament):
        """add results for round 1"""

        # store current_round_number
        current_round_number = last_tournament.current_round_number

        # use random results for the first round
        new_res = [
            # 1st match
            (
                # player 1 of 1st match
                (new_four_players[0].player_id, 1),  # id, score
                # player 2 of 1st match
                (new_four_players[1].player_id, 0),  # id, score
            ),
            # 2nd match
            (
                # 1st player of 2nd match
                (new_four_players[2].player_id, 1),  # id, score
                # 2nd player of the 2nd match
                (new_four_players[3].player_id, 0),  # id, score
            ),
        ]

        # do update
        last_tournament.update_current_round(new_res)

        # next round
        last_tournament._next_round()

        # reload from the database the correct tournament
        tournament_id = last_tournament.tournament_id
        tournament = Tournament.search(tournament_id)

        # check current_round_number is OK
        if tournament is not None:
            assert (current_round_number + 1) == tournament.current_round_number
        else:
            logging.warning("Tournament is None")

    def test_add_3rd_results(self, new_four_players, last_tournament):
        """add results for round 1"""

        abcd_list = [(0, 2, 1, 3), (0, 3, 1, 2)]
        for a, b, c, d in abcd_list:

            # store current_round_number
            current_round_number = last_tournament.current_round_number

            # use random results for the first round
            new_res = [
                # 1st match
                (
                    # player 1 of 1st match
                    (new_four_players[a].player_id, 1),  # id, score
                    # player 2 of 1st match
                    (new_four_players[b].player_id, 0),  # id, score
                ),
                # 2nd match
                (
                    # 1st player of 2nd match
                    (new_four_players[c].player_id, 1),  # id, score
                    # 2nd player of the 2nd match
                    (new_four_players[d].player_id, 0),  # id, score
                ),
            ]

            # do update
            last_tournament.update_current_round(new_res)

            # next round
            last_tournament._next_round()

            #
            logging.critical(
                f"last_tournament.tournament_id: {last_tournament.tournament_id}"
            )

    def test_get_score(self, new_four_players, last_tournament):
        """Test the get_score method"""

        # Iterate through each player
        for player in new_four_players:
            # Get the player's ID
            player_id = player.player_id

            # Call the get_score method for the current player
            player_score = last_tournament.get_score(player_id)

            # Log the player's ID and score
            logging.info(f"Player ID: {player_id}, Score: {player_score}")

            # Check if the actual score is an integer
            assert isinstance(player_score, int)
