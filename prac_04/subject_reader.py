"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display subject details."""
    subjects = get_subjects()
    display_subjects(subjects)


def display_subjects(subjects):
    """Display subject details."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


def get_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []  # Store data in list
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        subject.append(parts)  # Adds the parts to the subject list
        print("----------")
    input_file.close()
    return subject  # Data returned as nested list


main()
