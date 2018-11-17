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

        cursor = model.read_halbzeug(ui.comboBox_material.currentText())
        sfgFound = False

        for dataset in cursor:
            sizeA = int(dataset[2])
            sizeB = int(dataset[3])
            sizeC = int(dataset[4])

            if a <= sizeA and b <= sizeB and c <= sizeC:
                sfgFound = True
                set_sizes(ui,str(sizeA),str(sizeB),str(sizeC),"")
                return
            else:
                pass

        if sfgFound == False:
            set_no_size(ui)
        else:
            pass


def connect_size_fields(ui):
    ui.lineEdit_bodySideA.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_bodySideB.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_bodySideC.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_allowanceSideA.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_allowanceSideB.textChanged.connect(lambda: calc_semifinished(ui))
    ui.lineEdit_allowanceSideC.textChanged.connect(lambda: calc_semifinished(ui))

def fill_comboBox_material(ui):
    cursor = model.read_all_materials();
    for dataset in cursor:
        ui.comboBox_material.addItem(str(dataset[0]))

def connect_comboBoxes(ui):
    ui.comboBox_material.currentIndexChanged.connect(lambda: calc_semifinished(ui))

def defaults(ui):
    fill_comboBox_material(ui)
    connect_size_fields(ui)
    connect_comboBoxes(ui)
