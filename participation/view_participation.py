import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def view_participation():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
    participation.participation_id,
    students.name,
    events.event_name
    FROM participation
    JOIN students
    ON participation.student_id = students.student_id
    JOIN events
    ON participation.event_id = events.event_id
    """)

    records = cursor.fetchall()

    if len(records) == 0:
        print("No participation records found!")

    else:
        print("\nParticipation Details")

        print("ID\tStudent Name\tEvent Name")

        for record in records:
            print(record[0], "\t",
                  record[1], "\t\t",
                  record[2])

    conn.close()


if __name__ == "__main__":
    view_participation()