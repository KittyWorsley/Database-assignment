import sqlite3 as db


connection = db.connect("doner.db")
cursor = connection.cursor()


doner_info = """
CREATE TABLE IF NOT EXISTS doner_info (
    first_name TEXT NOT NULL,
    sur_name TEXT NOT NULL,
    phone_number INTEGER,
    business_name TEXT,
    donation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    donation_source TEXT NOT NULL,
    donation_amount INTEGER,
    gift_aid TEXT,
    date_of_donation DATE NOT NULL,
    postcode TEXT
);
"""
cursor.execute(doner_info)

donation_tbl=('''
CREATE TABLE IF NOT EXISTS Donation (
    donation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER NOT NULL,
    donation_source TEXT NOT NULL,
    donation_amount INTEGER,
    gift_aid TEXT,
    date_of_donation DATE NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES Donor(id)
    ''')
cursor.execute(donation_tbl)

gift_aid_tbl=('''
 CREATE TABLE IF NOT EXISTS GiftAid (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    TEXT NOT NULL              
''')
cursor.execute(gift_aid_tbl)

cursor.execute("INSERT INTO gift_aid_tbl (status) VALUES ('Yes')")
cursor.execute("INSERT INTO gift_aid_tbl  (status) VALUES ('No')")

cursor.execute('''
INSERT INTO Donation (donor_id, donation_source, donation_amount, gift_aid, date_of_donation)
VALUES (donor_id, 'Online', 100, 'Yes', '2025-04-24'))
'''), 
cursor.executemany('''
INSERT INTO doner_info (first_name, sur_name, phone_number, business_name,
    donation_source, donation_amount, gift_aid, date_of_donation, postcode)
 ''')

connection.commit()
connection.close()