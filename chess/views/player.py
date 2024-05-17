from typing import List
from chess.templates.player import PlayerTemplate
from chess.models.players import Player


class PlayerView:
    """View class for player management."""

    @classmethod
    def menu(cls, data={}):
        """Display the player menu and handle user input."""
        choice = PlayerTemplate.menu()

        if choice == "1":
            return cls.create_player, data
        elif choice == "2":
            return "exit", data
        else:
            return cls.menu, data

    @staticmethod
    def create_player() -> dict:
        """Create a new player."""

        return PlayerTemplate.create()

    @staticmethod
    def display_players(players: List[dict]):
        """Display a list of players."""

        PlayerTemplate.display_players(players)

    @staticmethod
    def confirm_delete(player: dict) -> bool:
        """Confirm player deletion."""

        return PlayerTemplate.confirm_delete(player)

    @staticmethod
    def deleted_successfully(player: dict):
        """Confirmation message for successful delete."""

        PlayerTemplate.deleted_successfully(player)

    @staticmethod
    def update_player(player: dict) -> dict:
        """Update player attributes."""

        return PlayerTemplate.update_player(player)


# class PlayerView:
#
#     @staticmethod
#     def create_player(tournament=None):
#         """Handles creating a new player and adding them to the tournament if specified."""
#
#         p_dict = PlayerTemplate.create()
#
#         firstname = p_dict["firstname"]
#         lastname = p_dict["lastname"]
#         birthdate = p_dict["birthdate"]
#
#         new_player = Player(
#             firstname=firstname,
#             lastname=lastname,
#             birthdate=birthdate,
#         )
#
#         new_player.create()
#         print("Player created successfully.")
#
#         if tournament:
#             try:
#                 tournament.add_player(new_player.player_id)
#                 # TODO : etre sur que ca save bien ;) update()
#                 print("Player added to the tournament.")
#             except ValueError as e:
#                 print(e)
