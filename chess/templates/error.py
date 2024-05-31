class GenericErrorTemplate:
    """Template for the error."""

    @staticmethod
    def not_implemented(*args, **kwargs) -> None:

        print("This feature is not implemented yet ! .")

        return None

    @staticmethod
    def generic_error(message, *args, **kwargs) -> None:

        print("An error occured.")
        print(message)

        return None


class TournamentErrorTemplate:
    """Template for tournament errors."""

    @classmethod
    def nb_player(cls) -> None:
        """not enough /too many players"""

        print("\nError: The number of players must be 4.")

    @classmethod
    def tournament_live(cls) -> None:
        """no add players / no change status / no change players"""

        print("\nError: This tournament is already live / No possible to add players.")

    @classmethod
    def player_already_added(cls) -> None:
        """no 2 same players in the tournement"""

        print("\nError: This player is already added to the tournament.")

    @classmethod
    def player_not_found(cls) -> None:
        """not player found in the db"""

        print("\nError: This player is not found in the database.")

    @classmethod
    def tournament_closed(cls) -> None:
        """no add palyer, no updtae round no change status no change players"""

        print("\nError: This tournament is closed.")


class PlayerErrorTemplate:
    pass
