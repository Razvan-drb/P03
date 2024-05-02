from ..templates.player import PlayerTemplate

# from ..models.player import Player


class PlayerView:

    @classmethod
    def menu(self, data={}):

        choice = PlayerTemplate.menu()

        if choice == "1":
            return "PlayerView_create", data

        elif choice == "2":
            return "PlayerView_list_all", data

        else:

            return "MainView_menu", data

    @classmethod
    def create(self, data={}):

        player = PlayerTemplate.create()

        # player = Player(**output)
        # player.save()

        PlayerTemplate.ok_created(player)

        return "PlayerView_menu", {"player": player}

    @classmethod
    def list_all(self, data={}):

        # players = Player.list_all()
        players = [
            {"name": "John"},
            {"name": "Doe"},
            {"name": "Jane"},
        ]

        choice = PlayerTemplate.list_all(players)

        if choice:
            data["selected_player"] = players[int(choice) - 1]

        return "PlayerView_menu", data
