import json
import os

# File to store tasks persistently
TODO_FILE = 'todo_list.json'

def load_tasks():
    # Load tasks from the JSON file if it exists
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    # Save the current list of tasks to the JSON file
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks found. Your list is empty!")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "[X]" if task['completed'] else "[ ]"
            print(f"{index}. {status} {task['title']}")
    print("-----------------------\n")

def add_task(tasks):
    title = input("Enter the new task description: ")
    tasks.append({'title': title, 'completed': False})
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['title']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print("Welcome to the Python Task Manager!")
    tasks = load_tasks()
    
    while True:
        print("\nMain Menu:")
        print("1. View Tasks")
        print("2. Add a Task")
        print("3. Mark Task as Completed")
        print("4. Delete a Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting application. Have a highly productive day!")
            break
        else:
            print("Invalid choice. Please select a valid number from the menu.")

if __name__ == "__main__":
    main()