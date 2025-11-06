"""
Programming Language
Estimate: 25 minutes
Actual: Approximately 40 - 45 minutes
"""


class ProgrammingLanguage:
    """Represent the Programming Language Class."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise Programming Language class attributes; name, typing, reflection, year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """String output to return"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return true if language is dynamic, false if static."""
        if self.typing == "Dynamic":
            return True
        else:
            return False
