from src.storage import load_employees, save_employee,export_top_performer
from src.analysis import find_top_performer, average_rating, average_tasks,employee_of_the_month
from src.visualize import plot_tasks_vs_rating,plot_tasks_vs_rating_bar
from src.employee import Employee

def main():
    while True:
        print("\n=== Employee Performance Tracker ===")
        print("1. View all employees")
        print("2. Add new employee")
        print("3. Analyze performance")
        print("4. Visualize data")
        print("5. Employee of the Month")
        print("6. Export top performer")
        print("7. Visualize (bar chart)")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            employees = load_employees()
            for e in employees:
                print(e)

       
        elif choice == '2':
            name = input("Enter name: ")
            dept = input("Enter department: ")
            hours = input("Enter hours worked: ")
            tasks = input("Enter tasks completed: ")
            rating = input("Enter rating: ")
            emp = Employee(name, dept, hours, tasks, rating)
            save_employee(emp)
            print(" Employee added successfully!")

        elif choice == '3':
            employees = load_employees()
            top = find_top_performer(employees)
            print(f" Top Performer: {top.name} ({top.rating})")
            print(f"Average Rating: {average_rating(employees):.2f}")
            print(f"Average Tasks: {average_tasks(employees):.2f}")

        elif choice == '4':
            employees = load_employees()
            plot_tasks_vs_rating(employees)
        elif choice == '5':
          employees = load_employees()
          best = employee_of_the_month(employees)
          if best:
           print(f" Employee of the Month: {best.name}")
           print(f"Department: {best.department}")
           print(f"Tasks Completed: {best.tasks_completed}, Rating: {best.rating}")
       

        elif choice == '6':
            employees = load_employees()
            top = find_top_performer(employees)
            export_top_performer(top)

        elif choice == '7':
            employees = load_employees()
            plot_tasks_vs_rating_bar(employees)

        elif choice == '8':
            print("Thankyou")
            break


        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()