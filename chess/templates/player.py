"""
un peu comme du html 
"""


class PlayerTemplate:

    @classmethod
    def create(cls) -> dict:

        print("Creating a new player...")
        firstname = input("Enter the first name of the player: ")
        lastname = input("Enter the last name of the player: ")
        birthdate = input("Enter the birthdate of the player (optional): ")

        return {
            "firstname": firstname,
            "lastname": lastname,
            "birthdate": birthdate,
        }

    @classmethod
    def update(cls, player_dict: dict) -> dict:

        for k, v in player_dict.items():
            print(f"Current value for {k} is  {v}")
            new_value = input(
                f"Enter the new NEW value for {k}  if needed else JUST PRESS ENTER"
            )

            if new_value:
                player_dict[k] = new_value

        return player_dict

    @classmethod
    def delete(cls, player_dict: dict) -> bool:
        """Delete a player."""

        print(f"selected player: {player_dict}")
        ans = input("Are you sure you want to delete this player? (y/n): ")

        if ans.lower() == "y":
            print("Deleting a player...")
            return True

        return False

    @classmethod
    def list_all(cls, players: list[dict]):
        """List all players."""

        print("Listing all players...")

        for player in players:
            print(player)

        return None
