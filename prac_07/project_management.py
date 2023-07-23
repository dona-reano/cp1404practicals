"""
CP1404 Practical 07- Project Management Program
Time estimated: 90 minutes
Time taken:
"""
from project import Project

FILE_HEADER = "Name\tStart Date	Priority\tCost Estimate\tCompletion Percentage"

FILENAME = "projects.txt"

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit"

COMPLETED = 100


def main():
    """Project management program that loads from and saves to a data file."""
    print(MENU)
    projects = []
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            projects = load_projects(projects)
        elif choice == 'S':
            save_projects(projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            print("Filter")
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            print("Update")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def add_project(projects):
    """Add a new project to the list of projects"""
    print("Let's add a new project")
    project_to_add = get_valid_string("Name: ")
    start_date = get_valid_string("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    projects.append(Project(project_to_add, start_date, priority, cost_estimate, percent_complete))


def get_valid_string(prompt):  # Reused function from past classes to get a valid string
    """Prompt the user for a non-empty string."""
    string = input(prompt)
    while string == "":
        print("Input cannot be blank")
        string = input(prompt)
    return string


def display_projects(projects):
    """Displays incomplete and completed projects."""
    print("Incomplete projects:")
    for project in projects:
        if not project.completion_percentage == COMPLETED:
            print(f"{project}")
    print("Completed projects:")
    for project in projects:
        if project.completion_percentage == COMPLETED:
            print(f"{project}")


def save_projects(projects):
    """Saves project details to a data file."""
    file_name = input("Save to file name: ")
    out_file = open(file_name, 'w')
    print(FILE_HEADER, file=out_file)
    for project in projects:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate:.1f}\t"
              f"{project.completion_percentage}", file=out_file)
    out_file.close()
    print(f"Saved projects to {file_name}")


def load_projects(projects):
    """Loads a data file containing project details."""
    file_name = input("Load from file name: ")
    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    return projects


main()
