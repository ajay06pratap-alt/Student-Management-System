import json

# Load students from JSON file
try:
    with open("student.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []


def save_data():
    """Save student data to JSON file."""
    with open("student.json", "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll Number: ")

    # Check duplicate roll number
    for student in students:
        if student["roll_no"] == roll_no:
            print("\nRoll number already exists!")
            return

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)
    save_data()
    print("\nStudent added successfully!")


def view_students():
    if not students:
        print("\nNo students found.")
        return

    print("\n===== Student List =====")

    for student in students:
        print(f"Name    : {student['name']}")
        print(f"Roll No : {student['roll_no']}")
        print("-" * 25)


def search_student():
    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print(f"Name    : {student['name']}")
            print(f"Roll No : {student['roll_no']}")
            return

    print("\nStudent not found.")


def delete_student():
    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_data()
            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")


# Main Menu
while True:
    print("\n========== Student Management ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("\nThank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")