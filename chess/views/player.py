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
            return cls.read_all_players, data
        elif choice == "3":
            return "exit", data
        else:
            return cls.menu, data

    @staticmethod
    def create_player():
        """Create a new player."""

        player_data = PlayerTemplate.create()
        new_player = Player(
            firstname=player_data["firstname"],
            lastname=player_data["lastname"],
            birthdate=player_data["birthdate"]
        )
        new_player.create()
        print("Player created successfully.")
        return PlayerView.menu

    @staticmethod
    def read_all_players():  # Update method name
        """List all players."""

        players = Player.read_all()
        players_dict = [player.to_dict() for player in players if isinstance(player, Player)]
        PlayerTemplate.read_all(players_dict)
        return PlayerView.menu

    @staticmethod
    def display_players(players: List[dict]):
        """Display a list of players."""

        PlayerTemplate.read_all(players)

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

        updated_data = PlayerTemplate.update_player(player)
        player_instance = Player.from_dict(updated_data)
        player_instance.update()
        return player_instance
