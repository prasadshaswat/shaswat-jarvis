tasks = []

def show_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print("Added task:", task)

def delete_task(task_number):
    try:
        removed_task = tasks.pop(task_number-1)
        print("Removed task:", removed_task)
    except IndexError:
        print("Sorry, no task with that number.")
while True:
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("\nOptions: add, delete, quit")
    user_input = input("> ").lower()

    if user_input == "quit":
        break
    elif user_input == "add":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif user_input == "delete":
        try:
            task_number = int(input("Enter task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Error: There's no task with that number.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            continue
    else:
        print("Unknown option")
