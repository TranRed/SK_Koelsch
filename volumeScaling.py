# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'volumeScaling.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 556)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 510, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 331, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.toolButton_add = QtWidgets.QToolButton(Dialog)
        self.toolButton_add.setGeometry(QtCore.QRect(20, 510, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/greenPlus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_add.setIcon(icon)
        self.toolButton_add.setObjectName("toolButton_add")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Taschen definieren"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Mengenstaffel (Stück)"))
        self.toolButton_add.setText(_translate("Dialog", "..."))

