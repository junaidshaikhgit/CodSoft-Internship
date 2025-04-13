import json
import os
from datetime import datetime

TASKS_FILE = "todo_tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, "r") as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                print("⚠ Error loading tasks. Starting with an empty list.")
                self.tasks = []

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def display_tasks(self):
        if not self.tasks:
            print("\n📭 Your task list is empty.")
            return
        print("\n📝 Your Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✅ Done" if task["completed"] else "❌ Pending"
            print(f"{i}. {task['title']} | Status: {status} | Created: {task['created']}")

    def add_task(self, title):
        task = {
            "title": title,
            "completed": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        print("✅ Task added successfully!")

    def mark_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            print("🔁 Task status updated.")
        else:
            print("❌ Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"🗑 Task '{removed['title']}' deleted.")
        else:
            print("❌ Invalid task number.")

    def run(self):
        while True:
            print("\n===== TO-DO LIST MENU =====")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Mark Task Complete/Incomplete")
            print("4. Delete Task")
            print("5. Exit and Save")
            print("===========================\n")

            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                self.display_tasks()

            elif choice == "2":
                title = input("🖊 Enter task title: ").strip()
                if title:
                    self.add_task(title)
                else:
                    print("⚠ Task cannot be empty.")

            elif choice == "3":
                try:
                    self.display_tasks()
                    index = int(input("Enter task number to toggle status: ")) - 1
                    self.mark_task(index)
                except ValueError:
                    print("⚠ Please enter a valid number.")

            elif choice == "4":
                try:
                    self.display_tasks()
                    index = int(input("Enter task number to delete: ")) - 1
                    self.delete_task(index)
                except ValueError:
                    print("⚠ Please enter a valid number.")

            elif choice == "5":
                self.save_tasks()
                print("💾 Tasks saved. Goodbye!")
                break

            else:
                print("❌ Invalid input. Please choose between 1-5.")

if __name__ == "__main__":
    TaskManager().run()
