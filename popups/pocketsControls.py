from PyQt5 import QtCore, QtWidgets
from popups import pockets
import model, utils


def create_copy():
    previousData = model.getPockets()
    restoredData = []

    for dataset in previousData:
        first = True
        line = []
        restoredData.append(line)
        for item in dataset:
            if first == True:
                copy = QtWidgets.QComboBox()
                for i in range (0,item.count()):
                    copy.addItem(item.itemText(i))
                copy.setCurrentIndex(item.currentIndex())

                first = False
            else:
                copy = QtWidgets.QTableWidgetItem(item)

            line.append(copy)

    return restoredData

def add_pocket(ui):
    rowCount = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(rowCount)

    comboBox = QtWidgets.QComboBox()
    sides = ["Unten (AxB)","Oben (AxB)","Vorne (BxC)","Hinten (BxC)", "Links (AxC)", "Rechts (AxC)"]
    for entry in sides:
        comboBox.addItem(entry)

    ui.tableWidget.setCellWidget(rowCount,0,comboBox)

    checkBoxItem = QtWidgets.QTableWidgetItem()
    checkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
    checkBoxItem.setCheckState(QtCore.Qt.Unchecked)
    ui.tableWidget.setItem(rowCount,2,checkBoxItem)

def revert_data(oldState):
    model.setPockets(oldState)

def update(dialogUi, mainUi):
    model.setPockets(utils.build_list_from_pocket_table(dialogUi.tableWidget))
    mainUi.lineEdit_pockets.setText(str(dialogUi.tableWidget.rowCount()))

def connect_buttons(dialogUi, mainUi, previousData):
    dialogUi.toolButton_add.clicked.connect(lambda: add_pocket(dialogUi))
    dialogUi.buttonBox.accepted.connect(lambda: update(dialogUi, mainUi))
    dialogUi.buttonBox.rejected.connect(lambda: revert_data(previousData))

def show(mainUi):
    dialog = QtWidgets.QDialog()
    dialog.ui = pockets.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    header = dialog.ui.tableWidget.horizontalHeader()
    for i in range(0,4):
        if i == 3:
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        else:
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    previousData = create_copy()
    utils.fill_table_from_pocket_list(dialog.ui.tableWidget, model.getPockets())
    connect_buttons(dialog.ui, mainUi, previousData)
    dialog.exec_()
