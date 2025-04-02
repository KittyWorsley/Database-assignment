import sqlite3 as db
connection = db.connect ("doner.py")

cursor = connection.cursor()

doner_info = """
CREATE TABLE IF NOT EXISTS 'doner info'
'first_name' TEXT NOT NULL,
'sur_name' TEXT NOT NULL,
'phone number' INTEGER
'business_name' TEXT,
'donation ID' INTEGER
'donation_source' TEXT NOT NULL,
'donation amount' INTEGER
'gift_aid' TEXT
'date_of_donation' DATE NOT NULL,
'postcode' TEXT,
"""
cursor.execute(doner_info)


connection.commit()


connection.close()
