from PyQt5 import QtCore, QtWidgets
import model, utils
from popups import sfg

def set_first_call(bool):
    global first_call
    first_call = bool

def add_sfg(dialog, material):
    rowCount = dialog.ui.tableWidget.rowCount()
    dialog.ui.tableWidget.insertRow(rowCount)
    dialog.ui.tableWidget.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(rowCount+1)))
    dialog.ui.tableWidget.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(material))

def update(dialog, mainUi):
    data = utils.build_list_from_table(dialog.ui.tableWidget)
    for dataset in data:
        for item in dataset:    
            if item.text() == '':
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Bitte alle Felder füllen")
                msg.setWindowTitle("Fehler")
                msg.exec_()
                return
    model.setSfg(data)
    dialog.close()

def exit(dialog):
    dialog.close()

def connect_buttons(dialog, mainUi, material):
    dialog.ui.toolButton_add.clicked.connect(lambda: add_sfg(dialog,material))
    dialog.ui.toolButton_confirm.clicked.connect(lambda: update(dialog, mainUi))
    dialog.ui.toolButton_cancel.clicked.connect(lambda: exit(dialog))

def show(material, mainUi):
    global first_call
    dialog = QtWidgets.QDialog()
    dialog.ui = sfg.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.ui.tableWidget.verticalHeader().setVisible(False)
    header = dialog.ui.tableWidget.horizontalHeader()
    for i in range(0,5):
        header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
    if first_call == True:
        utils.fill_table_from_sfg_list(dialog.ui.tableWidget, model.read_halbzeug(material))
        model.setSfg(utils.build_list_from_table(dialog.ui.tableWidget))
        set_first_call(False)
    else:
        utils.fill_table_from_list(dialog.ui.tableWidget, model.getSfg())
    connect_buttons(dialog, mainUi, material)
    dialog.exec_()
