"""
CP1404 Practical 06 - Programming Language class
Time estimated: 30 minutes
Time taken: 28 minutes
"""


class ProgrammingLanguage:
    """Represent Programming Language object."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a ProgrammingLanguage with the values.

        name: string, refer to ProgrammingLanguage object
        typing: string, Static or Dynamic typing
        reflection: Boolean, True or False
        year: integer, first appearance of language in a year"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)


if __name__ == "__main__":
    run_tests()
