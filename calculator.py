import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Simple Calculator by NIKHIL")


a_label = tk.Label(window, text="Number 1:")
a_label.grid(column=0, row=0)
a_entry = tk.Entry(window, width=20)
a_entry.grid(column=1, row=0)

b_label = tk.Label(window, text="Number 2:")
b_label.grid(column=0, row=1)
b_entry = tk.Entry(window, width=20)
b_entry.grid(column=1, row=1)

operation_label = tk.Label(window, text="Operation:")
operation_label.grid(column=0, row=2)
operation_var = tk.StringVar(window)
operation_var.set("Add")  # default value
operation_menu = tk.OptionMenu(window, operation_var, "Add", "Subtract", "Multiply", "Divide", "Modulus")
operation_menu.grid(column=1, row=2)

def calculate():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        operation = operation_var.get()

        if operation == "Add":
            result = a + b
        elif operation == "Subtract":
            result = a - b
        elif operation == "Multiply":
            result = a * b
        elif operation == "Divide":
            if b == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = a / b
        elif operation == "Modulus":
            if b == 0:
                messagebox.showerror("Error", "Modulus by zero is not allowed.")
                return
            result = a % b

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(column=1, row=3)


result_label = tk.Label(window, text="Result:")
result_label.grid(column=0, row=4)
result_value_label = tk.Label(window, text="")
result_value_label.grid(column=1, row=4)


window.mainloop()
