from typing import List

from chess.models.players import Player
from chess.templates.player import PlayerTemplate


class PlayerView:
    """View class for player management."""

    @staticmethod
    def create_player() -> dict:
        """Create a new player."""

        # CODE LOGIQUE POUR CREER UN JOUEUR
        return PlayerTemplate.create()

    @staticmethod
    def display_players(players: List[dict]):
        """Display a list of players."""

        # TODO ajouter CODE logique pour faire la liste des joueurs
        PlayerTemplate.display_players(players)

    @staticmethod
    def confirm_delete(player: dict) -> bool:
        """Confirm player deletion."""

        # ajouter code logique pour trouver et supprimer un joueur
        PlayerTemplate.confirm_delete(player)

        PlayerTemplate.deleted_successfully(player)

        return None

    @staticmethod
    def update_player(player: dict) -> dict:
        """Update player attributes."""

        # ajouter CODE LOGIQUE pour mettre a jour un joueur
        return PlayerTemplate.update_player(player)
