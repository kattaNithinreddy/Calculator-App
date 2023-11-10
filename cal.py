import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create the number buttons
buttons = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 0, 2),
    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("0", 3, 0),
]

for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, padx=40, pady=20, command=lambda number=button_text: button_click(number))
    button.grid(row=row+1, column=column)

# Create the operator buttons
operators = [
    ("+", 0, 3),
    ("-", 1, 3),
    ("*", 2, 3),
    ("/", 3, 3),
]

for operator_text, row, column in operators:
    operator = tk.Button(window, text=operator_text, padx=40, pady=20, command=lambda op=operator_text: button_click(op))
    operator.grid(row=row+1, column=column)

# Create the clear and equal buttons
clear_button = tk.Button(window, text="Clear", padx=79, pady=20, command=button_clear)
clear_button.grid(row=4, column=0, columnspan=2)

equal_button = tk.Button(window, text="=", padx=91, pady=20, command=button_equal)
equal_button.grid(row=4, column=2, columnspan=2)

# Run the main event loop
window.mainloop()
