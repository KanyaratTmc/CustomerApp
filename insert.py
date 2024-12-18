import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# เพิ่มข้อมูลนักเรียน
#c.execute("INSERT INTO students (name, age) VALUES ('lisa', 26)")
c.execute("INSERT INTO students (name, age) VALUES ('jenny', 27)")

# บันทึกการเปลี่ยนแปลง
conn.commit()

conn.close()
