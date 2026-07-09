from student import (
    add_student,
    update_student,
    search_student,
    display_students
)

while True:
    print("\n======================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Display Students")
    print("5. Exit")
    print("======================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("\nThank you for using the Student Management System.")
        break

    else:
        print("\nInvalid choice! Please try again.\n")