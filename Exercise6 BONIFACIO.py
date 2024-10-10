from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.Label1 = Label(win, fg="black", text="Standard Calculator", font=("Arial Narrow", 20))
        self.Label1.place(x=100, y=35)

        self.Label1 = Label(win, fg="black", text="redj pogi", font=("Arial Narrow", 11))
        self.Label1.place(x=10, y=265)

        self.Label2 = Label(win, fg="black", text="Number 1:", font=("Arial Narrow", 13))
        self.Label2.place(x=75, y=90)
        self.Entry1 = Entry(win, bd=4, font=("Arial Narrow", 13))
        self.Entry1.place(x=150, y=90)

        self.Label3 = Label(win, fg="black", text="Number 2:", font=("Arial Narrow", 13))
        self.Label3.place(x=75, y=120)
        self.Entry2 = Entry(win, bd=4, font=("Arial Narrow", 13))
        self.Entry2.place(x=150, y=120)

        self.Label4 = Label(win, fg="black", text="Result:", font=("Arial Narrow", 13))
        self.Label4.place(x=100, y=150)
        self.Entry3 = Entry(win, bd=4, font=("Arial Narrow", 13))
        self.Entry3.place(x=150, y=150)

        self.Button1 = Button(win, fg="green", text=" Add ", font=("Arial Narrow", 13))
        self.Button1.place(x=45, y=200)
        self.Button1.bind('<Button-1>', self.add)

        self.Button2 = Button(win, fg="red", text=" Subtract ", font=("Arial Narrow", 13))
        self.Button2.place(x=93, y=200)
        self.Button2.bind('<Button-1>', self.subtract)

        self.Button3 = Button(win, fg="blue", text=" Multiply ", font=("Arial Narrow", 13))
        self.Button3.place(x=167, y=200)
        self.Button3.bind('<Button-1>', self.multiply)

        self.Button4 = Button(win, fg="orange", text=" Divide ", font=("Arial Narrow", 13))
        self.Button4.place(x=238, y=200)
        self.Button4.bind('<Button-1>', self.divide)

        self.ClearButton = Button(win, fg="black", text=" Clear ", font=("Arial Narrow", 13), command=self.clear)
        self.ClearButton.place(x=300, y=200)

        self.ExitButton = Button(win, fg="black", text="  Exit  ", font=("Arial Narrow", 12), command=win.quit)
        self.ExitButton.place(x=350, y=265)

    def add(self, win):
        self.Entry3.delete(0, 'end')
        try:
            num1 = float(self.Entry1.get())
            num2 = float(self.Entry2.get())
            result = num1 + num2
            self.Entry3.insert(END, str(result))
        except ValueError:
            self.Entry3.insert(END, "Error: Invalid Input")

    def subtract(self, win):
        self.Entry3.delete(0, 'end')
        try:
            num1 = float(self.Entry1.get())
            num2 = float(self.Entry2.get())
            result = num1 - num2
            self.Entry3.insert(END, str(result))
        except ValueError:
            self.Entry3.insert(END, "Error: Invalid Input")

    def multiply(self, win):
        self.Entry3.delete(0, 'end')
        try:
            num1 = float(self.Entry1.get())
            num2 = float(self.Entry2.get())
            result = num1 * num2
            self.Entry3.insert(END, str(result))
        except ValueError:
            self.Entry3.insert(END, "Error: Invalid Input")

    def divide(self, win):
        self.Entry3.delete(0, 'end')
        try:
            num1 = float(self.Entry1.get())
            num2 = float(self.Entry2.get())
            if num2 != 0:
                result = num1 / num2
                self.Entry3.insert(END, str(result))
            else:
                self.Entry3.insert(END, "Error: Div by 0")
        except ValueError:
            self.Entry3.insert(END, "Error: Invalid Input")

    def clear(self):
        self.Entry1.delete(0, 'end')
        self.Entry2.delete(0, 'end')
        self.Entry3.delete(0, 'end')

window = Tk()
MyWin = MyWindow(window)

window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.config(bg="white")

window.mainloop()
