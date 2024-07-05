import tkinter as tk

class ToDoList:
  def __init__(self, master):
    self.master = master
    master.title("To-Do List")

    self.tasks = []
    self.task_entry = tk.Entry(master, width=50)
    self.task_entry.pack(padx=10, pady=10)
    self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
    self.add_button.pack(pady=10)
    self.task_list = tk.Listbox(master, width=50)
    self.task_list.pack(padx=10, pady=10)
    self.mark_completed_button = tk.Button(master, text="Mark Completed", command=self.mark_completed)
    self.mark_completed_button.pack(pady=10)
    self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
    self.remove_button.pack(pady=10)

  def add_task(self):
    task = self.task_entry.get()
    if task:
      self.tasks.append(task)
      self.task_list.insert(tk.END, task)
      self.task_entry.delete(0, tk.END) 

  def mark_completed(self):
    selected_index = self.task_list.curselection()
    if selected_index:
      index = int(selected_index[0])
      self.tasks.pop(index)
      self.task_list.delete(index) 

  def remove_task(self):
    selected_index = self.task_list.curselection()
    if selected_index:
      index = int(selected_index[0])
      self.tasks.pop(index) 
      self.task_list.delete(index)  


root = tk.Tk()
todo_list = ToDoList(root)
root.mainloop()
