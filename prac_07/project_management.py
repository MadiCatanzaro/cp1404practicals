"""
Project Management
Estimate: 2 hours
Actual: 1:56 so far
"""

import datetime
from operator import attrgetter


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise Class objects."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Display string representation of Project."""
        return (
            f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, estimate: "
            f"${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        """Display string representation of Project."""
        return f"({self.name}, {self.start_date.strftime("%d/%m/%Y")}, {self.priority}, {self.cost_estimate}, {self.completion_percentage})"

    def __lt__(self, other):
        """Return true if self is less than other."""
        return self.priority < other.priority

    def is_complete(self):
        """Return true if completion percentage is 100."""
        return self.completion_percentage == 100


MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Main function for Project Management."""
    print("Welcome to Pythonic Project Management")
    projects = load_file("projects.txt")
    print(f"Loaded {(len(projects))} from projects.txt")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            try:
                filename = input("File to load: ")
                load_file(filename)
                print(f"{filename} loaded")
            except FileNotFoundError:
                print("File not found")
        elif choice == "S":
            filename = input("File to save: ")
            save_to_file(filename, projects)
        elif choice == "D":
            incomplete, complete = (separate_complete_projects(projects))
            display_projects(incomplete, complete)
        elif choice == "F":
            sort_by_date(projects)
        elif choice == "A":
            add_project(projects)
            # print(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid menu option")
        print(MENU)
        choice = input(">>> ").upper()
    quit_program(projects)


def sort_by_date(projects):
    """Sort projects by date after a given date."""
    current_projects = []
    is_valid = False
    while not is_valid:
        try:
            user_date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            user_date = datetime.datetime.strptime(user_date_string, "%d/%m/%Y").date()
            is_valid = True
        except ValueError:
            print("Invalid date input")

    for project in projects:
        if project.start_date > user_date:
            current_projects.append(project)
    for project in sorted(current_projects, key=attrgetter("start_date")):
        print(project)


def update_projects(projects):
    """Update percentage or priority of project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    is_valid = False
    while not is_valid:
        try:
            project_to_modify = int(input("Project choice: "))
            is_valid = True
        except IndexError:  # does not handle IndexErrors
            print("Invalid project choice, must be chosen from the given project numbers")
        except ValueError:
            print("Invalid project choice, please enter a number")
    print(projects[project_to_modify])
    try:
        percentage = int(input("New Percentage: "))
    except ValueError:
        percentage = projects[project_to_modify].percentage
    try:
        priority = int(input("New Priority: "))
    except ValueError:
        priority = projects[project_to_modify].priority

    projects[project_to_modify].completion_percentage = percentage
    projects[project_to_modify].priority = priority


def quit_program(projects):
    """Quit program, optionally saving projects to project.txt file."""
    quitting_save_option = input("Would you like to save to projects.txt? (Y/N) ").upper()
    if quitting_save_option == 'Y':
        save_to_file("project.txt", projects)
        print("Projects saved.")
    print("Thank you for using custom-built project management software.")


def save_to_file(filename, projects):
    """Save projects to specified file."""
    save_file = open(filename, "w")
    for project in projects:
        print(project, file=save_file)
    save_file.close()


def add_project(projects):
    """Add new project to projects."""
    is_valid = False
    print("Let's add a new project")
    while not is_valid:
        try:
            name = input("Name: ")
            start_date_string = input("Start date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            completion_percentage = int(input("Completion percentage: "))
            is_valid = True

        except ValueError:
            print("Invalid project input")
    projects.append(Project(name, date, priority, cost_estimate, completion_percentage))


def load_file(filename):
    """Load projects from file and process into an appropriate format."""
    projects = []
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        date_string = parts[1]
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])
        project = Project(parts[0], date, priority, cost_estimate, completion_percentage)
        projects.append(project)
    return projects


def separate_complete_projects(projects):
    """Separate files into complete and incomplete."""
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    return incomplete_projects, complete_projects


def display_projects(incomplete_projects, complete_projects):
    """Display incomplete and complete projects."""
    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"\t{project}")
    print("Completed projects:")
    for project in sorted(complete_projects):
        print(f"\t{project}")


main()
