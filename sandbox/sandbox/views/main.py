from templates.main import MainTemplate
from templates.player import PlayerTemplate


class MainView:

    @classmethod
    def menu(self, data={}):
        """ """

        choice = MainTemplate.menu()

        if choice == "1":
            return "PlayerView.menu", data

        elif choice == "42":

            return "exit", data

        else:
            return "MainView.menu", data
