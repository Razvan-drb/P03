import datetime
import secrets


from chess.templates.player import PlayerTemplate


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

        # INTERDIT
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

    def create_player(self):
        """Create a new player and add them to the tournament if it exists."""
        # Call the template to get player data from the user
        p_dict = PlayerTemplate.create()

        # Extract player details from the dictionary
        firstname = p_dict["firstname"]
        lastname = p_dict["lastname"]
        birthdate = p_dict["birthdate"]

        # Create a Player object
        new_player = Player(
            firstname=firstname,
            lastname=lastname,
            birthdate=birthdate,
        )

        # Insert the player into the database
        new_player.create()

        # Add the player ID to the list of players
        self.players.append(new_player.player_id)

        print("Player created successfully.")

        # If a tournament is already created, add the player to the tournament
        if self.tournament:
            try:
                self.tournament.add_player(new_player.player_id)
                print("Player added to the tournament.")
            except ValueError as e:
                print(e)

    def play_rounds_auto(self):
        if self.tournament:
            try:
                while self.tournament.status == "In Progress":
                    current_round = self.tournament.get_current_round()
                    if current_round:
                        self.tournament.update_current_round()
                    else:
                        print("No round available to play.")
            except ValueError as e:
                print(e)
        else:
            print("No tournament available to play rounds.")

    def _next_round(self):
        """Move to the next round."""
        if self.tournament.current_round_number == self.tournament.N_ROUNDS - 1:
            self.tournament.status = "Completed"
        else:
            self.tournament.current_round_number += 1
        self.tournament.update()

    def get_current_round(self):
        c = self.tournament.current_round
        return Round.from_dict(c.to_dict())

    def get_score(self, player_id):
        """Calculate the score of a player throughout the tournament."""

        player_score = 0
        for round_id in self.tournament.round_id_list:
            round_data = Round.search_by("round_id", round_id)
            if round_data:
                for match in round_data.matches:
                    for player_tuple in match:
                        if player_tuple[0] == player_id:
                            player_score += player_tuple[1]
        return player_score

    def display_player_scores(self):
        """Display the scores of all players participating in the tournament."""

        if self.tournament:
            print("\nPlayer Scores:")
            for player_id in self.players:
                player = Player.read_one(player_id)
                if player:
                    player_name = f"{player.firstname} {player.lastname}"
                    player_score = self.get_score(player_id)
                    print(f"{player_name}: {player_score}")
                else:
                    print(f"Player with ID {player_id} not found.")
        else:
            print("No tournament available to display player scores.")

    def display_available_tournaments(self):
        pass
