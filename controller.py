from PyQt5 import QtCore, QtGui, QtWidgets
import main, model
import model
import pockets
import utils

def set_sizes(ui,a,b,c,msg):
    ui.lineEdit_semifinishedSideA.setText(a)
    ui.lineEdit_semifinishedSideB.setText(b)
    ui.lineEdit_semifinishedSideC.setText(c)
    ui.label_sizeNotFound.setText(msg)

def set_no_size(ui):
    #size not available
    set_sizes(ui,"0","0","0","Kein passendes Halbzeug verfügbar")

def build_alt_message(alt, sfgA, sfgB, sfgC):
    msg = "Als Halbzeug " + str(sfgA) + "x" + str(sfgB) + "x" + str(sfgC) +" verfügbar. " + alt
    return msg

def find_alternative(a,b,c,sfgA,sfgB,sfgC,volume):
    result = dict()
    result['volume'] = volume

    if a <= sfgA:
        if c<=sfgB and b<=sfgC:
            result['found'] = True
            result['msg'] = build_alt_message("(AxCxB)", sfgA, sfgB, sfgC )
            return result
    elif b<=sfgA:
        if a<=sfgB and c<=sfgC:
            result['found'] = True
            result['msg'] = build_alt_message("(BxAxC)", sfgA, sfgB, sfgC )
            return result
        elif c<=sfgB and a<=sfgC:
            result['found'] = True
            result['msg'] = build_alt_message("(BxCxA)", sfgA, sfgB, sfgC )
            return result
    elif c<=sfgA:
        if a<=sfgB and b<=sfgC:
            result['found'] = True
            result['msg'] = build_alt_message("(CxAxB)", sfgA, sfgB, sfgC )
            return result
        elif b<=sfgB and a<=sfgC:
            result['found'] = True
            result['msg'] = build_alt_message("(CxBxA)", sfgA, sfgB, sfgC )
            return result

    result['found'] = False
    result['msg'] = ""
    return result

def calc_semifinished(ui):
    if ui.comboBox_material.currentText() != '':
        if (
            (not ui.lineEdit_bodySideA.text().isdigit()) or
            (not ui.lineEdit_bodySideB.text().isdigit()) or
            (not ui.lineEdit_bodySideC.text().isdigit()) or
            (not ui.lineEdit_allowanceSideA.text().isdigit()) or
            (not ui.lineEdit_allowanceSideB.text().isdigit()) or
            (not ui.lineEdit_allowanceSideC.text().isdigit())):
            set_sizes(ui,"0","0","0","Bitte nur Zahlen eingeben")
        else:
            a = int(ui.lineEdit_bodySideA.text()) + int(ui.lineEdit_allowanceSideA.text())
            b = int(ui.lineEdit_bodySideB.text()) + int(ui.lineEdit_allowanceSideB.text())
            c = int(ui.lineEdit_bodySideC.text()) + int(ui.lineEdit_allowanceSideC.text())
    
            resultSet = model.read_halbzeug(ui.comboBox_material.currentText()[:6])
            sfgFound = False
            altFound = False
            msg = ""
    
            for dataset in resultSet:
                sizeA = int(dataset['a'])
                sizeB = int(dataset['b'])
                sizeC = int(dataset['c'])
                volume = int(dataset['volumen'])
                sfgIsCurrent = False
    
                if a <= sizeA and b <= sizeB and c <= sizeC and sfgFound == False:
                    sfgIsCurrent = True
                    sfgFound = True
                    sfgFoundVolume = volume
                    set_sizes(ui,str(sizeA),str(sizeB),str(sizeC),"")
    
                if altFound == False:
    
                    alternative = find_alternative(a,b,c,sizeA,sizeB,sizeC,volume)
                    altFound = alternative['found']
                    if altFound == True and sfgIsCurrent == False:
                        msg = alternative['msg']
                        if sfgFound == True:
                            if alternative['volume'] >= sfgFoundVolume:
                                #only show message if alternative is smaller
                                msg = ""
    
            if sfgFound == False:
                set_no_size(ui)
    
            if altFound == True and msg != "":
                ui.label_sizeNotFound.setText(msg)

def connect_size_fields(ui):
    ui.lineEdit_bodySideA.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_bodySideB.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_bodySideC.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_allowanceSideA.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_allowanceSideB.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_allowanceSideC.textChanged.connect(lambda: calc_semifinished(ui))

def fill_comboBox_material(ui):
    ui.comboBox_material.clear()
    resultSet = model.read_all_materials();
    for dataset in resultSet:
        ui.comboBox_material.addItem(str(dataset['material']) + " - " + str(dataset['normbez']) + " - " + str(dataset['chembez']))

def add_filter_to_comboBox(comboBox):
    #the widget accepts focus by both tabbing and clicking
    comboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
    comboBox.setEditable(True)

    # add a filter model to filter matching items
    comboBox.pFilterModel = QtCore.QSortFilterProxyModel(comboBox)
    comboBox.pFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
    comboBox.pFilterModel.setSourceModel(comboBox.model())

    # add a completer, which uses the filter model
    comboBox.completer = QtWidgets.QCompleter(comboBox.pFilterModel, comboBox)

    # always show all (filtered) completions
    comboBox.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
    comboBox.setCompleter(comboBox.completer)

    # connect signals
    comboBox.lineEdit().textEdited.connect(comboBox.pFilterModel.setFilterFixedString)
    comboBox.completer.activated.connect(lambda:on_completer_activated(comboBox,comboBox.currentText()))

# on selection of an item from the completer, select the corresponding item from combobox
def on_completer_activated(comboBox, text):
    if text:
        index = comboBox.findText(text)
        comboBox.setCurrentIndex(index)
        comboBox.activated[str].emit(comboBox.itemText(index))

def add_pocket(ui):
    rowCount = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(rowCount)
    checkBoxItem = QtWidgets.QTableWidgetItem()
    checkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
    checkBoxItem.setCheckState(QtCore.Qt.Unchecked)
    ui.tableWidget.setItem(rowCount,2,checkBoxItem)


def update_pocket_data(dialogUi, mainUi):
    model.setPockets(utils.build_list_from_table(dialogUi.tableWidget))
    mainUi.lineEdit_pockets.setText(str(dialogUi.tableWidget.rowCount()))

def connect_pocket_buttons(dialogUi, mainUi):
    dialogUi.toolButton_add.clicked.connect(lambda: add_pocket(dialogUi))
    dialogUi.buttonBox.accepted.connect(lambda: update_pocket_data(dialogUi, mainUi))

def define_pockets(mainUi):
    dialog =  QtWidgets.QDialog()
    dialog.ui = pockets.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    header = dialog.ui.tableWidget.horizontalHeader()
    for i in range(0,4):
        if i == 3:
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        else:
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
    utils.fill_table_from_list(dialog.ui.tableWidget, model.getPockets())
    connect_pocket_buttons(dialog.ui, mainUi)
    dialog.exec_()

def fill_comboBox_machine(ui):
    resultSet = model.read_all_machines();
    for dataset in resultSet:
        ui.comboBox_machine.addItem(str(dataset['bez']))

def connect_comboBoxes(ui):
    ui.comboBox_material.currentIndexChanged.connect(lambda: calc_semifinished(ui))

def connect_pushButtons(ui):
    ui.pushButton_newMaterial.clicked.connect(lambda: on_click_new_material(ui))
    ui.pushButton_editMaterial.clicked.connect(lambda: on_click_edit_material(ui))  

def on_click_new_material(ui):
    ui_mm = main.MaterialDialog('N')
    ui_mm.pushButton_save.clicked.connect(lambda: on_click_material_save(ui_mm,ui))
    ui_mm.exec()

def on_click_material_save(ui_mm,ui):
    if ui_mm.mode == 'E':
        model.update_material((ui_mm.lineEdit_standard.text(),ui_mm.lineEdit_chemical.text(),ui_mm.lineEdit_density.text(),ui_mm.lineEdit_price.text(),ui_mm.lineEdit_material.text()))
    elif ui_mm.mode == 'N':
        if ( ui_mm.lineEdit_material.text() == '' or
             ui_mm.lineEdit_standard.text() == '' or
             ui_mm.lineEdit_chemical.text() == '' or
             ui_mm.lineEdit_density.text() == '' or
             ui_mm.lineEdit_price.text() == '' ):
             msg = QtWidgets.QMessageBox()
             msg.setIcon(QtWidgets.QMessageBox.Warning)
             msg.setText("Bitte alle Felder füllen")
             msg.setWindowTitle("Fehler")
             msg.exec_()
             return
        else:
             model.insert_material((ui_mm.lineEdit_material.text(),ui_mm.lineEdit_standard.text(),ui_mm.lineEdit_chemical.text(),ui_mm.lineEdit_density.text(),ui_mm.lineEdit_price.text()))
    fill_comboBox_material(ui)
    ui_mm.accept()

def on_click_material_delete(ui_mm,ui):
    model.delete_material((ui_mm.lineEdit_material.text(),))
    fill_comboBox_material(ui)
    ui_mm.accept()
                           
def on_click_edit_material(ui):
    ui_mm = main.MaterialDialog('E')
    index = ui.comboBox_material.currentIndex()
    resultSet = model.read_all_materials()
    record = resultSet[index]
    ui_mm.lineEdit_material.setText(str(record['material']))
    ui_mm.lineEdit_material.setReadOnly(True)
    ui_mm.lineEdit_standard.setText(str(record['normbez']))   
    ui_mm.lineEdit_chemical.setText(str(record['chembez']))   
    ui_mm.lineEdit_density.setText(str(record['dichte']))   
    ui_mm.lineEdit_price.setText(str(record['preis']))       
    ui_mm.pushButton_save.clicked.connect(lambda: on_click_material_save(ui_mm,ui))
    ui_mm.pushButton_delete.clicked.connect(lambda: on_click_material_delete(ui_mm,ui))
    ui_mm.exec()

def connect_buttons(ui):
    ui.pushButton_pockets.clicked.connect(lambda: define_pockets(ui))

def defaults(ui):
    add_filter_to_comboBox(ui.comboBox_material)
    add_filter_to_comboBox(ui.comboBox_machine)
    add_filter_to_comboBox(ui.comboBox_aging)
    fill_comboBox_material(ui)
    fill_comboBox_machine(ui)
    connect_size_fields(ui)
    connect_comboBoxes(ui)
    connect_pushButtons(ui)
    connect_buttons(ui)
    model.initPockets()
