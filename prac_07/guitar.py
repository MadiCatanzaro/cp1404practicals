"""
Guitar
"""

CURRENT_YEAR = 2022


class Guitar:
    """Represent Guitar Class"""

    def __init__(self, name="", year=0, cost=0.00):
        """Initialise Guitar class attributes; name, year, cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string output for a Guitar."""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def __repr__(self):
        """Return representative string output for a Guitar."""
        return f"({self.name}, {self.year}, {self.cost})"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Return the age of the guitar, calculated from the given year and the current year."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Return true if the guitar is vintage (over or equal to 50 years old), and false if under 50 years old."""
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False
