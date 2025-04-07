import json

class Task:
    def __init__(self, task_name, task_desc, due_date, priority, category, complete=False):
        self.task_name = task_name
        self.task_desc = task_desc
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.complete = complete

    def complete_task(self):
        """Mark the task as complete."""
        self.complete = True

    def to_dict(self):
        """Convert task to dictionary for JSON storage."""
        return {
            "task_name": self.task_name,
            "task_desc": self.task_desc,
            "due_date": self.due_date,
            "priority": self.priority,
            "category": self.category,
            "complete": self.complete
        }

    @staticmethod
    def from_dict(data):
        """Create a Task instance from a dictionary."""
        return Task(**data)

    def __str__(self):
        """Return a formatted string representation of the task."""
        status = "✔ Completed" if self.complete else "✘ Not Completed"
        return f"[{status}] {self.task_name} (Due: {self.due_date}, Priority: {self.priority}, Category: {self.category})"


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = list(self.load_tasks())  # Load tasks using the generator

    def load_tasks(self):
        """Generator that loads tasks from the JSON file one by one."""
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    yield Task.from_dict(item)  # Yield one task at a time
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error loading file! Returning empty task list.")
            return  # Returns an empty generator

    def save_file(self):
        """Save tasks to the JSON file."""
        try:
            with open(self.filename, "w") as file:
                json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        except Exception as e:
            print(f"Error saving file! {e}")

    def add_task(self, task_name, task_desc, due_date, priority, category):
        """Add a new task."""
        new_task = Task(task_name, task_desc, due_date, priority, category)
        self.tasks.append(new_task)
        self.save_file()
        print(f"Task '{task_name}' added successfully!")

    def list_tasks(self):
        """List all tasks."""
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def complete_task(self, task_index):
        """Mark a task as completed."""
        try:
            self.tasks[task_index - 1].complete_task()
            self.save_file()
            print(f"Task '{self.tasks[task_index - 1].task_name}' marked as complete!")
        except IndexError:
            print("Invalid task index.")

    def delete_task(self, task_index):
        """Delete a task."""
        try:
            removed_task = self.tasks.pop(task_index - 1)
            self.save_file()
            print(f"Task '{removed_task.task_name}' deleted successfully!")
        except IndexError:
            print("Invalid task index.")


def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Task Name: ")
            task_desc = input("Task Description: ")
            due_date = input("Due Date: ")
            priority = input("Priority (Low/Medium/High): ")
            category = input("Category: ")
            manager.add_task(task_name, task_desc, due_date, priority, category)

        elif choice == "2":
            print("\nYour Tasks:")
            manager.list_tasks()

        elif choice == "3":
            manager.list_tasks()
            task_index = int(input("Enter the task number to mark as complete: "))
            manager.complete_task(task_index)

        elif choice == "4":
            manager.list_tasks()
            task_index = int(input("Enter the task number to delete: "))
            manager.delete_task(task_index)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
