import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("600x600")

        # Entry widget for new task
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        # Add Task button
        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Buttons for delete and mark done
        self.delete_button = tk.Button(self.root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.mark_done_button = tk.Button(self.root, text="Mark as Done", width=20, command=self.mark_done)
        self.mark_done_button.pack(pady=5)

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected)
            self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            task = self.task_listbox.get(selected)
            if not task.startswith("✔ "):
                self.task_listbox.delete(selected)
                self.task_listbox.insert(selected, f"✔ {task}")
                self.save_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def save_tasks(self):
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            tasks = self.task_listbox.get(0, tk.END)
            for task in tasks:
                f.write(task + "\n")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                tasks = f.readlines()
                for task in tasks:
                    self.task_listbox.insert(tk.END, task.strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
