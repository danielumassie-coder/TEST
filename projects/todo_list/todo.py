"""
Project: To-Do List Application
=================================

Create a simple to-do list manager that can:
- Add tasks
- Mark tasks as complete
- Delete tasks
- Display all tasks

This project practices:
- Lists
- Dictionaries
- Functions
- User input
- Control flow
"""

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("To-Do List Manager")
    print("=" * 40)
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")
    print("=" * 40)

def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\nNo tasks yet! Add one to get started.")
        return
    
    print("\nYour Tasks:")
    print("-" * 40)
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['completed'] else " "
        print(f"{i}. [{status}] {task['title']}")
    print("-" * 40)

def add_task(tasks):
    """Add a new task"""
    title = input("\nEnter task description: ").strip()
    if title:
        task = {
            'title': title,
            'completed': False
        }
        tasks.append(task)
        print(f"✓ Task added: {title}")
    else:
        print("Task cannot be empty!")

def complete_task(tasks):
    """Mark a task as complete"""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter task number to complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"✓ Task completed: {tasks[task_num - 1]['title']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    """Delete a task"""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"✓ Task deleted: {deleted_task['title']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main program loop"""
    tasks = []
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nGoodbye! Stay productive!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
