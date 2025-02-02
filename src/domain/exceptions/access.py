from domain.exceptions.base import DomainError


class AuthenticationError(DomainError):
    pass


class AccessDeniedError(DomainError):
    pass
