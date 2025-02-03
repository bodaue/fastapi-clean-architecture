class ApplicationError(Exception):
    pass


class UserAlreadyExistsError(ApplicationError):
    def __init__(self, email: str) -> None:
        super().__init__(f"User '{email}' already exists")


class UserDoesNotExistsError(ApplicationError):
    def __init__(self) -> None:
        super().__init__("User does not exists")
