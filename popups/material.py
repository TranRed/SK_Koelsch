# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'material.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Material(object):
    def setupUi(self, Material):
        Material.setObjectName("Material")
        Material.resize(400, 264)
        self.groupBox = QtWidgets.QGroupBox(Material)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 321, 151))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_material = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_material.setGeometry(QtCore.QRect(190, 0, 113, 21))
        self.lineEdit_material.setObjectName("lineEdit_material")
        self.label_material = QtWidgets.QLabel(self.groupBox)
        self.label_material.setGeometry(QtCore.QRect(20, 0, 151, 17))
        self.label_material.setObjectName("label_material")
        self.lineEdit_standard = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_standard.setGeometry(QtCore.QRect(190, 30, 113, 21))
        self.lineEdit_standard.setObjectName("lineEdit_standard")
        self.label_standard = QtWidgets.QLabel(self.groupBox)
        self.label_standard.setGeometry(QtCore.QRect(20, 30, 151, 17))
        self.label_standard.setObjectName("label_standard")
        self.lineEdit_chemical = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_chemical.setGeometry(QtCore.QRect(190, 60, 113, 21))
        self.lineEdit_chemical.setObjectName("lineEdit_chemical")
        self.label_chemical = QtWidgets.QLabel(self.groupBox)
        self.label_chemical.setGeometry(QtCore.QRect(20, 60, 151, 17))
        self.label_chemical.setObjectName("label_chemical")
        self.label_density = QtWidgets.QLabel(self.groupBox)
        self.label_density.setGeometry(QtCore.QRect(20, 90, 141, 17))
        self.label_density.setObjectName("label_density")
        self.lineEdit_density = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_density.setGeometry(QtCore.QRect(190, 90, 113, 21))
        self.lineEdit_density.setObjectName("lineEdit_density")
        self.label_price = QtWidgets.QLabel(self.groupBox)
        self.label_price.setGeometry(QtCore.QRect(20, 120, 151, 17))
        self.label_price.setObjectName("label_price")
        self.lineEdit_price = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_price.setGeometry(QtCore.QRect(190, 120, 113, 21))
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.pushButton_save = QtWidgets.QPushButton(Material)
        self.pushButton_save.setGeometry(QtCore.QRect(300, 220, 87, 29))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_delete = QtWidgets.QPushButton(Material)
        self.pushButton_delete.setGeometry(QtCore.QRect(210, 220, 87, 29))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_sfg = QtWidgets.QPushButton(Material)
        self.pushButton_sfg.setGeometry(QtCore.QRect(50, 180, 281, 29))
        self.pushButton_sfg.setObjectName("pushButton_sfg")

        self.retranslateUi(Material)
        QtCore.QMetaObject.connectSlotsByName(Material)
        Material.setTabOrder(self.lineEdit_material, self.lineEdit_standard)
        Material.setTabOrder(self.lineEdit_standard, self.lineEdit_chemical)
        Material.setTabOrder(self.lineEdit_chemical, self.lineEdit_density)
        Material.setTabOrder(self.lineEdit_density, self.lineEdit_price)
        Material.setTabOrder(self.lineEdit_price, self.pushButton_sfg)
        Material.setTabOrder(self.pushButton_sfg, self.pushButton_delete)
        Material.setTabOrder(self.pushButton_delete, self.pushButton_save)

    def retranslateUi(self, Material):
        _translate = QtCore.QCoreApplication.translate
        Material.setWindowTitle(_translate("Material", "Material"))
        self.label_material.setText(_translate("Material", "Werkstoffnummer"))
        self.label_standard.setText(_translate("Material", "Normbezeichnung"))
        self.label_chemical.setText(_translate("Material", "Chemische Bezeichnung"))
        self.label_density.setText(_translate("Material", "Dichte [kg/dm³]"))
        self.label_price.setText(_translate("Material", "Preis [€/kg]"))
        self.pushButton_save.setText(_translate("Material", "Speichern"))
        self.pushButton_delete.setText(_translate("Material", "Löschen"))
        self.pushButton_sfg.setText(_translate("Material", "Halbzeuge pflegen"))

