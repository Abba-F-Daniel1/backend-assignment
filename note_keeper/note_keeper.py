import os
import time
from datetime import datetime


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_banner():
    """Display a stylish banner"""
    banner = """
    ╔═══════════════════════════════════════╗
    ║           📝 NOTE KEEPER 📝           ║
    ║         Your Digital Memory Box       ║
    ╚═══════════════════════════════════════╝    
    """
    print(banner)


def show_loading_animation(duration=1):
    """Show a simple loading animation"""
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{animation[i]} Loading...", end="")
        time.sleep(0.1)
        i = (i + 1) % len(animation)
    print("\r" + " " * 20 + "\r", end="")


def format_note(note):
    """Format note with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"[{timestamp}] {note}"


def load_notes():
    """Load notes from file"""
    if not os.path.exists("notes.txt"):
        return []

    with open("notes.txt", "r") as file:
        notes = file.readlines()
    return [note.strip() for note in notes]


def save_notes(notes):
    """Save notes to file"""
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")


def add_note(note):
    """Add a new note"""
    notes = load_notes()
    formatted_note = format_note(note)
    notes.append(formatted_note)
    save_notes(notes)
    show_loading_animation(0.5)
    print("✨ Note added successfully! ✨")


def list_notes():
    """Display all notes"""
    notes = load_notes()
    if not notes:
        print("📭 No notes found! Your memory box is empty...")
        return

    print("\n📚 Your Notes Collection:")
    print("═" * 50)
    for index, note in enumerate(notes):
        print(f"│ {index + 1}. {note}")
    print("═" * 50)
    print(f"Total Notes: {len(notes)}")


def delete_note(index):
    """Delete a note by index"""
    notes = load_notes()
    if not notes:
        print("📭 No notes to delete!")
        return

    try:
        index = int(index) - 1
        if 0 <= index < len(notes):
            deleted_note = notes.pop(index)
            save_notes(notes)
            show_loading_animation(0.5)
            print(f"🗑️  Deleted note: {deleted_note}")
        else:
            print("❌ Invalid note index!")
    except ValueError:
        print("⚠️  Please enter a valid number!")


def show_menu():
    """Display the menu options"""
    menu = """
    🔸 1. Add a Memory    [📝]
    🔸 2. View Collection [📚]
    🔸 3. Remove Note     [❌]
    🔸 4. Exit Keeper    [👋]
    """
    print(menu)


def main():
    while True:
        clear_screen()
        show_banner()
        show_menu()

        choice = input("\n💫 What would you like to do? (1-4): ")

        if choice == "1":
            note = input("\n✏️  Enter your memory: ")
            add_note(note)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            list_notes()
            index = input("\n🔍 Enter note number to remove: ")
            delete_note(index)
        elif choice == "4":
            print("\n👋 Thank you for using Note Keeper! Goodbye!")
            time.sleep(1)
            clear_screen()
            break
        else:
            print("❌ Invalid choice! Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
