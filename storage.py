"""
storage.py

Handles reading and writing student records to disk as JSON.
Isolating persistence here means the storage format (or even the
backend, e.g. swapping JSON for SQLite later) can change without
touching the GUI code at all.
"""

import json
import os
from typing import List

from models import Student

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")


def save_students(students: List[Student], path: str = DATA_FILE) -> None:
    """Write the full list of students to a JSON file on disk."""
    payload = [student.to_dict() for student in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def load_students(path: str = DATA_FILE) -> List[Student]:
    """
    Load students from a JSON file.

    Returns an empty list if the file does not exist yet (first run)
    or if it is empty/corrupted, so the app always starts cleanly.
    """
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

    return [Student.from_dict(entry) for entry in raw]