import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App(CODSOFT)")
        self.tasks = []

        
        self.task_list_box = tk.Listbox(self.root, width=40)
        self.task_list_box.pack(padx=10, pady=10)

       
        self.task_entry_field = tk.Entry(self.root, width=40)
        self.task_entry_field.pack(padx=10, pady=10)

        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.task_entry_field.get()
        if task:
            self.tasks.append(task)
            self.task_list_box.insert(tk.END, task)
            self.task_entry_field.delete(0, tk.END)

    def update_task(self):
        try:
            task_index = self.task_list_box.curselection()[0]
            task = self.task_entry_field.get()
            if task:
                self.tasks[task_index] = task
                self.task_list_box.delete(task_index)
                self.task_list_box.insert(task_index, task)
                self.task_entry_field.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Select a task to update")

    def delete_task(self):
        try:
            task_index = self.task_list_box.curselection()[0]
            self.tasks.pop(task_index)
            self.task_list_box.delete(task_index)
        except:
            messagebox.showerror("Error", "Select a task to delete")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()