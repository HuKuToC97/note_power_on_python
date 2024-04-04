# main.py
import sys
import re
from typing import List
from exceptions import NoteNotFoundException
from managers.note_manager import NoteManager

class NoteApp:
    """Класс приложения для управления заметками через консольный интерфейс.

    Атрибуты:
        manager (NoteManager): Менеджер заметок для выполнения операций.
    """
    def __init__(self) -> None:
        """Инициализация приложения с созданием экземпляра менеджера заметок."""
        self.manager = NoteManager()

    def setup_argparse(self) -> None:
        """Отображает доступные команды и примеры их использования."""
        print("Доступные команды: create, edit, delete, list, exit\n Важно использовать одинарные ковычки там где это указывается")
        print("Примеры использования:")
        print("  - Создать заметку: create 'Заголовок' 'Содержимое'")
        print("  - Редактировать заметку: edit 'ID' 'Новый заголовок' 'Новое содержимое'")
        print("  - Удалить заметку: delete 'ID'")
        print("  - Показать все заметки: list")
        print("  - Показать заметку: show 'ID'")
        print("  - Справка: help")
        print("  - Выйти: exit")

    def process_command(self, command: str, arguments: str) -> None:
        """Обрабатывает команды, введенные пользователем.

        Аргументы:
            command (str): Команда, введенная пользователем.
            arguments (str): Строка аргументов команды.
        """
        args = re.findall(r"'([^']*)'", arguments)
        try:
            if command == 'create' and len(args) == 2:
                title, content = args
                self.manager.create_note(title, content)
                print("Заметка успешно создана.")
            elif command == 'edit' and len(args) == 3:
                note_id, new_title, new_content = args
                self.manager.edit_note(note_id, new_title, new_content)
                print("Заметка успешно отредактирована.")
            elif command == 'delete' and len(args) == 1:
                self.manager.delete_note(args[0])
                print("Заметка успешно удалена.")
            elif command == 'list':
                self.manager.list_notes()
            elif command == 'show' and len(args) == 1:
                self.manager.show_note(args[0])
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
                user_input = input("\nВведите команду: ").strip().split(' ', 1)
                command = user_input[0]
                arguments = user_input[1] if len(user_input) > 1 else ''
                self.process_command(command, arguments)
            except IndexError as e:
                print(f"Ошибка обработки команды: {e}")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    app = NoteApp()
    app.run()
