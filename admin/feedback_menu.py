import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def feedback_menu():

    while True:

        print("\n========== Feedback Menu ==========")
        print("1. Add Feedback")
        print("2. View Feedback")
        print("3. Search Feedback")
        print("4. Update Feedback")
        print("5. Delete Feedback")
        print("6. Back to Admin Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            from recommendation_feedback.add_feedback import add_feedback
            add_feedback()

        elif choice == "2":
            from recommendation_feedback.view_feedback import view_feedback
            view_feedback()

        elif choice == "3":
            from recommendation_feedback.search_feedback import search_feedback
            search_feedback()

        elif choice == "4":
            from recommendation_feedback.update_feedback import update_feedback
            update_feedback()

        elif choice == "5":
            from recommendation_feedback.delete_feedback import delete_feedback
            delete_feedback()

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    feedback_menu()