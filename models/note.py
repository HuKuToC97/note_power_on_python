# models/note.py
from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Note:
    """Класс, представляющий заметку.

    Атрибуты:
        title (str): Заголовок заметки.
        content (str): Содержание заметки.
        id (str): Уникальный идентификатор заметки.
        create_date (datetime): Дата создания заметки.
        last_modified (datetime): Дата последнего изменения заметки.
    """
    title: str
    content: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    create_date: datetime = field(default_factory=datetime.now)
    last_modified: datetime = field(default_factory=datetime.now)

    def to_json(self):
        """Сериализует объект в JSON."""
        return {
            'title': self.title,
            'content': self.content,
            'id': self.id,
            'create': self.create_date.isoformat(),
            'last_modified': self.last_modified.isoformat()
        }

    def to_csv(self) -> str:
        return f"{self.id};{self.title};{self.content};{self.create_date.isoformat()};{self.last_modified.isoformat()}"

    @staticmethod
    def from_json(data):
        """Создает объект из JSON."""
        return Note(
            title=data['title'],
            content=data['content'],
            id=data['id'],
            create_date=datetime.fromisoformat(data['create']),
            last_modified=datetime.fromisoformat(data['last_modified'])
        )

