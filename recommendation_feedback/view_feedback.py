import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def view_feedback():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    feedback.feedback_id,
    students.name,
    events.event_name,
    feedback.feedback
    FROM feedback
    JOIN students
    ON feedback.student_id = students.student_id
    JOIN events
    ON feedback.event_id = events.event_id
    """)

    records = cursor.fetchall()

    if len(records) == 0:
        print("No feedback found!")

    else:
        print("\nFeedback Details")
        print("-" * 90)

        print(f"{'ID':<8}{'Student Name':<18}{'Event Name':<25}{'Feedback':<30}")

        print("-" * 90)

        for record in records:
            print(f"{record[0]:<8}{record[1]:<18}{record[2]:<25}{record[3]:<30}")

        print("-" * 90)

    conn.close()


if __name__ == "__main__":
    view_feedback()