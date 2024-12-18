import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# อ่านข้อมูลทั้งหมดจากตาราง students
c.execute("SELECT * FROM students")
#c.execute("SELECT * FROM students WHERE name = 'jenny'" )
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()