import json

class JsonStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, data):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Ошибка сохранения в JSON: {e}")

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except IOError:
            return []  # Возвращает пустой список, если файл не существует
