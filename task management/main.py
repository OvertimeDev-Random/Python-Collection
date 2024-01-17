from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.title("Task Managment")

tasks = []

def AddTask():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(END, task)
        entry.delete(0, END)  # Clear the entry field
        messagebox.showinfo("Success", "Successfully added task")
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def DeleteTask():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        listbox.delete(selected_task_index)
        messagebox.showinfo("Success", "Successfully removed task")
    else:
        messagebox.showwarning("Warning", "Please select a task to delete")

# Entry field for adding tasks
entry = Entry(root, width=30)
entry.place(x=50, y=50)

#Label for Entry field for adding tasks
EntryLabel = Label(root, text="Enter task name")
EntryLabel.place(x=250, y=50)

# Buttons for adding and deleting tasks
B = Button(root, text="Add Task", command=AddTask)
B2 = Button(root, text="Delete Task", command=DeleteTask)
B.place(x=75, y=350)
B2.place(x=150, y=350)

# Listbox to display tasks with checkboxes
listbox = Listbox(root, selectmode=SINGLE, width=50, height=15)
listbox.place(x=50, y=100)

root.mainloop()