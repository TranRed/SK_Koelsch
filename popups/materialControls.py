import model
from PyQt5 import QtWidgets, QtGui
from popups import sfgControls, material
import controller, utils
import numpy as np
import skimage.io as io

class MaterialDialog(QtWidgets.QDialog, material.Ui_Material):
    def __init__(self, mode, parent=None):
        self.mode = mode
        super(MaterialDialog, self).__init__(parent)
        self.setupUi(self)
        if self.mode == 'N':
            self.pushButton_sfg.setHidden(True)
            self.pushButton_delete.setHidden(True)

def change_button_color(ui_mm, color):
    style = "background-color:" + color + ";"
    ui_mm.pushButton_colorPicker.setStyleSheet(style);

def get_color_from_image(ui_mm):
    fileDialog = QtWidgets.QFileDialog()
    path = fileDialog.getOpenFileName(None, "Bild wählen ...", "", "Images (*.png *.bmp *.jpg *.jpeg *.tif *.gif)")

    if path[0] != '':
        img = io.imread(path[0])[:, :, :, ]
        if img.shape[2] == 2:
             msg = QtWidgets.QMessageBox()
             msg.setIcon(QtWidgets.QMessageBox.Warning)
             msg.setText("Das ausgewählte bild ist graustufig. Bitte wählen Sie ein farbiges Bild.")
             msg.setWindowTitle("Fehler")
             msg.exec_()
        elif img.shape[2] == 3:
            pass #image already usable
        elif img.shape[2] == 4:
            img = io.imread(path[0])[:, :, :-1 ]
        else:
             msg = QtWidgets.QMessageBox()
             msg.setIcon(QtWidgets.QMessageBox.Warning)
             msg.setText("Fehler beim auslesen der Bilddatei. Bitte wählen sie ein anderes Bild.")
             msg.setWindowTitle("Fehler")
             msg.exec_()


        avg_color_per_row = np.average(img, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)

        global globalColorField
        globalColorField = utils.convert_rgb_to_hex(int(avg_color[0]),int(avg_color[1]),int(avg_color[2]))
        change_button_color(ui_mm, globalColorField)

def color_picker(ui_mm, recordColor):
    recordRGB = utils.convert_hex_to_rgb(recordColor)
    color = QtWidgets.QColorDialog.getColor(QtGui.QColor(recordRGB['red'],recordRGB['green'],recordRGB['blue']))
    if color.isValid():
        global  globalColorField
        globalColorField = utils.convert_rgb_to_hex(color.red(),color.green(),color.blue())
        change_button_color(ui_mm, globalColorField)

def connect_common_buttons(ui_mm, ui):
    global globalColorField
    ui_mm.pushButton_save.clicked.connect(lambda: on_click_material_save(ui_mm,ui))
    ui_mm.pushButton_colorPicker.clicked.connect(lambda: color_picker(ui_mm, globalColorField))
    ui_mm.pushButton_colorFromImage.clicked.connect(lambda: get_color_from_image(ui_mm))


def on_click_new_material(ui):
    ui_mm = MaterialDialog('N')
    global globalColorField
    globalColorField = '#ffffff'
    connect_common_buttons(ui_mm, ui)
    change_button_color(ui_mm, globalColorField)

    ui_mm.exec()

def on_click_material_save(ui_mm,ui):
    global globalColorField
    if ui_mm.mode == 'E':
        model.update_material((ui_mm.lineEdit_standard.text(),ui_mm.lineEdit_chemical.text(),ui_mm.lineEdit_density.text(),ui_mm.lineEdit_price.text(),globalColorField,ui_mm.lineEdit_material.text()))
        if model.getSfg() != []:
            model.update_halbzeug((ui_mm.lineEdit_material.text(),), utils.create_tuple_from_list(model.getSfg()))
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
             model.insert_material((ui_mm.lineEdit_material.text(),ui_mm.lineEdit_standard.text(),ui_mm.lineEdit_chemical.text(),ui_mm.lineEdit_density.text(),ui_mm.lineEdit_price.text(),globalColorField))
    controller.fill_comboBox_material(ui)
    ui_mm.accept()

def on_click_material_delete(ui_mm,ui):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("Material wirklich löschen?")
    msg.setWindowTitle("Bestätigung")
    msg.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
    buttonY = msg.button(QtWidgets.QMessageBox.Yes)
    buttonY.setText('Ja')
    buttonN = msg.button(QtWidgets.QMessageBox.No)
    buttonN.setText('Nein')
    msg.buttonClicked.connect(lambda msgbtn: confirmation(msgbtn, ui_mm, ui))
    msg.exec_()

def confirmation(button,ui_mm,ui):
    if button.text() == 'Ja':
        model.delete_material((ui_mm.lineEdit_material.text(),))
        controller.fill_comboBox_material(ui)
        ui_mm.accept()

def on_click_edit_sfg(material,mainUi):
    sfgControls.show(material,mainUi)

def on_click_edit_material(ui):
    ui_mm = MaterialDialog('E')
    index = ui.comboBox_material.currentIndex()
    resultSet = model.read_all_materials()
    record = resultSet[index]
    ui_mm.lineEdit_material.setText(str(record['material']))
    ui_mm.lineEdit_material.setReadOnly(True)
    ui_mm.lineEdit_standard.setText(str(record['normbez']))
    ui_mm.lineEdit_chemical.setText(str(record['chembez']))
    ui_mm.lineEdit_density.setText(str(record['dichte']))
    ui_mm.lineEdit_price.setText(str(record['preis']))
    global globalColorField
    globalColorField = str(record['farbe'])
    change_button_color(ui_mm, globalColorField)
    sfgControls.set_first_call(True)
    ui_mm.pushButton_sfg.clicked.connect(lambda: on_click_edit_sfg(ui_mm.lineEdit_material.text(),ui))
    ui_mm.pushButton_delete.clicked.connect(lambda: on_click_material_delete(ui_mm,ui))
    connect_common_buttons(ui_mm, ui)
    ui_mm.exec()
