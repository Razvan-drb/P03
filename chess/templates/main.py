"""
Templates for the main menu.
"""


class MainTemplate:
    """Template for the main menu."""

    @classmethod
    def menu(cls) -> str:
        """Display main menu options."""

        print("\nMain Menu")
        print("1. Players")
        print("2. Tournaments")
        print("3. Exit")

        return input("Enter the number you want: ")
