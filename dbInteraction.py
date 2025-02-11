import sqlite3

conn = sqlite3.connect('db.sqlite')

cursor = conn.cursor()

cursor.execute('SELECT * FROM User')

rows = cursor.fetchall()

for row in rows:
    print(row.name)
    print("HELLO")