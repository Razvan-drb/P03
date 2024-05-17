from views.main import MainView
from views.player import PlayerView

routes = {
    # MainView
    "MainView.menu": MainView.menu,
    # PlayerView
    "PlayerView.menu": PlayerView.menu,
    "PlayerView.create": PlayerView.create,
    "PlayerView.list_all": PlayerView.list_all,
    "exit": "exit",
}


def main():

    view_str = "MainView.menu"
    data = {}

    while True:

        if view_str == "exit":
            raise ArithmeticError("Fin du programme")

        view_func = routes[view_str]
        view_str, data = view_func(data)


if __name__ == "__main__":
    main()
