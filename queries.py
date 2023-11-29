import sqlite3

conn = sqlite3.connect("blood_bank.db")
c = conn.cursor()

#Query 1
c.execute("SELECT * FROM Donor")
donors = c.fetchall()

for donor in donors:
    print(donor)


#Query 2
c.execute("SELECT * FROM Patient WHERE blood_type='A+'")
patients_a_positive = c.fetchall()

for patient in patients_a_positive:
    print(patient)


#Query 3
c.execute("SELECT * FROM Hospital WHERE address='Mumbai'")
hospitals_in_mumbai = c.fetchall()

for hospital in hospitals_in_mumbai:
    print(hospital)


#Query 4
c.execute("SELECT * FROM Donor WHERE blood_type='O+' AND address='Kolkata'")
o_positive_donors_in_kolkata = c.fetchall()

for donor in o_positive_donors_in_kolkata:
    print(donor)


#Query 5
c.execute("SELECT COUNT(*) FROM Patient")
total_patients = c.fetchone()[0]

print("Total number of patients:", total_patients)

conn.close()