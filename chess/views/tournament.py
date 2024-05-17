import secrets
from chess.models.tournaments import Tournament


class TournamentManagementSystem:
    """Handles tournament management operations."""

    def __init__(self):
        self.tournament = None

    def menu(self):
        """Display the tournament management menu."""
        while True:
            print("\n===== Tournament Management System Menu =====")
            print("1. Create Tournament")
            print("2. Launch Tournament")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.create_tournament(
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
                        self.tournament = selected_tournament
                        self.launch_tournament()
                    else:
                        print("Tournament not found.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

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

        print("Automatically creating rounds...")
        for round_number in range(1, self.tournament.N_ROUNDS + 1):
            matches = []
            self.tournament._add_round(round_number, matches)
        print("Rounds created successfully.")

    def launch_tournament(self):
        """Launches the tournament."""

        if self.tournament:
            try:
                self.tournament.update_status("In Progress")
                print("Tournament launched successfully.")
            except ValueError as e:
                print(e)
        else:
            print("No tournament available to launch.")

    def list_all_tournaments(self):
        """Lists all available tournaments."""

        list_tournaments = Tournament.read_all()
        display_available_tournaments(list_tournaments)

    def get_current_round(self, tournament):
        """Get the current round for the given tournament."""
        return tournament.current_round

    def _next_round(self):
        """Move to the next round."""
        if self.tournament.current_round_number == self.tournament.N_ROUNDS - 1:
            self.tournament.status = "Completed"
        else:
            self.tournament.current_round_number += 1
        self.tournament.update()

def play_rounds(tms, tournament):
    """Plays rounds for the given tournament."""

    if tournament:
        try:
            while tournament.status == "In Progress":
                current_round = tms.get_current_round(tournament)
                if current_round:
                    tms._next_round()
                else:
                    print("No round available to play.")
        except ValueError as e:
            print(e)
    else:
        print("No tournament available to play rounds.")

def display_available_tournaments(list_tournaments: list) -> str:
    """Display a list of available tournaments."""

    if list_tournaments:
        print("\nAvailable Tournaments:")
        for i, tournament in enumerate(list_tournaments):
            print(f"{i} - {tournament}")
    else:
        print("No tournaments available.")

    return ""
