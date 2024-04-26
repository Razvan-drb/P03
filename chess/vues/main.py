"""
Vues module for the chess application
"""
import logging
import sys

from chess.models.tournaments import Tournament
from chess.vues.player import TournamentManagementSystem
from chess.vues.tournament import display_available_tournaments


# add route to access this function


# def main():
#     show_all = Tournament.read_all()
#     chosen_tournament_id = display_available_tournaments(show_all)
#
#     if chosen_tournament_id:
#         selected_tournament = Tournament.read_one(chosen_tournament_id)
#         if selected_tournament:
#             print("You have selected the tournament:")
#             print(selected_tournament)
#         else:
#             logging.warning("Tournament not found.")
#
# if __name__ == "__main__":
#     main()

# def main():
#
#     show_all = Tournament.read_all()
#     display_available_tournaments(show_all)


# def DummyView():
#
#     # READ
#     # li = Model.get_all()
#     # out = Template.my_template(li)
#
#     # CREATE
#     # plyaer = Player(out)
#     # player.save()
#     # None = Template.ok_created(dict(player)
#     # go to menu player
#
#     # return ??????  ===> POINT HYPER SENSIBE A DISCUTER
#
#     pass
#
#
# if __name__ == "__main__":
#     main()


def main():
    tms = TournamentManagementSystem()

    while True:
        print("\n===== Tournament Management System =====")
        print("1. Create Tournament")
        print("2. Create Player")
        print("3. Launch Tournament")
        print("4. Play Round")
        print("5. View Player Scores")
        print("6. Exit")
        print("7. Display Available Tournaments")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            tms.create_tournament()
        elif choice == "2":
            tms.create_player()
        elif choice == "3":
            show_all = Tournament.read_all()
            chosen_tournament_id = display_available_tournaments(show_all)
            if chosen_tournament_id:
                selected_tournament = Tournament.read_one(chosen_tournament_id)
                if selected_tournament:
                    tms.launch_tournament(selected_tournament)
                else:
                    logging.warning("Tournament not found.")
        elif choice == "4":
            show_all = Tournament.read_all()
            chosen_tournament_id = display_available_tournaments(show_all)
            if chosen_tournament_id:
                selected_tournament = Tournament.read_one(chosen_tournament_id)
                if selected_tournament:
                    tms.play_rounds_auto(selected_tournament)
                else:
                    logging.warning("Tournament not found.")
        elif choice == "5":
            tms.display_player_scores()
        elif choice == "6":
            print("Exiting the program...")
            sys.exit()
        elif choice == "7":
            # Display available tournaments and select one
            show_all = Tournament.read_all()
            chosen_tournament_id = display_available_tournaments(show_all)
            if chosen_tournament_id:
                selected_tournament = Tournament.read_one(chosen_tournament_id)
                if selected_tournament:
                    # Display selected tournament details
                    print("You have selected the tournament:")
                    print(selected_tournament)
                else:
                    logging.warning("Tournament not found.")
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()


# TODO choose tournament from available list of tournaments available