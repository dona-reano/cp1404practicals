"""Score menu program"""

MENU = """G - Get a valid score (0-100)
P - Print result
S - Show stars
Q - Quit"""


def main():
    """Get a numeric score to determine status and print using functions."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            get_valid_score()
        elif choice == "P":
            determine_status(score)
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_status(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_asterisks(score):
    print("*" * score)


main()
