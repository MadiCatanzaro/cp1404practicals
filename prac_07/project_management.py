"""
Project Management
Estimate: 2 hours
Actual:
"""


class Project:

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.00, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion_percentage}"

    def __repr__(self):
        return f"({self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion_percentage})"


MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    projects = []
    print("Welcome to Pythonic Project Management")
    load_file("projects.txt")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_file("projects.txt")
            print("stop")
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu option")
            print(MENU)
            choice = input(">>> ").upper()


def load_file(filename):
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        print(parts)


main()
