from templates.player import PlayerTemplate

# from ..models.player import Player


class PlayerView:

    @classmethod
    def menu(self, data={}):

        choice = PlayerTemplate.menu()

        if choice == "1":
            return "PlayerView.create", data

        elif choice == "2":
            return "PlayerView.list_all", data

        elif choice == "42":

            return "exit", data
        else:

            return "MainView.menu", data

    @classmethod
    def create(self, data={}):

        player = PlayerTemplate.create()

        # player = Player(**output)
        # player.save()

        PlayerTemplate.ok_created(player)

        return "PlayerView.menu", {"player": player}

    @classmethod
    def list_all(self, data={}):

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
