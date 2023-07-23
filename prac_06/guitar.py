"""
CP1404 Practical 06 - Define a Guitar class
Time estimated: 15 minutes
Time taken: 18 minutes
"""
import datetime

CURRENT_YEAR = datetime.date.today().year
VINTAGE_AGE = 50


class Guitar:
    """Store details of Guitar class object.

    name: string, refer to guitar object name
    year: integer, year manufactured
    cost: float, guitar cost"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Guitar object in the form of a string"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return age of guitar using the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if Guitar object is considered vintage using age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Sort Guitar objects by year released."""
        return self.year < other.year
