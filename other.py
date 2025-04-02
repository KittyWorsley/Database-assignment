import sqlite3 as db
connection = db.connect ("events.py")

cursor = connection.cursor()

other_tble = """
CREATE TABLE IF NOT EXIST
 'house_number' TEXT,
 ' notes' TEXT
"""
cursor.execute(other_tble)


connection.commit()


connection.close()
