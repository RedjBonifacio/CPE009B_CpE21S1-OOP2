import tkinter as tk
from tkinter import messagebox, filedialog
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(False, False)

        self.result_var = tk.StringVar()
        self.create_widgets()

        self.bind('<Control-q>', lambda e: self.exit_program())

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), justify='right', bd=10)
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('exp', 5, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, command=lambda t=text: self.on_button_click(t), font=("Arial", 18), bd=5)
            button.grid(row=row, column=col, sticky='nsew', ipadx=10, ipady=10)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_to_file)
        file_menu.add_command(label="Load", command=self.load_from_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_program)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set('')
        elif char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
                self.save_to_file(expression + ' = ' + str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid expression")
                self.result_var.set('')
        elif char in ('sin', 'cos', 'exp'):
            try:
                value = float(self.result_var.get())
                if char == 'sin':
                    result = math.sin(math.radians(value))
                elif char == 'cos':
                    result = math.cos(math.radians(value))
                elif char == 'exp':
                    result = math.exp(value)
                self.result_var.set(result)
                self.save_to_file(f"{char}({value}) = {result}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input for sin/cos/exp")
                self.result_var.set('')
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

    def save_to_file(self, data):
        with open("calculator_history.txt", "a") as file:
            file.write(data + '\n')

    def load_from_file(self):
        try:
            with open("calculator_history.txt", "r") as file:
                history = file.read()
            messagebox.showinfo("History", history)
        except FileNotFoundError:
            messagebox.showerror("Error", "No history file found")

    def exit_program(self):
        self.quit()

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

    