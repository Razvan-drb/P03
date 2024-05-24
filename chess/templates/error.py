class ErrorTemplate:
    """Template for the error."""

    @staticmethod
    def not_implemented(*args, **kwargs) -> None:

        print("This feature is not implemented yet ! .")

        return None

    @staticmethod
    def generic_error(message, *args, **kwargs) -> None:

        print("An error occured.")
        print(message)

        return None
