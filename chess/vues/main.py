"""
Vues module for the chess application
"""

from chess.templates.main_menu import display_available_tournaments
from chess.models.tournaments import Tournament

# add route to access this function


def main():

    show_all = Tournament.read_all()
    display_available_tournaments(show_all)


def DummyView():

    # READ
    # li = Model.get_all()
    # out = Template.my_template(li)

    # CREATE
    # plyaer = Player(out)
    # player.save()
    # None = Template.ok_created(dict(player)
    # go to menu player

    # return ??????  ===> POINT HYPER SENSIBE A DISCUTER

    pass


if __name__ == "__main__":
    main()
