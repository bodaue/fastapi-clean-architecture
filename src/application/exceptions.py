class ApplicationError(Exception):
    pass


class UserAlreadyExistsError(ApplicationError):
    def __init__(self, email: str) -> None:
        super().__init__(f"User '{email}' already exists")


class InvalidCredentialsError(ApplicationError):
    pass


class InvalidPasswordError(ApplicationError):
    pass


class LogInError(ApplicationError):
    pass


class AuthenticationRequiredError(ApplicationError):
    pass
