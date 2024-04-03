# storages/json_storage.py
import json
from typing import List, Any

class JsonStorage:
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path

    def save(self, data: List[Any]) -> None:
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Ошибка сохранения в JSON: {e}")

    def load(self) -> List[dict]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError):  # Обработка ошибки чтения файла или ошибки декодирования JSON
            return []  # Возвращает пустой список, если файл не существует или пустой
