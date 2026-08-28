import secrets
import string
import tkinter as tk
from tkinter import BooleanVar, StringVar, ttk


def main() -> None:

    def password_to_generate() -> None:
        length_of_password = int(password_length.get())

        character_choices = string.ascii_lowercase
        if upper.get():
            character_choices += string.ascii_uppercase
        if digits.get():
            character_choices += string.digits
        if symbols.get():
            character_choices += string.punctuation

        password = ""
        for _ in range(length_of_password):
            password += " ".join(secrets.choice(character_choices))

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

    upper = BooleanVar(value=False)
    digits = BooleanVar(value=False)
    symbols = BooleanVar(value=False)

    ttk.Checkbutton(mainframe, text="Include uppercase", variable=upper).grid(column=0, row=2)
    ttk.Checkbutton(mainframe, text="Include digits", variable=digits).grid(column=1, row=2)
    ttk.Checkbutton(mainframe, text="Include symbols", variable=symbols).grid(column=2, row=2)

    generated_password = StringVar()
    ttk.Label(mainframe, textvariable=generated_password).grid(row=3, columnspan=3)



    root.mainloop()
