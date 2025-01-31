from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Reuse our existing note functions with slight modifications


def load_notes():
    if not os.path.exists("notes.txt"):
        return []
    with open("notes.txt", "r") as file:
        return [note.strip() for note in file.readlines()]


def save_notes(notes):
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")


def format_note(note):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"[{timestamp}] {note}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/command', methods=['POST'])
def handle_command():
    command = request.json.get('command', '').strip()

    if not command:
        return jsonify({"response": "Please enter a command."})

    parts = command.split(maxsplit=1)
    cmd = parts[0].lower()

    if cmd == "help":
        return jsonify({"response": """
Available commands:
  add <note>    - Add a new note
  list          - Show all notes
  delete <num>  - Delete note by number
  clear         - Clear the terminal
  help          - Show this help message
"""})

    elif cmd == "add" and len(parts) > 1:
        note = format_note(parts[1])
        notes = load_notes()
        notes.append(note)
        save_notes(notes)
        return jsonify({"response": "✨ Note added successfully! ✨"})

    elif cmd == "list":
        notes = load_notes()
        if not notes:
            return jsonify({"response": "📭 No notes found!"})
        response = "📚 Your Notes Collection:\n" + "═" * 50 + "\n"
        for i, note in enumerate(notes, 1):
            response += f"│ {i}. {note}\n"
        response += "═" * 50 + f"\nTotal Notes: {len(notes)}"
        return jsonify({"response": response})

    elif cmd == "delete" and len(parts) > 1:
        try:
            index = int(parts[1]) - 1
            notes = load_notes()
            if 0 <= index < len(notes):
                deleted = notes.pop(index)
                save_notes(notes)
                return jsonify({"response": f"🗑️ Deleted note: {deleted}"})
            return jsonify({"response": "❌ Invalid note number!"})
        except ValueError:
            return jsonify({"response": "⚠️ Please enter a valid number!"})

    elif cmd == "clear":
        return jsonify({"response": "clear"})

    return jsonify({"response": f"❌ Unknown command. Type 'help' for available commands."})


if __name__ == '__main__':
    app.run(debug=True)
