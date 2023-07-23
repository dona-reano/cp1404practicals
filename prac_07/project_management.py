"""
CP1404 Practical 07- Project Management Program
Time estimated: 90 minutes
Time taken:
"""
FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            print("Load")
        elif choice == 'S':
            print("Save")
        elif choice == 'D':
            print("Display")
        elif choice == 'F':
            print("Filter")
        elif choice == 'A':
            print("Add")
        elif choice == 'U':
            print("Update")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


main()
