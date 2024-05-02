from chess.models.players import Player
from chess.templates.player import PlayerTemplate


class PlayerView:

    @staticmethod
    def create_player(tournament=None):
        """Handles creating a new player and adding them to the tournament if specified."""

        p_dict = PlayerTemplate.create()

        firstname = p_dict["firstname"]
        lastname = p_dict["lastname"]
        birthdate = p_dict["birthdate"]

        new_player = Player(
            firstname=firstname,
            lastname=lastname,
            birthdate=birthdate,
        )

        new_player.create()
        print("Player created successfully.")

        if tournament:
            try:
                tournament.add_player(new_player.player_id)
                # TODO : etre sur que ca save bien ;) update()
                print("Player added to the tournament.")
            except ValueError as e:
                print(e)
