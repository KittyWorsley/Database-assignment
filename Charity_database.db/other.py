import sqlite3 as db


connection = db.connect("other.db")
cursor = connection.cursor()



doner_tbl=('''
     CREATE TABLE IF NOT EXISTS Donor (
    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL ''')
cursor.execute(doner_tbl)

doner_information_tbl=('''
  CREATE TABLE IF NOT EXISTS Doner information (
    donor_id INTEGER,
    address_id INTEGER,
    FOREIGN KEY (donor_id) REFERENCES Donor(donor_id),
    FOREIGN KEY (address_id) REFERENCES HouseAddress(address_id) ''')
cursor.execute(doner_information_tbl)

doner_notes_tbl=('''
CREATE TABLE IF NOT EXISTS DonorNotes (
    donor_id INTEGER,
    note_id INTEGER,
    FOREIGN KEY (donor_id) REFERENCES Donor(donor_id),
    FOREIGN KEY (note_id) REFERENCES Notes(note_id)
    ''')
cursor.execute(doner_notes_tbl)
  

cursor.executemany('''
INSERT INTO OtherTable (house_number, notes)
VALUES''')

connection.commit()
connection.close()