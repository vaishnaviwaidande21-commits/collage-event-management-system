import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def search_feedback():

    conn = get_connection()
    cursor = conn.cursor()

    print("\nSearch Feedback")
    print("1. Search By Student ID")
    print("2. Search By Event ID")

    choice = input("Enter your choice: ")

    if choice == "1":

        student_id = input("Enter Student ID: ")

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
        WHERE students.student_id=?
        """, (student_id,))


    elif choice == "2":

        event_id = input("Enter Event ID: ")

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
        WHERE events.event_id=?
        """, (event_id,))

    else:
        print("Invalid choice!")
        conn.close()
        return


    records = cursor.fetchall()

    if records:

        print("\nFeedback Found")
        print("----------------------------")
        print("ID\tStudent Name\tEvent Name\tFeedback")

        for record in records:
            print(record[0], "\t",
                  record[1], "\t\t",
                  record[2], "\t",
                  record[3])

    else:
        print("No feedback record found!")

    conn.close()


if __name__ == "__main__":
    search_feedback()