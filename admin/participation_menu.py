import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def participation_menu():

    while True:

        print("\n========== Participation Menu ==========")
        print("1. Add Participation")
        print("2. View Participation")
        print("3. Search Participation")
        print("4. Update Participation")
        print("5. Delete Participation")
        print("6. Back to Admin Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            from participation.add_participation import add_participation
            add_participation()

        elif choice == "2":
            from participation.view_participation import view_participation
            view_participation()

        elif choice == "3":
            from participation.search_participation import search_participation
            search_participation()

        elif choice == "4":
            from participation.update_participation import update_participation
            update_participation()

        elif choice == "5":
            from participation.delete_participation import delete_participation
            delete_participation()

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    participation_menu()