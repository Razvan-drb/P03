import secrets

from chess.models.players import Player
from chess.models.rounds import Round
from chess.models.tournaments import Tournament
from chess.templates.tournament import TournamentTemplate
from chess.views.player import PlayerView

# TODO display rankings and pass to completed once all rounds played !!!!!!!!!!!!!!!!!!!!!!!!!


class TournamentView:
    """Handles tournament management operations."""

    def __init__(self):
        self.tournament = None

    def menu(self):
        while True:
            choice = TournamentTemplate.menu()

            if choice == "1":
                name = input("Enter tournament name: ")
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                description = input("Enter tournament description: ")
                location = input("Enter tournament location: ")

                self.create_tournament(
                    name, start_date, end_date, description, location
                )
            elif choice == "2":
                self.add_player_to_tournament()
            elif choice == "3":
                self.launch_tournament_menu()
            elif choice == "4":
                self.display_rankings()
            elif choice == "5":
                self.list_all_tournaments()
            elif choice == "6":
                self.view_rounds_and_input_scores()
            elif choice == "7":
                return "MainView.menu"
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

    @staticmethod
    def list_all_tournaments():
        """List all available tournaments."""
        tournaments_data = Tournament.db.all()
        tournaments = [Tournament.from_dict(data) for data in tournaments_data]

        TournamentView.display_available_tournaments(tournaments)

    @staticmethod
    def create_tournament(name, start_date, end_date, description, location):
        """Creates a new tournament."""
        tournament_id = secrets.token_hex(2)
        tournament = Tournament(
            name,
            start_date,
            end_date,
            description,
            location,
            tournament_id=tournament_id,
        )
        tournament.create()
        TournamentView.auto_create_rounds(tournament)

    @staticmethod
    def auto_create_rounds(tournament):
        """Automatically creates rounds for the tournament."""
        if tournament:
            print("Automatically creating rounds...")
            for round_number in range(tournament.N_ROUNDS):
                matches = []
                tournament._add_round(round_number, matches)
            print("Rounds created successfully.")

    @staticmethod
    def launch_tournament_menu():
        """Menu to select and launch a tournament."""

        TournamentView.list_all_tournaments()
        choice = input(
            "Enter the number of the tournament to launch ('' or 0 to return): "
        )

        if choice.isdigit():
            index = int(choice) - 1
            list_tournaments = Tournament.read_all()
            if 0 <= index < len(list_tournaments):
                selected_tournament = list_tournaments[index]
                TournamentView.launch_tournament(selected_tournament)
            else:
                print("Invalid tournament selection.")
        elif choice == "" or choice == "0":
            print("Returning to main menu.")
        else:
            print("Invalid input. Returning to main menu.")

    @staticmethod
    def launch_tournament(tournament):
        """Launches the selected tournament."""

        if tournament:
            if tournament.status == "Created":
                try:
                    if TournamentTemplate.launch():
                        tournament.update_status("In Progress")
                        print(f"Tournament '{tournament.name}' launched successfully.")
                    else:
                        print("Launch cancelled.")
                except ValueError as e:
                    print(e)
            else:
                print(f"Tournament '{tournament.name}' cannot be launched.")
        else:
            print("No tournament selected.")

    @staticmethod
    def create_new_round(tournament):
        """Create a new round in the tournament."""

        if tournament:
            if TournamentTemplate.new_round():
                TournamentView.auto_create_rounds(tournament)
            else:
                print("Round creation cancelled.")
        else:
            print("No tournament available to create a new round.")

    @staticmethod
    def display_available_tournaments(list_tournaments: list) -> str:
        """Display a list of available tournaments with numbering."""

        if list_tournaments:
            print("\nAvailable Tournaments:")
            for i, tournament in enumerate(list_tournaments):
                print(f"{i + 1}.")
                print(f"Name: {tournament.name}")
                print(f"Description: {tournament.description}")
                print(f"Location: {tournament.location}")
                print(f"Status: {tournament.status}")
                print(f"Start Date: {tournament.start_date}")
                print(f"End Date: {tournament.end_date}")
        else:
            print("No tournaments available.")
        return ""

    @staticmethod
    def add_player_to_tournament():
        """Add a player to a selected tournament."""

        player = PlayerView.select_player()
        if not player:
            return

        tournaments = Tournament.read_all()
        TournamentView.display_available_tournaments(tournaments)

        choice = input(
            "Enter the number of the tournament to add the player ('' or 0 to return): "
        )

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(tournaments):
                selected_tournament = tournaments[index]
                selected_tournament.add_player(player.player_id)
                print(
                    f"{player.firstname} {player.lastname} added to {selected_tournament.name}."
                )
            else:
                print("Invalid tournament selection.")
        elif choice == "" or choice == "0":
            print("Returning to menu.")
        else:
            print("Invalid input.")

    @staticmethod
    def view_rounds_and_input_scores():
        """View rounds of a selected tournament and input scores."""

        tournaments = Tournament.read_all()
        TournamentView.display_available_tournaments(tournaments)

        choice = input(
            "Enter the number of the tournament to view rounds and input scores('' or 0 to return):"
        )

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(tournaments):
                selected_tournament = tournaments[index]
                print(f"**** Selected tournament: {selected_tournament.to_dict()}")
                TournamentView.display_rounds(selected_tournament)
            else:
                print("Invalid tournament selection.")
        elif choice == "" or choice == "0":
            print("Returning to menu.")
        else:
            print("Invalid input.")

    @staticmethod
    def display_rounds(tournament):
        """Display rounds of the selected tournament and allow score input."""

        print(f"\nRounds for Tournament: {tournament.name}")
        for i, round_id in enumerate(tournament.round_id_list):
            print(f"{i + 1}. Round {i + 1}")

        round_choice = input(
            "Enter the number of the round to input scores ('' or 0 to return): "
        )
        if round_choice.isdigit():
            round_index = int(round_choice) - 1
            if 0 <= round_index < len(tournament.round_id_list):
                round_id = tournament.round_id_list[round_index]
                print(f"Debug: Selected round_id: {round_id}")
                TournamentView.input_scores(round_id)
            else:
                print("Invalid round selection.")
        elif round_choice == "" or round_choice == "0":
            print("Returning to menu.")
        else:
            print("Invalid input.")

    @staticmethod
    def input_scores(round_id):
        """Input scores for matches in a selected round."""

        round_data = Round.read_one(round_id)
        if not round_data:
            print(f"Round with ID {round_id} not found.")
            return

        print(f"\nRound Number: {round_data.round_number}")
        print("\nMatches in the round:")
        print(f"Debug: round_data.matches = {round_data.matches}")

        if not round_data.matches:
            print("No matches found in this round.")
            return

        updated_matches = []

        for match in round_data.matches:
            if isinstance(match[0], list) and len(match[0]) == 2:
                # Match already has scores, just continue
                player_1_data, player_2_data = match[0], match[1]
            elif isinstance(match, list) and len(match) == 2:
                # Match has player IDs but no scores
                player_1_data, player_2_data = [match[0], 0], [match[1], 0]
            else:
                print(f"Invalid match structure: {match}")
                continue

            player_1_id, player_1_score = player_1_data
            player_2_id, player_2_score = player_2_data

            # Retrieve player data
            player_1 = Player.read_one(player_1_id)
            player_2 = Player.read_one(player_2_id)

            # Validate player data
            if not player_1:
                print(f"Invalid data for Player ID: {player_1_id}")
                continue

            if not player_2:
                print(f"Invalid data for Player ID: {player_2_id}")
                continue

            # Safely retrieve player attributes using attribute access
            player_1_firstname = player_1.firstname if hasattr(player_1, 'firstname') else ''
            player_1_lastname = player_1.lastname if hasattr(player_1, 'lastname') else ''

            player_2_firstname = player_2.firstname if hasattr(player_2, 'firstname') else ''
            player_2_lastname = player_2.lastname if hasattr(player_2, 'lastname') else ''

            print(f"Match: {player_1_firstname} {player_1_lastname} vs {player_2_firstname} "
                  f"{player_2_lastname}")

            try:
                player_1_score = int(input(f"Enter score for {player_1_firstname} "
                                           f"{player_1_lastname}: "))
                player_2_score = int(input(f"Enter score for {player_2_firstname} "
                                           f"{player_2_lastname}: "))
            except ValueError:
                print("Invalid score input. Please enter valid numbers.")
                continue

            # Update match score in the updated_matches
            updated_matches.append([[player_1_id, player_1_score], [player_2_id, player_2_score]])

        # After updating all matches, update the round_data
        round_data.matches = updated_matches
        round_data.update()

        # Check if this was the last round and update tournament status if necessary
        tournament_id = round_id.split("_round_")[0]
        tournament_data = Tournament.read_one(tournament_id)

        if tournament_data:
            if isinstance(tournament_data, dict):
                tournament = Tournament.from_dict(tournament_data)
            else:
                print(f"Error: Expected tournament data to be a dictionary, "
                      f"but got {type(tournament_data)}")
                return

            if round_data.round_number == tournament.N_ROUNDS - 1:
                tournament.update_status("Completed")

    @staticmethod
    def display_rankings():
        """Static method to display rankings of the selected tournament."""
        TournamentView.list_all_tournaments()
        choice = input("Enter the number of the tournament to display rankings (or 0 to return): ")

        if choice.isdigit():
            index = int(choice) - 1
            tournaments = Tournament.read_all()
            if 0 <= index < len(tournaments):
                selected_tournament = tournaments[index]
                print(f"**** Debug: Selected tournament: {selected_tournament.to_dict()}")
                TournamentView.display_rankings_for_tournament(selected_tournament)
            else:
                print("Invalid tournament selection.")
        elif choice == "" or choice == "0":
            print("Returning to menu.")
        else:
            print("Invalid input.")

    @staticmethod
    def display_rankings_for_tournament(tournament):
        """Static method to display rankings of the selected tournament."""
        if tournament:
            rankings = tournament.get_rankings()
            if rankings:
                TournamentTemplate.display_rankings(rankings=rankings)
            else:
                print("No rankings available.")
        else:
            print("No tournament available to display rankings.")
