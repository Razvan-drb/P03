import sys

from chess.templates.tournament import TournamentManagementSystem


def display_available_tournaments(list_tournaments: list) -> str:
    """Display a list of available tournaments."""

    if list_tournaments:
        print("\nAvailable Tournaments:")
        for i, tournament in enumerate(list_tournaments):
            print(f"{i} - {tournament}")
    else:
        print("No tournaments available.")

    return input(
        "\nEnter the ID of the tournament you want to choose (or press Enter to return to the main menu): "
    )


##### INTERDIT ###### => View :)


def main():
    tms = TournamentManagementSystem()

    while True:
        print("\n===== Tournament Management System =====")
        print("1. Create Tournament")
        print("2. Create Player")
        print("3. Launch Tournament")
        print("4. Play Round")
        print("5. View Player Scores")
        print("6. Exit")
        print("7. Display Available Tournaments")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            tms.create_tournament()
        elif choice == "2":
            tms.create_player()
        elif choice == "3":
            tms.launch_tournament()
        elif choice == "4":
            tms.play_rounds_auto()
        elif choice == "5":
            tms.display_player_scores()
        elif choice == "6":
            print("Exiting the program...")
            sys.exit()
        elif choice == "7":
            show_all = Tournament.read_all()
            display_available_tournaments(show_all)
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

# TODO choose tournament from available list of tournaments available
