from dataclasses import asdict
from datetime import datetime
from typing import List, Optional
import uuid
from models.note import Note
from storages.json_storage import JsonStorage
from storages.csv_storage import CsvStorage

class NoteManager:
    def __init__(self, json_file_path: str = 'notes.json', csv_file_path: str = 'notes.csv') -> None:
        self.json_storage: JsonStorage = JsonStorage(json_file_path)
        self.csv_storage: CsvStorage = CsvStorage(csv_file_path)
        self.notes: List[Note] = self.load_notes()

    def generate_id(self) -> str:
        return str(uuid.uuid4())

    def load_notes(self) -> List[Note]:
        notes_json: List[dict] = self.json_storage.load()
        return [Note(**note) for note in notes_json]

    def create_note(self, title: str, content: str) -> None:
        note: Note = Note(id=self.generate_id(), title=title, content=content, last_modified=datetime.now())
        self.notes.append(note)
        self.save_notes()

    def save_notes(self) -> None:
        notes_dict: List[dict] = [asdict(note) for note in self.notes]
        self.json_storage.save(notes_dict)
        self.csv_storage.save([note.to_csv() for note in self.notes])

    def read_notes(self, date_filter: Optional[str] = None) -> List[Note]:
        if date_filter:
            filter_date: datetime = datetime.strptime(date_filter, "%Y-%m-%d").date()
            return [note for note in self.notes if note.last_modified.date() == filter_date]
        return self.notes

    def edit_note(self, note_id: str, new_title: Optional[str] = None, new_content: Optional[str] = None) -> Optional[Note]:
        for note in self.notes:
            if note.id == note_id:
                if new_title is not None:
                    note.title = new_title
                if new_content is not None:
                    note.content = new_content
                note.last_modified = datetime.now()
                self.save_notes()
                return note
        return None

    def delete_note(self, note_id: str) -> None:
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()
