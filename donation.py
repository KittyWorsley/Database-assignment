import sqlite3 as db
connection = db.connect ("donation.py")

cursor = connection.cursor()

donnation_info = """
CREATE TABLE IF NOT EXIST
'donation_ID'INTEGER NIT NULL
'donation_source' TEXT NOT NULL
'donation amount' INTEGER
'business_name' TEXT,
'gift_aid'TEXT
'date_of_donation' DATE NOT NULL,
"""
cursor.execute(donnation_info)


connection.commit()


connection.close()
