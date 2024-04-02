from dataclasses import asdict
import uuid
from datetime import datetime
from models.note import Note
from storages.json_storage import JsonStorage
from storages.csv_storage import CsvStorage

class NoteManager:
    def __init__(self, json_file_path='notes.json', csv_file_path='notes.csv'):
        self.json_storage = JsonStorage(json_file_path)
        self.csv_storage = CsvStorage(csv_file_path)
        self.notes = self.load_notes()

    def generate_id(self):
        """Генерирует уникальный идентификатор для новой заметки."""
        return str(uuid.uuid4())

    def load_notes(self):
        """Загружает заметки из файла."""
        # Примерно так, но нужна обработка исключений и проверка существования файла
        notes_json = self.json_storage.load()
        return [Note(**note) for note in notes_json]

    def create_note(self, title, content):
        """Создает новую заметку и сохраняет ее."""
        note = Note(id=self.generate_id(), title=title, content=content, last_modified=datetime.now())
        self.notes.append(note)
        self.save_notes()

    def save_notes(self):
        """Сохраняет все заметки в файлы JSON и CSV."""
        notes_dict = [asdict(note) for note in self.notes]  
        self.json_storage.save(notes_dict)
        self.csv_storage.save([note.to_csv() for note in self.notes])

    def read_notes(self):
        """Возвращает список всех заметок."""
        return self.notes

    def edit_note(self, note_id, new_title=None, new_content=None):
        for note in self.notes:
            if note.id == note_id:
                if new_title:
                    note.title = new_title
                if new_content:
                    note.content = new_content
                note.last_modified = datetime.now()
                self.save_notes()
                return note
        return None

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

