"""
Vues module for the chess application
"""

from chess.templates.main_menu import display_available_tournaments
from chess.models.tournaments import Tournament
# add route to access this function


def main():

    show_all = Tournament.read_all()
    display_available_tournaments(show_all)


if __name__ == "__main__":
    main()



