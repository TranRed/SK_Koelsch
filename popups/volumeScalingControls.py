from PyQt5 import QtCore, QtWidgets
from popups import volumeScaling
import model, utils

def create_copy():
    previousData = model.getVolumeScaling()
    restoredData = []

    for dataset in previousData:
        line = []
        restoredData.append(line)
        for item in dataset:
            copy = QtWidgets.QTableWidgetItem(item)
            line.append(copy)

    return restoredData

def add_volumeScaling(ui):
    rowCount = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(rowCount)

def update(dialogUi, mainUi):
    model.setVolumeScaling(utils.build_list_from_table(dialogUi.tableWidget))
    mainUi.lineEdit_volumeScaling.setText(str(dialogUi.tableWidget.rowCount()))

def revert_data(oldState):
    model.setVolumeScaling(oldState)

def connect_buttons(dialogUi, mainUi, previousData):
    dialogUi.toolButton_add.clicked.connect(lambda: add_volumeScaling(dialogUi))
    dialogUi.buttonBox.accepted.connect(lambda: update(dialogUi, mainUi))
    dialogUi.buttonBox.rejected.connect(lambda: revert_data(previousData))

def show(mainUi):
    dialog = QtWidgets.QDialog()
    dialog.ui = volumeScaling.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    header = dialog.ui.tableWidget.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    previousData = create_copy()
    utils.fill_table_from_list(dialog.ui.tableWidget, model.getVolumeScaling())
    connect_buttons(dialog.ui, mainUi, previousData)
    dialog.exec_()
