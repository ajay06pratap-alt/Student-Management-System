import sqlite3

# Database Connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_no TEXT UNIQUE NOT NULL
)
""")
conn.commit()


def add_student():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll Number: ")

    try:
        cursor.execute(
            "INSERT INTO students(name, roll_no) VALUES(?, ?)",
            (name, roll_no)
        )
        conn.commit()
        print("\nStudent added successfully!")

    except sqlite3.IntegrityError:
        print("\nRoll number already exists!")


def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("\nNo students found.")
        return

    print("\n===== Student List =====")
    for student in students:
        print(f"ID      : {student[0]}")
        print(f"Name    : {student[1]}")
        print(f"Roll No : {student[2]}")
        print("-" * 25)


def search_student():
    roll_no = input("Enter Roll Number: ")

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print(f"ID      : {student[0]}")
        print(f"Name    : {student[1]}")
        print(f"Roll No : {student[2]}")
    else:
        print("\nStudent not found.")


def delete_student():
    roll_no = input("Enter Roll Number: ")

    cursor.execute(
        "DELETE FROM students WHERE roll_no = ?",
        (roll_no,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("\nStudent deleted successfully!")
    else:
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

conn.close()