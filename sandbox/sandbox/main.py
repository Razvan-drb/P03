from views.main import MainView
from views.player import PlayerView


routes = {
    # MainView
    "MainView_menu": MainView.menu,
    # PlayerView
    "PlayerView_menu": PlayerView.menu,
    "PlayerView_create": PlayerView.create,
    "PlayerView_list_all": PlayerView.list_all,
}


def main():

    view_str = "MainView_menu"
    data = {}

    while True:

        view_func = routes[view_str]
        view_str, data = view_func(data)
