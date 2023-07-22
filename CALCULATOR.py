#-------------------------------------------------------------------------------
# Name:       Atharva Waghmare
# Purpose:    TASK 2
#
# Author:      atharva
# Created:     16-07-2023
# Copyright:   (c) athar 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox

def on_button_click(button_text):
    global entry
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error: Division by zero")
            messagebox.showerror("Error", "Cannot divide by zero.")
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            messagebox.showerror("Error", f"An error occurred: {e}")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

def create_button(frame, text):
    return tk.Button(frame, text=text, padx=20, pady=10, font=("Arial", 16),
                     command=lambda: on_button_click(text))

def create_calculator():
    global entry
    root = tk.Tk()
    root.title("Simple Calculator")

    entry = tk.Entry(root, width=15, font=("Arial", 20))
    entry.grid(row=0, column=0, columnspan=4)

    button_texts = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "=", "+",
        "C"
    ]

    row = 1
    col = 0
    for text in button_texts:
        button = create_button(root, text)
        button.grid(row=row, column=col)
        col += 1
        if col > 3:
            col = 0
            row += 1

    root.mainloop()

if __name__ == "__main__":
    create_calculator()
