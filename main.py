import argparse
from managers.note_manager import NoteManager

def main():
    manager = NoteManager()

    parser = argparse.ArgumentParser(description="Управление заметками")
    parser.add_argument('--create', nargs=2, help='Создать заметку. Аргументы: заголовок, содержание')
    parser.add_argument('--edit', nargs=3, help='Редактировать заметку. Аргументы: id, новый заголовок, новое содержание')
    parser.add_argument('--delete', help='Удалить заметку по id')
    parser.add_argument('--list', action='store_true', help='Показать все заметки')

    args = parser.parse_args()

    if args.create:
        title, content = args.create
        manager.create_note(title, content)
        print("Заметка создана.")

if __name__ == "__main__":
    main()
