import re


def validate_password(password):
    """Validate a password against basic security requirements."""

    if not isinstance(password, str):
        return False, "Password must be a string."

    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain an uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain a lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain a number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain a special character."

    return True, "Password is valid."


if __name__ == "__main__":
    user_password = input("Enter a password: ")
    is_valid, message = validate_password(user_password)

    print(message)