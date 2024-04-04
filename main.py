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
        """Отображает доступные команды и примеры их использования, включая сортировку списка заметок."""
        print("Доступные команды: create, edit, delete, list, show, help, exit\nВажно использовать одинарные кавычки там, где это указывается")
        print("Примеры использования:")
        print("  - Создать заметку: create 'Заголовок' 'Содержимое'")
        print("  - Редактировать заметку: edit 'ID' 'Новый заголовок' 'Новое содержимое'")
        print("  - Удалить заметку: delete 'ID'")
        print("  - Показать все заметки: list")
        print("    - Показать все заметки, отсортированные по дате создания: list sort create")
        print("    - Показать все заметки, отсортированные по дате последнего изменения: list sort modif")
        print("    - Показать все заметки в обратном порядке: list sort create r или list sort modif r")
        print("  - Показать заметку: show 'ID'")
        print("  - Справка: help")
        print("  - Выйти: exit\n")
        print("\n!!!ВАЖНО использовать одинарные кавычки там, где это указывается\n")

    def process_command(self, command: str, arguments: str) -> None:
        """Обрабатывает команды, введенные пользователем.

        Аргументы:
            command (str): Команда, введенная пользователем.
            arguments (str): Строка аргументов команды.
        """
        # Извлекаем аргументы команды, заключенные в одиночные кавычки
        args = re.findall(r"'([^']*)'", arguments)

        # Добавляем разделение на части для всей команды, чтобы корректно обрабатывать аргументы сортировки
        full_command = command.split() + arguments.split()
        base_command = full_command[0]

        sort_type = None
        reverse = False

        # Определяем аргументы сортировки
        if 'sort' in full_command:
            if 'create' in full_command:
                sort_type = 'create'
                reverse = 'r' not in full_command
            elif 'modif' in full_command:
                sort_type = 'modif'
                reverse = 'r' not in full_command

        try:
            if base_command == 'create' and len(args) == 2:
                title, content = args
                self.manager.create_note(title, content)
                print("Заметка успешно создана.")
            elif base_command == 'edit' and len(args) == 3:
                note_id, new_title, new_content = args
                self.manager.edit_note(note_id, new_title, new_content)
                print("Заметка успешно отредактирована.")
            elif base_command == 'delete' and len(args) == 1:
                self.manager.delete_note(args[0])
                print("Заметка успешно удалена.")
            elif base_command == 'list':
                # Вызываем метод list_notes с учетом аргументов сортировки
                self.manager.list_notes(sort=sort_type, reverse=reverse)
            elif base_command == 'show' and len(args) == 1:
                self.manager.show_note(args[0])
            elif base_command == 'help':
                self.setup_argparse()
            elif base_command == 'exit':
                print("Завершение работы программы.")
                sys.exit(0)
            else:
                print("Неизвестная команда или некорректные аргументы. Попробуйте еще раз.\nВажно использовать одинарные кавычки там, где это требуется")
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
