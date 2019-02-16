# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sfg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(642, 556)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.toolButton_add = QtWidgets.QToolButton(Dialog)
        self.toolButton_add.setGeometry(QtCore.QRect(20, 510, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/greenPlus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_add.setIcon(icon)
        self.toolButton_add.setObjectName("toolButton_add")
        self.toolButton_delete = QtWidgets.QToolButton(Dialog)
        self.toolButton_delete.setGeometry(QtCore.QRect(60, 510, 31, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_delete.setIcon(icon1)
        self.toolButton_delete.setObjectName("toolButton_delete")
        self.toolButton_cancel = QtWidgets.QToolButton(Dialog)
        self.toolButton_cancel.setGeometry(QtCore.QRect(440, 510, 81, 31))
        self.toolButton_cancel.setObjectName("toolButton_cancel")
        self.toolButton_confirm = QtWidgets.QToolButton(Dialog)
        self.toolButton_confirm.setGeometry(QtCore.QRect(540, 510, 81, 31))
        self.toolButton_confirm.setObjectName("toolButton_confirm")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Halbzeuge pflegen"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Werkstoffnummer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "a"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "b"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Stange"))
        self.toolButton_add.setText(_translate("Dialog", "..."))
        self.toolButton_delete.setText(_translate("Dialog", "..."))
        self.toolButton_cancel.setText(_translate("Dialog", "Abbrechen"))
        self.toolButton_confirm.setText(_translate("Dialog", "Bestätigen"))

