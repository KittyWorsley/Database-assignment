import sqlite3 as db
connection = db.connect ("events.py")

cursor = connection.cursor()


events_tbl = """CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER NOT NULL,
    donation_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    email TEXT,
    phone_number TEXT
    """
cursor.execute(events_tbl)


connection.commit()


connection.close()
