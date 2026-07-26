import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def search_student():

    conn = get_connection()
    cursor = conn.cursor()

    print("\nSearch Student")
    print("1. Search By Student ID")
    print("2. Search By Name")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_id=?",
            (student_id,)
        )

    elif choice == "2":
        name = input("Enter Student Name: ")

        cursor.execute(
            "SELECT * FROM students WHERE name=?",
            (name,)
        )

    else:
        print("Invalid choice!")
        conn.close()
        return

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("----------------------------")
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Email:", student[2])
        print("Phone:", student[3])
        print("Department:", student[4])

    else:
        print("Student not found!")

    conn.close()


if __name__ == "__main__":
    search_student()