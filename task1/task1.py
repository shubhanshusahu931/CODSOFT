import json
import os

TASK_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = input("Enter task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added Sucessfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found in list ")
    else:
        for i, task in enumerate(tasks, 1):
            status = "done" if task["completed"] else "not done"
            print(f"{i}. {task['task']} [{status}]")

def delete_task():
    view_tasks()
    tasks = load_tasks()
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks(tasks)
            print(f" Deleted Sucessfully : {removed['task']}")
        else:
            print(" Task not found in list ")
    except:
        print(" Invalid input!")

def mark_task():
    view_tasks()
    tasks = load_tasks()
    try:
        num = int(input("Enter task number to mark completed: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["completed"] = True
            save_tasks(tasks)
            print(" Task marked as completed.")
        else:
            print(" Invalid task number.")
    except:
        print(" Please enter a number.")

def menu():
    while True:
        print("\n To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print(" Invalid option.")

menu()
