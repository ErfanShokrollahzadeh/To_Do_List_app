import tkinter
import tkinter.messagebox
import pickle # to save and load tasks

root = tkinter.Tk()
root.title("To-Do List by python")

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

root.mainloop()