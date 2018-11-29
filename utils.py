from PyQt5 import QtCore, QtGui, QtWidgets

def build_list_from_table(tableWidget):
    rowCount = tableWidget.rowCount()
    columnCount = tableWidget.columnCount()

    data = []

    for row in range (0, rowCount):
        dataset = []
        data.append(dataset)
        for column in range (0, columnCount):
            item = QtWidgets.QTableWidgetItem(tableWidget.item(row,column))
            data[row].append(item)

    return data


def fill_table_from_list(tableWidget, data):
    rowIndex = 0
    for dataset in data:
        tableWidget.insertRow(rowIndex)
        columnIndex = 0

        for item in dataset:
            tableWidget.setItem(rowIndex,columnIndex,item)
            columnIndex += 1

        rowIndex += 1
