# Student Grade Manager - v1 (Command Line version)
# Simple program to add students, add marks, and calculate averages.

import json
import os

FILENAME = "students.txt"

students = []


def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            data = f.read()
            if data:
                return json.loads(data)
    return []


def save_data():
    with open(FILENAME, "w") as f:
        json.dump(students, f)


def add_student():
    name = input("Enter student name: ")
    new_student = {"name": name, "marks": []}
    students.append(new_student)
    print(name + " has been added.")


def add_mark():
    if len(students) == 0:
        print("No students yet. Add a student first.")
        return

    show_students()
    choice = input("Enter the number of the student: ")

    try:
        index = int(choice) - 1
    except:
        print("That's not a number.")
        return

    if index < 0 or index >= len(students):
        print("Invalid choice.")
        return

    mark = input("Enter the mark: ")
    try:
        mark = float(mark)
    except:
        print("That's not a valid mark.")
        return

    students[index]["marks"].append(mark)
    print("Mark added.")


def show_students():
    if len(students) == 0:
        print("No students added yet.")
        return

    print("\n--- Students ---")
    for i in range(len(students)):
        s = students[i]
        print(str(i + 1) + ". " + s["name"] + " - marks: " + str(s["marks"]))
    print("----------------\n")


def calculate_average():
    if len(students) == 0:
        print("No students yet.")
        return

    show_students()
    choice = input("Enter the number of the student: ")

    try:
        index = int(choice) - 1
    except:
        print("That's not a number.")
        return

    if index < 0 or index >= len(students):
        print("Invalid choice.")
        return

    marks = students[index]["marks"]
    if len(marks) == 0:
        print(students[index]["name"] + " has no marks yet.")
        return

    total = 0
    for m in marks:
        total = total + m
    avg = total / len(marks)

    print(students[index]["name"] + "'s average is: " + str(avg))


def find_highest_lowest():
    if len(students) == 0:
        print("No students yet.")
        return

    best_student = None
    best_avg = -1
    worst_student = None
    worst_avg = 101

    for s in students:
        if len(s["marks"]) == 0:
            continue
        avg = sum(s["marks"]) / len(s["marks"])
        if avg > best_avg:
            best_avg = avg
            best_student = s["name"]
        if avg < worst_avg:
            worst_avg = avg
            worst_student = s["name"]

    if best_student is None:
        print("No marks recorded yet for anyone.")
        return

    print("Highest scorer: " + best_student + " (" + str(best_avg) + ")")
    print("Lowest scorer: " + worst_student + " (" + str(worst_avg) + ")")


def print_menu():
    print("\n===== Student Grade Manager =====")
    print("1. Add student")
    print("2. Add mark")
    print("3. Show all students")
    print("4. Calculate average for a student")
    print("5. Show highest/lowest scorer")
    print("6. Save and exit")
    print("==================================")


def main():
    global students
    students = load_data()

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_mark()
        elif choice == "3":
            show_students()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            find_highest_lowest()
        elif choice == "6":
            save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option, try again.")


main()