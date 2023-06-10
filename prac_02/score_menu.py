"""Score menu program"""


MENU = """G - Get a valid score (0-100)
P - Print result
S - Show stars
Q - Quit"""


"""Get a numeric score and display the same amount of asterisks."""
score = int(input("Enter score: "))
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "G":
        score = int(input("Enter score: "))
    elif choice == "P":
        if score < 0 or score > 100:
            print("Invalid score")
        elif score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        else:
            print("Bad")
    elif choice == "S":
        print("*" * score)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Farewell.")
