import sys
import mysql.connector
from PyQt5.QtWidgets import QWidget,QApplication,QTableWidget,QTableWidgetItem,QVBoxLayout

app = QApplication(sys.argv)

qwidget = QWidget()

qwidget.setWindowTitle('Stock Control System')
qwidget.resize(425,210)

layout = QVBoxLayout()

tableWidget = QTableWidget()
tableWidget.setColumnCount(3)
tableWidget.setRowCount(5)

tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem('Name'))
tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem('Age'))
tableWidget.setHorizontalHeaderItem(2,QTableWidgetItem('Job'))

database = mysql.connector.connect(
    host = 'localhost'
    user = 'yourusername'
    password = 'yourpassword'
    )

for i in range(0, 5):
    name,age,job = 'test','test','test'
    tableWidget.setItem(i,0,QTableWidgetItem(name))
    tableWidget.setItem(i,1,QTableWidgetItem(str(age)))
    tableWidget.setItem(i,2,QTableWidgetItem(job))

layout.addWidget(tableWidget)
qwidget.setLayout(layout)
qwidget.show()
