

import csv
import os
from src.employee import Employee

# === File paths ===
FILE_PATH = "data/employees.csv"
TOP_FILE_PATH = "data/top_performer.csv"

def load_employees():
    """Loads employee data from CSV and returns a list of Employee objects."""
    employees = []
    try:
        with open(FILE_PATH, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not row or not any(row.values()):
                    continue
                try:
                    employees.append(Employee(
                        name=row.get('name'),
                        department=row.get('department'),
                        hours_worked=float(row.get('hours_worked', 0)),
                        tasks_completed=int(row.get('tasks_completed', 0)),
                        rating=float(row.get('rating', 0))
                    ))
                except ValueError as ve:
                    print(f"Skipping row due to conversion error: {row} → {ve}")
    except FileNotFoundError:
        print(" employees.csv file not found. Please make sure it exists in the data/ folder.")
    return employees

def save_employee(emp):
    """Appends a new employee record to the CSV file, adding headers if needed."""
    file_exists = os.path.isfile(FILE_PATH)
    write_header = not file_exists or os.path.getsize(FILE_PATH) == 0

    with open(FILE_PATH, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["name", "department", "hours_worked", "tasks_completed", "rating"])
        writer.writerow([
            emp.name,
            emp.department,
            emp.hours_worked,
            emp.tasks_completed,
            emp.rating
        ])

def export_top_performer(employee):
    """Exports the top performer data into a new CSV file."""
    with open(TOP_FILE_PATH, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "department", "hours_worked", "tasks_completed", "rating"])
        writer.writerow([
            employee.name,
            employee.department,
            employee.hours_worked,
            employee.tasks_completed,
            employee.rating
        ])
    print(f" Top performer exported to {TOP_FILE_PATH}")