from tkinter import *

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("650x410+300+150")

        self.setup_ui()
        self.load_tasks()

    def setup_ui(self):
        # UI Setup
        self.label = Label(self.root, text="To-Do List App", font='Arial 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.add_label = Label(self.root, text="Add Task", font='Arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.add_label.place(x=40, y=54)

        self.tasks_label = Label(self.root, text="Tasks", font='Arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.tasks_label.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font='Arial 20 bold')
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)

        self.add_button = Button(self.root, text="Add", font='Arial 20 bold italic', width=10, bd=5, bg='orange', fg='black', command=self.add_task)
        self.add_button.place(x=30, y=180)

        self.edit_button = Button(self.root, text="Edit", font='Arial 20 bold italic', width=10, bd=5, bg='orange', fg='black', command=self.edit_task)
        self.edit_button.place(x=30, y=230)

        self.delete_button = Button(self.root, text="Delete", font='Arial 20 bold italic', width=10, bd=5, bg='orange', fg='black', command=self.delete_task)
        self.delete_button.place(x=30, y=280)

    def load_tasks(self):
        try:
            with open('da.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            print("Data file not found.")

    def add_task(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('da.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)

    def edit_task(self):
        selection = self.main_text.curselection()
        if selection:
            index = selection[0]
            current_task = self.main_text.get(index)
            self.text.delete(1.0, END)
            self.text.insert(END, current_task)

            def save_edit():
                new_content = self.text.get(1.0, END).strip()
                if new_content:
                    self.main_text.delete(index)
                    self.main_text.insert(index, new_content)
                    with open('da.txt', 'r+') as file:
                        tasks = file.readlines()
                        file.seek(0)
                        tasks[index] = new_content + '\n'
                        file.writelines(tasks)
                        file.truncate()
                    edit_window.destroy()

            edit_window = Toplevel(self.root)
            edit_window.title("Edit Task")
            edit_window.geometry("300x150+500+200")

            edit_label = Label(edit_window, text="Edit Task", font='Arial 18 bold')
            edit_label.pack()

            save_button = Button(edit_window, text="Save", font='Arial 12', command=save_edit)
            save_button.pack()

    def delete_task(self):
        try:
            selection = self.main_text.curselection()
            if selection:
                index = selection[0]
                self.main_text.delete(index)
                with open('da.txt', 'r+') as file:
                    tasks = file.readlines()
                    file.seek(0)
                    for i, task in enumerate(tasks):
                        if i != index:
                            file.write(task)
                    file.truncate()
        except IndexError:
            pass

def main():
    root = Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
