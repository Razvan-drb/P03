import secrets
from chess.models.players import Player
from chess.models.tournaments import Tournament
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
            # is the possibility to go to main menu anticpicated ?
        # return "TournamentView.menu", data        return "PlayerView.menu", data

    @staticmethod
    def create_tournament(data={}):
        """Creates a new tournament."""

        # call the template 
        # create tournament object 
        # save in db 

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

        # select tournament 
        # reucper tournament id 
        # recup tourmmane i db
        # display tournment data

        # check if 
            # nb player ok
            # status ok
            # ==> conditions ok pour lauch tournament
        
        # if  so : 
        #     tempalte confimation launch tournament

        # if confim : 
        #     t.chanhe_status("live")
        #     t.update() in db

        return "TournamentView.menu", data    # return "TournamentView.menu", data

    @staticmethod
    def add_player(data={}):
        """Add a player to the tournament."""

        # load the tournament with tournament id in data["tournament_id"]
        # TournamenView.add_player(tournament_dict)
        # DO Objsct player T.add_player(player)...

        # return "TournamentView.menu", data
    # return "TournamentView.menu", data

    @staticmethod
    def list_all_tournaments(data={}):
        """Lists all available tournaments."""
        list_tournaments = Tournament.read_all()
        # return "TournamentView.menu", data    display_available_tournaments(list_tournaments)

    @staticmethod
    def create_new_round(data={}):
        """Create a new round in the tournament."""
        if self.tournament:
            TournamentTemplate.new_round()
            self.auto_create_rounds()
        else:
            pass
        # return "TournamentView.menu", data        print("No tournament available to create a new round.")

    @staticmethod
    def display_rankings(data={}):
        """Display rankings of the tournament."""
        if self.tournament:
            rankings = self.tournament.calculate_rankings()
            TournamentTemplate.display_rankings(rankings)
        else:
            print("No tournament available to display rankings.")

    # return "TournamentView.menu", data

    @staticmethod
    def get_current_round(self, tournament):
        """Get the current round for the given tournament."""
        # return "TournamentView.menu", data    return tournament.current_round

    @staticmethod
    def _next_round(data={}):
        """Move to the next round."""
        if self.tournament.current_round_number == self.tournament.N_ROUNDS - 1:
            self.tournament.status = "Completed"
        else:
            self.tournament.current_round_number += 1
        # return "TournamentView.menu", data    self.tournament.update()

    @staticmethod
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
        # return "TournamentView.menu", data    print("No tournament available to play rounds.")

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
