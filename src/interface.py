import tkinter as tk

from AppButton import AppButton
from AppLabel import AppLabel
from AppListbox import AppListbox


class Interface:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Task Manager")
        self.root.geometry("620x620")
        self.root.config(bg="#f0f0f0")

        AppLabel(root, "Введите задачу:").pack(padx=20, pady=(15, 4), fill="x")
        self.task_entry = tk.Entry(root, font=("Arial", 11))
        self.task_entry.pack(padx=20, fill="x")
        self.task_entry.bind("<Return>", lambda event: app.add_task())

        AppLabel(root, "Новая задача для замены:").pack(
            padx=20, pady=(10, 4), fill="x"
        )
        self.update_entry = tk.Entry(root, font=("Arial", 11))
        self.update_entry.pack(padx=20, fill="x")

        AppLabel(root, "Список задач (выберите задачу для изменения или удаления):").pack(
            padx=20, pady=(12, 4), fill="x"
        )
        self.task_list = AppListbox(root)
        self.task_list.pack(padx=20, pady=4, fill="both", expand=True)

        buttons = tk.Frame(root, bg="#f0f0f0")
        buttons.pack(pady=8)
        AppButton(buttons, "Добавить задачу", app.add_task).grid(row=0, column=0, padx=5, pady=4)
        AppButton(buttons, "Изменить выбранную", app.edit_task).grid(row=0, column=1, padx=5, pady=4)
        AppButton(buttons, "Удалить выбранную", app.delete_task).grid(row=1, column=0, padx=5, pady=4)
        AppButton(buttons, "Обновить список", app.refresh_tasks).grid(row=1, column=1, padx=5, pady=4)

    def show_tasks(self, tasks):
        self.task_list.show_tasks(tasks)

    def selected_task(self):
        return self.task_list.get_selected_task()
