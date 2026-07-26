import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def admin_menu():

    while True:

        print("\n========== Admin Menu ==========")
        print("1. Student Module")
        print("2. Event Module")
        print("3. Participation Module")
        print("4. Feedback Module")
        print("5. Reports")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            from admin.student_menu import student_menu
            student_menu()

        elif choice == "2":
            from admin.event_menu import event_menu
            event_menu()

        elif choice == "3":
            from admin.participation_menu import participation_menu
            participation_menu()

        elif choice == "4":
            from admin.feedback_menu import feedback_menu
            feedback_menu()

        elif choice == "5":
            from reports.generate_report import generate_report
            generate_report()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    admin_menu()