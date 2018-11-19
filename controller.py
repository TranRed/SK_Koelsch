from PyQt5 import QtCore, QtGui, QtWidgets
import model

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
    
    #the widget accepts focus by both tabbing and clicking
    ui.comboBox_material.setFocusPolicy(QtCore.Qt.StrongFocus)
    ui.comboBox_material.setEditable(True)
    
    # add a filter model to filter matching items
    ui.comboBox_material.pFilterModel = QtCore.QSortFilterProxyModel(ui.comboBox_material)
    ui.comboBox_material.pFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
    ui.comboBox_material.pFilterModel.setSourceModel(ui.comboBox_material.model())

    # add a completer, which uses the filter model
    ui.comboBox_material.completer = QtWidgets.QCompleter(ui.comboBox_material.pFilterModel, ui.comboBox_material)
    
    # always show all (filtered) completions
    ui.comboBox_material.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
    ui.comboBox_material.setCompleter(ui.comboBox_material.completer)

    # connect signals
    ui.comboBox_material.lineEdit().textEdited.connect(ui.comboBox_material.pFilterModel.setFilterFixedString)
    ui.comboBox_material.completer.activated.connect(lambda:on_completer_activated(ui,ui.comboBox_material.currentText()))
    
    resultSet = model.read_all_materials();
    for dataset in resultSet:
        ui.comboBox_material.addItem(str(dataset['material']) + " - " + str(dataset['normbez']) + " - " + str(dataset['chembez']))

# on selection of an item from the completer, select the corresponding item from combobox 
def on_completer_activated(ui, text):
    if text:
        index = ui.comboBox_material.findText(text)
        ui.comboBox_material.setCurrentIndex(index)
        ui.comboBox_material.activated[str].emit(ui.comboBox_material.itemText(index))

def fill_comboBox_maschine(ui):
    resultSet = model.read_all_machines();
    for dataset in resultSet:
        ui.comboBox_machine.addItem(str(dataset['bez']))

def connect_comboBoxes(ui):
    ui.comboBox_material.currentIndexChanged.connect(lambda: calc_semifinished(ui))

def defaults(ui):
    fill_comboBox_material(ui)
    fill_comboBox_maschine(ui)
    connect_size_fields(ui)
    connect_comboBoxes(ui)
