import sqlite3

def get_connection():
    conn = sqlite3.connect("database/college_event.db")
    return conn