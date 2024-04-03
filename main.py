# main.py
import sys
from typing import List
from managers.note_manager import NoteManager

class NoteApp:
    def __init__(self) -> None:
        self.manager = NoteManager()

    def setup_argparse(self) -> None:
        print("Доступные команды: create, edit, delete, list, exit")
        print("Примеры использования:")
        print("  - Создать заметку: create 'Заголовок' 'Содержимое'")
        print("  - Редактировать заметку: edit 'ID' 'Новый заголовок' 'Новое содержимое'")
        print("  - Удалить заметку: delete 'ID'")
        print("  - Показать все заметки: list")
        print("  - Выйти: exit")

    def process_command(self, command: str, arguments: List[str]) -> None:
        try:
            if command == 'create' and len(arguments) >= 2:
                title = ' '.join(arguments[0].split()[1:-1])
                content = ' '.join(arguments[1].split()[1:-1])
                self.manager.create_note(title, content)
            elif command == 'edit' and len(arguments) >= 3:
                note_id, new_title, new_content = arguments
                self.manager.edit_note(note_id, new_title, new_content)
            elif command == 'delete' and len(arguments) == 1:
                self.manager.delete_note(arguments[0])
            elif command == 'list' and not arguments:
                self.manager.list_notes()
            elif command == 'exit':
                print("Завершение работы программы.")
                sys.exit(0)
            else:
                print("Неизвестная команда или некорректные аргументы. Попробуйте еще раз.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def run(self) -> None:
        self.setup_argparse()
        while True:
            user_input = input("\nВведите команду: ").strip().split()
            command, arguments = user_input[0], user_input[1:]
            self.process_command(command, arguments)

if __name__ == "__main__":
    app = NoteApp()
    app.run()
