"""
CP1404 Practical 06 - Test Guitar class
Time estimated: 20 minutes
Time taken: 19 minutes
"""

from prac_06.guitar import Guitar


def run_tests():
    """Test for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2013, 799.50)

    print(f"{guitar.name} get_age() - Expected 101. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    run_tests()
