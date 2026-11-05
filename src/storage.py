import json
from pathlib import Path
TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Загружает задачи из JSON-файла."""
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
        return tasks if isinstance(tasks, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Сохраняет список задач в JSON-файл."""
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
