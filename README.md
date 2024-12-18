# My Customers Application
โปรแกรม `My Customers` ถูกพัฒนาด้วย Python และ PyQt6 เพื่อจัดการข้อมูลลูกค้า โปรแกรมสามารถเพิ่ม แก้ไข และลบข้อมูลลูกค้า รวมถึงแสดงรายละเอียดต่างๆ เช่น ชื่อ นามสกุล เบอร์โทรศัพท์ อีเมล และที่อยู่ นอกจากนี้ยังรองรับการอัปโหลดรูปภาพโปรไฟล์ลูกค้า

## ฟีเจอร์
1. **เพิ่มลูกค้า:** บันทึกข้อมูลลูกค้าพร้อมรูปภาพ
2. **แก้ไขข้อมูลลูกค้า:** อัปเดตข้อมูลลูกค้าที่มีอยู่
3. **ลบลูกค้า:** ลบข้อมูลลูกค้าจากฐานข้อมูล
4. **แสดงรายการลูกค้า:** แสดงรายการลูกค้าในรูปแบบรายการ
5. **แสดงข้อมูลลูกค้า:** แสดงรายละเอียดลูกค้าเมื่อเลือกจากรายการ

## การติดตั้ง
1. ติดตั้ง Python (เวอร์ชัน 3.6 ขึ้นไป)
2. ติดตั้งไลบรารีที่จำเป็น:
   ```bash
   pip install PyQt6 Pillow
    ```
3. สร้างไฟล์ฐานข้อมูล SQLite customers.db และโฟลเดอร์ images สำหรับจัดเก็บรูปภาพ
## การใช้งาน
1. รันไฟล์ main.py ด้วยคำสั่ง:
 ```
python main.py
 ```

2. ใช้ GUI เพื่อจัดการข้อมูลลูกค้า

## Program Description
The My Customers application is developed using Python and PyQt6 to manage customer information. The program allows adding, updating, and deleting customer records, displaying details such as name, surname, phone number, email, and address. It also supports uploading profile pictures for customers.

## Features 🛠️
- Add Customer: Save customer data along with a profile picture.
- Edit Customer: Update existing customer details.
- Delete Customer: Remove customer data from the database.
- Customer List: Display a list of all customers.
- View Customer Details: Show customer details when selected from the list.
## Installation ⚙️
1. Install Python (version 3.6 or later).
2. Install the required libraries:
 ```
pip install PyQt6 Pillow
 ```
3. Create a SQLite database file named customers.db and an images folder for storing profile pictures.
## Usage 🚀
1. Run the main.py file using the command:
 ```
python main.py
 ```
2. Use the GUI to manage customer records.

---

Developer 👨‍💻
Kanyarat Thammachot
© 2024