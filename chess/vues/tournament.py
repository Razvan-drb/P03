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