"""
Main View module : Contains the MainView class and the main function.
"""

from chess.templates.main import MainTemplate
from chess.templates.player import PlayerTemplate
from chess.views.player import PlayerView
from chess.views.tournament import TournamentView
from chess.templates.tournament import TournamentTemplate
from chess.models.tournaments import Tournament


class MainView:
    @staticmethod
    def menu(data={}):
        """Display the main menu and handle user input."""
        choice = MainTemplate.menu()

        if choice == "1":
            return "PlayerView.menu", data
        elif choice == "2":
            return "TournamentView.menu", data
        elif choice == "3":
            return "exit", data
        else:
            # ErrorTemplate.invalid_choice()
            return "MainView.menu", data


def main():
    while True:
        action, data = MainView.menu()
        if action == "exit":
            print("Exiting the program...")
            break
        elif action == "PlayerView.menu":
            player_choice = PlayerTemplate.menu()
            if player_choice == "1":
                PlayerTemplate.create()
            elif player_choice == "2":
                PlayerView.read_all_players()
            elif player_choice == "3":
                pass
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        elif action == "TournamentView.menu":
            while True:
                print("\n===== Tournament Menu =====")
                choice = TournamentView.menu()

                if choice == "1":
                    tournament_data = TournamentTemplate.create()
                    Tournament.create(tournament_data)
                elif choice == "2":
                    show_all = Tournament.read_all()
                    chosen_tournament_id = TournamentTemplate.display_available_tournaments(show_all)
                    if chosen_tournament_id:
                        selected_tournament = Tournament.read_one(chosen_tournament_id)
                        if selected_tournament:
                            TournamentView.launch_tournament({"tournament_id": chosen_tournament_id})
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

# # TODO list all tournaments !!!!!!!!!!!!!!


# # add route to access this function


# # def main():
# #     show_all = Tournament.read_all()
# #     chosen_tournament_id = display_available_tournaments(show_all)
# #
# #     if chosen_tournament_id:
# #         selected_tournament = Tournament.read_one(chosen_tournament_id)
# #         if selected_tournament:
# #             print("You have selected the tournament:")
# #             print(selected_tournament)
# #         else:
# #             logging.warning("Tournament not found.")
# #
# # if __name__ == "__main__":
# #     main()

# # def main():
# #
# #     show_all = Tournament.read_all()
# #     display_available_tournaments(show_all)


# # def DummyView():
# #
# #     # READ
# #     # li = Model.get_all()
# #     # out = Template.my_template(li)
# #
# #     # CREATE
# #     # plyaer = Player(out)
# #     # player.save()
# #     # None = Template.ok_created(dict(player)
# #     # go to menu player
# #
# #     # return ??????  ===> POINT HYPER SENSIBE A DISCUTER
# #
# #     pass
# #
# #
# # if __name__ == "__main__":
# #     main()


# # TODO choose tournament from available list of tournaments available
