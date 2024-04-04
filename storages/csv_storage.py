# storages/csv_storage.py
import csv
from typing import List

class CsvStorage:
    """Класс для работы с хранилищем заметок в формате CSV.

    Атрибуты:
        file_path (str): Путь к файлу хранилища.
    """
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def save(self, data: List[str]) -> None:
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            for row in data:
                writer.writerow(row.split(';'))

    def load(self) -> List[List[str]]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return list(csv.reader(file, delimiter=';'))
        except FileNotFoundError:
            return []
