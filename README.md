# 📚 Student Grade Manager (v2)

![Python](https://img.shields.io/badge/Python-3.x-yellow?style=flat-square&logo=python&logoColor=black)
![Status](https://img.shields.io/badge/Status-CLI%20only-lightgrey?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-black?style=flat-square)

A command-line tool to manage students and their grades — now refactored to use classes instead of plain dictionaries. This is the second version in a 3-part progression: **v1 (basic CLI)** → **v2 (OOP CLI, you are here)** → **v3 (GUI)**.

---

## 📑 Table of Contents

- [What's New in v2](#-whats-new-in-v2)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Menu Guide](#-menu-guide)
- [Notes](#-notes)
- [Roadmap](#-roadmap)
- [License](#-license)

---

## ✨ What's New in v2

| Change | v1 | v2 |
|---|---|---|
| Data structure | Dictionaries | `Student` class with methods |
| Code organization | All logic in functions | `Student` + `GradeManager` classes |
| Delete student | ❌ | ✅ (with confirmation) |
| Duplicate name check | ❌ | ✅ |
| String formatting | `+` concatenation | f-strings |

---

## 🚀 Features

- ➕ Add a student
- 📝 Add marks for a student
- 📋 View all students and their marks
- 📊 Calculate a student's average
- 🏆 Find the highest and lowest scorer in the class
- 🗑️ Delete a student (with confirmation prompt)
- 💾 Save/load data automatically using a local file

---

## 🛠 Requirements

- Python 3.x
- No external libraries — just the Python standard library

Check if Python is installed:

```bash
python3 --version
```

If that doesn't work, try:

```bash
python --version
```

---

## 📦 Installation

```bash
git clone <your-repo-url>
cd <repo-folder>
python3 grade_manager.py
```

---

## ▶️ Usage

Run the script and you'll see a menu:

```
===== Student Grade Manager (v2) =====
1. Add student
2. Add mark
3. Show all students
4. Calculate average for a student
5. Show highest/lowest scorer
6. Delete a student
7. Save and exit
========================================
```

Type a number and press Enter to choose an option.

---

## 📋 Menu Guide

| Option | Action |
|---|---|
| `1` | Add a new student (blocks duplicate names) |
| `2` | Add a mark to an existing student |
| `3` | List all students and their marks |
| `4` | Show one student's average |
| `5` | Show the highest and lowest scorer in the class |
| `6` | Delete a student (asks for confirmation first) |
| `7` | Save all data and exit |

> ⚠️ Always exit using option `7` — closing the terminal directly will not save your data.

---

## 📝 Notes

- Data is saved to `students.txt` in the same folder — don't delete it manually.
- Marks must be between `0` and `100`.
- This version is still CLI-only. A full GUI version (v3) is next.

---

## 🗺 Roadmap

- [x] v1 — Basic CLI with functions
- [x] v2 — Refactored to use classes
- [ ] v3 — GUI version with Tkinter

---