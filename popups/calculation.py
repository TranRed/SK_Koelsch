# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(592, 379)
        self.label_mek = QtWidgets.QLabel(Dialog)
        self.label_mek.setGeometry(QtCore.QRect(30, 30, 211, 16))
        self.label_mek.setObjectName("label_mek")
        self.label_mgk = QtWidgets.QLabel(Dialog)
        self.label_mgk.setGeometry(QtCore.QRect(30, 50, 211, 16))
        self.label_mgk.setObjectName("label_mgk")
        self.label_fek = QtWidgets.QLabel(Dialog)
        self.label_fek.setGeometry(QtCore.QRect(30, 70, 211, 16))
        self.label_fek.setObjectName("label_fek")
        self.label_fgk = QtWidgets.QLabel(Dialog)
        self.label_fgk.setGeometry(QtCore.QRect(30, 90, 211, 16))
        self.label_fgk.setObjectName("label_fgk")
        self.label_cogm = QtWidgets.QLabel(Dialog)
        self.label_cogm.setGeometry(QtCore.QRect(30, 110, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_cogm.setFont(font)
        self.label_cogm.setObjectName("label_cogm")
        self.label_vgk = QtWidgets.QLabel(Dialog)
        self.label_vgk.setGeometry(QtCore.QRect(30, 150, 211, 16))
        self.label_vgk.setObjectName("label_vgk")
        self.spinBox_vgk = QtWidgets.QSpinBox(Dialog)
        self.spinBox_vgk.setEnabled(True)
        self.spinBox_vgk.setGeometry(QtCore.QRect(250, 150, 42, 22))
        self.spinBox_vgk.setMaximum(100)
        self.spinBox_vgk.setProperty("value", 15)
        self.spinBox_vgk.setObjectName("spinBox_vgk")
        self.label_vgk_percent = QtWidgets.QLabel(Dialog)
        self.label_vgk_percent.setGeometry(QtCore.QRect(300, 150, 21, 16))
        self.label_vgk_percent.setObjectName("label_vgk_percent")
        self.label_cogs = QtWidgets.QLabel(Dialog)
        self.label_cogs.setGeometry(QtCore.QRect(30, 180, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_cogs.setFont(font)
        self.label_cogs.setObjectName("label_cogs")
        self.label_rebates = QtWidgets.QLabel(Dialog)
        self.label_rebates.setGeometry(QtCore.QRect(30, 220, 211, 16))
        self.label_rebates.setObjectName("label_rebates")
        self.spinBox_rebates = QtWidgets.QSpinBox(Dialog)
        self.spinBox_rebates.setEnabled(True)
        self.spinBox_rebates.setGeometry(QtCore.QRect(250, 220, 42, 22))
        self.spinBox_rebates.setMaximum(100)
        self.spinBox_rebates.setProperty("value", 5)
        self.spinBox_rebates.setObjectName("spinBox_rebates")
        self.label_rebates_percent = QtWidgets.QLabel(Dialog)
        self.label_rebates_percent.setGeometry(QtCore.QRect(300, 220, 21, 16))
        self.label_rebates_percent.setObjectName("label_rebates_percent")
        self.label_skonto = QtWidgets.QLabel(Dialog)
        self.label_skonto.setGeometry(QtCore.QRect(30, 250, 211, 16))
        self.label_skonto.setObjectName("label_skonto")
        self.label_skonto_percent = QtWidgets.QLabel(Dialog)
        self.label_skonto_percent.setGeometry(QtCore.QRect(300, 250, 21, 16))
        self.label_skonto_percent.setObjectName("label_skonto_percent")
        self.spinBox_skonto = QtWidgets.QSpinBox(Dialog)
        self.spinBox_skonto.setEnabled(True)
        self.spinBox_skonto.setGeometry(QtCore.QRect(250, 250, 42, 22))
        self.spinBox_skonto.setMaximum(100)
        self.spinBox_skonto.setProperty("value", 3)
        self.spinBox_skonto.setObjectName("spinBox_skonto")
        self.label_profit = QtWidgets.QLabel(Dialog)
        self.label_profit.setGeometry(QtCore.QRect(30, 280, 211, 16))
        self.label_profit.setObjectName("label_profit")
        self.label_profit_percent = QtWidgets.QLabel(Dialog)
        self.label_profit_percent.setGeometry(QtCore.QRect(300, 280, 21, 16))
        self.label_profit_percent.setObjectName("label_profit_percent")
        self.spinBox_profit = QtWidgets.QSpinBox(Dialog)
        self.spinBox_profit.setEnabled(True)
        self.spinBox_profit.setGeometry(QtCore.QRect(250, 280, 42, 22))
        self.spinBox_profit.setMaximum(100)
        self.spinBox_profit.setProperty("value", 20)
        self.spinBox_profit.setObjectName("spinBox_profit")
        self.label_price = QtWidgets.QLabel(Dialog)
        self.label_price.setGeometry(QtCore.QRect(30, 320, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")
        self.lineEdit_mek = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_mek.setEnabled(False)
        self.lineEdit_mek.setGeometry(QtCore.QRect(370, 30, 201, 22))
        self.lineEdit_mek.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_mek.setObjectName("lineEdit_mek")
        self.lineEdit_mgk = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_mgk.setEnabled(False)
        self.lineEdit_mgk.setGeometry(QtCore.QRect(370, 50, 201, 22))
        self.lineEdit_mgk.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_mgk.setObjectName("lineEdit_mgk")
        self.lineEdit_fek = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_fek.setEnabled(False)
        self.lineEdit_fek.setGeometry(QtCore.QRect(370, 70, 201, 22))
        self.lineEdit_fek.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_fek.setObjectName("lineEdit_fek")
        self.lineEdit_fgk = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_fgk.setEnabled(False)
        self.lineEdit_fgk.setGeometry(QtCore.QRect(370, 90, 201, 22))
        self.lineEdit_fgk.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_fgk.setObjectName("lineEdit_fgk")
        self.lineEdit_cogm = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_cogm.setEnabled(False)
        self.lineEdit_cogm.setGeometry(QtCore.QRect(370, 110, 201, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_cogm.setFont(font)
        self.lineEdit_cogm.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_cogm.setObjectName("lineEdit_cogm")
        self.lineEdit_vgk = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_vgk.setEnabled(False)
        self.lineEdit_vgk.setGeometry(QtCore.QRect(370, 150, 201, 22))
        self.lineEdit_vgk.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_vgk.setObjectName("lineEdit_vgk")
        self.lineEdit_cogs = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_cogs.setEnabled(False)
        self.lineEdit_cogs.setGeometry(QtCore.QRect(370, 180, 201, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_cogs.setFont(font)
        self.lineEdit_cogs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_cogs.setObjectName("lineEdit_cogs")
        self.lineEdit_rebates = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_rebates.setEnabled(False)
        self.lineEdit_rebates.setGeometry(QtCore.QRect(370, 220, 201, 22))
        self.lineEdit_rebates.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_rebates.setObjectName("lineEdit_rebates")
        self.lineEdit_skonto = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_skonto.setEnabled(False)
        self.lineEdit_skonto.setGeometry(QtCore.QRect(370, 250, 201, 22))
        self.lineEdit_skonto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_skonto.setObjectName("lineEdit_skonto")
        self.lineEdit_profit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_profit.setEnabled(False)
        self.lineEdit_profit.setGeometry(QtCore.QRect(370, 280, 201, 22))
        self.lineEdit_profit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_profit.setObjectName("lineEdit_profit")
        self.lineEdit_price = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price.setEnabled(False)
        self.lineEdit_price.setGeometry(QtCore.QRect(370, 310, 201, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(380, 340, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kalkulation"))
        self.label_mek.setText(_translate("Dialog", "Materialeinzelkosten:"))
        self.label_mgk.setText(_translate("Dialog", "Materialgemeinkosten:"))
        self.label_fek.setText(_translate("Dialog", "Fertigungseinzelkosten:"))
        self.label_fgk.setText(_translate("Dialog", "Fertigungsgemeinkosten:"))
        self.label_cogm.setText(_translate("Dialog", "Herstellkosten der Erzeugung:"))
        self.label_vgk.setText(_translate("Dialog", "Vertriebsgemeinkosten:"))
        self.label_vgk_percent.setText(_translate("Dialog", "%"))
        self.label_cogs.setText(_translate("Dialog", "Herstellkosten des Umsatzes:"))
        self.label_rebates.setText(_translate("Dialog", "Rabatt:"))
        self.label_rebates_percent.setText(_translate("Dialog", "%"))
        self.label_skonto.setText(_translate("Dialog", "Skonto:"))
        self.label_skonto_percent.setText(_translate("Dialog", "%"))
        self.label_profit.setText(_translate("Dialog", "Marge:"))
        self.label_profit_percent.setText(_translate("Dialog", "%"))
        self.label_price.setText(_translate("Dialog", "Verkaufspreis:"))
        self.lineEdit_mek.setText(_translate("Dialog", "0"))
        self.lineEdit_mgk.setText(_translate("Dialog", "0"))
        self.lineEdit_fek.setText(_translate("Dialog", "0"))
        self.lineEdit_fgk.setText(_translate("Dialog", "0"))
        self.lineEdit_cogm.setText(_translate("Dialog", "0"))
        self.lineEdit_vgk.setText(_translate("Dialog", "0"))
        self.lineEdit_cogs.setText(_translate("Dialog", "0"))
        self.lineEdit_rebates.setText(_translate("Dialog", "0"))
        self.lineEdit_skonto.setText(_translate("Dialog", "0"))
        self.lineEdit_profit.setText(_translate("Dialog", "0"))
        self.lineEdit_price.setText(_translate("Dialog", "0"))

