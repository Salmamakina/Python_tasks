import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""

        # Entry widget to display the expression/result
        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4)

        # Creating buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == "=":
                tk.Button(root, text=button, width=10, height=3, command=self.evaluate).grid(row=row, column=col, columnspan=2)
            else:
                tk.Button(root, text=button, width=5, height=3, command=lambda b=button: self.append_to_expression(b)).grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        tk.Button(root, text='C', width=5, height=3, command=self.clear).grid(row=row, column=0)

    def append_to_expression(self, char):
        self.expression += str(char)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
