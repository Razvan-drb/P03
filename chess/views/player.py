from typing import List
from chess.templates.player import PlayerTemplate
from chess.models.players import Player
from chess.templates.error import ErrorTemplate


class PlayerView:
    """View class for player management."""

    @staticmethod
    def menu(data={}):
        """Display the player menu and handle user input."""

        choice = PlayerTemplate.menu()

        if choice == "1":
            return "PlayerView.create_player", data
        elif choice == "2":
            return "PlayerView.read_all_players", data
        elif choice == "3":
            return "exit", data
        else:
            # is the possibility to go to main menu anticpicated ?
            return "PlayerView.menu", data

    @staticmethod
    def create_player(data={}):
        """Create a new player."""

        player_data = PlayerTemplate.create()

        new_player = Player(
            firstname=player_data["firstname"],
            lastname=player_data["lastname"],
            birthdate=player_data["birthdate"],
        )
        new_player.create()

        # print("Player created successfully.")

        return "PlayerView.menu", data

    @staticmethod
    def read_all_players(data={}):  # Update method name
        """List all players."""

        players = Player.read_all()

        players_dict = [
            player.to_dict() for player in players if isinstance(player, Player)
        ]

        PlayerTemplate.read_all(players_dict)

        return "PlayerView.menu", data

    @staticmethod
    def select_a_player(data={}):
        """Display a list of players."""

        # GOOD IDEA BUT => SELECT DIRECTLY IN APPORIORATE VIES
        # PlayerTemplate.read_all(players)

        ErrorTemplate.not_implemented("Not implemented yet")

        return "PlayerView.menu", data

    @staticmethod
    def update_player(data={}) -> dict:
        """Update player attributes."""

        # SELECT PLAYER
        #   => selection ici ??? => crée  un tempalte ?? =>  ALLEZ GO
        #   OU view à part ???  ==> NON PAS BONNE OPTION

        # ID DU PLAYER
        # LOAD DU PLAYER EN BASE read by id => Player.read_one(id)
        # TRASNFORM TO DICT
        # tEMPLATE update player CHNAGE ATTRIBUTES
        # UPDATE PLAYER IN DB
        # save ... => p.update()

        return "PlayerView.menu", data

    # @staticmethod
    # def confirm_delete(data={}) -> bool:
    #     """Confirm player deletion."""

    #     return PlayerTemplate.confirm_delete(player)

    # @staticmethod
    # def deleted_successfully(data={}):
    #     """Confirmation message for successful delete."""

    #     PlayerTemplate.deleted_successfully(player)
