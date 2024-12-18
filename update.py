import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# อัปเดตข้อมูลนักเรียน
c.execute("UPDATE students SET age = 23 WHERE name = 'jenny'")

conn.commit()

conn.close()
