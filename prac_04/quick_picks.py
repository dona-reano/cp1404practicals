"""
CP1404 - "Quick Pick" Lottery Ticket Generator
"""
import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Cannot be less than 0.")
        number_of_quick_picks = int(input("How many quick picks? "))
    for quick_pick in range(number_of_quick_picks):
        quick_picks = []
        for i in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()

        print(" ".join(f"{number:2}" for number in quick_picks))


main()
