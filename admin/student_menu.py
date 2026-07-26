import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def student_menu():

    while True:

        print("\n========== Student Menu ==========")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back to Admin Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            from student.add_student import add_student
            add_student()

        elif choice == "2":
            from student.view_student import view_students
            view_students()

        elif choice == "3":
            from student.search_student import search_student
            search_student()

        elif choice == "4":
            from student.update_student import update_student
            update_student()

        elif choice == "5":
            from student.delete_student import delete_student
            delete_student()

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    student_menu()