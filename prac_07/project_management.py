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
            print("Add")
        elif choice == 'U':
            print("Update")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.completion_percentage == COMPLETED:
            print(f"{project}")
    print("Completed projects:")
    for project in projects:
        if project.completion_percentage == COMPLETED:
            print(f"{project}")


def save_projects(projects):
    file_name = input("Save to file name: ")
    out_file = open(file_name, 'w')
    print(FILE_HEADER, file=out_file)
    for project in projects:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate:.1f}\t"
              f"{project.completion_percentage}", file=out_file)
    out_file.close()
    print(f"Saved projects to {file_name}")


def load_projects(projects):
    file_name = input("Load from file name: ")
    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    return projects


main()
