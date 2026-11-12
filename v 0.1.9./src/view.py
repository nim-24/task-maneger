import tkinter as tk
from tkinter import messagebox

from Interface import Interface
from storage import load_tasks, save_tasks


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.tasks = load_tasks()
        self.interface = Interface(root, self)
        self.refresh_tasks()

    def refresh_tasks(self):
        self.interface.show_tasks(self.tasks)

    def add_task(self):
        task = self.interface.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Ошибка", "Введите задачу")
            return

        self.tasks.append(task)
        save_tasks(self.tasks)
        self.interface.task_entry.delete(0, tk.END)
        self.refresh_tasks()

    def edit_task(self):
        old_task = self.interface.selected_task()
        new_task = self.interface.update_entry.get().strip()

        if old_task is None:
            messagebox.showwarning("Ошибка", "Сначала выберите задачу в списке")
            return
        if not new_task:
            messagebox.showwarning("Ошибка", "Введите новый текст задачи")
            return

        index = self.tasks.index(old_task)
        self.tasks[index] = new_task
        save_tasks(self.tasks)
        self.interface.update_entry.delete(0, tk.END)
        self.refresh_tasks()

    def delete_task(self):
        task = self.interface.selected_task()
        if task is None:
            messagebox.showwarning("Ошибка", "Сначала выберите задачу в списке")
            return

        self.tasks.remove(task)
        save_tasks(self.tasks)
        self.refresh_tasks()


def main():
    root = tk.Tk()
    TaskManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()
