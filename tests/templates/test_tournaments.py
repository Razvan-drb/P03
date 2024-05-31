"""
This module contains the template for the Tournaments class.
"""

import logging
import pytest

from chess.templates.tournament import TournamentTemplate


class TestTournamentTemplate:

    def test_update_current_round(self):
        """Template for updating the current round."""

        match_list = [
            [["player1", -1], ["player2", -1]],
            [["player3", -1], ["player4", -1]],
        ]

        TournamentTemplate.update_current_round(match_list)

        logging.warning(match_list)
