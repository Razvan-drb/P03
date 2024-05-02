# tournament_management.py

import datetime
import secrets

# Pas de modeles dans les temlates ;)


class TournamentManagementSystem:
    def __init__(self):
        self.tournament = None
        self.players = []

    def create_tournament(self):
        print("Creating a new tournament...")
        name = input("Enter the name of the tournament: ")
        while True:
            start_date = input("Enter the start date of the tournament (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(start_date, "%Y-%m-%d")
                break
            except ValueError:
                print(
                    "Invalid date format. Please enter the date in YYYY-MM-DD format."
                )
        while True:
            end_date = input("Enter the end date of the tournament (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(end_date, "%Y-%m-%d")
                break
            except ValueError:
                print(
                    "Invalid date format. Please enter the date in YYYY-MM-DD format."
                )
        description = input("Enter the description of the tournament: ")
        location = input("Enter the location of the tournament: ")

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

        # Automatically create rounds
        self.auto_create_rounds()

        # Launch tournament if enough players
        if len(self.players) >= self.tournament.N_PLAYERS:
            self.launch_tournament()

    def auto_create_rounds(self):
        print("Automatically creating rounds...")
        for round_number in range(1, self.tournament.N_ROUNDS + 1):
            matches = []
            self.tournament._add_round(round_number, matches)
        print("Rounds created successfully.")

    def launch_tournament(self):
        if self.tournament:
            try:
                self.tournament.update_status("In Progress")
                print("Tournament launched successfully.")
            except ValueError as e:
                print(e)
        else:
            print("No tournament available to launch.")
