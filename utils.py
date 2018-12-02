from PyQt5 import QtCore, QtGui, QtWidgets

def build_list_from_pocket_table(tableWidget):
    rowCount = tableWidget.rowCount()
    columnCount = tableWidget.columnCount()

    data = []

    for row in range (0, rowCount):
        dataset = []
        data.append(dataset)
        for column in range (0, columnCount):
            if column == 0:
                item = QtWidgets.QComboBox()
                old = tableWidget.cellWidget(row,column)
                for i in range (0,old.count()):
                    item.addItem(old.itemText(i))
                item.setCurrentIndex(old.currentIndex())
            else:
                item = QtWidgets.QTableWidgetItem(tableWidget.item(row,column))

            data[row].append(item)


    return data


def fill_table_from_pocket_list(tableWidget, data):
    rowIndex = 0
    for dataset in data:
        tableWidget.insertRow(rowIndex)
        columnIndex = 0

        for item in dataset:
            if columnIndex == 0:
                tableWidget.setCellWidget(rowIndex,columnIndex,item)
            else:
                tableWidget.setItem(rowIndex,columnIndex,item)
            columnIndex += 1

        rowIndex += 1

def fill_table_from_sfg_list(tableWidget, data): 
    rowIndex = 0
    for dataset in data:
        keys = dataset.keys()
        tableWidget.insertRow(rowIndex)
        columnIndex = 0

        for key in keys:
            tableWidget.setItem(rowIndex,columnIndex,QtWidgets.QTableWidgetItem(str(dataset[key])))
            columnIndex += 1

        rowIndex += 1

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
