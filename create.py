import sqlite3

# สร้างการเชื่อมต่อกับฐานข้อมูล หากไม่มีจะสร้างใหม่
conn = sqlite3.connect('example.db')
c = conn.cursor()

# สร้างตารางใหม่
c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')

# ปิดการเชื่อมต่อกับฐานข้อมูล
conn.close()
