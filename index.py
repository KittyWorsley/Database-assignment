import sqlite3 as db
connection = db.connect ("charity database.py")

cursor = connection.cursor()

donor_table = '''
CREATE TABLE IF NOT EXISTS Donor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    'first_name' TEXT NOT NULL,
    'surname' TEXT NOT NULL,
    'business_name' TEXT,
    'phone_number' TEXT,
    'postcode' TEXT,
    'house_number' TEXT
)
'''
cursor.execute(donor_table)


donation_table = '''
CREATE TABLE IF NOT EXISTS Donation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    'donor_id' INTEGER NOT NULL,
    'amount_donated' REAL NOT NULL,
    'date_of_donation' DATE NOT NULL,
    'donation_source' TEXT,
    'gift_aid' TEXT,
    'notes' TEXT,
    FOREIGN KEY (donor_id) REFERENCES Donor (id)
)
'''
cursor.execute(donation_table)


event_table = '''
CREATE TABLE IF NOT EXISTS Event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
   'name' TEXT NOT NULL,
    'email' TEXT,
    'phone_number' TEXT
)
'''
cursor.execute(event_table)


event_donation_table = '''
CREATE TABLE IF NOT EXISTS EventDonation (
    'event_id' INTEGER NOT NULL,
    'donation_id' INTEGER NOT NULL,
    PRIMARY KEY (event_id, donation_id),
    FOREIGN KEY (event_id) REFERENCES Event (id),
    FOREIGN KEY (donation_id) REFERENCES Donation (id)
)
'''
cursor.execute(event_donation_table)


connection.commit()


connection.close()
