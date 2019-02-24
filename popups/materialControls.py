import model
from PyQt5 import QtWidgets, QtGui
from popups import sfgControls, material
import controller, utils
import numpy as np
import skimage.io as io
import re
import locale
from decimal import *

class colorField():
    def __init__(self):
        self._colorValue = '#ffffff'

    def getColorValue(self):
        return self._colorValue

    def setColorValue(self, color):
        self._colorValue = color


class MaterialDialog(QtWidgets.QDialog, material.Ui_Material):
    def __init__(self, mode, parent=None):
        self.mode = mode
        super(MaterialDialog, self).__init__(parent)
        self.setupUi(self)
        if self.mode == 'N':
            self.pushButton_sfg.setHidden(True)
            self.pushButton_delete.setHidden(True)

def change_button_color(ui_mm, globalColor):
    style = "background-color:" + globalColor.getColorValue() + ";"
    ui_mm.pushButton_colorPicker.setStyleSheet(style);

def get_color_from_image(ui_mm, globalColor):
    fileDialog = QtWidgets.QFileDialog()
    path = fileDialog.getOpenFileName(None, "Bild wählen ...", "", "Images (*.png *.bmp *.jpg *.jpeg *.tif *.gif)")

    if path[0] != '':
        image = io.imread(path[0])[:, :, :, ]
        if image.shape[2] == 2:
            utils.show_message_box(QtWidgets.QMessageBox.Warning,"Das ausgewählte bild ist graustufig. Bitte wählen Sie ein farbiges Bild.","Fehler")
            return
        elif image.shape[2] == 3:
            pass #image already usable
        elif image.shape[2] == 4:
            image = io.imread(path[0])[:, :, :-1 ]
        else:
             utils.show_message_box(QtWidgets.QMessageBox.Warning,"Fehler beim auslesen der Bilddatei. Bitte wählen sie ein anderes Bild.","Fehler")
             return

        average_color_per_row = np.average(image, axis=0)
        average_color = np.average(average_color_per_row, axis=0)

        globalColor.setColorValue(utils.convert_rgb_to_hex(int(average_color[0]),int(average_color[1]),int(average_color[2])))
        change_button_color(ui_mm, globalColor)

def color_picker(ui_mm, globalColor):
    recordRGB = utils.convert_hex_to_rgb(globalColor.getColorValue())
    color = QtWidgets.QColorDialog.getColor(QtGui.QColor(recordRGB['red'],recordRGB['green'],recordRGB['blue']))
    if color.isValid():
        globalColor.setColorValue(utils.convert_rgb_to_hex(color.red(),color.green(),color.blue()))
        change_button_color(ui_mm, globalColor)

def connect_common_buttons(ui_mm, ui, globalColor):
    ui_mm.pushButton_save.clicked.connect(lambda: on_click_material_save(ui_mm,ui, globalColor))
    ui_mm.pushButton_colorPicker.clicked.connect(lambda: color_picker(ui_mm, globalColor))
    ui_mm.pushButton_colorFromImage.clicked.connect(lambda: get_color_from_image(ui_mm, globalColor))


def on_click_new_material(ui):
    locale.setlocale(locale.LC_ALL, '')
    ui_mm = MaterialDialog('N')
    globalColor = colorField()
    connect_common_buttons(ui_mm, ui, globalColor)
    change_button_color(ui_mm, globalColor)

    ui_mm.exec()

def on_click_material_save(ui_mm,ui,globalColor):
    if not re.match("[0-9]{1}[.]{1}[0-9]{4}",ui_mm.lineEdit_material.text()):
         utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte geben Sie die Werkstoffnummer im Format 0.0000 ein","Fehler")
         return

    decimalPoint = locale.localeconv()['decimal_point']
    seperator = locale.localeconv()['thousands_sep']
    densityStr = str(ui_mm.lineEdit_density.text()).replace(seperator, '')

    if not re.match("\d+(?:\,\d{0,3})?$",densityStr):
        utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte geben Sie die Dichte im Format 0"+decimalPoint+"000 ein","Fehler")
        return

    #settings for regular numbers and currency can be different
    #they are mostlikely the same in 99.999% of the cases, but this is the clean way to code it
    decimalPoint = locale.localeconv()['mon_decimal_point']
    seperator = locale.localeconv()['mon_thousands_sep']
    priceStr = str(ui_mm.lineEdit_price.text()).replace(seperator, '')

    if not re.match("\d+(?:\,\d{0,2})?$",priceStr):
        utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte geben Sie den Preis im Format 0"+decimalPoint+"00 ein","Fehler")
        return

    density = locale.atof(densityStr)
    price = locale.atof(priceStr)


    if ui_mm.mode == 'E':
        model.update_material((ui_mm.lineEdit_standard.text(),ui_mm.lineEdit_chemical.text(),density,price,globalColor.getColorValue(),ui_mm.lineEdit_material.text()))
        if model.getSfg() != []:
            model.update_sfg((ui_mm.lineEdit_material.text(),), utils.create_tuple_from_list(model.getSfg()))
    elif ui_mm.mode == 'N':
        if ( ui_mm.lineEdit_material.text() == '' or
             ui_mm.lineEdit_standard.text() == '' or
             ui_mm.lineEdit_chemical.text() == '' or
             ui_mm.lineEdit_density.text() == '' or
             ui_mm.lineEdit_price.text() == '' ):
             utils.show_message_box(QtWidgets.QMessageBox.Warning,"Bitte alle Felder füllen","Fehler")
             return
        else:
            model.insert_material((ui_mm.lineEdit_material.text(),ui_mm.lineEdit_standard.text(),ui_mm.lineEdit_chemical.text(),density,price,globalColor.getColorValue()))
    controller.refresh_comboBox_material(ui, ui_mm.lineEdit_material.text(),ui_mm.lineEdit_standard.text(),ui_mm.lineEdit_chemical.text())
    ui_mm.accept()

def on_click_material_delete(ui_mm,ui):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Question)
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
    locale.setlocale(locale.LC_ALL, '')
    ui_mm = MaterialDialog('E')
    index = ui.comboBox_material.currentIndex()
    resultSet = model.read_all_materials()
    record = resultSet[index]
    ui_mm.lineEdit_material.setText(str(record['material']))
    ui_mm.lineEdit_material.setReadOnly(True)
    ui_mm.lineEdit_standard.setText(str(record['normbez']))
    ui_mm.lineEdit_chemical.setText(str(record['chembez']))
    density = Decimal(record['dichte']).quantize(Decimal("0.000"), ROUND_HALF_UP)
    ui_mm.lineEdit_density.setText(str('{0:n}'.format(density)))
    price = Decimal(record['preis']).quantize(Decimal("0.00"), ROUND_HALF_UP)
    ui_mm.lineEdit_price.setText(str('{0:n}'.format(price)))
    globalColor = colorField()
    globalColor.setColorValue(str(record['farbe']))
    change_button_color(ui_mm, globalColor)
    sfgControls.set_first_call(True)
    ui_mm.pushButton_sfg.clicked.connect(lambda: on_click_edit_sfg(ui_mm.lineEdit_material.text(),ui))
    ui_mm.pushButton_delete.clicked.connect(lambda: on_click_material_delete(ui_mm,ui))
    connect_common_buttons(ui_mm, ui, globalColor)
    ui_mm.exec()
