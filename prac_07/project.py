"""
CP1404 Practical 07- Project Management class module
"""


class Project:
    """Define a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project object and its attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return Project object in the form of a string"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}" \
               f", completion: {self.completion_percentage}%"
