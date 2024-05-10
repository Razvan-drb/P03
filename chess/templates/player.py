from typing import List


class PlayerTemplate:
    """Template for player management."""

    @classmethod
    def menu(cls) -> str:
        """Display menu options."""

        print("\nPlayer Menu")
        print("1. Create a player")
        print("2. List all players")
        print("3. Return to the main menu")
        return input("Enter the number you want: ")

    @classmethod
    def create(cls) -> dict:
        """Create a new player."""

        print("\nCreating a new player...")
        firstname = input("Enter the first name of the player: ")
        lastname = input("Enter the last name of the player: ")
        birthdate = input("Enter the birthdate of the player (optional): ")

        return {
            "firstname": firstname,
            "lastname": lastname,
            "birthdate": birthdate,
        }

    @classmethod
    def display_players(cls, players: List[dict]):
        """Display a list of players."""

        print("\nList of Players:")
        for i, player in enumerate(players, 1):
            print(f"{i}. {player['firstname']} {player['lastname']}")

    @classmethod
    def confirm_delete(cls, player: dict) -> bool:
        """Confirm player deletion."""

        print(f"\nSelected player: {player['firstname']} {player['lastname']}")
        ans = input("Are you sure you want to delete this player? (y/n): ")
        return ans.lower() == "y"

    @classmethod
    def deleted_successfully(cls, player: dict):
        """Confirmation message for successful delete."""

        print(f"Player {player['firstname']} {player['lastname']} deleted successfully.")

    @classmethod
    def update_player(cls, player: dict) -> dict:
        """Update player attributes."""

        print("\nUpdate Player")
        for key, value in player.items():
            new_value = input(f"Enter new value for {key} (or press Enter to keep): ")
            if new_value:
                player[key] = new_value
        return player
