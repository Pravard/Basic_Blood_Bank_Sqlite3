import sqlite3

conn = sqlite3.connect("blood_bank.db")
c = conn.cursor()

# Donor table
c.execute('''
    CREATE TABLE IF NOT EXISTS Donor (
        donor_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        blood_type TEXT NOT NULL,
        contact_number TEXT NOT NULL,
        address TEXT,
        hospital_id INTEGER,
        FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
    )
''')

# Patient table
c.execute('''
    CREATE TABLE IF NOT EXISTS Patient (
        patient_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        blood_type TEXT NOT NULL,
        contact_number TEXT NOT NULL,
        address TEXT,
        hospital_id INTEGER,
        FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
    )
''')

# Hospital table
c.execute('''
    CREATE TABLE IF NOT EXISTS Hospital (
        hospital_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        contact_number TEXT NOT NULL,
        address TEXT
    )
''')

c.executemany('''
    INSERT OR IGNORE INTO Donor (donor_id, name, blood_type, contact_number, address, hospital_id)
    VALUES (?, ?, ?, ?, ?, ?)
''', [
    (1, 'Amit Sharma', 'A+', '9876543210', 'Delhi', 1),
    (2, 'Priya Patel', 'B-', '8765432109', 'Mumbai', 2),
    (3, 'Rahul Verma', 'O+', '7654321098', 'Kolkata', 3),
    (4, 'Sonia Gupta', 'AB+', '6543210987', 'Chennai', 4),
    (5, 'Ankit Singh', 'A-', '5432109876', 'Bangalore', 5)
])

c.executemany('''
    INSERT OR IGNORE INTO Patient (patient_id, name, blood_type, contact_number, address, hospital_id)
    VALUES (?, ?, ?, ?, ?, ?)
''', [
    (1, 'Riya Kapoor', 'B+', '8765432101', 'Pune', 1),
    (2, 'Arjun Singh', 'O-', '7654321092', 'Hyderabad', 2),
    (3, 'Neha Reddy', 'AB-', '6543210983', 'Ahmedabad', 3),
    (4, 'Kunal Mehta', 'A+', '5432109874', 'Jaipur', 4),
    (5, 'Aisha Khan', 'B-', '4321098765', 'Lucknow', 5)
])

c.executemany('''
    INSERT OR IGNORE INTO Hospital (hospital_id, name, contact_number, address)
    VALUES (?, ?, ?, ?)
''', [
    (1, 'City Hospital', '9876543211', 'Delhi'),
    (2, 'Metro Medical Center', '8765432102', 'Mumbai'),
    (3, 'Royal Healthcare', '7654321093', 'Kolkata'),
    (4, 'Sunshine Hospital', '6543210984', 'Chennai'),
    (5, 'Greenwood Clinic', '5432109875', 'Bangalore')
])


conn.commit()
conn.close()


