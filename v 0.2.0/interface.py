import tkinter as tk
from tkinter import messagebox, ttk

from task import Task


class AppButton(ttk.Button):
    """Кнопка интерфейса приложения."""


class AppEntry(ttk.Entry):
    """Поле ввода интерфейса приложения."""


class AppLabel(ttk.Label):
    """Текстовая подпись интерфейса приложения."""


class AppListbox(tk.Listbox):
    """Список задач с поддержкой выделения."""


class Interface:
    """Окна и виджеты. Действия передаются фасаду через callbacks."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Менеджер задач")
        self.root.geometry("760x500")
        self.root.minsize(620, 420)
        self.on_add = lambda: None
        self.on_update = lambda task_id: None
        self.on_delete = lambda task_id: None
        self.on_toggle = lambda task_id: None
        self._tasks: list[Task] = []
        self._make_layout()

    def connect(self, *, add, update, delete, toggle) -> None:
        self.on_add, self.on_update = add, update
        self.on_delete, self.on_toggle = delete, toggle

    def _make_layout(self) -> None:
        frame = ttk.Frame(self.root, padding=16)
        frame.pack(fill="both", expand=True)
        AppLabel(frame, text="Менеджер задач", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        AppLabel(frame, text="Добавляйте задачи, отмечайте выполнение и сохраняйте список.").pack(anchor="w", pady=(2, 12))

        form = ttk.LabelFrame(frame, text="Новая задача", padding=10)
        form.pack(fill="x", pady=(0, 12))
        AppLabel(form, text="Название").grid(row=0, column=0, sticky="w")
        self.title_var = tk.StringVar()
        self.title_entry = AppEntry(form, textvariable=self.title_var)
        self.title_entry.grid(row=0, column=1, sticky="ew", padx=(8, 0))
        AppLabel(form, text="Автор").grid(row=1, column=0, sticky="w", pady=(8, 0))
        self.author_var = tk.StringVar()
        AppEntry(form, textvariable=self.author_var).grid(row=1, column=1, sticky="ew", padx=(8, 0), pady=(8, 0))
        AppLabel(form, text="Описание").grid(row=2, column=0, sticky="nw", pady=(8, 0))
        self.description = tk.Text(form, height=3, wrap="word")
        self.description.grid(row=2, column=1, sticky="ew", padx=(8, 0), pady=(8, 0))
        form.columnconfigure(1, weight=1)
        AppButton(form, text="Добавить задачу", command=self._add_clicked).grid(row=3, column=1, sticky="e", pady=(8, 0))

        listing = ttk.LabelFrame(frame, text="Список задач", padding=8)
        listing.pack(fill="both", expand=True)
        self.listbox = AppListbox(listing, height=10, activestyle="dotbox", exportselection=False)
        scroll = ttk.Scrollbar(listing, orient="vertical", command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scroll.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        scroll.pack(side="left", fill="y")
        buttons = ttk.Frame(listing)
        buttons.pack(side="left", fill="y", padx=(10, 0))
        AppButton(buttons, text="Выполнено / вернуть", command=self._toggle_clicked).pack(fill="x", pady=(0, 6))
        AppButton(buttons, text="Изменить название", command=self._edit_clicked).pack(fill="x", pady=6)
        AppButton(buttons, text="Удалить", command=self._delete_clicked).pack(fill="x", pady=6)
        self.status = AppLabel(frame, text="")
        self.status.pack(anchor="w", pady=(8, 0))

    def _selected(self) -> Task | None:
        selection = self.listbox.curselection()
        return self._tasks[selection[0]] if selection and selection[0] < len(self._tasks) else None

    def _add_clicked(self) -> None:
        title = self.title_var.get().strip()
        if not title:
            messagebox.showwarning("Нужно название", "Введите название задачи.", parent=self.root)
            self.title_entry.focus_set()
            return
        self.on_add(title, self.description.get("1.0", "end-1c").strip(), self.author_var.get().strip())
        self.title_var.set("")
        self.description.delete("1.0", "end")
        self.title_entry.focus_set()

    def _toggle_clicked(self) -> None:
        task = self._selected()
        if task:
            self.on_toggle(task.id)

    def _delete_clicked(self) -> None:
        task = self._selected()
        if task and messagebox.askyesno("Удалить задачу", f"Удалить «{task.title}»?", parent=self.root):
            self.on_delete(task.id)

    def _edit_clicked(self) -> None:
        task = self._selected()
        if not task:
            return
        dialog = tk.Toplevel(self.root)
        dialog.title("Изменить название")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.resizable(False, False)
        ttk.Label(dialog, text="Название задачи:").pack(anchor="w", padx=12, pady=(12, 4))
        value = tk.StringVar(value=task.title)
        entry = AppEntry(dialog, textvariable=value, width=44)
        entry.pack(padx=12, pady=4)
        entry.focus_set()
        def save() -> None:
            title = value.get().strip()
            if not title:
                messagebox.showwarning("Нужно название", "Название не может быть пустым.", parent=dialog)
                return
            self.on_update(task.id, title)
            dialog.destroy()
        entry.bind("<Return>", lambda _event: save())
        ttk.Button(dialog, text="Сохранить", command=save).pack(anchor="e", padx=12, pady=12)

    def show_tasks(self, tasks: list[Task]) -> None:
        self._tasks = list(tasks)
        self.listbox.delete(0, "end")
        for task in self._tasks:
            mark = "✓" if task.status == "Выполнена" else "○"
            self.listbox.insert("end", f"{mark}  {task.title}    [{task.status}]    {task.author}")
        self.status.configure(text=f"Всего задач: {len(self._tasks)}")

    def ask_confirm(self, title: str, message: str) -> bool:
        return messagebox.askyesno(title, message, parent=self.root)
