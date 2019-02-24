from PyQt5 import QtCore, QtWidgets
import model, figure

from popups import pocketsControls, volumeScalingControls, sfgControls, materialControls, calculationControls


def perform_calculation(ui):
    calculationControls.show(ui)


def set_sizes(ui,a,b,c,message):
    ui.lineEdit_semifinishedSideA.setText(a)
    ui.lineEdit_semifinishedSideB.setText(b)
    ui.lineEdit_semifinishedSideC.setText(c)
    ui.label_sizeNotFound.setText(message)

    global cuboid
    materialData = model.read_material(ui.comboBox_material.currentText()[:6])

    if ( int(a) == 0 or int(b) == 0 or int(c) == 0 ):
        #show default cuboid
        cuboid.change_plot(0, 1, 1, materialData)
    else:
        cuboid.change_plot(int(a), int(b), int(c), materialData)

def set_no_size(ui):
    #size not available
    set_sizes(ui,"0","0","0","Kein passendes Halbzeug verfügbar")

def build_message_for_alternative(alt, sfgA, sfgB, sfgC):
    message = "Als Halbzeug " + str(sfgA) + "x" + str(sfgB) + "x" + str(sfgC) +" verfügbar. " + alt
    return message

def create_sfg_checkresult(volume,found,message):
    result = dict()

    result['volume'] = volume
    result['found'] = found
    result['message'] = message

    return result

def check_if_sfg_is_a_valid_alternative(a,b,c,sfgA,sfgB,sfgC,volume):

    if a <= sfgB:
        if b<=sfgA and c<=sfgC:
            result = create_sfg_checkresult(volume, True, build_message_for_alternative("(BxAxC)", sfgA, sfgB, sfgC ))
            return result
        elif b<=sfgC and c<=sfgB:
            result = create_sfg_checkresult(volume, True, build_message_for_alternative("(CxAxB)", sfgA, sfgB, sfgC ))
            return result

    if a <= sfgC:
        if b<=sfgA and c<=sfgB:
            result = create_sfg_checkresult(volume, True, build_message_for_alternative("(BxCxA)", sfgA, sfgB, sfgC ))
            return result
        elif b<=sfgB and c<=sfgA:
            result = create_sfg_checkresult(volume, True, build_message_for_alternative("(CxBxA)", sfgA, sfgB, sfgC ))
            return result

    if b <= sfgC:
        if a<=sfgA and c<=sfgB:
            result = create_sfg_checkresult(volume, True, build_message_for_alternative("(AxCxB)", sfgA, sfgB, sfgC ))
            return result
        elif a<=sfgB and c<=sfgA:
            result = create_sfg_checkresult(volume, True, build_message_for_alternative("(CxAxB)", sfgA, sfgB, sfgC ))
            return result

    result = create_sfg_checkresult(volume, False, "")
    return result

def are_side_inputs_valid(ui):
    if ((not ui.lineEdit_bodySideA.text().isdigit()) or
        (not ui.lineEdit_bodySideB.text().isdigit()) or
        (not ui.lineEdit_bodySideC.text().isdigit()) or
        (not ui.lineEdit_allowanceSideA.text().isdigit()) or
        (not ui.lineEdit_allowanceSideB.text().isdigit()) or
        (not ui.lineEdit_allowanceSideC.text().isdigit())):
        return False
    else:
        return True

def find_next_fitting_sfg(semiFinishedGoods,ui):
    sfgFound = False
    alternativeFound = False
    message = ""

    a = int(ui.lineEdit_bodySideA.text()) + int(ui.lineEdit_allowanceSideA.text())
    b = int(ui.lineEdit_bodySideB.text()) + int(ui.lineEdit_allowanceSideB.text())
    c = int(ui.lineEdit_bodySideC.text()) + int(ui.lineEdit_allowanceSideC.text())

    for sfg in semiFinishedGoods:
        sizeA = int(sfg['a'])
        sizeB = int(sfg['b'])
        sizeC = int(sfg['stange'])
        volume = sizeA * sizeB * c
        sfgIsCurrent = False

        if a <= sizeA and b <= sizeB and c <= sizeC and sfgFound == False:
            sfgIsCurrent = True
            sfgFound = True
            sfgFoundVolume = volume
            set_sizes(ui,str(sizeA),str(sizeB),str(c),"")

        if alternativeFound == False:
            checkResult = check_if_sfg_is_a_valid_alternative(a,b,c,sizeA,sizeB,sizeC,volume)
            alternativeFound = checkResult['found']
            if alternativeFound == True and sfgIsCurrent == False:
                message = checkResult['message']
                if sfgFound == True:
                    if checkResult['volume'] >= sfgFoundVolume:
                        #only show message if alternative is smaller
                        message = ""

    if sfgFound == False:
        set_no_size(ui)

    if alternativeFound == True and message != "":
        ui.label_sizeNotFound.setText(message)

def calc_semifinished(ui):
    if ui.comboBox_material.currentText() != '':
        if are_side_inputs_valid(ui) == False:
            set_sizes(ui,"0","0","0","Bitte nur Zahlen eingeben")
        else:
            find_next_fitting_sfg(model.read_halbzeug(ui.comboBox_material.currentText()[:6]),ui)


def connect_size_fields(ui):
    ui.lineEdit_bodySideA.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_bodySideB.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_bodySideC.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_allowanceSideA.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_allowanceSideB.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_allowanceSideC.textChanged.connect(lambda: calc_semifinished(ui))

def refresh_comboBox_material(ui, material, normbez, chembez):
    fill_comboBox_material(ui)
    index = ui.comboBox_material.findText((material + " - " + normbez + " - " + chembez),
                                            QtCore.Qt.MatchFixedString)
    if index >= 0:
         ui.comboBox_material.setCurrentIndex(index)

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

def define_volumeScaling(mainUi):
    volumeScalingControls.show(mainUi)

def define_pockets(mainUi):
    pocketsControls.show(mainUi)

def fill_comboBox_machine(ui):
    resultSet = model.read_all_machines();
    for dataset in resultSet:
        ui.comboBox_machine.addItem(str(dataset['id']) + " - " + str(dataset['bez']))

def connect_comboBoxes(ui):
    ui.comboBox_material.currentIndexChanged.connect(lambda: calc_semifinished(ui))

def connect_pushButtons(ui):
    ui.pushButton_pockets.clicked.connect(lambda: define_pockets(ui))
    ui.pushButton_volumeScaling.clicked.connect(lambda: define_volumeScaling(ui))
    ui.pushButton_calculation.clicked.connect(lambda: perform_calculation(ui))

def connect_actions(ui):
    ui.action_newMaterial.triggered.connect(lambda: materialControls.on_click_new_material(ui))
    ui.action_editMaterial.triggered.connect(lambda: materialControls.on_click_edit_material(ui))

def defaults(ui):
    add_filter_to_comboBox(ui.comboBox_material)
    add_filter_to_comboBox(ui.comboBox_machine)
    add_filter_to_comboBox(ui.comboBox_aging)
    fill_comboBox_material(ui)
    fill_comboBox_machine(ui)
    connect_actions(ui)
    connect_size_fields(ui)
    connect_comboBoxes(ui)
    connect_pushButtons(ui)
    model.initRuntimeVariables()
    global cuboid
    cuboid = figure.Window(ui.figure)
    calc_semifinished(ui)
