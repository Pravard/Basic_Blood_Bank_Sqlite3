import sqlite3

conn = sqlite3.connect("blood_bank.db")
c = conn.cursor()


conn.execute('PRAGMA foreign_keys = ON')


c.execute('''
    SELECT Donor.donor_id, Donor.name, Donor.blood_type, Donor.contact_number, Donor.address, Hospital.name AS hospital_name
    FROM Donor
    JOIN Hospital ON Donor.hospital_id = Hospital.hospital_id
''')

donors_with_hospitals = c.fetchall()

for donor in donors_with_hospitals:
    print(donor)

conn.close()
