import json

TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. If the file doesn't exist, return an empty list."""
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file with indentation for readability."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def view_json_file():
    """Read and display the JSON file contents in a formatted way."""
    try:
        with open(TODO_FILE, "r") as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))  # Pretty-print the JSON
    except FileNotFoundError:
        print("No tasks found. The file does not exist.")

def show_tasks(tasks):
    """Display all tasks in the list with status."""
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✖"
        print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    """Add a new task to the list."""
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added!")

def complete_task(tasks):
    """Mark a task as completed based on user input."""
    show_tasks(tasks)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task based on user input."""
    show_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    """Main function to handle user input for the to-do list."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        print("6. Open the JSON file")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        elif choice == "6":
            print("Opening JSON file:")
            view_json_file()  # Correct function call
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
