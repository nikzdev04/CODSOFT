import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Strong Password Generator")
        self.root.geometry("300x200")

        self.length_label = tk.Label(self.root, text="Enter password length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        self.use_uppercase = tk.BooleanVar()
        self.use_uppercase.set(True)
        self.uppercase_checkbox = tk.Checkbutton(self.root, text="Use uppercase letters", variable=self.use_uppercase)
        self.uppercase_checkbox.pack()

        self.use_lowercase = tk.BooleanVar()
        self.use_lowercase.set(True)
        self.lowercase_checkbox = tk.Checkbutton(self.root, text="Use lowercase letters", variable=self.use_lowercase)
        self.lowercase_checkbox.pack()

        self.use_numbers = tk.BooleanVar()
        self.use_numbers.set(True)
        self.numbers_checkbox = tk.Checkbutton(self.root, text="Use numbers", variable=self.use_numbers)
        self.numbers_checkbox.pack()

        self.use_special_chars = tk.BooleanVar()
        self.use_special_chars.set(True)
        self.special_chars_checkbox = tk.Checkbutton(self.root, text="Use special characters", variable=self.use_special_chars)
        self.special_chars_checkbox.pack()

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(self.root, text="Generated Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        use_uppercase = self.use_uppercase.get()
        use_lowercase = self.use_lowercase.get()
        use_numbers = self.use_numbers.get()
        use_special_chars = self.use_special_chars.get()

        chars = ''
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_lowercase:
            chars += string.ascii_lowercase
        if use_numbers:
            chars += string.digits
        if use_special_chars:
            chars += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

root = tk.Tk()
app = PasswordGenerator(root)
root.mainloop()