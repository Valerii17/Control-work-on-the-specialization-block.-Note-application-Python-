import json
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def print_note(note):
    print("ID:", note["id"])
    print("Заголовок:", note["title"])
    print("Тело заметки:", note["body"])
    print("Дата/время создания:", note["created_at"])
    print("Дата/время последнего изменения:", note["updated_at"])
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    created_at = datetime.datetime.now().isoformat()
    updated_at = created_at
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "created_at": created_at,
        "updated_at": updated_at
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            print("Редактирование заметки:")
            print_note(note)
            note["title"] = input("Введите новый заголовок: ")
            note["body"] = input("Введите новое тело заметки: ")
            note["updated_at"] = datetime.datetime.now().isoformat()
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            print("Удаление заметки:")
            print_note(note)
            confirm = input("Вы уверены, что хотите удалить эту заметку? (y/n): ")
            if confirm.lower() == "y":
                notes.remove(note)
                save_notes(notes)
                print("Заметка успешно удалена")
            return
    print("Заметка с указанным ID не найдена")

def filter_notes_by_date():
    date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Неверный формат даты")
        return
    filtered_notes = [note for note in notes if note["created_at"].split("T")[0] == date_str]
    if len(filtered_notes) == 0:
        print("Заметки с указанной датой не найдены")
    else:
        print("Список заметок с датой", date_str + ":")
        for note in filtered_notes:
            print_note(note)

def print_all_notes():
    if len(notes) == 0:
        print("Список заметок пуст")
    else:
        print("Список всех заметок:")
        for note in notes:
            print_note(note)
            print()
