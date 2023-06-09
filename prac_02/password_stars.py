"""Get password with minimum length and display asterisks."""

MINIMUM_LENGTH = 6


def version_1():
    """Get password that meets minimum character length and print the same amount of asterisks."""
    password = input(f"Enter a password (minimum {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short.")
        password = input(f"Enter a password (minimum {MINIMUM_LENGTH} characters): ")
    print("*" * len(password))


version_1()


def main():
    """Get password and print using functions."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get password that meets the minimum character length."""
    password = input(f"Enter a password (minimum {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short.")
        password = input(f"Enter a password (minimum {MINIMUM_LENGTH} characters): ")
    return password


def print_asterisks(password):
    """Print the same amount of asterisks as there are characters in the password."""
    print("*" * len(password))


main()
