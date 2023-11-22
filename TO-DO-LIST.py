import tkinter as tk
from tkinter import ttk, messagebox

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        list_update()
        task_field.delete(0, 'end')

def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        updated_task = task_field.get()

        if len(updated_task) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            tasks[selected_index] = updated_task
            list_update()
            task_field.delete(0, 'end')

    except IndexError:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Update.')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        tasks.clear()
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("700x650+550+150")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#6C52FF")

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="#6C52FF")
    functions_frame = tk.Frame(guiWindow, bg="#6C52FF")
    listbox_frame = tk.Frame(guiWindow, bg="#6C52FF")

    header_frame.pack(fill="both")
    functions_frame.pack(side="right", expand=True, fill="both")
    listbox_frame.pack(side="left", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="The To-Do List",
        font=("Brush Script MT", "40"),
        background="#6C52FF",
        foreground="#000000")
    
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Brush Script MT", "20"),
        background="#6C52FF",
        foreground="black")
   
    task_label.place(x=30, y=40)
    task_field = ttk.Entry(
        functions_frame,
        font=("Brush Script MT", "17"),
        width=18,
        background="#FFF8DC",
        foreground="black")
    
    task_field.place(x=30, y=80)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task
    )
    update_button = ttk.Button(
        functions_frame,
        text="Update Task",
        width=24,
        command=update_task
    )
    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task
    )
    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks
    )
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close
    )
    
    add_button.place(x=30, y=120)
    update_button.place(x=30, y=160)
    del_button.place(x=30, y=200)
    del_all_button.place(x=30, y=240)
    exit_button.place(x=30, y=280)

    task_listbox = tk.Listbox(
        listbox_frame,
        font=("Brush Script MT", "17"),
        width=25,
        height=18,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#6C52FF",
        selectforeground="#000000"
    )
    
    task_listbox.place(x=40, y=30)

    list_update()
    guiWindow.mainloop()
