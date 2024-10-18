import string
import random
import tkinter as tkc
from tkinter import messagebox

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(15))
    password_entry.delete(0, tkc.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    window.clipboard_clear()
    window.clipboard_append(password)
    messagebox.showinfo("Password Generator", "Password copied to clipboard.")

window = tkc.Tk()
window.title("Password Generator")

password_label = tkc.Label(text="Password:")
password_label.grid(row=0, column=0, pady=10)

password_entry = tkc.Entry(show="*", width=30)
password_entry.grid(row=0, column=1, pady=10)

generate_button = tkc.Button(text="Generate", command=generate_password)
generate_button.grid(row=1, column=0, pady=10)

copy_button = tkc.Button(text="Copy", command=copy_password)
copy_button.grid(row=1, column=1, pady=10)

window.mainloop()
