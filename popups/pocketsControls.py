from PyQt5 import QtCore, QtWidgets
from popups import pockets
import model, utils
import re


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

def selected_side(dialogUi, row):
    return dialogUi.tableWidget.cellWidget(row,0).itemText(dialogUi.tableWidget.cellWidget(row,0).currentIndex())

def add_pocket(dialogUi, mainUi):
    rowCount = dialogUi.tableWidget.rowCount()
    dialogUi.tableWidget.insertRow(rowCount)

    comboBox = QtWidgets.QComboBox()
    sides = ["A (oben)","A' (unten)","B (vorne)","B' (hinten)", "C (rechts)", "C' (links)"]
    for entry in sides:
        comboBox.addItem(entry)

    comboBox.currentIndexChanged.connect(lambda: handle_item_change(dialogUi, mainUi))

    dialogUi.tableWidget.setCellWidget(rowCount,0,comboBox)

    checkBoxItem = QtWidgets.QTableWidgetItem()
    checkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
    checkBoxItem.setCheckState(QtCore.Qt.Unchecked)
    dialogUi.tableWidget.setItem(rowCount,2,checkBoxItem)

    dialogUi.tableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem("0"))
    dialogUi.tableWidget.setItem(rowCount, 3, QtWidgets.QTableWidgetItem("0"))
    dialogUi.tableWidget.setItem(rowCount, 4, QtWidgets.QTableWidgetItem("0"))

def delete_rows(ui):
    selectedRows = ui.tableWidget.selectionModel().selectedRows()
    for index in sorted(selectedRows):
        ui.tableWidget.removeRow(index.row())

def revert_data(oldState):
    model.setPockets(oldState)

def check_pocket_size(side, a, b, depth, rowOut, mainUi):
    if (   side == "A (oben)"
        or side == "A' (unten)" ):
        checkSize_a = a
        checkSize_b = depth
        checkSize_c = b
    elif (  side == "B (vorne)"
         or side == "B' (hinten)"):
        checkSize_a = a
        checkSize_b = b
        checkSize_c = depth
    elif (  side == "C (rechts)"
        or  side == "C' (links)"):
        checkSize_a = depth
        checkSize_b = b
        checkSize_c = a


    if (    checkSize_a > int(mainUi.lineEdit_bodySideA.text())
        or  checkSize_b > int(mainUi.lineEdit_bodySideB.text())
        or  checkSize_c > int(mainUi.lineEdit_bodySideC.text())):

        utils.show_message_box(QtWidgets.QMessageBox.Warning,"Dimensionen der Tasche in Zeile "+str(rowOut)+" passen nicht auf den eigegeben Hüllkörper!","Fehler")
        #@TO-DO: closing and reopening the dialog seems a bit sketchy, better solution needed
        show(mainUi)


def update(dialogUi, mainUi):
    model.setPockets(utils.build_list_from_pocket_table(dialogUi.tableWidget))
    mainUi.lineEdit_pockets.setText(str(dialogUi.tableWidget.rowCount()))

    for row in range(0,dialogUi.tableWidget.rowCount()):
        rowOut = int(row) + int(1)
        if ( dialogUi.tableWidget.item(row,1) == None
            or not re.match("^\d+$",dialogUi.tableWidget.item(row,1).text())):
            utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte geben Sie eine ganze Zahl als Tiefe in Zeile "+str(rowOut)+" ein.","Fehler")
            #@TO-DO: closing and reopening the dialog seems a bit sketchy, better solution needed
            show(mainUi)
            return
        if ( dialogUi.tableWidget.item(row,3) == None
            or not re.match("^\d+$",dialogUi.tableWidget.item(row,3).text())):
            utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte geben Sie eine ganze Zahl als Hüllfläche: a in Zeile "+str(rowOut)+" ein.","Fehler")
            #@TO-DO: closing and reopening the dialog seems a bit sketchy, better solution needed
            show(mainUi)
            return
        if ( dialogUi.tableWidget.item(row,4) == None
            or not re.match("^\d+$",dialogUi.tableWidget.item(row,4).text())):
            utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte geben Sie eine ganze Zahl als Hüllfläche: b in Zeile "+str(rowOut)+" ein.","Fehler")
            #@TO-DO: closing and reopening the dialog seems a bit sketchy, better solution needed
            show(mainUi)
            return

        check_pocket_size(  selected_side(dialogUi, row),
                            int(dialogUi.tableWidget.item(row,3).text()),
                            int(dialogUi.tableWidget.item(row,4).text()),
                            int(dialogUi.tableWidget.item(row,1).text()),
                            rowOut, mainUi)

def find_full_pocket_depth(side, mainUi):
    if (   side == "A (oben)"
        or side == "A' (unten)" ):
        return mainUi.lineEdit_bodySideB.text()
    elif (  side == "B (vorne)"
         or side == "B' (hinten)"):
        return mainUi.lineEdit_bodySideC.text()
    elif (  side == "C (rechts)"
        or  side == "C' (links)"):
        return mainUi.lineEdit_bodySideA.text()


def handle_item_change(dialogUi, mainUi):
    #changing flags in this method to editable triggers the change Event
    #this lead to "infinite" calls ending in an runtime error
    #only doing stuff on the first call and exiting later calls prevents that
    global recursionCounter
    recursionCounter += 1

    if recursionCounter > 1:
        recursionCounter -= 1
        return

    for row in range(0,dialogUi.tableWidget.rowCount()):
        #when a new line is created new widgets are added without type
        #None-Type objects lead to runtime errors in the following code
        #no check for empty line
        if dialogUi.tableWidget.item(row,1) is None:
            continue
        if dialogUi.tableWidget.item(row,2).checkState() == QtCore.Qt.Checked:
            dialogUi.tableWidget.item(row,1).setText(find_full_pocket_depth(selected_side(dialogUi, row), mainUi))
            flags = dialogUi.tableWidget.item(row,1).flags()
            dialogUi.tableWidget.item(row,1).setFlags(flags & ~QtCore.Qt.ItemIsEditable
                                                            & ~QtCore.Qt.ItemIsEnabled )

        else:
            #getting default flags from a new object seemed to be the easiest and most reliable way while testing this
            flags = QtWidgets.QTableWidgetItem().flags()
            dialogUi.tableWidget.item(row,1).setFlags(flags)

    recursionCounter -= 1


def connect_buttons(dialogUi, mainUi, previousData):
    dialogUi.toolButton_add.clicked.connect(lambda: add_pocket(dialogUi, mainUi))
    dialogUi.toolButton_delete.clicked.connect(lambda: delete_rows(dialogUi))
    dialogUi.buttonBox.accepted.connect(lambda: update(dialogUi, mainUi))
    dialogUi.buttonBox.rejected.connect(lambda: revert_data(previousData))

def register_item_changed(dialogUi, mainUi):
        global recursionCounter
        recursionCounter = 0
        dialogUi.tableWidget.itemChanged.connect(lambda: handle_item_change(dialogUi, mainUi))

def show(mainUi):
    previousData = create_copy()
    dialog = utils.customDialog(previousData,"popups.pocketsControls")
    dialog.ui = pockets.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    header = dialog.ui.tableWidget.horizontalHeader()
    for i in range(0,4):
        if i == 3:
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        else:
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)


    utils.fill_table_from_pocket_list(dialog.ui.tableWidget, model.getPockets())
    connect_buttons(dialog.ui, mainUi, previousData)
    register_item_changed(dialog.ui, mainUi)
    dialog.exec_()
