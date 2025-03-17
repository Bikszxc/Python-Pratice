import json
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    # Load tasks from file
    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # Save tasks to file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    # Add a new task
    def add_task(self, title, deadline):
        new_task = {
            "title": title,
            "deadline": deadline,
            "completed": False
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"✅ Task '{title}' added successfully!\n")

    # View all tasks
    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.\n")
        else:
            print("📋 Your Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "✔️" if task["completed"] else "❗"
                print(f"{idx}. {task['title']} (Deadline: {task['deadline']}) - {status}")
            print()

    # Mark a task as completed
    def mark_completed(self, task_number):
        try:
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print(f"✅ Task {task_number} marked as completed!\n")
        except IndexError:
            print("❌ Invalid task number.\n")

    # Delete a task
    def delete_task(self, task_number):
        try:
            deleted_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"🗑️ Task '{deleted_task['title']}' deleted successfully!\n")
        except IndexError:
            print("❌ Invalid task number.\n")

# Main Menu
def main():
    manager = TaskManager()

    while True:
        print("=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            while True:
                deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
                try:
                    datetime.strptime(deadline, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Enter a valid date! (YYYY-MM-DD)")
            manager.add_task(title, deadline)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.view_tasks()
            task_num = int(input("Enter task number to mark as completed: ").strip())
            manager.mark_completed(task_num)

        elif choice == "4":
            manager.view_tasks()
            task_num = int(input("Enter task number to delete: ").strip())
            manager.delete_task(task_num)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
