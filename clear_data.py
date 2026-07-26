from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("DELETE FROM students")

conn.commit()
conn.close()

print("All student records deleted successfully!")