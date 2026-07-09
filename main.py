from student import add_student, update_student

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_student()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.\n")