"""
CODSOFT Python Internship - Task 1
To-Do List Application (Command-Line)
"""

tasks = []

def show_menu():
    print("\n" + "="*40)
    print("        📝 TO-DO LIST APP")
    print("="*40)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Complete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    print("="*40)

def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("❌ Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    print(f"✅ Task '{title}' added successfully!")

def view_tasks():
    if not tasks:
        print("📭 No tasks found. Add some tasks first!")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "✔ Done" if task["done"] else "⏳ Pending"
        print(f"{i}. [{status}] {task['title']}")

def mark_complete():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(f"✅ Task '{tasks[num-1]['title']}' marked as complete!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def update_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_title = input("Enter new task title: ").strip()
            if not new_title:
                print("❌ Title cannot be empty.")
                return
            old_title = tasks[num - 1]["title"]
            tasks[num - 1]["title"] = new_title
            print(f"✅ Task '{old_title}' updated to '{new_title}'!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Task '{removed['title']}' deleted!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    print("Welcome to To-Do List App!")
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("👋 Goodbye! Stay productive!")
            break
        else:
            print("❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
