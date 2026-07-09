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
    print("\nStudent added successfully.\n")


def update_student():
    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")
            student["department"] = input("Enter New Department: ")

            print("\nStudent updated successfully.\n")
            return

    print("\nStudent not found.\n")

def search_student():
    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print(f"Roll No    : {student['roll_no']}")
            print(f"Name       : {student['name']}")
            print(f"Department : {student['department']}\n")
            return

    print("\nStudent not found.\n")


def display_students():
    if len(students) == 0:
        print("\nNo student records available.\n")
        return

    print("\n------ Student List ------")

    for student in students:
        print(f"Roll No    : {student['roll_no']}")
        print(f"Name       : {student['name']}")
        print(f"Department : {student['department']}")
        print("--------------------------")