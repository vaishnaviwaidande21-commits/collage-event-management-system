import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_connection import get_connection


def view_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:
        print("No student records found!")

    else:
        print("\nStudent Details")
        print("-" * 80)

        print(f"{'ID':<8}{'Name':<15}{'Email':<25}{'Phone':<15}{'Department':<15}")

        print("-" * 80)

        for student in students:
            print(f"{student[0]:<8}{student[1]:<15}{student[2]:<25}{student[3]:<15}{student[4]:<15}")

        print("-" * 80)

    conn.close()


if __name__ == "__main__":
    view_students()