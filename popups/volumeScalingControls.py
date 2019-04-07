from PyQt5 import QtCore, QtWidgets
from popups import volumeScaling
import model, utils
import re

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
    uniques = []

    #set original data once in case validation returns an error
    model.setVolumeScaling(utils.build_list_from_table(dialogUi.tableWidget))
    mainUi.lineEdit_volumeScaling.setText(str(dialogUi.tableWidget.rowCount()))

    for row in range(0,dialogUi.tableWidget.rowCount()):
        rowOut = int(row) + int(1)
        if ( dialogUi.tableWidget.item(row,0) == None
            or not re.match("^\d+$",dialogUi.tableWidget.item(row,0).text())
            or dialogUi.tableWidget.item(row,0).text() == '0' ):
            utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte geben Sie eine ganze Zahl (>0) in Zeile "+str(rowOut)+" ein.","Fehler")
            #@TO-DO: closing and reopening the dialog seems a bit sketchy, better solution needed
            show(mainUi)
            return #only one message at a time

        scaling = int(dialogUi.tableWidget.item(row,0).text())
        if scaling not in uniques:
            uniques.append(scaling)


    #remove extra lines and adjust texts of remaining lines accordingly
    while len(uniques) < dialogUi.tableWidget.rowCount():
        dialogUi.tableWidget.removeRow(dialogUi.tableWidget.rowCount() - 1)

    uniques.sort()
    for row in range(0,len(uniques)):
        dialogUi.tableWidget.item(row,0).setText(str(uniques[row]))

    #set final result
    model.setVolumeScaling(utils.build_list_from_table(dialogUi.tableWidget))
    mainUi.lineEdit_volumeScaling.setText(str(dialogUi.tableWidget.rowCount()))

def revert_data(oldState):
    model.setVolumeScaling(oldState)

def delete_rows(ui):
    selectedRows = ui.tableWidget.selectionModel().selectedRows()
    for index in sorted(selectedRows):
        ui.tableWidget.removeRow(index.row())

def connect_buttons(dialogUi, mainUi, previousData):
    dialogUi.toolButton_add.clicked.connect(lambda: add_volumeScaling(dialogUi))
    dialogUi.toolButton_delete.clicked.connect(lambda: delete_rows(dialogUi))
    dialogUi.buttonBox.accepted.connect(lambda: update(dialogUi, mainUi))
    dialogUi.buttonBox.rejected.connect(lambda: revert_data(previousData))

def show(mainUi):
    previousData = create_copy()
    dialog = utils.customDialog(previousData,"popups.volumeScalingControls")
    dialog.ui = volumeScaling.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    header = dialog.ui.tableWidget.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    utils.fill_table_from_list(dialog.ui.tableWidget, model.getVolumeScaling())
    connect_buttons(dialog.ui, mainUi, previousData)
    dialog.exec_()
