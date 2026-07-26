from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# Student Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    department TEXT
)
""")

# Event Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS events(
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_date TEXT,
    venue TEXT,
    description TEXT
)
""")

# Participation Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS participation(
    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    event_id INTEGER
)
""")

# Feedback Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback(
    feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    event_id INTEGER,
    feedback TEXT
)
""")

conn.commit()
conn.close()

print("Database tables created successfully!")