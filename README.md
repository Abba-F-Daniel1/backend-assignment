# 📝 Note Keeper

A stylish and interactive note-taking application with both CLI and web terminal interfaces. Store your memories, thoughts, and notes with timestamps in a beautiful terminal-like environment.

## ✨ Features

### Command Line Interface (CLI)
- Interactive menu-driven interface
- Stylish ASCII art banners
- Loading animations
- Emoji-based UI elements
- Automatic timestamping
- File-based storage

### Web Terminal Interface
- Browser-based terminal experience
- Command history navigation (up/down arrows)
- Real-time command processing
- Responsive design
- Dark theme (Tokyo Night inspired)

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Flask (for web interface)
- Modern web browser (for web interface)

### Installation
 1. Clone the repository
```bash
   git clone https://github.com/Abba-F-Daniel1/backend-assignment/
cd note-keeper
```
2. Create a virtual environment
```bash
python -m venv .venv
On Windows
.venv\Scripts\activate
On macOS/Linux
source .venv/bin/activate
```
3. Install dependencies
```bash
pip install flask
```

## 💻 Usage

### CLI Version
Run the CLI version with:
```bash
python note_keeper.py
```

Available options:
- 1️⃣ Add a Memory
- 2️⃣ View Collection
- 3️⃣ Remove Note
- 4️⃣ Exit Keeper

### Web Version
Start the web server:
```bash
python web_app.py
```

Visit `http://localhost:5000` in your browser.

Available commands:
- `help` - Show available commands
- `add <note>` - Add a new note
- `list` - Show all notes
- `delete <number>` - Delete note by number
- `clear` - Clear the terminal

## 🗂️ Project Structure
```bash
note_keeper/
├── note_keeper.py # CLI version
├── web_app.py # Flask web application
├── notes.txt # Note storage
├── templates/
│ └── index.html # Web interface template
└── static/
├── css/
│ └── style.css # Terminal styling
└── js/
└── terminal.js # Terminal functionality
```

## 🎨 Features in Detail

### Note Management
- Automatic timestamping of notes
- Persistent storage in text file
- Sequential numbering
- Easy deletion by note number

### User Interface
- Clean and intuitive design
- Visual feedback for actions
- Error handling with friendly messages
- Loading animations
- Command history

### Storage
- File-based storage using `notes.txt`
- Each note includes timestamp
- Human-readable format

## 🛠️ Technical Details

### CLI Version
- Pure Python implementation
- Uses standard library modules
- Cross-platform compatibility
- Terminal-based UI

### Web Version
- Flask backend
- Vanilla JavaScript frontend
- Custom CSS styling
- RESTful API endpoints

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- Inspired by classic terminal applications
- Tokyo Night color scheme
- Terminal emoji art community

## 🔮 Future Enhancements
- [ ] User authentication
- [ ] Note categories
- [ ] Search functionality
- [ ] Cloud sync
- [ ] Rich text formatting
- [ ] Export/import capabilities

## 📫 Contact

Abba Daniel - [@frederickabba](https://twitter.com/frederickabba)

Project Link: [Note Keeper](https://github.com/Abba-F-Daniel1/backend-assignment/)
