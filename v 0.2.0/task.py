from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass
class Task:
    """Одна задача в приложении."""

    id: str
    title: str
    description: str = ""
    status: str = "Новая"
    author: str = ""
    created_at: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        return cls(
            id=str(data["id"]),
            title=str(data["title"]),
            description=str(data.get("description", "")),
            status=str(data.get("status", "Новая")),
            author=str(data.get("author", "")),
            created_at=str(data.get("created_at", "")),
        )

    @staticmethod
    def timestamp() -> str:
        return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
