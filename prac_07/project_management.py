"""
Project Management
Estimate: 2 hours
Actual:
"""

import datetime

class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, estimate: ${self.cost_estimate:.2f},"
                f" completion: {self.completion_percentage}%")

    def __repr__(self):
        return f"({self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion_percentage})"

    def __lt__(self, other):
        return self.priority < other.priority


MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_file("projects.txt")
    print(f"Loaded {(len(projects))} from projects.txt")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("File to load: ")
            load_file(filename)
            print(f"{filename} loaded")
        elif choice == "S":
            filename = input("File to save: ")
            save_to_file(filename, projects)
        elif choice == "D":
            incomplete, complete = (test_complete_projects(projects))
            display_projects(incomplete, complete)
        elif choice == "F":
            user_date_string = input("Show projects that start after date (d/m/yyyy): ")
            user_date = datetime.datetime.strptime(user_date_string, "%d/%m/%Y").date()
            for project in projects:
                if project.start_date > user_date:
                    print(sorted(project)) # HERE
        elif choice == "A":
            add_project(projects)
            print(projects)
        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_to_modify = input("Project choice: ")
            print(project[project_to_modify])
            percentage = int(input("New Percentage: "))
            priority = int(input("New Priority: "))
        else:
            print("Invalid menu option")
        print(MENU)
        choice = input(">>> ").upper()
    quitting_save_option = input("Would you like to save to projects.txt? (Y/N) ").upper
    if quitting_save_option == 'Y':
        save_to_file("project.txt", projects)
    else:
        print("Thank you for using custom-built project management software.")



def save_to_file(filename, projects):
    save_file = open(filename, "w")
    for project in projects:
        print(project, file=save_file)
    save_file.close()


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (d/m/yyyy): ")
    date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Completion percentage: "))
    projects.append(Project(name, date, priority, cost_estimate, completion_percentage))


def load_file(filename):
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


def test_complete_projects(projects):
    complete_projects = []
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    return incomplete_projects, complete_projects


def display_projects(incomplete_projects, complete_projects):
    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"\t{project}")
    print("Complete projects:")
    for project in sorted(complete_projects):
        print(f"\t{project}")


main()
