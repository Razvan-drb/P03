from templates.main import MainTemplate
from templates.player import PlayerTemplate


class MainView:

    @classmethod
    def menu(self, data={}):
        """ """

        choice = MainTemplate.menu()

        if choice == "1":
            return "PlayerView_menu", data

        else:
            return "MainView_menu", data
