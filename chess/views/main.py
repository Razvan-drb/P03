from chess.models.players import Player
from chess.templates.main import MainTemplate
from chess.templates.player import PlayerTemplate
from chess.views.player import PlayerView
from chess.views.tournament import TournamentManagementSystem, display_available_tournaments
from chess.models.tournaments import Tournament


class MainView:

    @classmethod
    def menu(cls, data={}):
        """Display the main menu and handle user input."""

        choice = MainTemplate.menu()

        if choice == "1":
            return PlayerView.menu, data

        elif choice == "2":
            return TournamentManagementSystem.menu, data

        elif choice == "3":
            return "exit", data

        else:
            return cls.menu, data


def main():
    while True:
        action, data = MainView.menu()
        if action == "exit":
            print("Exiting the program...")
            break
        elif action == PlayerView.menu:
            player_choice = PlayerTemplate.menu()
            if player_choice == "1":
                PlayerTemplate.create()
            elif player_choice == "2":
                PlayerView.read_all_players()
            elif player_choice == "3":
                pass
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        elif action == TournamentManagementSystem.menu:
            tms = TournamentManagementSystem()
            while True:
                print("\n===== Tournament Management System =====")
                print("1. Create Tournament")
                print("2. Launch Tournament")
                print("3. Exit")

                choice = input("Enter your choice (1-3): ")

                if choice == "1":
                    tms.create_tournament(
                        input("Enter the name of the tournament: "),
                        input("Enter the start date of the tournament (YYYY-MM-DD): "),
                        input("Enter the end date of the tournament (YYYY-MM-DD): "),
                        input("Enter the description of the tournament: "),
                        input("Enter the location of the tournament: "),
                    )
                elif choice == "2":
                    show_all = Tournament.read_all()
                    chosen_tournament_id = display_available_tournaments(show_all)
                    if chosen_tournament_id:
                        selected_tournament = Tournament.read_one(chosen_tournament_id)
                        if selected_tournament:
                            tms.tournament = selected_tournament
                            tms.launch_tournament()
                        else:
                            print("Tournament not found.")
                elif choice == "3":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
        else:
            action(data)


if __name__ == "__main__":
    main()

# TODO list all tournaments !!!!!!!!!!!!!!


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


# TODO choose tournament from available list of tournaments available
