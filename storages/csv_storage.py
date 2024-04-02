import csv

class CsvStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, data):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row.split(';'))  # Предполагается, что данные уже в формате CSV строки

    def load(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return list(csv.reader(file))
        except IOError:
            return []  # Аналогично JSON, возвращаем пустой список
