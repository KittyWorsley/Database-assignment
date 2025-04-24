import sqlite3 as db


connection = db.connect("donation.db")  

cursor = connection.cursor()


donation_info = ("""
CREATE TABLE IF NOT EXISTS donations (
'donation_ID' INTEGER PRIMARY KEY AUTOINCREMENT,
'donation_source' TEXT NOT NULL,
'donation_amount' INTEGER NOT NULL,
'business_name' TEXT,
'gift_aid' TEXT,
'date_of_donation' DATE NOT NULL
FOREIGN KEY (donation_source_id) REFERENCES DonationSource(id),
FOREIGN KEY (gift_aid_id) REFERENCES gift_aid_tbl(id)
)

);
""")
cursor.execute(donation_info)

donation_source_tbl=('''
CREATE TABLE IF NOT EXISTS DonationSource (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_name TEXT NOT NULL
);
''')
cursor.execute(donation_source_tbl)

gift_aid_tbl=('''
CREATE TABLE IF NOT EXISTS gift_aid_tbl  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL
    ''')
cursor.execute(gift_aid_tbl)

cursor.execute("INSERT OR IGNORE INTO DonationSource (source_name) VALUES (?)", ('Online',))

cursor.execute("INSERT OR IGNORE INTO DonationSource (source_name) VALUES (?)", ('Event',))

cursor.execute("INSERT OR IGNORE INTO gift_aid_tbl (status) VALUES (?)", ('Yes',))
cursor.execute("INSERT OR IGNORE INTO gift_aid_tbl (status) VALUES (?)", ('No',))

cursor.executemany('''
INSERT INTO donations(donation_source, donation_amount, business_name,gift_aid, date_of_donation)       
VALUES( donation samples)
''')



connection.commit()


connection.close()