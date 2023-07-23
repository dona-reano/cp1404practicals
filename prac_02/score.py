"""
CP1404 - Determine score status using functions
"""
import random


def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(determine_status(score))
    print("Random result generated:", determine_status(random.randint(0, 100)))


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
