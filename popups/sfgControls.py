from PyQt5 import QtCore, QtWidgets
import model, utils
from popups import sfg

def create_copy():
    previousData = model.getSfg()
    restoredData = []

    for dataset in previousData:
        line = []
        restoredData.append(line)
        for item in dataset:
            copy = QtWidgets.QTableWidgetItem(item)
            line.append(copy)

    return restoredData

def add_sfg(ui, material):
    rowCount = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(rowCount)
    ui.tableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(rowCount+1)))
    ui.tableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(material))

def update(dialogUi, mainUi):
    model.setSfg(utils.build_list_from_table(dialogUi.tableWidget))

def revert_data(oldState):
    model.setSfg(oldState)

def connect_buttons(dialogUi, mainUi, previousData,material):
    dialogUi.toolButton_add.clicked.connect(lambda: add_sfg(dialogUi,material))
    dialogUi.buttonBox.accepted.connect(lambda: update(dialogUi, mainUi))
    dialogUi.buttonBox.rejected.connect(lambda: revert_data(previousData))

def show(material, mainUi):
    dialog = QtWidgets.QDialog()
    dialog.ui = sfg.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.ui.tableWidget.verticalHeader().setVisible(False)
    header = dialog.ui.tableWidget.horizontalHeader()
    for i in range(0,5):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
    previousData = create_copy()
    utils.fill_table_from_sfg_list(dialog.ui.tableWidget, model.read_halbzeug(material))
    connect_buttons(dialog.ui, mainUi, previousData, material)
    dialog.exec_()
