import json
import os
import tempfile
from pathlib import Path

from task import Task


class StorageManager:
    """Читает и записывает задачи в JSON-файл."""

    def __init__(self, path: str | Path = "data/tasks.json") -> None:
        self.path = Path(path)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            if not isinstance(raw, list):
                raise ValueError("Корень JSON должен быть списком")
            return [Task.from_dict(item) for item in raw]
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"Не удалось прочитать {self.path}: {exc}") from exc

    def save(self, tasks: list[Task]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps([task.to_dict() for task in tasks], ensure_ascii=False, indent=2)
        temp_name = None
        try:
            with tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", dir=self.path.parent,
                delete=False, suffix=".tmp"
            ) as temp:
                temp.write(payload)
                temp_name = temp.name
            os.replace(temp_name, self.path)
        finally:
            if temp_name and os.path.exists(temp_name):
                os.unlink(temp_name)
