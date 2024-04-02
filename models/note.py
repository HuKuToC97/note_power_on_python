from dataclasses import dataclass, asdict
import datetime
import json

@dataclass
class Note:
    id: str
    title: str
    content: str
    last_modified: datetime.datetime

    def to_json(self):
        return json.dumps(asdict(self), default=str)

    def to_csv(self):
        return f'{self.id};{self.title};{self.content};{self.last_modified.isoformat()}'
