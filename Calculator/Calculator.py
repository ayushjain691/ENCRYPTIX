import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.config(bg="#1E1E1E")

        # Create the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Display area for numbers and results
        self.display = tk.Entry(self.root, font=("Helvetica", 20), borderwidth=2, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Configure grid rows and columns to be responsive with a fixed standard size
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        # Buttons for digits
        digits = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 1)
        ]
        for (text, row, col) in digits:
            button = tk.Button(self.root, text=text, font=("Helvetica", 18), bg="#61AFEF", fg="#1E1E1E",
                               command=lambda t=text: self.on_digit_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Buttons for operations
        operations = [
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
        ]
        for (text, row, col) in operations:
            button = tk.Button(self.root, text=text, font=("Helvetica", 18), bg="#E06C75", fg="#1E1E1E",
                               command=lambda t=text: self.on_operation_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Button for equal sign
        equals_button = tk.Button(self.root, text='=', font=("Helvetica", 18), bg="#98C379", fg="#1E1E1E",
                                  command=self.on_equal_click)
        equals_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

        # Button for clear
        clear_button = tk.Button(self.root, text='C', font=("Helvetica", 18), bg="#E06C75", fg="#1E1E1E",
                                 command=self.on_clear_click)
        clear_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        # Set minimum size for the calculator window
        self.root.minsize(300, 400)

    def on_digit_click(self, digit):
        current_text = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, current_text + digit)

    def on_operation_click(self, operation):
        current_text = self.display.get()
        if current_text and current_text[-1] not in "+-*/":
            self.display.insert(tk.END, operation)

    def on_equal_click(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.display.delete(0, tk.END)

    def on_clear_click(self):
        self.display.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
