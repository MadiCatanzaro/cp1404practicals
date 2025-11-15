"""
Project Management
Estimate: 2 hours
Actual: Approximately 2hrs 30mins for overall project task
"""


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
        return (f"({self.name}, {self.start_date.strftime("%d/%m/%Y")}, {self.priority}, {self.cost_estimate}, "
                f"{self.completion_percentage})")

    def __lt__(self, other):
        """Return true if self is less than other."""
        return self.priority < other.priority

    def is_complete(self):
        """Return true if completion percentage is 100."""
        return self.completion_percentage == 100
