import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def event_menu():

    while True:

        print("\n========== Event Menu ==========")
        print("1. Add Event")
        print("2. View Event")
        print("3. Search Event")
        print("4. Update Event")
        print("5. Delete Event")
        print("6. Back to Admin Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            from event.add_event import add_event
            add_event()

        elif choice == "2":
            from event.view_event import view_events
            view_events()

        elif choice == "3":
            from event.search_event import search_event
            search_event()

        elif choice == "4":
            from event.update_event import update_event
            update_event()

        elif choice == "5":
            from event.delete_event import delete_event
            delete_event()

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    event_menu()