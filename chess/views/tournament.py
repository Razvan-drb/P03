import secrets

from chess.models.players import Player
from chess.models.tournaments import Tournament
from chess.templates.tournament import TournamentTemplate


class TournamentView:
    """Handles tournament management operations."""

    def __init__(self):
        self.tournament = None

    def menu(self):
        """Display the tournament management menu."""
        while True:
            choice = TournamentTemplate.menu()

            if choice == "1":
                tournament_data = TournamentTemplate.create()
                self.create_tournament(
                    tournament_data["name"],
                    tournament_data["start_date"],
                    tournament_data["end_date"],
                    tournament_data["description"],
                    tournament_data["location"],
                )
            elif choice == "2":
                self.add_player()
            elif choice == "3":
                self.launch_tournament_menu()
            elif choice == "4":
                self.create_new_round()
            elif choice == "5":
                self.display_rankings()
            elif choice == "6":
                self.list_all_tournaments()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

    def list_all_tournaments(self):
        """Lists all available tournaments."""

        list_tournaments = Tournament.read_all()

        if list_tournaments:
            for tournament in list_tournaments:
                TournamentTemplate.display_tournament(tournament)
        else:
            print("No tournaments available.")

    def create_tournament(self, name, start_date, end_date, description, location):
        """Creates a new tournament."""
        tournament_id = secrets.token_hex(2)
        self.tournament = Tournament(
            name,
            start_date,
            end_date,
            description,
            location,
            tournament_id=tournament_id,
        )
        self.tournament.create()
        self.auto_create_rounds()

    def auto_create_rounds(self):
        """Automatically creates rounds for the tournament."""
        if self.tournament:
            print("Automatically creating rounds...")
            for round_number in range(1, self.tournament.N_ROUNDS + 1):
                matches = []
                self.tournament._add_round(round_number, matches)
            print("Rounds created successfully.")

    def launch_tournament_menu(self):
        """Menu to select and launch a tournament."""
        self.list_all_tournaments()
        choice = input("Enter the number of the tournament to launch ('' or 0 to return): ")

        if choice.isdigit():
            index = int(choice) - 1
            list_tournaments = Tournament.read_all()
            if 0 <= index < len(list_tournaments):
                selected_tournament = list_tournaments[index]
                self.launch_tournament(selected_tournament)
            else:
                print("Invalid tournament selection.")
        elif choice == "" or choice == "0":
            print("Returning to main menu.")
        else:
            print("Invalid input. Returning to main menu.")

    def launch_tournament(self, tournament):
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

    def add_player(self):
        """Add a player to the tournament."""
        player_data = TournamentTemplate.add_player()
        if player_data:
            new_player = Player(
                firstname=player_data["firstname"],
                lastname=player_data["lastname"],
                birthdate=player_data["birthdate"]
            )
            new_player.create()
            print("Player added successfully.")

    def create_new_round(self):
        """Create a new round in the tournament."""
        if self.tournament:
            if TournamentTemplate.new_round():
                self.auto_create_rounds()
            else:
                print("Round creation cancelled.")
        else:
            print("No tournament available to create a new round.")

    def display_rankings(self):
        """Display rankings of the tournament."""
        if self.tournament:
            TournamentTemplate.display_rankings(rankings=self.tournament)
        else:
            print("No tournament available to display rankings.")

    @staticmethod
    def display_available_tournaments(list_tournaments: list) -> str:
        """Display a list of available tournaments."""

        if list_tournaments:
            print("\nAvailable Tournaments:")
            for i, tournament in enumerate(list_tournaments):
                print(f"{i} - {tournament}")
        else:
            print("No tournaments available.")
        return ""
