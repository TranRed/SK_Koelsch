import main, model
from PyQt5 import QtWidgets
from popups import sfgControls

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

def on_click_edit_sfg(material,mainUi):
    sfgControls.show(material,mainUi)

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
    ui_mm.pushButton_sfg.clicked.connect(lambda: on_click_edit_sfg(ui_mm.lineEdit_material.text(),ui))
    ui_mm.pushButton_save.clicked.connect(lambda: on_click_material_save(ui_mm,ui))
    ui_mm.pushButton_delete.clicked.connect(lambda: on_click_material_delete(ui_mm,ui))
    ui_mm.exec()
