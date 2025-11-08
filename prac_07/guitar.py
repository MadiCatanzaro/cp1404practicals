"""
Guitar
"""

CURRENT_YEAR = 2022


class Guitar:
    """Represent Guitar Class"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar class attributes; name, year, cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string output."""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def __repr__(self):
        """Return representative string output???"""
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


def main():
    guitars = []
    in_file = open("guitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(parts[0], year, cost)
        guitars.append(guitar)
    print(guitars)

    # sort(guitars[0], guitars[1])
    print(sorted(guitars))
    # print(new_guitars)


main()
