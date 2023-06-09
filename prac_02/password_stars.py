"""Get password with minimum length and display asterisks."""

MINIMUM_LENGTH = 6

password = input(f"Enter a password (minimum {MINIMUM_LENGTH} characters): ")
while len(password) < MINIMUM_LENGTH:
    print("Password is too short.")
    password = input(f"Enter a password (minimum {MINIMUM_LENGTH} characters): ")
print("*" * len(password))
