"""
CP1404 Practical 07 - More Guitars!
"""

import csv
from prac_06.guitar import Guitar  # import Guitar class used from Practical 06

FILENAME = "guitars.csv"

guitars = []
in_file = open(FILENAME, 'r')
reader = csv.reader(in_file)
for line in reader:
    guitar = Guitar(line[0], int(line[1]), float(line[2]))
    guitars.append(guitar)
in_file.close()
guitars.sort()

print("These are your current guitars:")
for guitar in guitars:
    print(guitar)

guitar_name = input("Name: ")
while guitar_name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_to_add = Guitar(guitar_name, year, cost)
    guitars.append(guitar_to_add)
    print(f"Added {guitar_to_add} to list.")
    guitar_name = input("Name: ")
