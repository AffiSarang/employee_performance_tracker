
import matplotlib.pyplot as plt

def plot_tasks_vs_rating(employees):
    if not employees:
        print(" No employee data available to plot.")
        return

    names = [e.name for e in employees]
    tasks = [e.tasks_completed for e in employees]
    ratings = [e.rating for e in employees]

    plt.scatter(tasks, ratings, color='blue')
    plt.title("Tasks Completed vs Rating")
    plt.xlabel("Tasks Completed")
    plt.ylabel("Performance Rating")

    for i, name in enumerate(names):
        plt.text(tasks[i], ratings[i], name)

    plt.show()

def plot_tasks_vs_rating_bar(employees):
    if not employees:
        print(" No employee data available to plot.")
        return

    names = [e.name for e in employees]
    tasks = [e.tasks_completed for e in employees]
    ratings = [e.rating for e in employees]

    fig, ax1 = plt.subplots()

    ax1.bar(names, tasks, color='lightblue', label='Tasks Completed')
    ax1.set_xlabel("Employee")
    ax1.set_ylabel("Tasks Completed", color='blue')

    ax2 = ax1.twinx()
    ax2.plot(names, ratings, color='red', marker='o', label='Rating')
    ax2.set_ylabel("Performance Rating", color='red')

    plt.title("Employee Tasks vs Performance Rating")
    fig.tight_layout()
    plt.show()