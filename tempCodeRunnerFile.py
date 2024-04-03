# main.py
import argparse
from managers.note_manager import NoteManager

def setup_argparse():
    parser = argparse.ArgumentParser(description="Управление заметками")
    parser.add_argument('--create', nargs=2, metavar=('TITLE', 'CONTENT'), help='Создать заметку')
    parser.add_argument('--edit', nargs=3, metavar=('ID', 'TITLE', 'CONTENT'), help='Редактировать заметку')
    parser.add_argument('--delete', metavar='ID', help='Удалить заметку по ID')
    parser.add_argument('--list', nargs='?', const='', metavar='[DATE_FILTER]', help='Список всех заметок, опционально с фильтрацией по дате')
    return parser.parse_args()

def main():
    args = setup_argparse()
    manager = NoteManager()

    if args.create:
        title, content = args.create
        manager.create_note(title, content)
        print("Заметка создана успешно.")
    elif args.edit:
        note_id, new_title, new_content = args.edit
        if manager.edit_note(note_id, new_title, new_content):
            print("Заметка обновлена успешно.")
        else:
            print("Заметка с таким ID не найдена.")
    elif args.delete:
        manager.delete_note(args.delete)
        print("Заметка удалена успешно.")
    elif args.list is not None:
        notes = manager.read_notes(args.list)
        for note in notes:
            print(f"ID: {note.id}, Заголовок: {note.title}, Содержание: {note.content}, Изменена: {note.last_modified}")

if __name__ == "__main__":
    main()
