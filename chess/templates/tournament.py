#### NO MODELS IN TEMPLATES !!!!      ####
from typing import List, Dict


class TournamentTemplate:
    """Template for tournament management."""

    @classmethod
    def menu(cls) -> str:
        """Display tournament menu options."""
        print("\nTournament Menu")
        print("1. Create a tournament")
        print("2. Add a player")
        print("3. Launch tournament")
        print("4. Create a new round")
        print("5. Display rankings")
        print("6. Return to the main menu")

        return input("Enter the number you want: ")

    @classmethod
    def create(cls) -> Dict:
        """Template for creating a tournament."""
        print("\nCreating a new tournament...")
        name = input("Enter the name of the tournament: ")
        start_date = input("Enter the start date of the tournament (YYYY-MM-DD): ")
        end_date = input("Enter the end date of the tournament (YYYY-MM-DD): ")
        description = input("Enter the description of the tournament: ")
        location = input("Enter the location of the tournament: ")

        return {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "location": location,
        }

    @classmethod
    def add_player(cls) -> Dict:
        """Template for adding a player to the tournament."""
        print("\nAdding a new player...")
        firstname = input("Enter the first name of the player: ")
        lastname = input("Enter the last name of the player: ")
        birthdate = input("Enter the birthdate of the player (YYYY-MM-DD): ")

        return {
            "firstname": firstname,
            "lastname": lastname,
            "birthdate": birthdate,
        }

    @classmethod
    def launch(cls) -> str:
        """Template for launching the tournament."""
        print("\nLaunching the tournament...")
        return input("Press Enter to confirm launching the tournament.")

    @classmethod
    def new_round(cls) -> None:
        """Template for creating a new round."""
        print("\nCreating a new round...")

    @classmethod
    def display_rankings(cls, rankings: List[Dict]) -> None:
        """Template for displaying rankings."""
        print("\nRankings:")
        for rank, player in enumerate(rankings, start=1):
            print(f"{rank}. {player['firstname']} {player['lastname']} - {player['score']} points")



# class TournamentManagementSystem:

#     def __init__(self, tournament_class):
#         self.tournament_class = tournament_class
#         self.tournament = None
#         self.players = []

#     def create_tournament(self):
#         print("Creating a new tournament...")
#         name = input("Enter the name of the tournament: ")
#         while True:
#             start_date = input("Enter the start date of the tournament (YYYY-MM-DD): ")
#             try:
#                 datetime.datetime.strptime(start_date, "%Y-%m-%d")
#                 break
#             except ValueError:
#                 print(
#                     "Invalid date format. Please enter the date in YYYY-MM-DD format."
#                 )
#         while True:
#             end_date = input("Enter the end date of the tournament (YYYY-MM-DD): ")
#             try:
#                 datetime.datetime.strptime(end_date, "%Y-%m-%d")
#                 break
#             except ValueError:
#                 print(
#                     "Invalid date format. Please enter the date in YYYY-MM-DD format."
#                 )
#         description = input("Enter the description of the tournament: ")
#         location = input("Enter the location of the tournament: ")

#         tournament_id = secrets.token_hex(2)

#         self.tournament = self.tournament_class(
#             name,
#             start_date,
#             end_date,
#             description,
#             location,
#             tournament_id=tournament_id,
#         )
#         self.tournament.create()

#         # Automatically create rounds
#         self.auto_create_rounds()

#         # Launch tournament if enough players
#         if len(self.players) >= self.tournament.N_PLAYERS:
#             self.launch_tournament()

#     def auto_create_rounds(self):
#         print("Automatically creating rounds...")
#         for round_number in range(1, self.tournament.N_ROUNDS + 1):
#             matches = []
#             self.tournament.add_round(round_number, matches)
#         print("Rounds created successfully.")

#     def launch_tournament(self):
#         if self.tournament:
#             try:
#                 self.tournament.update_status("In Progress")
#                 print("Tournament launched successfully.")
#             except ValueError as e:
#                 print(e)
#         else:
#             print("No tournament available to launch.")
