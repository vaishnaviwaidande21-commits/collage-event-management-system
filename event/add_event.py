import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def add_event():

    conn = get_connection()
    cursor = conn.cursor()

    event_name = input("Enter Event Name: ")
    event_date = input("Enter Event Date: ")
    venue = input("Enter Venue: ")
    description = input("Enter Event Description: ")

    cursor.execute("""
    INSERT INTO events(event_name, event_date, venue, description)
    VALUES(?,?,?,?)
    """,
    (event_name, event_date, venue, description))

    conn.commit()
    conn.close()

    print("Event added successfully!")


if __name__ == "__main__":
    add_event()