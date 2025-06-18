# 🗂️ AutoOrganizer

**AutoOrganizer** is a simple yet powerful Python CLI tool that auto-sorts files in a specified folder into categorized subfolders (like `doc/`, `pic/`, `audio/`, `video/`, `archive/`, or based on custom mappings in your `extensions.py`).

---

## 🔧 Features

- Automatically detects file types using extension lists:
  - **Documents**, **Images**, **Audio**, **Video**, **Archives**
  - Other types mapped via `extn` dictionary
  - Unrecognized extensions placed in `Other Files/`
- Creates categorized folders as needed
- Handles mixed-case extensions (e.g. `.JPG`, `.Pdf`)
- Works on **Windows**, **macOS**, and **Linux**

---

## ⚙️ Requirements

- Python 3.6+
- Standard library modules: `os`, `sys`, `shutil`
- Your project files:
```
  project_folder/
  ├── AutoOrganizer.py
  └── extensions.py
```
---
## 🛠️ Installation
1. Clone the repository:
```
    git clone URL
    cd File-Organizer
```
2. (Optional) Set up a virtual environment:
```
    python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3, No extra dependencies—just Python.

---
## 🚀 Usage
```
    python main.py <path_to_your_folder>
```
---
## 📄 Example
Say you have:
```
Downloads/
├── report.pdf
├── photo.JPG
├── song.mp3
├── video.mp4
├── archive.zip
├── script.py
└── notes.TXT
```
Running:
```
    python main.py Downloads
```
Will reorganize into:
```
Downloads/
├── doc/
│   ├── report.pdf
│   └── notes.TXT
├── pic/
│   └── photo.JPG
├── audio/
│   └── song.mp3
├── video/
│   └── video.mp4
├── archive/
│   └── archive.zip
├── Python Script/
│   └── script.py
└── Other Files/
```

---
## 🧩 Customization
- Edit `extensions.py` to adjust or add file types.

- Folder names derive from the lists `doc`, `pic`, `audi`, `video`, `archive` and the keys of `extn`.

- Unmapped types go to `Other Files/`.

---
## 🧪 Testing
1. Make a test directory with dummy files (e.g. `.docx`, .`exe`, `.mp4`, `.bmp`, `.rar`)

2. Run the organizer against it

3. Verify files are moved into the right folders

---
## ❗ Troubleshooting
- **FileNotFoundError** — Check your startup path; use absolute paths or `cd` into the correct directory.
- **PermissionError** — Ensure Python has rights to read/write in the folder.
- **Name collisions** — Duplicate filenames may get overwritten. You might add timestamp or numbering logic if needed.

---
## ✅ Contributing

Contributions welcome! Whether it’s better extensions, GUI, packaging improvements, or recursion support—feel free to submit an issue or pull request.
