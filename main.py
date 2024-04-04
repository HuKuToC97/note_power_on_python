# main.py
from typing import List
import sys
from exceptions import NoteNotFoundException
from managers.note_manager import NoteManager

class NoteApp:
    def __init__(self) -> None:
        self.manager = NoteManager()

    def setup_argparse(self) -> None:
        """Отображает доступные команды и примеры их использования."""
        print("Доступные команды: create, edit, delete, list, exit")
        print("Примеры использования:")
        print("  - Создать заметку: create 'Заголовок' 'Содержимое'")
        print("  - Редактировать заметку: edit 'ID' 'Новый заголовок' 'Новое содержимое'")
        print("  - Удалить заметку: delete 'ID'")
        print("  - Показать все заметки: list")
        print("  - Показать заметку: show 'ID'")
        print("  - Справка: help")
        print("  - Выйти: exit")

    def process_command(self, command: str, arguments: List[str]) -> None:
        """Обрабатывает команды, введенные пользователем."""
        try:
            if command == 'create' and len(arguments) >= 2:
                title, content = arguments[0], ' '.join(arguments[1:])
                self.manager.create_note(title, content)
                print("Заметка успешно создана.")
            elif command == 'edit' and len(arguments) >= 3:
                note_id, new_title, new_content = arguments[0], arguments[1], ' '.join(arguments[2:])
                self.manager.edit_note(note_id, new_title, new_content)
                print("Заметка успешно отредактирована.")
            elif command == 'delete' and len(arguments) == 1:
                self.manager.delete_note(arguments[0])
                print("Заметка успешно удалена.")
            elif command == 'list':
                self.manager.list_notes()
            elif command == 'show' and len(arguments) == 1:
                self.manager.show_note(arguments[0])
            elif command == 'help':
                self.setup_argparse()
            elif command == 'exit':
                print("Завершение работы программы.")
                sys.exit(0)
            else:
                print("Неизвестная команда или некорректные аргументы. Попробуйте еще раз.")
        except NoteNotFoundException as e:
            print(f"Ошибка: {e}. Проверьте ID заметки.")
        except FileNotFoundError:
            print("Ошибка: Файл данных не найден.")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

    def run(self) -> None:
        """Запускает приложение, обрабатывая пользовательский ввод."""
        self.setup_argparse()
        while True:
            try:
                user_input = input("\nВведите команду: ").strip().split(maxsplit=1)
                command = user_input[0]
                arguments = user_input[1].split(' ') if len(user_input) > 1 else []
                self.process_command(command, arguments)
            except IndexError as e:
                print(f"Ошибка обработки команды: {e}")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    app = NoteApp()
    app.run()
