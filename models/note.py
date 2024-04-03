from dataclasses import dataclass, asdict
from datetime import datetime
import json

@dataclass
class Note:
    id: str
    title: str
    content: str
    last_modified: datetime

    def to_json(self) -> str:
        return json.dumps(asdict(self), default=str)

    def to_csv(self) -> str:
        return f'{self.id};{self.title};{self.content};{self.last_modified.isoformat()}'
