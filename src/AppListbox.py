import tkinter as tk
class AppListbox(tk.Listbox):
    """Список задач с методами для отображения и выбора."""

    def __init__(self, master):
        super().__init__(
            master,
            width=50,
            height=12,
            bg="white",
            fg="black",
            selectbackground="#2878c8",
            font=("Arial", 11),
        )

    def show_tasks(self, tasks):
        self.delete(0, tk.END)
        for task in tasks:
            self.insert(tk.END, task)

    def get_selected_task(self):
        selection = self.curselection()
        if not selection:
            return None
        return self.get(selection[0])
