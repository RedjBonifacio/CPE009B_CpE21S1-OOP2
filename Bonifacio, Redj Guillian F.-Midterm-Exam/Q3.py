import tkinter as tk

class FullNameDisplayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Midterm in OOP")
        self.geometry("600x300")

        self.label = tk.Label(self, text="Enter your fullname:", fg="red")
        self.label.place(x=50, y=100)

        self.name_input = tk.Entry(self, bd = 5)
        self.name_input.place(x=300, y=100, width = 250, height = 35)

        self.button = tk.Button(self, text="Click to display your Fullname", command=self.display_name, fg="red")
        self.button.place(x=50, y=150)

        self.output = tk.Entry(self, bd = 5)
        self.output.place(x=300, y=150, width = 250, height = 35)

    def display_name(self):
        name = self.name_input.get()
        self.output.config(state='normal')
        self.output.delete(0, tk.END)
        self.output.insert(0, name)

if __name__ == "__main__":
    app = FullNameDisplayApp()
    app.mainloop()