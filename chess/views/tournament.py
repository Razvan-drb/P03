import secrets
from chess.models.players import Player
from chess.models.tournaments import Tournament
from chess.templates.tournament import TournamentTemplate


class TournamentManagementSystem:
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
                TournamentTemplate.launch()
                self.tournament.update_status("In Progress")
                print("Tournament launched successfully.")
            except ValueError as e:
                print(e)
        else:
            print("No tournament available to launch.")

    def add_player(self):
        """Add a player to the tournament."""
        player_data = TournamentTemplate.add_player()
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
            TournamentTemplate.new_round()
            self.auto_create_rounds()
        else:
            print("No tournament available to create a new round.")

    def display_rankings(self):
        """Display rankings of the tournament."""
        if self.tournament:
            rankings = self.tournament.calculate_rankings()
            TournamentTemplate.display_rankings(rankings)
        else:
            print("No tournament available to display rankings.")

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
