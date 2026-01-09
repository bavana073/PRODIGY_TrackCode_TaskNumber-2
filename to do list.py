import tkinter as tk
from tkinter import messagebox, simpledialog

def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def edit_task():
    try:
        index = listbox.curselection()[0]
        old_task = listbox.get(index)
        new_task = simpledialog.askstring(
            "Edit Task", "Edit your task:", initialvalue=old_task
        )
        if new_task:
            listbox.delete(index)
            listbox.insert(index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete")

root = tk.Tk()
root.title("To-Do List App")
root.geometry("350x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", width=15, command=add_task).pack(pady=5)
tk.Button(root, text="Edit Task", width=15, command=edit_task).pack(pady=5)
tk.Button(root, text="Delete Task", width=15, command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

root.mainloop()
