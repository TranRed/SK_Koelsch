from PyQt5 import QtCore, QtWidgets
import model, utils
from popups import sfg
from decimal import *
import re

def revert_data(oldState):
    model.setSfg(oldState)

def create_copy():
    previousData = model.getSfg()
    restoredData = []

    for dataset in previousData:
        first = True
        line = []
        restoredData.append(line)

        for item in dataset:
            copy = QtWidgets.QTableWidgetItem(item)
            line.append(copy)

    return restoredData

def set_first_call(bool):
    global first_call
    first_call = bool

def add_sfg(dialog, material):
    global initializing
    initializing = True
    rowCount = dialog.ui.tableWidget.rowCount()
    dialog.ui.tableWidget.insertRow(rowCount)
    dialog.ui.tableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(rowCount+1)))
    dialog.ui.tableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(material))
    dialog.ui.tableWidget.setItem(rowCount, 2, QtWidgets.QTableWidgetItem("0"))
    dialog.ui.tableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem("0"))
    dialog.ui.tableWidget.setItem(rowCount, 4, QtWidgets.QTableWidgetItem("0"))

    make_item_not_editable(dialog.ui.tableWidget.item(rowCount,0))
    make_item_not_editable(dialog.ui.tableWidget.item(rowCount,1))

    initializing = False

def update(dialog, mainUi):
    data = utils.build_list_from_table(dialog.ui.tableWidget)
    for dataset in data:
        column = 0
        for item in dataset:
            column += 1
            #text in first two items (ID, material) are automatically set and do not need to be checked here
            if column < 3:
                continue

            if item.text() == '':
                utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte alle Felder füllen","Fehler")
                return
            elif ( item.text() == '0'
                   or not re.match("^\d+$", item.text())):
                utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte geben Sie nur Zahlen (>0) ein","Fehler")
                return

    model.setSfg(data)
    dialog.set_previous(previousData = create_copy())
    dialog.close()

def exit(dialog):
    dialog.close()

def delete_rows(ui):
    selectedRows = ui.tableWidget.selectionModel().selectedRows()
    for index in sorted(selectedRows):
        ui.tableWidget.removeRow(index.row())

    for row in range(0,ui.tableWidget.rowCount()):
        ui.tableWidget.item(row,0).setText(str(row + 1))

def connect_buttons(dialog, mainUi, material):
    dialog.ui.toolButton_add.clicked.connect(lambda: add_sfg(dialog,material))
    dialog.ui.toolButton_delete.clicked.connect(lambda: delete_rows(dialog.ui))
    dialog.ui.toolButton_confirm.clicked.connect(lambda: update(dialog, mainUi))
    dialog.ui.toolButton_cancel.clicked.connect(lambda: exit(dialog))


def make_item_not_editable(item):
    item.setFlags(item.flags()  & ~QtCore.Qt.ItemIsEditable
                                & ~QtCore.Qt.ItemIsEnabled)

def handle_item_change(tableWidget):
    global initializing
    #only check after data was initialized
    if initializing == True:
        return

    for row in range(0,tableWidget.rowCount()):
        for column in range(2,4):
            if not re.match("^\d+$",tableWidget.item(row,column).text()):
                utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte geben Sie eine ganze Zahlen ein.","Fehler")
                return

def register_item_changed(tableWidget):
        tableWidget.itemChanged.connect(lambda: handle_item_change(tableWidget))



def format_number(item):
    item.setText(str(Decimal(item.text()).quantize(Decimal("0"), ROUND_HALF_UP)))

def show(material, mainUi):
    global first_call
    global initializing
    initializing = True

    dialog = utils.customDialog(previousData = create_copy(),caller = "popups.sfgControls")
    dialog.ui = sfg.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    header = dialog.ui.tableWidget.horizontalHeader()
    dialog.ui.tableWidget.setColumnHidden(0, True)
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    for i in range(2,4):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
    if first_call == True:
        utils.fill_table_from_sfg_list(dialog.ui.tableWidget, model.read_sfg(material))
        model.setSfg(utils.build_list_from_table(dialog.ui.tableWidget))
        dialog.set_previous(previousData = create_copy())
        set_first_call(False)
    else:
        utils.fill_table_from_list(dialog.ui.tableWidget, model.getSfg())



    for row in range(0,dialog.ui.tableWidget.rowCount()):
        make_item_not_editable(dialog.ui.tableWidget.item(row,0))
        make_item_not_editable(dialog.ui.tableWidget.item(row,1))

        format_number(dialog.ui.tableWidget.item(row,2))
        format_number(dialog.ui.tableWidget.item(row,3))
        format_number(dialog.ui.tableWidget.item(row,4))


    register_item_changed(dialog.ui.tableWidget)
    connect_buttons(dialog, mainUi, material)
    initializing = False
    dialog.exec_()
