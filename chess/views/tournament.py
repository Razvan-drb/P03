import secrets
from chess.models.players import Player
from chess.models.tournaments import Tournament
from chess.templates import tournament
from chess.templates.tournament import TournamentTemplate


class TournamentView:
        # return "TournamentView.menu", data"""Handles tournament management operations."""

    @staticmethod
    def menu(data={}):
        """Display the tournament management menu."""

        choice = TournamentTemplate.menu()

        if choice == "1":
            # tournament_data = TournamentTemplate.create()
            # self.create_tournament(
            #     tournament_data["name"],
            #     tournament_data["start_date"],
            #     tournament_data["end_date"],
            #     tournament_data["description"],
            #     tournament_data["location"],
            # )
            return "TournamentView.create_tournament", data

        elif choice == "2":

            # show_all = Tournament.read_all()
            # chosen_tournament_id = display_available_tournaments(show_all)
            # if chosen_tournament_id:
            #     selected_tournament = Tournament.read_one(chosen_tournament_id)
            #     if selected_tournament:
            #         self.tournament = selected_tournament
            #         self.launch_tournament()
            #     else:
            #         print("Tournament not found.")
            return "TournamentView.list_all_tournaments", data

        elif choice == "3":
            # Select / Load a Specific Tournament
            return "TournamentView.Select", data

        else:
             print("Invalid choice.")
            # is the possibility to go to main menu anticpicated ?
        # return "TournamentView.menu", data        return "PlayerView.menu", data

    @staticmethod
    def create_tournament(data={}):
        """Creates a new tournament."""

        # Call the template to get tournament data
        tournament_data = TournamentTemplate.create()

        # Create tournament object
        tournament = Tournament(
            name=tournament_data["name"],
            start_date=tournament_data["start_date"],
            end_date=tournament_data["end_date"],
            description=tournament_data["description"],
            location=tournament_data["location"],
        )

        tournament.create()

        return "TournamentView.menu", data


    # @staticmethod
    # def auto_create_rounds(data={}):
    #     """Automatically creates rounds for the tournament."""
    #     print("Automatically creating rounds...")
    #     for round_number in range(1, self.tournament.N_ROUNDS + 1):
    #         matches = []
    #         self.tournament._add_round(round_number, matches)
        # return "TournamentView.menu", data#     print("Rounds created successfully.")

    @staticmethod  
    def select(data={}):
        """ """

        id = TournamentTemplate.select() # a coder 

        # get the tournament from the db
        # self.tournament = Tournament.read_one(id) 

        data["tournament_id"] = id
        # return "TournamentView.menu", data    # return "TournamentView.menu", data

    @staticmethod
    def launch_tournament(data={}):
        """Launches the tournament."""

        tournament_id = input("Enter the tournament ID to launch: ")

        # Retrieve tournament by ID from the database
        tournament = Tournament.read_one(tournament_id)

        if not tournament:
            print("Tournament not found.")
            return "TournamentView.menu", data

        # Display tournament data
        TournamentTemplate.display_tournament(tournament)

        # Check if conditions are met for launching the tournament
        if len(Player.all_ids()) >= 4 and tournament.status == "Created":
            confirmation = TournamentTemplate.launch(None)

            if confirmation:
                tournament.status = "In Progress"
                tournament.update()
                print("Tournament launched successfully.")
            else:
                print("Tournament launch canceled.")
        else:
            print("Tournament conditions not met for launching.")

        return "TournamentView.menu", data

    @staticmethod
    def add_player(data={}):
        """Add a player to the tournament."""

        # Load the tournament with tournament id
        tournament_id = data.get("tournament_id")
        if not tournament_id:
            print("No tournament ID provided.")
            return "MainMenu", data

        tournament = Tournament.read_one(tournament_id)
        if not tournament:
            print("Tournament not found.")
            return "MainMenu", data

        player_data = TournamentTemplate.add_player()

        if player_data is None:
            return "MainMenu", data

        # player object
        player = Player(
            firstname=player_data["firstname"],
            lastname=player_data["lastname"],
            birthdate=player_data["birthdate"],
        )

        # Add player to tournament
        tournament.add_player(player)

        # Update tournament
        tournament.update()
        print("Player added successfully.")

        return "MainMenu", data

    @staticmethod
    def list_all_tournaments(data={}):
        """Lists all available tournaments."""

        list_tournaments = Tournament.read_all()
        # return "TournamentView.menu", data, display_available_tournaments(list_tournaments)

    @staticmethod
    def create_new_round(tournament=None, data={}):
        """Create a new round in the tournament."""

        if tournament:
            TournamentTemplate.new_round()
            tournament.auto_create_rounds()
        else:
            print("No tournament available to create a new round.")
        return "TournamentView.menu", data

    @staticmethod
    def display_rankings(tournament=None):
        """Display rankings of the tournament."""

        if tournament:
            rankings = tournament.calculate_rankings()
            TournamentTemplate.display_rankings(rankings)
        else:
            print("No tournament available to display rankings.")

    # return "TournamentView.menu", data

    @staticmethod
    def get_current_round(self, tournament):
        """Get the current round for the given tournament."""
        # return "TournamentView.menu", data    return tournament.current_round

    @staticmethod
    def _next_round(tournament=None, data={}):
        """Move to the next round."""

        if tournament:
            if tournament.current_round_number == tournament.N_ROUNDS - 1:
                tournament.status = "Completed"
            else:
                tournament.current_round_number += 1
            tournament.update()
            print("Moved to the next round successfully.")
        else:
            print("No tournament available to move to the next round.")
        return "TournamentView.menu", data

    @staticmethod
    def play_rounds(tournament):
        """Plays rounds for the given tournament."""

        if tournament:
            try:
                while tournament.status == "In Progress":
                    current_round = Tournament.get_current_round()
                    if current_round:
                        Tournament._next_round()
                    else:
                        print("No round available to play.")
            except ValueError as e:
                print(e)
        else:
            print("No tournament available to play rounds.")

    @staticmethod
    def display_available_tournaments(list_tournaments: list) -> str:
        """Display a list of available tournaments."""

        if list_tournaments:
            print("\nAvailable Tournaments:")
            for i, tournament in enumerate(list_tournaments):
                print(
                    f"{i + 1}. {tournament.name} (ID: {tournament.id})")
        else:
            print("No tournaments available.")
        return ""

