from chess.views.main import MainView
from chess.views.player import PlayerView
from chess.views.tournament import TournamentView

MV = "MainView.menu"


class App:
    routes = {
        MV: MainView.menu,
        "PlayerView.menu": PlayerView.menu,
        "PlayerView.create_player": PlayerView.create_player,
        "PlayerView.read_all_players": PlayerView.read_all_players,
        "TournamentView.menu": TournamentView().menu,
        "TournamentView.create_tournament":
            lambda data: TournamentView().create_tournament(**data),
        "TournamentView.add_player_to_tournament":
            TournamentView().add_player_to_tournament,
        "TournamentView.launch_tournament_menu":
            TournamentView().launch_tournament_menu,
        "TournamentView.create_new_round": TournamentView().create_new_round,
        "TournamentView.display_rankings": TournamentView.display_rankings,
        "TournamentView.list_all_tournaments":
            lambda data: TournamentView().list_all_tournaments(),
        "TournamentView.view_rounds_and_input_scores":
            TournamentView().view_rounds_and_input_scores,
        "exit": "exit",
    }

    def __init__(self):
        #  constructor for a class, responsible
        #  for initializing the object's state.
        #  the initialization logic is not required for the specific class.
        pass

    def run(self):
        view_str = MV
        data = {}

        while view_str != "exit":
            view_function = self.routes.get(view_str)
            if not view_function:
                print(f"Error: No route found for {view_str}")
                break

            view_str, data = self.handle_view(view_str, view_function, data)

            if view_str == MV:
                print("Returning to the main menu...\n")

        print("Exiting the program...")

    @staticmethod
    def handle_view(view_str, view_function, data):
        if callable(view_function):
            try:
                if view_str in ["TournamentView.create_tournament",
                                "TournamentView.list_all_tournaments"]:
                    return view_function(data), data
                else:
                    result = view_function()
                    if isinstance(result, tuple) and len(result) == 2:
                        return result
                    else:
                        return result, {}
            except ValueError:
                return view_function(), data
        else:
            return view_function, data
