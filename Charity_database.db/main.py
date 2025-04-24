import sqlite3 as db
connection = db.connect ("charity database.db")

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

donation_source_tble = ('''
   CREATE TABLE IF NOT EXISTS DonationSource(
       id INTERGER PRIMARY KEY AUTOINCREMENT
       'source_name' TEXT NOT NULL)
   
''')
cursor.execute(donation_source_tble)

gift_aid_tbl= ('''
   CREATE TABLE IF NOT EXIST Gift_Aid
id INTEGER PRIMARY KEY AUTOINCREMENT,
   'text' NOT NULL UNIQUE)
   ''')
cursor.execute(gift_aid_tbl)                  
              

event_table =( '''
CREATE TABLE IF NOT EXISTS Event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
   'name' TEXT NOT NULL,
    'email' TEXT,
    'phone_number' TEXT
)
''')
cursor.execute(event_table)

event_donation_table = ('''
CREATE TABLE IF NOT EXISTS EventDonation (
    'event_id' INTEGER NOT NULL,
    'donation_id' INTEGER NOT NULL,
    PRIMARY KEY (event_id, donation_id),
    FOREIGN KEY (event_id) REFERENCES Event (id),
    FOREIGN KEY (donation_id) REFERENCES Donation (id)
)
''')
cursor.execute(event_donation_table)
cursor.execute('''
INSERT  INTO doner( first_name,surname, business_name, phone_number, postcode,house_number)
VALUES (Claire,Smith,busyBEEs, 098756473, SQ23,5QL, 106)''')

donor_id = cursor.lastrowid
cursor.execute('''
INSERT INTO  Event( name,email,phone_number)  
VALUES(busyBEEs,busyBEEs@charitydonation.com, 098756473)''')
event_id = cursor.lastrowid

cursor.execute('''
INSERT INTO EventDonation (event_id, donation_id))
VALUES(1234, 4563)''')
connection.commit()

connection.close()


1