import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def delete_student():

    conn = get_connection()
    cursor = conn.cursor()

    student_id = input("Enter Student ID to delete: ")

    cursor.execute(
        "SELECT * FROM students WHERE student_id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:

        print("\nStudent Details")
        print("----------------")
        print("Name:", student[1])
        print("Email:", student[2])

        confirm = input("Are you sure you want to delete? (yes/no): ")

        if confirm.lower() == "yes":

            cursor.execute(
                "DELETE FROM students WHERE student_id=?",
                (student_id,)
            )

            conn.commit()
            print("Student deleted successfully!")

        else:
            print("Delete cancelled!")

    else:
        print("Student not found!")

    conn.close()


if __name__ == "__main__":
    delete_student()