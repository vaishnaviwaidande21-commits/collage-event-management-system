import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def update_participation():

    conn = get_connection()
    cursor = conn.cursor()

    participation_id = input("Enter Participation ID to update: ")

    cursor.execute(
        "SELECT * FROM participation WHERE participation_id=?",
        (participation_id,)
    )

    participation = cursor.fetchone()

    if participation:

        print("\nCurrent Details")
        print("----------------")
        print("Student ID:", participation[1])
        print("Event ID:", participation[2])

        print("\nEnter New Details")

        student_id = input("Enter New Student ID: ")
        event_id = input("Enter New Event ID: ")

        cursor.execute("""
        UPDATE participation
        SET student_id=?, event_id=?
        WHERE participation_id=?
        """,
        (student_id, event_id, participation_id))

        conn.commit()

        print("Participation updated successfully!")

    else:
        print("Participation record not found!")

    conn.close()


if __name__ == "__main__":
    update_participation()