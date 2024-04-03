# managers/note_manager.py
from datetime import datetime
from typing import List
from models.note import Note
from storages.json_storage import JsonStorage
from storages.csv_storage import CsvStorage

class NoteManager:
    def __init__(self, json_file_path: str = 'notes.json', csv_file_path: str = 'notes.csv') -> None:
        self.json_storage = JsonStorage(json_file_path)
        self.csv_storage = CsvStorage(csv_file_path)
        self.notes = self.load_notes()

    def load_notes(self) -> List[Note]:
        notes_json = self.json_storage.load()
        notes = [Note(title=note['title'], content=note['content'], id=note['id'], last_modified=datetime.fromisoformat(note['last_modified'])) for note in notes_json]
        return notes

    def create_note(self, title: str, content: str) -> None:
        note = Note(title=title, content=content)
        self.notes.append(note)
        self.save_notes()


    def edit_note(self, note_id: str, new_title: str, new_content: str) -> None:
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.content = new_content
                note.last_modified = datetime.now()
                self.save_notes()
                return
        raise ValueError("Note ID not found.")

    def delete_note(self, note_id: str) -> None:
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

    def list_notes(self) -> None:
        for note in self.notes:
            print(f"ID: {note.id}, Title: {note.title}, Last Modified: {note.last_modified.strftime('%Y-%m-%d %H:%M:%S')}")

    def save_notes(self) -> None:
        self.json_storage.save([note.to_json() for note in self.notes])
        self.csv_storage.save([note.to_csv() for note in self.notes])
