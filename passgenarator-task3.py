import string
import random
import tkinter as tk
from tkinter import messagebox

def gen_pwd(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(chars) for _ in range(length))
    return pwd

def on_gen():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be a positive integer.")
        pwd = gen_pwd(length)
        result_lbl.config(text="Generated Password: " + pwd)
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter the length of the password:").pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

gen_btn = tk.Button(root, text="Generate Password", command=on_gen)
gen_btn.pack(pady=10)

result_lbl = tk.Label(root, text="Generated Password: ")
result_lbl.pack(pady=10)

root.mainloop()
