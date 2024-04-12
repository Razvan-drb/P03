import sys

from chess.templates.tournament import TournamentManagementSystem


def main():
    tms = TournamentManagementSystem()

    while True:
        print("\n===== Tournament Management System =====")
        print("1. Create Tournament")
        print("2. Create Player")
        print("3. Launch Tournament")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            tms.create_tournament()
        elif choice == "2":
            tms.create_player()
        elif choice == "3":
            tms.launch_tournament()
        elif choice == "4":
            print("Exiting the program...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
