import json
from datetime import datetime

class NotesApp:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.load_notes_from_file()

    def save_notes_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.notes, file, ensure_ascii=False, indent=2)

    def load_notes_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def display_notes(self):
        for note in self.notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Body: {note['body']}, Created at: {note['created_at']}")

    def add_note(self, title, body):
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'body': body,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes.append(note)
        print("Note added successfully!")
        self.save_notes_to_file()

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = title
                note['body'] = body
                note['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Note edited successfully!")
                self.save_notes_to_file()
                return
        print("Note not found.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                self.notes.remove(note)
                print("Note deleted successfully!")
                self.save_notes_to_file()
                return
        print("Note not found.")

    def filter_notes_by_date(self, date):
        filtered_notes = [note for note in self.notes if note['created_at'].startswith(date)]
        for note in filtered_notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Body: {note['body']}, Created at: {note['created_at']}")


if __name__ == "__main__":
    app = NotesApp()

    while True:
        print("\nOptions:")
        print("1. Display all notes")
        print("2. Add a new note")
        print("3. Edit a note")
        print("4. Delete a note")
        print("5. Filter notes by date")
        print("6. Save notes to file")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            app.display_notes()
        elif choice == '2':
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            app.add_note(title, body)
        elif choice == '3':
            note_id = int(input("Enter note ID to edit: "))
            title = input("Enter new note title: ")
            body = input("Enter new note body: ")
            app.edit_note(note_id, title, body)
        elif choice == '4':
            note_id = int(input("Enter note ID to delete: "))
            app.delete_note(note_id)
        elif choice == '5':
            date = input("Enter date (YYYY-MM-DD): ")
            app.filter_notes_by_date(date)
        elif choice == '6':
            app.save_notes_to_file()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")
