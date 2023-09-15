import random
import string
import tkinter as tk

def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    result_label.config(text=f"Generated Password: {password}")


window = tk.Tk()
window.title("Password Generator by Sachin ")


length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=(10,0))
length_entry = tk.Entry(window)
length_entry.pack(pady=(0,10))

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=(0,10))


result_label = tk.Label(window, font=("Helvetica", 12), wraplength=300)
result_label.pack()

window.mainloop()
