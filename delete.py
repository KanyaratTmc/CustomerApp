import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# ลบข้อมูลนักเรียน
c.execute("DELETE FROM students WHERE name = 'lisa'")

conn.commit()

conn.close()
