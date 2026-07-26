import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def update_event():

    conn = get_connection()
    cursor = conn.cursor()

    event_id = input("Enter Event ID to update: ")

    cursor.execute(
        "SELECT * FROM events WHERE event_id=?",
        (event_id,)
    )

    event = cursor.fetchone()

    if event:

        print("\nCurrent Event Details")
        print("-------------------------")
        print("Event Name:", event[1])
        print("Event Date:", event[2])
        print("Venue:", event[3])
        print("Description:", event[4])

        print("\nEnter New Details")

        event_name = input("Enter New Event Name: ")
        event_date = input("Enter New Event Date: ")
        venue = input("Enter New Venue: ")
        description = input("Enter New Description: ")

        cursor.execute("""
        UPDATE events
        SET event_name=?, event_date=?, venue=?, description=?
        WHERE event_id=?
        """,
        (event_name, event_date, venue, description, event_id))

        conn.commit()

        print("Event updated successfully!")

    else:
        print("Event not found!")

    conn.close()


if __name__ == "__main__":
    update_event()