class PlayerTemplate:
    """Template for creating a player."""

    @classmethod
    def menu(self):
        """ """
        print("Player Menu")
        print("1. Create a player")
        print("2. List all players")
        print("3. Return to the main menu")

        return input("Enter the number of the action you want to take: ")

    @classmethod
    def create(self):
        """Creates a player with random attributes."""

        firstname = input("Enter the player's first name: ")
        lastname = input("Enter the player's last name: ")
        birthdate = input("Enter the player's birthdate (YYYY-MM-DD): ")

        return {
            "firstname": firstname,
            "lastname": lastname,
            "birthdate": birthdate,
        }

    @classmethod
    def ok_created(self, player: dict):
        """"""

        print(
            f"Player {player['firstname']} {player['lastname']} created successfully!"
        )

        return None

    @classmethod
    def list_all(self, pl_list: list[dict]) -> int:
        """List all players."""

        print("List of players:")

        for i, player in enumerate(pl_list):
            print(f"{i+1}. {player} ")

        return input(
            "Enter the number of the player you want to select or press Enter to cancel:"
        )
