import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

def main():
    global entry, listbox

    root = tk.Tk()
    root.title("To-Do List")

    
    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    
    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack(pady=5)

  
    remove_button = tk.Button(root, text="Remove Task", command=remove_task)
    remove_button.pack(pady=5)

    
    listbox = tk.Listbox(root, width=50)
    listbox.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
