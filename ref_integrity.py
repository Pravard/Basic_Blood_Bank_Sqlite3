import sqlite3

conn = sqlite3.connect("blood_bank.db")
c = conn.cursor()

conn.execute('PRAGMA foreign_keys = ON')

# try:
#     conn.execute('BEGIN')
#     c.execute("DELETE FROM Hospital WHERE hospital_id = ?", (1,))
# except sqlite3.IntegrityError as e:
#     print(f"Referential Integrity Error: {e}")
# finally:
#     conn.execute('ROLLBACK')

c.execute("DELETE FROM Hospital WHERE hospital_id = ?", (1,))

conn.close()
