import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def search_event():

    conn = get_connection()
    cursor = conn.cursor()

    print("\nSearch Event")
    print("1. Search By Event ID")
    print("2. Search By Event Name")

    choice = input("Enter your choice: ")

    if choice == "1":

        event_id = input("Enter Event ID: ")

        cursor.execute(
            "SELECT * FROM events WHERE event_id=?",
            (event_id,)
        )

    elif choice == "2":

        event_name = input("Enter Event Name: ")

        cursor.execute(
            "SELECT * FROM events WHERE event_name=?",
            (event_name,)
        )

    else:
        print("Invalid choice!")
        conn.close()
        return

    event = cursor.fetchone()

    if event:

        print("\nEvent Found")
        print("----------------------")
        print("Event ID:", event[0])
        print("Event Name:", event[1])
        print("Event Date:", event[2])
        print("Venue:", event[3])
        print("Description:", event[4])

    else:
        print("Event not found!")

    conn.close()


if __name__ == "__main__":
    search_event()