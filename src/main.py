import json
import os

DATA_FILE = "students.json"

# -----------------------------
# Utility Functions
# -----------------------------

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def generate_id(data):
    if not data:
        return 1
    return max(student['id'] for student in data) + 1

# -----------------------------
# Core Features
# -----------------------------

def add_student():
    data = load_data()

    name = input("Enter student name: ")
    age = input("Enter age: ")
    department = input("Enter department: ")
    cgpa = input("Enter CGPA: ")

    student = {
        "id": generate_id(data),
        "name": name,
        "age": age,
        "department": department,
        "cgpa": cgpa
    }

    data.append(student)
    save_data(data)

    print("\n Student added successfully!\n")


def view_students():
    data = load_data()

    if not data:
        print("\n No student records found.\n")
        return

    print("\n--- Student Records ---")
    for student in data:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Department: {student['department']}")
        print(f"CGPA: {student['cgpa']}")
        print("-----------------------")


def search_student():
    data = load_data()
    keyword = input("Enter name to search: ").lower()

    results = [s for s in data if keyword in s['name'].lower()]

    if not results:
        print("\n No matching students found.\n")
        return

    print("\n Search Results:")
    for student in results:
        print(student)


def update_student():
    data = load_data()
    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("Invalid ID")
        return

    for student in data:
        if student['id'] == student_id:
            print("Leave blank to keep current value")

            name = input(f"Name ({student['name']}): ")
            age = input(f"Age ({student['age']}): ")
            department = input(f"Department ({student['department']}): ")
            cgpa = input(f"CGPA ({student['cgpa']}): ")

            if name:
                student['name'] = name
            if age:
                student['age'] = age
            if department:
                student['department'] = department
            if cgpa:
                student['cgpa'] = cgpa

            save_data(data)
            print("\n Student updated successfully!\n")
            return

    print("\n Student not found!\n")


def delete_student():
    data = load_data()
    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Invalid ID")
        return

    new_data = [s for s in data if s['id'] != student_id]

    if len(new_data) == len(data):
        print("\n Student not found!\n")
        return

    save_data(new_data)
    print("\n Student deleted successfully!\n")

# -----------------------------
# Menu System
# -----------------------------

def menu():
    while True:
        print("""
===== Student Information Management System =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

# -----------------------------
# Entry Point
# -----------------------------

if __name__ == "__main__":
    menu()
