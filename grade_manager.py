# Student Grade Manager - v2
# Refactored v1 to use a class instead of dictionaries.

import json
import os

FILENAME = "students.txt"


class Student:
    def __init__(self, name, marks=None):
        self.name = name
        self.marks = marks if marks else []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def highest(self):
        if len(self.marks) == 0:
            return 0
        return max(self.marks)

    def lowest(self):
        if len(self.marks) == 0:
            return 0
        return min(self.marks)

    def to_dict(self):
        return {"name": self.name, "marks": self.marks}


class GradeManager:
    def __init__(self):
        self.students = []
        self.load()

    def load(self):
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as f:
                content = f.read()
                if content:
                    data = json.loads(content)
                    for entry in data:
                        self.students.append(Student(entry["name"], entry["marks"]))

    def save(self):
        data = [s.to_dict() for s in self.students]
        with open(FILENAME, "w") as f:
            json.dump(data, f)

    def add_student(self, name):
        # check for duplicate names so we don't end up with two "Ali"s
        for s in self.students:
            if s.name.lower() == name.lower():
                print(f"{name} is already in the list.")
                return
        self.students.append(Student(name))
        print(f"{name} added.")

    def show_students(self):
        if len(self.students) == 0:
            print("No students yet.")
            return

        print("\n--- Students ---")
        for i, s in enumerate(self.students):
            print(f"{i + 1}. {s.name} - marks: {s.marks}")
        print("----------------\n")

    def get_student_choice(self):
        self.show_students()
        if len(self.students) == 0:
            return None

        choice = input("Enter the number of the student: ")
        try:
            index = int(choice) - 1
        except ValueError:
            print("That's not a number.")
            return None

        if index < 0 or index >= len(self.students):
            print("Invalid choice.")
            return None

        return self.students[index]

    def add_mark_to_student(self):
        student = self.get_student_choice()
        if student is None:
            return

        mark_input = input("Enter the mark (0-100): ")
        try:
            mark = float(mark_input)
        except ValueError:
            print("That's not a valid mark.")
            return

        if mark < 0 or mark > 100:
            print("Mark should be between 0 and 100.")
            return

        student.add_mark(mark)
        print("Mark added.")

    def show_average(self):
        student = self.get_student_choice()
        if student is None:
            return

        if len(student.marks) == 0:
            print(f"{student.name} has no marks yet.")
            return

        print(f"{student.name}'s average is {student.average():.2f}")

    def show_highest_lowest(self):
        students_with_marks = [s for s in self.students if len(s.marks) > 0]

        if len(students_with_marks) == 0:
            print("Nobody has marks yet.")
            return

        top_student = students_with_marks[0]
        bottom_student = students_with_marks[0]

        for s in students_with_marks:
            if s.average() > top_student.average():
                top_student = s
            if s.average() < bottom_student.average():
                bottom_student = s

        print(f"Highest scorer: {top_student.name} ({top_student.average():.2f})")
        print(f"Lowest scorer: {bottom_student.name} ({bottom_student.average():.2f})")

    def delete_student(self):
        student = self.get_student_choice()
        if student is None:
            return

        confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ")
        if confirm.lower() == "y":
            self.students.remove(student)
            print(f"{student.name} deleted.")
        else:
            print("Cancelled.")


def print_menu():
    print("\n===== Student Grade Manager (v2) =====")
    print("1. Add student")
    print("2. Add mark")
    print("3. Show all students")
    print("4. Calculate average for a student")
    print("5. Show highest/lowest scorer")
    print("6. Delete a student")
    print("7. Save and exit")
    print("========================================")


def main():
    manager = GradeManager()

    while True:
        print_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            name = input("Enter student name: ")
            manager.add_student(name)
        elif choice == "2":
            manager.add_mark_to_student()
        elif choice == "3":
            manager.show_students()
        elif choice == "4":
            manager.show_average()
        elif choice == "5":
            manager.show_highest_lowest()
        elif choice == "6":
            manager.delete_student()
        elif choice == "7":
            manager.save()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()