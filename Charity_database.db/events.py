import sqlite3 as db


connection = db.connect("events.db")
cursor = connection.cursor()


events_tbl = """
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL,
    email TEXT,
    phone_number TEXT
);
"""
cursor.execute(events_tbl)

donation_tbl=('''
   CREATE TABLE IF NOT EXISTS Donation (
    donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER NOT NULL,  
    donation_amount REAL NOT NULL,
    donation_source TEXT,
    date_of_donation DATE NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES Donor(id)   
    ''')
cursor.execute(donation_tbl)

event_donation_tbl=('''
       CREATE TABLE IF NOT EXISTS EventDonation (
    event_id INTEGER NOT NULL,
    donation_id INTEGER NOT NULL,
    PRIMARY KEY (event_id, donation_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id),
    FOREIGN KEY (donation_id) REFERENCES Donation(donation_id)          
    ''')
cursor.execute(event_donation_tbl)

cursor.execute ('''INSERT INTO Event (name, email, phone_number)
VALUES ('Charity Gala', 'charitygala@events.com', '1234567890')''')

event_id = cursor.lastrowid

cursor.executemany('''
INSERT INTO events (donation_id, name, email, phone_number)
 VALUES ''')
cursor.execute('''
INSERT INTO Donation (donor_id, donation_amount, donation_source, date_of_donation)
VALUES (1, 100.00, 'Online', '2025-04-24')''')
donation_id = cursor.lastrowid

cursor.execute('''
INSERT INTO EventDonation (event_id, donation_id)
VALUES (event_id, donation_id))
''')

connection.commit()
connection.close()
