
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from db_connection import get_connection


def add_student():

    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter Student Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    department = input("Enter Department: ")

    cursor.execute("""
    INSERT INTO students(name, email, phone, department)
    VALUES(?,?,?,?)
    """, (name, email, phone, department))

    conn.commit()
    conn.close()

    print("Student added successfully!")


if __name__ == "__main__":
    add_student()