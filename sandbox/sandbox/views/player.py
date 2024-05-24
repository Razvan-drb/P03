from templates.player import PlayerTemplate

# from views.main import MainView

# from ..models.player import Player


class PlayerView:

    @staticmethod
    def menu(data={}):

        choice = PlayerTemplate.menu()

        if choice == "1":
            return "PlayerView.create", data

        elif choice == "2":
            return "PlayerView.list_all", data

        elif choice == "42":

            return "exit", data
        else:

            return "MainView.menu", data

    @staticmethod
    def create(data={}):

        player = PlayerTemplate.create()

        # player = Player(**output)
        # player.save()

        PlayerTemplate.ok_created(player)

        return "PlayerView.menu", {"player": player}

    @staticmethod
    def list_all(data={}):

        # players = Player.list_all()
        players = [  # MOCK UP :p
            {"name": "John"},
            {"name": "Doe"},
            {"name": "Jane"},
        ]

        choice = PlayerTemplate.list_all(players)

        if choice:
            data["selected_player"] = players[int(choice) - 1]

        return "PlayerView.menu", data
