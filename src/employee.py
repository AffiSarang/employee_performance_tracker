class Employee:
    def __init__(self, name=None, department=None, hours_worked=0, tasks_completed=0, rating=0):
        # Safe string handling
        self.name = str(name or "").strip()
        self.department = str(department or "").strip()

        # Convert numbers safely
        try:
            self.hours_worked = float(hours_worked or 0)
        except ValueError:
            self.hours_worked = 0

        try:
            self.tasks_completed = int(tasks_completed or 0)
        except ValueError:
            self.tasks_completed = 0

        try:
            self.rating = float(rating or 0)
        except ValueError:
            self.rating = 0

    def __repr__(self):
        return f"{self.name} ({self.department}) - Hours: {self.hours_worked}, Tasks: {self.tasks_completed}, Rating: {self.rating}"