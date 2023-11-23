import tkinter as tk
from math import sqrt

def button_click(number):
    current = display_var.get()
    if current == "0":
        display_var.set(str(number))
    else:
        display_var.set(current + str(number))

def clear_entry():
    display_var.set("0")

def add():
    current = display_var.get()
    display_var.set(current + "+")

def subtract():
    current = display_var.get()
    display_var.set(current + "-")

def equals():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

def square_root():
    current = display_var.get()
    display_var.set(current + "√")

window = tk.Tk()
Width: int = 600
Height: int = 600
From_top_left: int = 500
From_top: int = 200
window.geometry(f'{Width}x{Height}+{From_top_left}+{From_top}')
display_var = tk.StringVar()
display_var.set("0")
Display = tk.Label(window, textvariable=display_var)
Display.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.1)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'CE', '=', '+',
    '√'
]

row_val = 0
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, font=("Times New Roman", 20), command=equals).grid(row=row_val, column=col_val)
    elif button == "CE":
        tk.Button(window, text=button, font=("Times New Roman", 20), command=clear_entry).grid(row=row_val, column=col_val)
    elif button == "√":
        tk.Button(window, text=button, font=("Times New Roman", 20), command=square_root).grid(row=row_val, column=col_val)
    elif button in {'+', '-', '*', '/'}:
        if button == '+':
            tk.Button(window, text=button, font=("Times New Roman", 20), command=add).grid(row=row_val, column=col_val)
        elif button == '-':
            tk.Button(window, text=button, font=("Times New Roman", 20), command=subtract).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, font=("Times New Roman", 20), command=lambda x=button: button_click(x)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
