# storages/json_storage.py
import json
from typing import List, Dict

class JsonStorage:
    """Класс для работы с хранилищем заметок в формате JSON.

    Атрибуты:
        file_path (str): Путь к файлу хранилища.
    """
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def save(self, data: List[Dict]) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load(self) -> List[Dict]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Возвращает пустой список, если файл не существует
