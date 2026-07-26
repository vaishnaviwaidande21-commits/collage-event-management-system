import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def add_participation():

    conn = get_connection()
    cursor = conn.cursor()

    student_id = input("Enter Student ID: ")
    event_id = input("Enter Event ID: ")

    cursor.execute("""
    INSERT INTO participation(student_id, event_id)
    VALUES(?,?)
    """,
    (student_id, event_id))

    conn.commit()
    conn.close()

    print("Participation added successfully!")


if __name__ == "__main__":
    add_participation()