from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from sys import platform
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "STOCK CONTROL SYSTEM"
        self.top = 100
        self.left = 100
        self.width = 650
        if platform == "darwin":
            self.height = 215
        elif platform == "win32":
            self.height = 197 #+31 per row
        
        self.InitWindow()

    @pyqtSlot()
    def save_click(self):
        print('SAVED')

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.creatingTables()
        button = QPushButton('SAVE', self)
        button.setToolTip('Save any changes made to the database.')
        button.move(532,23)
        button.clicked.connect(self.save_click)
        self.show()
    
    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(1, 200)

        self.tableWidget.setItem(0,0, QTableWidgetItem("ITEM ID"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("ITEM"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("STOCK"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("PRICE"))

        self.tableWidget.setItem(1,0, QTableWidgetItem("1"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cadbury Crunchie"))
        self.tableWidget.setItem(1,2, QTableWidgetItem("5"))
        self.tableWidget.setItem(1,3, QTableWidgetItem("£0.60"))

        self.tableWidget.setItem(2,0, QTableWidgetItem("2"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cadbury Dairy Milk"))
        self.tableWidget.setItem(2,2, QTableWidgetItem("5"))
        self.tableWidget.setItem(2,3, QTableWidgetItem("£1.00"))

        self.tableWidget.setItem(3,0, QTableWidgetItem("3"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Nestle KitKat"))
        self.tableWidget.setItem(3,2, QTableWidgetItem("5"))
        self.tableWidget.setItem(3,3, QTableWidgetItem("£0.60"))

        self.tableWidget.setItem(4,0, QTableWidgetItem("4"))
        self.tableWidget.setItem(4,1, QTableWidgetItem("Ferrero Rocher"))
        self.tableWidget.setItem(4,2, QTableWidgetItem("5"))
        self.tableWidget.setItem(4,3, QTableWidgetItem("£5.00"))

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
