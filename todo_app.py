import tkinter as tk
from tkinter import messagebox
import os

DATA_FILE = "todo_data.txt"

class TaskManager:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.geometry("420x450")

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Input field
        self.input_field = tk.Entry(self.master, font=('Arial', 12), width=35)
        self.input_field.pack(pady=12)

        # Add task button
        self.add_btn = tk.Button(self.master, text="Add Task", width=18, command=self.add_item)
        self.add_btn.pack()

        # Listbox to show tasks
        self.task_box = tk.Listbox(self.master, width=45, height=12, selectmode=tk.SINGLE, font=('Arial', 10))
        self.task_box.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self.master)
        btn_frame.pack(pady=5)

        self.complete_btn = tk.Button(btn_frame, text="Mark Done", width=15, command=self.mark_task)
        self.complete_btn.grid(row=0, column=0, padx=5)

        self.remove_btn = tk.Button(btn_frame, text="Remove Task", width=15, command=self.remove_item)
        self.remove_btn.grid(row=0, column=1, padx=5)

    def add_item(self):
        task_text = self.input_field.get().strip()
        if task_text:
            self.task_box.insert(tk.END, task_text)
            self.input_field.delete(0, tk.END)
            self.save_data()
        else:
            messagebox.showwarning("Empty Field", "Please enter a task before adding.")

    def remove_item(self):
        selected = self.task_box.curselection()
        if selected:
            self.task_box.delete(selected[0])
            self.save_data()
        else:
            messagebox.showwarning("No Selection", "Choose a task to remove.")

    def mark_task(self):
        selected = self.task_box.curselection()
        if selected:
            task = self.task_box.get(selected)
            if not task.startswith("[✓] "):
                self.task_box.delete(selected)
                self.task_box.insert(selected, "[✓] " + task)
                self.save_data()
        else:
            messagebox.showwarning("No Selection", "Choose a task to mark as done.")

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            for index in range(self.task_box.size()):
                file.write(self.task_box.get(index) + "\n")

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    self.task_box.insert(tk.END, line.strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
