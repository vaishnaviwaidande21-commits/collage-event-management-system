import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def add_feedback():

    conn = get_connection()
    cursor = conn.cursor()

    student_id = input("Enter Student ID: ")
    event_id = input("Enter Event ID: ")
    feedback = input("Enter Feedback: ")

    cursor.execute("""
    INSERT INTO feedback(student_id, event_id, feedback)
    VALUES(?,?,?)
    """,
    (student_id, event_id, feedback))

    conn.commit()
    conn.close()

    print("Feedback added successfully!")


if __name__ == "__main__":
    add_feedback()