import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def delete_feedback():

    conn = get_connection()
    cursor = conn.cursor()

    feedback_id = input("Enter Feedback ID to delete: ")

    cursor.execute(
        "SELECT * FROM feedback WHERE feedback_id=?",
        (feedback_id,)
    )

    feedback = cursor.fetchone()

    if feedback:

        print("\nFeedback Details")
        print("----------------")
        print("Student ID:", feedback[1])
        print("Event ID:", feedback[2])
        print("Feedback:", feedback[3])

        confirm = input("Are you sure you want to delete? (yes/no): ")

        if confirm.lower() == "yes":

            cursor.execute(
                "DELETE FROM feedback WHERE feedback_id=?",
                (feedback_id,)
            )

            conn.commit()

            print("Feedback deleted successfully!")

        else:
            print("Delete cancelled!")

    else:
        print("Feedback record not found!")

    conn.close()


if __name__ == "__main__":
    delete_feedback()