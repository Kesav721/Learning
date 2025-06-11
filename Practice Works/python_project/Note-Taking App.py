import json

NOTES_FILE = "notes.json"

def load_notes():
    """Load notes from a JSON file."""
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    """Save notes to a JSON file."""
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    """Add a new note."""
    note = input("Enter your note: ")
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Note added successfully!")

def view_notes():
    """Display all notes."""
    notes = load_notes()
    if not notes:
        print("No notes found.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

def delete_note():
    """Delete a note by index."""
    notes = load_notes()
    view_notes()
    
    try:
        index = int(input("Enter note number to delete: ")) - 1
        if 0 <= index < len(notes):
            del notes[index]
            save_notes(notes)
            print("Note deleted successfully!")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main menu for the Note-Taking App."""
    while True:
        print("\n📝 Note-Taking App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
