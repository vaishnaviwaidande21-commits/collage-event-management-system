import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def generate_report():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n========== College Event Management Report ==========")

    # Total Students
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    # Total Events
    cursor.execute("SELECT COUNT(*) FROM events")
    total_events = cursor.fetchone()[0]

    # Total Participation
    cursor.execute("SELECT COUNT(*) FROM participation")
    total_participation = cursor.fetchone()[0]

    # Total Feedback
    cursor.execute("SELECT COUNT(*) FROM feedback")
    total_feedback = cursor.fetchone()[0]


    print("Total Students       :", total_students)
    print("Total Events         :", total_events)
    print("Total Participation  :", total_participation)
    print("Total Feedback      :", total_feedback)

    print("====================================================")

    conn.close()


if __name__ == "__main__":
    generate_report()