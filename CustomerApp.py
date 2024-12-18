from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QListWidget, QLineEdit, QTextEdit, QMessageBox, QFileDialog, QMainWindow)
from PyQt6.QtGui import QPixmap, QFont
import sys, os
import sqlite3
from PIL import Image

con = sqlite3.connect('customers.db')
cur = con.cursor()
defaultImg = "person.png"
person_id = None

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Customers")
        self.setGeometry(450, 150, 750, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getCustomers()
        self.displayFirstRecord()

    def mainDesign(self):
        self.setStyleSheet("""
            QWidget {
                font-size: 14pt; 
                font-family: Arial Bold;
                color: #333333;
            }
            QPushButton {
                background-color: #5e90fa;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #5078c8;
            }
            QLabel {
                color: #2e2e2e;
            }
            QListWidget {
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
            QLineEdit, QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
            }
                """)
        self.customerList = QListWidget()
        self.customerList.itemClicked.connect(self.singleClick)
        self.btnNew = QPushButton("New")
        self.btnNew.clicked.connect(self.addCustomer)
        self.btnUpdate = QPushButton("Update")
        self.btnUpdate.clicked.connect(self.updateCustomer)
        self.btnDelete = QPushButton("Delete")
        self.btnDelete.clicked.connect(self.deleteCustomer)

    def layouts(self):
        
        ##################Layouts###########################
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        
        ##################Adding child layouts to main layout###########################
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout, 40)
        self.mainLayout.addLayout(self.rightMainLayout, 60)
        ########################adding widget o main layout#############################3
        self.rightTopLayout.addWidget(self.customerList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)
        ########################setting main window layout###############################
        self.setLayout(self.mainLayout)

    def addCustomer(self):
        self.newcustomer = AddCustomer()
        self.close()

    def getCustomers(self):
        query = "SELECT id, name, surname FROM customers"
        customers = cur.execute(query).fetchall()
        for customer in customers:
            self.customerList.addItem(f"{customer[0]}-{customer[1]} {customer[2]}")

    def displayFirstRecord(self):
        query = "SELECT * FROM customers ORDER BY ROWID ASC LIMIT 1"
        customer = cur.execute(query).fetchone()
        if customer:
            img = QLabel()
            img.setPixmap(QPixmap(f"images/{customer[5]}"))
            name = QLabel(customer[1])
            surname = QLabel(customer[2])
            phone = QLabel(customer[3])
            email = QLabel(customer[4])
            address = QLabel(customer[6])
            self.leftLayout.setVerticalSpacing(20)
            self.leftLayout.addRow("", img)
            self.leftLayout.addRow("Name: ", name)
            self.leftLayout.addRow("Surname :", surname)
            self.leftLayout.addRow("Phone :", phone)
            self.leftLayout.addRow("Email :", email)
            self.leftLayout.addRow("Address:", address)

    def singleClick(self):
        for i in reversed(range(self.leftLayout.count())):
            print(i)
            widget = self.leftLayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        customer = self.customerList.currentItem().text()
        print(customer)
        id = customer.split("-")[0]
        query = "SELECT * FROM customers WHERE id=?"
        person = cur.execute(query, (id,)).fetchone()
        if person:
            img = QLabel()
            img.setPixmap(QPixmap(f"images/{person[5]}"))
            name = QLabel(person[1])
            surname = QLabel(person[2])
            phone = QLabel(person[3])
            email = QLabel(person[4])
            address = QLabel(person[6])
            self.leftLayout.setVerticalSpacing(20)
            self.leftLayout.addRow("", img)
            self.leftLayout.addRow("Name: ", name)
            self.leftLayout.addRow("Surname :", surname)
            self.leftLayout.addRow("Phone :", phone)
            self.leftLayout.addRow("Email :", email)
            self.leftLayout.addRow("Address:", address)

    def deleteCustomer(self):
        if self.customerList.selectedItems():
            person = self.customerList.currentItem().text()
            id = person.split("-")[0]
            mbox = QMessageBox.question(self, "Warning", "Are you sure to delete this person?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if mbox == QMessageBox.StandardButton.Yes:
                try:
                    query = "DELETE FROM customers WHERE id=?"
                    cur.execute(query, (id,))
                    con.commit()
                    QMessageBox.information(self, "Info!!!", "Person has been deleted")
                    self.close()
                    self.main = Main()
                except Exception as e:
                    QMessageBox.information(self, "Warning!!!", f"Person has not been deleted. Error: {e}")
        else:
            QMessageBox.information(self, "Warning!!!", "Please select a person to delete")

    def updateCustomer(self):
        global person_id
        if self.customerList.selectedItems():
            person = self.customerList.currentItem().text()
            person_id = person.split("-")[0]
            self.updateWindow = UpdateCustomer()
            self.close()
        else:
            QMessageBox.information(self, "Warning!!!", "Please select a person to update")


class AddCustomer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Customers")
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.show()

    def UI(self):
        global defaultImg # ทำให้ตัวแปรนี้สามารถเข้าถึงได้จากฟังก์ชันอื่นๆ
        self.mainDesign()
        self.layouts()
    
    def closeEvent(self,event):
        self.main=Main()

    def mainDesign(self):
        self.setStyleSheet("""
            QWidget {
                font-size: 14pt; 
                font-family: Arial Bold;
                color: #333333;
            }
            QPushButton {
                background-color: #5e90fa;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #5078c8;
            }
            QLabel {
                color: #2e2e2e;
            }
            QListWidget {
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
            QLineEdit, QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
            }
                """)
        self.title = QLabel("Add Person")
        self.title.setStyleSheet('font-size: 24pt; font-family:Arial Bold;')
        self.imgLabel = QLabel()
        self.imgLabel.setPixmap(QPixmap(f"images/{defaultImg}"))
        self.nameLabel = QLabel("Name:")
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Enter Customer Name")
        self.surnameLabel = QLabel("Surname:")
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText("Enter Customer Surname")
        self.phoneLabel = QLabel("Phone:")
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter Customer Phone Number")
        self.emailLabel = QLabel("Email:")
        self.emailEntry = QLineEdit()
        self.emailEntry.setPlaceholderText("Enter Customer Email")
        self.imgButton = QPushButton("Browse")
        self.imgButton.clicked.connect(self.uploadImage)
        self.addressLabel = QLabel("Address:")
        self.addressEditor = QTextEdit()
        self.addButton = QPushButton("Add")
        self.addButton.clicked.connect(self.addCustomer)

    def layouts(self):
        ##########################creating main layouts#######################
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        
        ####################adding child layouts to main layout################
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgLabel)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110, 20, 10, 30)
        
        self.bottomLayout.addRow(self.nameLabel, self.nameEntry)
        self.bottomLayout.addRow(self.surnameLabel, self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLabel, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLabel, self.emailEntry)
        self.bottomLayout.addRow(self.imgButton)
        self.bottomLayout.addRow(self.addressLabel, self.addressEditor)
        self.bottomLayout.addRow("", self.addButton)

        ###################setting main layout for window##############################
        self.setLayout(self.mainLayout)


    def uploadImage(self):
        global defaultImg 
        size = (128, 128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')
        if ok:
            defaultImg = os.path.basename(self.fileName) 
            if not os.path.exists('images'): 
                os.makedirs('images') 
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save(f"images/{defaultImg}") # บันทึกภาพที่ปรับขนาดแล้ว
            self.imgLabel.setPixmap(QPixmap(f"images/{defaultImg}"))


    def addCustomer(self):
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImg
        address = self.addressEditor.toPlainText()
        if name and surname and phone:
            try:
                query = "INSERT INTO customers (name, surname, phone, email, img, address) VALUES (?, ?, ?, ?, ?, ?)"
                cur.execute(query, (name, surname, phone, email, img, address))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been added")
                self.close()
                self.main = Main()
            except Exception as e:
                QMessageBox.information(self, "Warning", "Person has not been added. Error: " + str(e))
        else:
            QMessageBox.information(self, "Warning", "Fields cannot be empty")






class UpdateCustomer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Customer")
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.show()

    def UI(self):
        self.getPerson()
        self.mainDesign()
        self.layouts()

    def closeEvent(self,event):
        self.main=Main()

    def getPerson(self):
        global person_id
        query = "SELECT * FROM customers WHERE id=?"
        customer = cur.execute(query, (person_id,)).fetchone()
        self.name = customer[1]
        self.surname = customer[2]
        self.phone = customer[3]
        self.email = customer[4]
        self.image = customer[5]
        self.address = customer[6]

    def mainDesign(self):
        self.setStyleSheet("""
            QWidget {
                font-size: 14pt; 
                font-family: Arial Bold;
                color: #333333;
            }
            QPushButton {
                background-color: #5e90fa;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #5078c8;
            }
            QLabel {
                color: #2e2e2e;
            }
            QListWidget {
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
            QLineEdit, QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
            }
                """)
        self.title = QLabel("Update Person")
        self.title.setStyleSheet('font-size: 24pt; font-family:Arial Bold;')
        self.imgLabel = QLabel()
        self.imgLabel.setPixmap(QPixmap(f"images/{self.image}"))
        self.nameLabel = QLabel("Name:")
        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.name)
        self.surnameLabel = QLabel("Surname:")
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setText(self.surname)
        self.phoneLabel = QLabel("Phone:")
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setText(self.phone)
        self.emailLabel = QLabel("Email:")
        self.emailEntry = QLineEdit()
        self.emailEntry.setText(self.email)
        self.imgButton = QPushButton("Browse")
        self.imgButton.clicked.connect(self.uploadImage)
        self.addressLabel = QLabel("Address:")
        self.addressEditor = QTextEdit()
        self.addressEditor.setText(self.address)
        self.updateButton = QPushButton("Update")
        self.updateButton.clicked.connect(self.updateCustomer)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgLabel)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110, 20, 10, 30)
        
        self.bottomLayout.addRow(self.nameLabel, self.nameEntry)
        self.bottomLayout.addRow(self.surnameLabel, self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLabel, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLabel, self.emailEntry)
        self.bottomLayout.addRow(self.imgButton)
        self.bottomLayout.addRow(self.addressLabel, self.addressEditor)
        self.bottomLayout.addRow("", self.updateButton)

        self.setLayout(self.mainLayout)

    def uploadImage(self):
        size = (128, 128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')
        if ok:
            self.image = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save(f"images/{self.image}")
            self.imgLabel.setPixmap(QPixmap(f"images/{self.image}"))

    def updateCustomer(self):
        global person_id
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        address = self.addressEditor.toPlainText()
        if name and surname and phone:
            try:
                query = "UPDATE customers SET name=?, surname=?, phone=?, email=?, img=?, address=? WHERE id=?"
                cur.execute(query, (name, surname, phone, email, self.image, address, person_id))
                con.commit()
                QMessageBox.information(self, "Success", "Person has been updated")
                self.close()
                self.main = Main()
            except Exception as e:
                QMessageBox.information(self, "Warning", "Person has not been updated. Error: " + str(e))
        else:
            QMessageBox.information(self, "Warning", "Fields cannot be empty")

def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()