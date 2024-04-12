import secrets
import datetime
import sys
from chess.models.tournaments import Tournament
from chess.models.players import Player


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
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        while True:
            end_date = input("Enter the end date of the tournament (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(end_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        description = input("Enter the description of the tournament: ")
        location = input("Enter the location of the tournament: ")

        tournament_id = secrets.token_hex(2)

        self.tournament = Tournament(name, start_date, end_date, description, location, tournament_id=tournament_id)
        self.tournament.create()

        # Automatically create rounds
        self.auto_create_rounds()

        # Launch tournament if enough players
        if len(self.players) >= self.tournament.N_PLAYERS:
            self.launch_tournament()

    def auto_create_rounds(self):
        print("Automatically creating rounds...")
        # Create rounds as needed, you can modify this logic based on your requirements
        for round_number in range(1, self.tournament.N_ROUNDS + 1):
            matches = []  # Implement your logic to generate matches
            self.tournament._add_round(round_number, matches)
        print("Rounds created successfully.")

    def launch_tournament(self):
        try:
            self.tournament.update_status("In Progress")
            print("Tournament launched successfully.")
        except ValueError as e:
            print(e)

    def create_player(self):
        print("Creating a new player...")
        firstname = input("Enter the first name of the player: ")
        lastname = input("Enter the last name of the player: ")
        birthdate = input("Enter the birthdate of the player (optional): ")

        # Create a Player object
        new_player = Player(firstname, lastname, birthdate)

        # Insert the player into the database
        new_player.create()

        # Add the player ID to the list of players
        self.players.append(new_player.player_id)

        print("Player created successfully.")

        # If tournament already created, add player to the tournament
        if self.tournament:
            try:
                self.tournament.add_player(new_player.player_id)
                print("Player added to the tournament.")
            except ValueError as e:
                print(e)


def main():
    tms = TournamentManagementSystem()

    while True:
        print("\n===== Tournament Management System =====")
        print("1. Create Tournament")
        print("2. Create Player")
        print("3. Launch Tournament")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            tms.create_tournament()
        elif choice == '2':
            tms.create_player()
        elif choice == '3':
            tms.launch_tournament()
        elif choice == '4':
            print("Exiting the program...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
