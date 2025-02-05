import re

password_pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d).{8,}$")


def validate_password(password: str) -> bool:
    return bool(password_pattern.match(password))
