import secrets
import string
import tkinter as tk
from tkinter import StringVar, ttk


def main() -> None:

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    all = upper + lower + digits + symbols

    def password_to_generate():
        length_of_password = int(password_length.get())

        password = ""
        for i in range(length_of_password):
            password += " ".join(secrets.choice(all))

        generated_password.set(password)



    #GUI

    root = tk.Tk()
    root.title("Password Generator")
    mainframe = ttk.Frame(root, padding=10)
    mainframe.grid(column=0, row=0, sticky="NWES")

    ttk.Label(mainframe, text="Enter password length:").grid(column=0, row=1, sticky="E")

    password_length = StringVar()
    password_length_entry = ttk.Entry(mainframe, width=7, textvariable=password_length)
    password_length_entry.grid(column=1, row=1, sticky="W")
    ttk.Button(mainframe, text="Generate", command=password_to_generate).grid(column=2, row=1)

    generated_password = StringVar()
    ttk.Label(mainframe, textvariable=generated_password).grid(row=2, columnspan=3)



    root.mainloop()
