"""
Emails
Estimate: 30 minutes
Actual: 48 minutes
"""


def main():
    """Store users' emails and names in a dictionary then print."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_expected_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_expected_name(email):
    """Retrieve expected name from users' emails."""
    prefix = email.split('@')[0]
    elements = prefix.split('.')
    name = " ".join(elements).title()
    return name


main()
