import random
import string 
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    other_characters = string.punctuation

    all_characters = lowercase + uppercase + digits + other_characters

    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def generate():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError("Please enter a positive number.")
        password = generate_password(length)
        result_label.config(text = f"Generated Password: {password}")
    except ValueError as e :
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text= "Enter the length of the password :").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate", command=generate)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row = 2, column= 0, columnspan=2, pady=10)

root.mainloop()