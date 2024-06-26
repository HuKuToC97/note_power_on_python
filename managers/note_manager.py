# managers/note_manager.py
from datetime import datetime
from typing import List, Optional
from models.note import Note
from storages.json_storage import JsonStorage
from storages.csv_storage import CsvStorage
from exceptions import NoteNotFoundException

class NoteManager:
    """Менеджер заметок, отвечающий за управление заметками.

    Атрибуты:
        json_storage (JsonStorage): Хранилище для заметок в формате JSON.
        csv_storage (CsvStorage): Хранилище для заметок в формате CSV.
        notes (List[Note]): Список заметок.
    """
    def __init__(self, json_file_path: str = 'notes.json', csv_file_path: str = 'notes.csv') -> None:
        self.json_storage = JsonStorage(json_file_path)
        self.csv_storage = CsvStorage(csv_file_path)
        self.notes = self.load_notes()

    def load_notes(self) -> List[Note]:
        notes_json = self.json_storage.load()
        notes = [Note.from_json(note) for note in notes_json]
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
        raise NoteNotFoundException(f"Заметка с ID {note_id} не найдена.")

    def delete_note(self, note_id: str) -> None:
        if not any(note.id == note_id for note in self.notes):
            raise NoteNotFoundException(f"Заметка с ID {note_id} не найдена.")
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

    def list_notes(self, sort: Optional[str] = None, reverse: bool = False) -> None:
        """Выводит список заметок с возможной сортировкой.

        Аргументы:
            sort (Optional[str]): Критерий сортировки ('create' или 'modif').
            reverse (bool): Флаг для сортировки по убыванию.
        """
        if sort == 'create':
            sorted_notes = sorted(self.notes, key=lambda note: note.create_date, reverse=reverse)
        elif sort == 'modif':
            sorted_notes = sorted(self.notes, key=lambda note: note.last_modified, reverse=reverse)
        else:
            sorted_notes = self.notes

        for note in sorted_notes:
            print(f"ID: {note.id}, Title: {note.title}, Created: {note.create_date.strftime('%Y-%m-%d %H:%M:%S')}, Last Modified: {note.last_modified.strftime('%Y-%m-%d %H:%M:%S')}")

    def save_notes(self) -> None:
        self.json_storage.save([note.to_json() for note in self.notes])
        self.csv_storage.save([note.to_csv() for note in self.notes])
    
    def show_note(self, note_id: str) -> None:
        for note in self.notes:
            if note.id == note_id:
                print(f"Title: {note.title}\nContent:\n{note.content}")
                return
        raise NoteNotFoundException(f"Заметка с ID {note_id} не найдена.")

