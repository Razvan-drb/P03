import sys

from chess.templates.tournament import TournamentManagementSystem


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

        choice = input("Enter your choice (1-6): ")

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
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

