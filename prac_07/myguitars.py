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
