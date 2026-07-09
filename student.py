students = []


def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "department": department
    }

    students.append(student)
    print("\n Student added successfully.\n")


def update_student():
    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")
            student["department"] = input("Enter New Department: ")

            print("\n Student updated successfully.\n")
            return

    print("\n Student not found.\n")


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\n===== Student Found =====")
            print(f"Roll Number : {student['roll_no']}")
            print(f"Name        : {student['name']}")
            print(f"Department  : {student['department']}")
            print("=========================\n")
            return

    print("\n Student not found.\n")


def display_students():
    if len(students) == 0:
        print("\nNo student records available.\n")
        return

    print("\n========== Student List ==========")

    for student in students:
        print(f"Roll Number : {student['roll_no']}")
        print(f"Name        : {student['name']}")
        print(f"Department  : {student['department']}")
        print("----------------------------------")