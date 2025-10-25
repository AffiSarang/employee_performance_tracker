def find_top_performer(employees):
    return max(employees, key=lambda e: e.rating)

def average_rating(employees):
    return sum(e.rating for e in employees) / len(employees)

def average_tasks(employees):
    return sum(e.tasks_completed for e in employees) / len(employees)

def employee_of_the_month(employees):
    """Returns the best employee based on weighted rating and tasks."""
    if not employees:
        print(" No employee data available to determine Employee of the Month.")
        return None
    return max(employees, key=lambda e: (e.rating * 0.7 + e.tasks_completed * 0.3))
