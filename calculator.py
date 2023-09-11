import tkinter as tk

def button_click(number):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Simple Calculator by Sachin ")


entry = tk.Entry(root, width=16, font=('Arial', 24), bd=5, justify='right')
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda button=button: button_click(button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=button_clear).grid(row=5, column=0)
tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 18), command=button_equal).grid(row=5, column=1, columnspan=3)

root.mainloop()
