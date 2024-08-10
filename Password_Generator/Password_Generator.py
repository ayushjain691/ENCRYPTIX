import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.config(bg="#282C34")

        # Create the GUI components
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Password Length:", font=("Helvetica", 12, "bold"),
                 bg="#282C34", fg="#61AFEF").pack(pady=10)
        self.length_entry = tk.Entry(self.root, font=("Helvetica", 12), width=10)
        self.length_entry.pack(pady=10)

        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        # Frame to hold the checkboxes and keep them centered
        checkbox_frame = tk.Frame(self.root, bg="#282C34")
        checkbox_frame.pack(pady=20)

        # Setting a consistent width for the checkboxes
        checkbox_width = 25

        self.uppercase_button = tk.Checkbutton(checkbox_frame, text="Include Uppercase Letters",
                                               variable=self.include_uppercase, font=("Helvetica", 10),
                                               bg="#282C34", fg="#ABB2BF", selectcolor="#98C379",
                                               activebackground="#E06C75", command=self.toggle_uppercase_color,
                                               width=checkbox_width, anchor='w')
        self.uppercase_button.pack(anchor='center', pady=5)

        self.numbers_button = tk.Checkbutton(checkbox_frame, text="Include Numbers",
                                             variable=self.include_numbers, font=("Helvetica", 10),
                                             bg="#282C34", fg="#ABB2BF", selectcolor="#98C379",
                                             activebackground="#E06C75", command=self.toggle_numbers_color,
                                             width=checkbox_width, anchor='w')
        self.numbers_button.pack(anchor='center', pady=5)

        self.special_button = tk.Checkbutton(checkbox_frame, text="Include Special Characters",
                                             variable=self.include_special, font=("Helvetica", 10),
                                             bg="#282C34", fg="#ABB2BF", selectcolor="#98C379",
                                             activebackground="#E06C75", command=self.toggle_special_color,
                                             width=checkbox_width, anchor='w')
        self.special_button.pack(anchor='center', pady=5)

        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password,
                                    font=("Helvetica", 12, "bold"), bg="#E06C75", fg="#282C34", activebackground="#61AFEF")
        generate_button.pack(pady=20)

        self.password_display = tk.Entry(self.root, state='readonly', justify='center', font=("Helvetica", 14, "bold"),
                                         width=24, bg="#98C379", fg="#282C34")
        self.password_display.pack(pady=10)

    def toggle_uppercase_color(self):
        if self.include_uppercase.get():
            self.uppercase_button.config(fg="#ABB2BF", selectcolor="#98C379")
        else:
            self.uppercase_button.config(fg="#E06C75", selectcolor="#E06C75")

    def toggle_numbers_color(self):
        if self.include_numbers.get():
            self.numbers_button.config(fg="#ABB2BF", selectcolor="#98C379")
        else:
            self.numbers_button.config(fg="#E06C75", selectcolor="#E06C75")

    def toggle_special_color(self):
        if self.include_special.get():
            self.special_button.config(fg="#ABB2BF", selectcolor="#98C379")
        else:
            self.special_button.config(fg="#E06C75", selectcolor="#E06C75")

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showerror("Error", "Password length must be at least 4 characters.")
                return

            characters = string.ascii_lowercase
            if self.include_uppercase.get():
                characters += string.ascii_uppercase
            if self.include_numbers.get():
                characters += string.digits
            if self.include_special.get():
                characters += string.punctuation

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_display.config(state='normal')
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the password length.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
