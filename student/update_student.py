import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def update_student():

    conn = get_connection()
    cursor = conn.cursor()

    student_id = input("Enter Student ID to update: ")

    cursor.execute(
        "SELECT * FROM students WHERE student_id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:

        print("\nCurrent Student Details")
        print("----------------------------")
        print("Name:", student[1])
        print("Email:", student[2])
        print("Phone:", student[3])
        print("Department:", student[4])

        print("\nEnter New Details")

        name = input("Enter New Name: ")
        email = input("Enter New Email: ")
        phone = input("Enter New Phone: ")
        department = input("Enter New Department: ")

        cursor.execute("""
        UPDATE students
        SET name=?, email=?, phone=?, department=?
        WHERE student_id=?
        """,
        (name, email, phone, department, student_id))

        conn.commit()

        print("Student updated successfully!")

    else:
        print("Student not found!")

    conn.close()


if __name__ == "__main__":
    update_student()