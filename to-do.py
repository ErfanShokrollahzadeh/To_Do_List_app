import tkinter
import tkinter.messagebox
import pickle # to save and load tasks
from tkinter import filedialog

# from tkinter import filedialog

# from tkinter import filedialog

root = tkinter.Tk()
root.title("To-Do List by python")


# Create functions
# def add_task():
#     task = entry_task.get()
#     if task != "":
#         listbox_tasks.insert(tkinter.END, task)
#         entry_task.delete(0, tkinter.END)
#     else:
#         tkinter.messagebox.showinfo("warning", " Please enter a task")

def add_task():
    task = entry_task.get()
    if task != "":
        # Add task to the listbox
        listbox_tasks.insert(tkinter.END, task)

        # Add task to the file
        with open("test.txt", "a") as file:
            file.write(task + "\n")

        # Clear the entry field
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showinfo("Warning", "Please enter a task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showinfo("warning", " Please select a task")

# def delete_task():
#     try:
#         # Get the selected task index
#         task_index = listbox_tasks.curselection()[0]
#
#         # Get the selected task
#         selected_task = listbox_tasks.get(task_index)
#
#         # Delete the task from the listbox
#         listbox_tasks.delete(task_index)
#
#         # Delete the task from the file
#         with open("test.txt", "r") as file:
#             lines = file.readlines()
#
#         with open("test.txt", "w") as file:
#             for line in lines:
#                 if line.strip() != selected_task:
#                     file.write(line)

    # except IndexError:
    #     tkinter.messagebox.showinfo("Warning", "Please select a task")
    # except Exception as e:
    #     tkinter.messagebox.showinfo("Error", f"An error occurred: {e}")

def edit_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(task_index)
        entry_task.delete(0, tkinter.END)  # Clear the entry field
        entry_task.insert(0, task_text)  # Populate the entry field with the selected task
        listbox_tasks.delete(task_index)  # Remove the selected task from the listbox
    except:
        tkinter.messagebox.showinfo("Warning", "Please select a task to edit.")

def save_edited_task():
    edited_task = entry_task.get()
    if edited_task:
        listbox_tasks.insert(tkinter.END, edited_task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showinfo("Warning", "Please enter a valid task.")

# def load_task():
#     try:
#         with open("test.txt", "r") as file:
#             tasks = file.readlines()
#
#         # Remove newline characters from each task and display in listbox
#         listbox_tasks.delete(0, tkinter.END)
#         for task in tasks:
#             task = task.strip()
#             listbox_tasks.insert(tkinter.END, task)
#
#     except FileNotFoundError:
#         tkinter.messagebox.showinfo("Warning", "No tasks found in the file.")
#     except Exception as e:
#         tkinter.messagebox.showinfo("Error", f"An error occurred: {str(e)}")

def load_task():
    try:
        # Ask the user to select a file
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])

        # Check if the user canceled the file dialog
        if not file_path:
            return

        with open(file_path, "r") as file:
            tasks = file.readlines()

        # Remove newline characters from each task and display in listbox
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            task = task.strip()
            listbox_tasks.insert(tkinter.END, task)

    except FileNotFoundError:
        tkinter.messagebox.showinfo("Warning", "No tasks found in the selected file.")
    except Exception as e:
        tkinter.messagebox.showinfo("Error", f"An error occurred: {str(e)}")

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    # print(tasks)
    pickle.dump(tasks, open("tasks.dat", "wb")) # wb = write binary

def exit_root():
    exit_task = tkinter.messagebox.askyesno("To-Do List by python", "Do you want to exit?")
    if exit_task > 0:
        root.destroy()
        return


# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

# Create scrollbar
scrollbar = tkinter.Scrollbar(frame_tasks)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

# create buttons
button_add_task = tkinter.Button(root, text="Add task", width=48, command=lambda: add_task())
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=lambda: delete_task())
button_delete_task.pack()

button_edit_task = tkinter.Button(root, text="Edit task", width=48, command=lambda: edit_task())
button_edit_task.pack()

button_save_edited_task = tkinter.Button(root, text="Save edited task", width=48, command=lambda: save_edited_task())
button_save_edited_task.pack()

button_load_task = tkinter.Button(root, text="Load task", width=48, command=lambda: load_task())
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save task", width=48, command=lambda: save_task())
button_save_task.pack()

button_exit = tkinter.Button(root, text="Exit", width=48, command=lambda: exit_root())
button_exit.pack()

root.mainloop()