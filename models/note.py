# models/note.py
from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Note:
    title: str
    content: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    last_modified: datetime = field(default_factory=datetime.now)

    def to_json(self):
        return {
            'title': self.title,
            'content': self.content,
            'id': self.id,
            'last_modified': self.last_modified.isoformat()
        }

    def to_csv(self) -> str:
        return f"{self.id};{self.title};{self.content};{self.last_modified.isoformat()}"

    @staticmethod
    def from_json(data):
        return Note(
            title=data['title'],
            content=data['content'],
            id=data['id'],
            last_modified=datetime.fromisoformat(data['last_modified'])
        )
