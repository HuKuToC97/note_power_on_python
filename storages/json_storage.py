# storages/json_storage.py
import json
from typing import List

class JsonStorage:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def save(self, data: List[dict]) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
                
    def load(self) -> List[dict]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Возвращает пустой список, если файл не существует

