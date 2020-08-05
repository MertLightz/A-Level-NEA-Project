import sys
import xlrd
from PyQt5.QtWidgets import QWidget,QApplication,QTableWidget,QTableWidgetItem,QVBoxLayout

wb = xlrd.open_workbook('stock.xlsx')
sheet = wb.sheet_by_index(0)

app = QApplication(sys.argv)

qwidget = QWidget()

qwidget.setWindowTitle('Stock Control System')
qwidget.resize(425,210)

layout = QVBoxLayout()

number_of_rows = sheet.nrows

tableWidget = QTableWidget()
tableWidget.setColumnCount(3)
tableWidget.setRowCount(number_of_rows)

tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem('Name'))
tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem('Age'))
tableWidget.setHorizontalHeaderItem(2,QTableWidgetItem('Job'))

for i in range(0, number_of_rows):
    name = sheet.cell_value(i,0)
    age = int(sheet.cell_value(i,1))
    job = sheet.cell_value(i,2)

    tableWidget.setItem(i,0,QTableWidgetItem(name))
    tableWidget.setItem(i,1,QTableWidgetItem(str(age)))
    tableWidget.setItem(i,2,QTableWidgetItem(job))

layout.addWidget(tableWidget)
qwidget.setLayout(layout)
qwidget.show()
