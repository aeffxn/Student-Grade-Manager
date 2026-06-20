"""
models.py

Defines the Student data class, which represents a single student and their recorded marks.

"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    """Represents a single student and their recorded marks."""

    name: str
    marks: List[float] = field(default_factory=list)

    def add_mark(self, mark: float) -> None:
        """Append a new mark for this student."""
        self.marks.append(mark)

    def average(self) -> float:
        """Return the average mark, or 0.0 if no marks exist."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def highest(self) -> float:
        """Return the highest recorded mark, or 0.0 if none exist."""
        return max(self.marks) if self.marks else 0.0

    def lowest(self) -> float:
        """Return the lowest recorded mark, or 0.0 if none exist."""
        return min(self.marks) if self.marks else 0.0

    def to_dict(self) -> dict:
        """Serialize this student into a JSON-friendly dictionary."""
        return {"name": self.name, "marks": self.marks}

    @staticmethod
    def from_dict(data: dict) -> "Student":
        """Reconstruct a Student instance from a stored dictionary."""
        return Student(name=data["name"], marks=list(data.get("marks", [])))