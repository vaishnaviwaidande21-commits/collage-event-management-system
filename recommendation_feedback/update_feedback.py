import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def update_feedback():

    conn = get_connection()
    cursor = conn.cursor()

    feedback_id = input("Enter Feedback ID to update: ")

    cursor.execute(
        "SELECT * FROM feedback WHERE feedback_id=?",
        (feedback_id,)
    )

    feedback = cursor.fetchone()

    if feedback:

        print("\nCurrent Feedback Details")
        print("-------------------------")
        print("Student ID:", feedback[1])
        print("Event ID:", feedback[2])
        print("Feedback:", feedback[3])

        print("\nEnter New Feedback")

        new_feedback = input("Enter Updated Feedback: ")

        cursor.execute("""
        UPDATE feedback
        SET feedback=?
        WHERE feedback_id=?
        """,
        (new_feedback, feedback_id))

        conn.commit()

        print("Feedback updated successfully!")

    else:
        print("Feedback record not found!")

    conn.close()


if __name__ == "__main__":
    update_feedback()