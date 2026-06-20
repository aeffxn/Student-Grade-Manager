# 🎓 Student Grade Manager (v3)

![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?style=flat-square&logo=python&logoColor=black)
![GUI](https://img.shields.io/badge/GUI-Tkinter-black?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-black?style=flat-square)

A desktop GUI application for managing student records and grades, built with Python's standard `tkinter` library. This is the third and final version in a 3-part progression: **v1 (basic CLI)** → **v2 (OOP CLI)** → **v3 (GUI, you are here)**.

---

## 📑 Table of Contents

- [What's New in v3](#-whats-new-in-v3)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Design](#-design)
- [Why Tkinter](#-why-tkinter)
- [Possible Extensions](#-possible-extensions)

---

## ✨ What's New in v3

| | v2 | v3 |
|---|---|---|
| Interface | Command line | Tkinter GUI |
| File structure | One file | Split into `models.py`, `storage.py`, `app.py`, `main.py` |
| Data persistence | Plain text file | JSON file, loaded/saved automatically |
| Visual feedback | Printed text | Live-updating table + stat cards |
| Styling | None (terminal) | Custom black & yellow theme throughout |

---

## 🚀 Features

- ➕ **Add students** by name (duplicate names blocked)
- 📝 **Record marks** (0–100) per student, as many as you like
- 📊 **Automatic statistics** — average, highest, and lowest mark per student
- 🏆 **Class-wide stats panel** — top scorer, lowest scorer, and class average, updated live
- 💾 **Persistent storage** — all data saved to `students.json`, reloaded automatically next time
- 🗑️ **Delete students** with a confirmation prompt to prevent accidental data loss

---

## 📂 Project Structure

```
student_grade_manager/
├── main.py        # entry point — run this
├── app.py         # GUI layer (Tkinter), all widgets and event handlers
├── models.py      # Student data class — pure logic, no UI
├── storage.py     # JSON persistence — load/save, no UI
└── students.json  # auto-created on first save (gitignored)
```

The split between `models.py`, `storage.py`, and `app.py` is deliberate: the data model and persistence logic have zero dependency on Tkinter, so they could be unit tested or reused (e.g. swapped to a different UI, or a database backend) without touching the GUI code.

---

## 🛠 Requirements

- Python 3.8+
- `tkinter` — included with most Python installations

Check if you have Python:

```bash
python3 --version
```

Check if you have tkinter:

```bash
python3 -m tkinter
```

A small test window should pop up. If you get a `No module named tkinter` error:

| OS | Fix |
|---|---|
| Windows | Reinstall Python from python.org, make sure "tcl/tk and IDLE" is checked during setup |
| macOS | `brew install python-tk` |
| Ubuntu/Debian | `sudo apt install python3-tk` |
| Fedora | `sudo dnf install python3-tkinter` |

---

## 📦 Installation

```bash
git clone https://github.com/aeffxn/Student-Grade-Manager.git
cd student_grade_manager
python3 main.py
```

All four `.py` files must stay in the same folder — `app.py` imports from `models.py` and `storage.py` directly.

---

## ▶️ Usage

1. Type a student's name in the **Add / Update Student** panel and click **Add Student**.
2. Click that student's row in the table to select them.
3. Type a mark (0–100) and click **Add Mark to Selected** (or press Enter).
4. Repeat to add as many marks as needed — **Average**, **Highest**, and **Lowest** columns update automatically.
5. The stats cards at the bottom show the top scorer, lowest scorer, and class average across all students.
6. Data saves automatically when you close the window, and reloads next time you open the app.

---

## 🎨 Design

Black background with a single consistent yellow accent (`#FFC800`) used throughout — buttons, headings, table headers, and the selection highlight — instead of default OS theme colors. Hover and press states are handled manually for a deliberate, non-default look. The one exception is the delete button, which uses red to signal a destructive action. This theme was chosen because I really like it :)

---

## 🤔 Why Tkinter

This is a native desktop app on purpose. `tkinter` ships with Python, so there's nothing extra to install beyond Python itself — no Node, no browser runtime, no server. The entire UI layer is a few hundred lines and runs entirely from the standard library.

---

## 🔮 Possible Extensions

- [ ] Export class results to CSV or PDF
- [ ] Per-subject grade tracking instead of a flat mark list
- [ ] Search/filter bar for large class lists
- [ ] Sort table columns by clicking headers

---