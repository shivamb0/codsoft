from tkinter import *
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x450+300+150')

        # Title Label
        self.label = Label(self.root, text='To-Do-List-App', font=('Times New Roman', 25), width=15, bg='white', fg='black')
        self.label.pack(side='top', fill=BOTH)

        # Add Task Label
        self.label2 = Label(self.root, text='Add Task', font=('Times New Roman', 25), width=15, bg='white', fg='black')
        self.label2.place(x=40, y=54)

        # Tasks Label
        self.label3 = Label(self.root, text='Tasks', font=('Times New Roman', 25), width=15, bg='white', fg='black')
        self.label3.place(x=320, y=54)

        # Listbox for tasks with Scrollbar
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL)
        self.main_text = Listbox(self.root, height=12, bd=5, width=30, font=('Times New Roman', 20), yscrollcommand=self.scrollbar.set)
        self.main_text.place(x=300, y=100)
        self.scrollbar.config(command=self.main_text.yview)
        self.scrollbar.place(x=580, y=100, height=200)

        # Text widget to enter new tasks
        self.text = Text(self.root, bd=3, height=2, width=22, font=('Times New Roman', 20))
        self.text.place(x=25, y=100)

        # Add Button
        self.button = Button(self.root, text='Add', font=('Times New Roman', 20),
                             width=10, bd=5, bg='white', fg='black', command=self.add)
        self.button.place(x=30, y=180)

        # Delete Button
        self.button2 = Button(self.root, text='Delete', font=('Times New Roman', 20),
                              width=10, bd=5, bg='white', fg='black', command=self.delete)
        self.button2.place(x=30, y=240)

        # Update Button
        self.button3 = Button(self.root, text='Update', font=('Times New Roman', 20),
                              width=10, bd=5, bg='white', fg='black', command=self.update)
        self.button3.place(x=30, y=300)

        # Load existing tasks from the file
        self.load_tasks()

    def add(self):
        content = self.text.get(1.0, END).strip()  # Get the task content
        if content:  # Check if content is not empty
            self.main_text.insert(END, content)  # Insert into Listbox
            self.write_to_file(content)  # Write task to file
            self.text.delete(1.0, END)  # Clear the text field
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete(self):
        delete_index = self.main_text.curselection()  # Get the selected item
        if delete_index:  # If an item is selected
            task_to_delete = self.main_text.get(delete_index)  # Get the task text
            if self.delete_from_file(task_to_delete):  # If task deleted successfully from file
                self.main_text.delete(delete_index)  # Delete the selected item from Listbox
            else:
                messagebox.showwarning("Deletion Error", "Task not found in file.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update(self):
        update_index = self.main_text.curselection()  # Get the selected item
        if update_index:  # If an item is selected
            new_task = self.text.get(1.0, END).strip()  # Get the new task content and strip it of leading/trailing whitespace
            if new_task:  # If new task content is provided
                old_task = self.main_text.get(update_index)  # Get the old task
                if self.update_task_in_file(old_task, new_task):  # Update task in file
                    self.main_text.delete(update_index)  # Remove the old task from the Listbox
                    self.main_text.insert(update_index, new_task)  # Insert the new task into Listbox
                    self.text.delete(1.0, END)  # Clear the text field
                else:
                    messagebox.showwarning("Update Error", "Task not found in file.")
            else:
                messagebox.showwarning("Input Error", "Please enter a new task.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def write_to_file(self, content):
        try:
            with open('data.txt', 'a') as file:
                file.write(content + "\n")  # Write task to file
        except Exception as e:
            messagebox.showerror("File Error", f"Error writing to file: {e}")

    def delete_from_file(self, task_to_delete):
        try:
            with open('data.txt', 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                task_found = False
                for line in lines:
                    if line.strip() == task_to_delete:
                        task_found = True
                    else:
                        file.write(line)
                file.truncate()
                return task_found
        except Exception as e:
            messagebox.showerror("File Error", f"Error reading or writing to file: {e}")
            return False

    def update_task_in_file(self, old_task, new_task):
        try:
            with open('data.txt', 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                task_found = False
                for line in lines:
                    if line.strip() == old_task:
                        file.write(new_task + "\n")  # Update task in file
                        task_found = True
                    else:
                        file.write(line)
                file.truncate()
                return task_found
        except Exception as e:
            messagebox.showerror("File Error", f"Error updating file: {e}")
            return False

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    self.main_text.insert(END, line.strip())
        except FileNotFoundError:
            pass


def main():
    root = Tk()
    ui = TodoApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
