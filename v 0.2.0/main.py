import tkinter as tk
from uuid import uuid4

from interface import Interface
from storage_manager import StorageManager
from task import Task


class TaskManager:
    """Фасад CRUD и точка запуска графического приложения."""

    def __init__(self, interface: Interface, storage: StorageManager) -> None:
        self.interface = interface
        self.storage = storage
        try:
            self.tasks = self.storage.load()
        except ValueError as exc:
            self.tasks = []
            error_message = str(exc)
            self.interface.root.after(
                100,
                lambda message=error_message: self.interface.status.configure(text=message),
            )
        self.interface.connect(
            add=self.create_task,
            update=self.edit_task,
            delete=self.delete_task,
            toggle=self.toggle_status,
        )
        self._refresh()

    def _refresh(self) -> None:
        self.interface.show_tasks(self.tasks)

    def _save_and_refresh(self) -> None:
        save_error = None
        try:
            self.storage.save(self.tasks)
        except OSError as exc:
            save_error = f"Ошибка сохранения: {exc}"
        self._refresh()
        if save_error:
            self.interface.status.configure(text=save_error)

    def create_task(self, title: str, description: str = "", author: str = "") -> Task:
        task = Task(id=uuid4().hex, title=title, description=description,
                    author=author, created_at=Task.timestamp())
        self.tasks.append(task)
        self._save_and_refresh()
        return task

    def edit_task(self, task_id: str, title: str) -> bool:
        task = self._find(task_id)
        if not task:
            return False
        task.title = title
        self._save_and_refresh()
        return True

    def delete_task(self, task_id: str) -> bool:
        task = self._find(task_id)
        if not task:
            return False
        self.tasks.remove(task)
        self._save_and_refresh()
        return True

    def toggle_status(self, task_id: str) -> bool:
        task = self._find(task_id)
        if not task:
            return False
        task.status = "Выполнена" if task.status != "Выполнена" else "Новая"
        self._save_and_refresh()
        return True

    def run(self) -> None:
        self.interface.root.mainloop()

    def _find(self, task_id: str) -> Task | None:
        return next((task for task in self.tasks if task.id == task_id), None)


def main() -> None:
    root = tk.Tk()
    interface = Interface(root)
    manager = TaskManager(interface, StorageManager())
    manager.run()


if __name__ == "__main__":
    main()
