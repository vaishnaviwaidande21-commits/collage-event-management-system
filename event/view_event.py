import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def view_events():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM events")

    events = cursor.fetchall()

    if len(events) == 0:
        print("No events found!")

    else:
        print("\nEvent Details")
        print("-" * 90)

        print(f"{'ID':<8}{'Event Name':<20}{'Date':<15}{'Venue':<20}{'Description':<25}")

        print("-" * 90)

        for event in events:
            print(f"{event[0]:<8}{event[1]:<20}{event[2]:<15}{event[3]:<20}{event[4]:<25}")

        print("-" * 90)

    conn.close()


if __name__ == "__main__":
    view_events()