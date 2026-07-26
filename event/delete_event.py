import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def delete_event():

    conn = get_connection()
    cursor = conn.cursor()

    event_id = input("Enter Event ID to delete: ")

    cursor.execute(
        "SELECT * FROM events WHERE event_id=?",
        (event_id,)
    )

    event = cursor.fetchone()

    if event:

        print("\nEvent Details")
        print("----------------")
        print("Event Name:", event[1])
        print("Event Date:", event[2])
        print("Venue:", event[3])

        confirm = input("Are you sure you want to delete? (yes/no): ")

        if confirm.lower() == "yes":

            cursor.execute(
                "DELETE FROM events WHERE event_id=?",
                (event_id,)
            )

            conn.commit()

            print("Event deleted successfully!")

        else:
            print("Delete cancelled!")

    else:
        print("Event not found!")

    conn.close()


if __name__ == "__main__":
    delete_event()