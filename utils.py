from PyQt5 import QtWidgets
from importlib import import_module

class customDialog(QtWidgets.QDialog):
    def __init__(self, previousData, caller, parent=None):
        super().__init__(  )
        self.set_previous(previousData)
        self.controller = import_module(caller)

    #self definde closeEvent needed
    def closeEvent(self,event):
        self.controller.revert_data(self.previousData)

    def set_previous(self, previousData):
        self.previousData = previousData

def show_message_box(icon,text,title):
     msg = QtWidgets.QMessageBox()
     msg.setIcon(icon)
     msg.setText(text)
     msg.setWindowTitle(title)
     msg.exec_()

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

def build_material_dict(dataset):
    materialData = dict()
    materialData['material'] = dataset[0]
    materialData['normbez'] = dataset[1]
    materialData['chembez'] = dataset[2]
    materialData['dichte'] = dataset[3]
    materialData['preis'] = dataset[4]
    materialData['farbe'] = dataset[5]
    return materialData

def build_machine_dict(dataset):
    machineData = dict()
    machineData['id'] = dataset[0]
    machineData['bez'] = dataset[1]
    machineData['achsen'] = dataset[2]
    machineData['mss'] = dataset[3]
    machineData['ruest'] = dataset[4]
    return machineData

def create_tuple_from_list(inputData):
    dataAsArray = []
    for dataset in inputData:
        datasetAsArray = []
        for item in dataset:
            datasetAsArray.append(item.text())
        dataAsArray.append(tuple(datasetAsArray))
    dataAsTupel = tuple(dataAsArray)
    return dataAsTupel

def convert_rgb_to_hex(red,green,blue):
    colorHex = '#%02x%02x%02x' % (int(red),int(green),int(blue))
    return colorHex

def convert_hex_to_rgb(colorHex):
    rgbValues = dict()
    rgbValues['red'] = int(colorHex[1:3], 16)
    rgbValues['green'] = int(colorHex[3:5], 16)
    rgbValues['blue'] = int(colorHex[5:7], 16)
    return rgbValues
