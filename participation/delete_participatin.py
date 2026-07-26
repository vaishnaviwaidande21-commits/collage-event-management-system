import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def delete_participation():

    conn = get_connection()
    cursor = conn.cursor()

    participation_id = input("Enter Participation ID to delete: ")

    cursor.execute(
        "SELECT * FROM participation WHERE participation_id=?",
        (participation_id,)
    )

    participation = cursor.fetchone()

    if participation:

        print("\nParticipation Details")
        print("----------------------")
        print("Student ID:", participation[1])
        print("Event ID:", participation[2])

        confirm = input("Are you sure you want to delete? (yes/no): ")

        if confirm.lower() == "yes":

            cursor.execute(
                "DELETE FROM participation WHERE participation_id=?",
                (participation_id,)
            )

            conn.commit()

            print("Participation deleted successfully!")

        else:
            print("Delete cancelled!")

    else:
        print("Participation record not found!")

    conn.close()


if __name__ == "__main__":
    delete_participation()