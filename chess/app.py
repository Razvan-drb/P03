from chess.views.main import MainView
from chess.views.player import PlayerView
from chess.views.tournament import TournamentView


class App:

    routes = {
        "MainView.menu": MainView.menu,
        "PlayerView.menu": PlayerView.menu,
        "PlayerView.create_player": PlayerView.create_player,
        "PlayerView.read_all_players": PlayerView.read_all_players,
        "TournamentView.menu": TournamentView().menu,
        "TournamentView.create_tournament": lambda data: TournamentView().create_tournament(
            **data
        ),
        "TournamentView.add_player_to_tournament": TournamentView().add_player_to_tournament,
        "TournamentView.launch_tournament_menu": TournamentView().launch_tournament_menu,
        "TournamentView.create_new_round": TournamentView().create_new_round,
        "TournamentView.display_rankings": TournamentView().display_rankings,
        "TournamentView.list_all_tournaments": lambda data: TournamentView().list_all_tournaments(),
        "TournamentView.view_rounds_and_input_scores": TournamentView().view_rounds_and_input_scores,
        "exit": "exit",
    }

    def __init__(self):
        pass

    def run(self):
        view_str = "MainView.menu"
        data = {}

        while True:
            if view_str == "exit":
                print("Exiting the program...")
                break

            view_function = self.routes.get(view_str)
            if view_function is None:
                print(f"Error: No route found for {view_str}")
                break

            if callable(view_function):
                if view_str in [
                    "TournamentView.create_tournament",
                    "TournamentView.list_all_tournaments",
                ]:
                    view_str = view_function(data)
                else:
                    view_str, data = view_function()
            else:
                view_str = view_function
