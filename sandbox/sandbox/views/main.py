from templates.main import MainTemplate
from templates.player import PlayerTemplate

# from views.player import PlayerView


class MainView:

    @staticmethod
    def menu(data={}):
        """ """

        choice = MainTemplate.menu()

        if choice == "1":
            return "MainView.menu", data

        elif choice == "42":
            return "exit", data

        else:
            return "MainView.menu", data
