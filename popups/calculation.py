# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculation.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(617, 419)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(410, 380, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 591, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_calc = QtWidgets.QWidget()
        self.tab_calc.setObjectName("tab_calc")
        self.lineEdit_fek = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_fek.setEnabled(False)
        self.lineEdit_fek.setGeometry(QtCore.QRect(360, 50, 201, 22))
        self.lineEdit_fek.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_fek.setObjectName("lineEdit_fek")
        self.label_skonto = QtWidgets.QLabel(self.tab_calc)
        self.label_skonto.setGeometry(QtCore.QRect(20, 230, 211, 16))
        self.label_skonto.setObjectName("label_skonto")
        self.label_skonto_percent = QtWidgets.QLabel(self.tab_calc)
        self.label_skonto_percent.setGeometry(QtCore.QRect(300, 230, 21, 16))
        self.label_skonto_percent.setObjectName("label_skonto_percent")
        self.lineEdit_vgk = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_vgk.setEnabled(False)
        self.lineEdit_vgk.setGeometry(QtCore.QRect(360, 130, 201, 22))
        self.lineEdit_vgk.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_vgk.setObjectName("lineEdit_vgk")
        self.label_profit = QtWidgets.QLabel(self.tab_calc)
        self.label_profit.setGeometry(QtCore.QRect(20, 200, 211, 16))
        self.label_profit.setObjectName("label_profit")
        self.label_profit_percent = QtWidgets.QLabel(self.tab_calc)
        self.label_profit_percent.setGeometry(QtCore.QRect(300, 200, 21, 16))
        self.label_profit_percent.setObjectName("label_profit_percent")
        self.label_cogm = QtWidgets.QLabel(self.tab_calc)
        self.label_cogm.setGeometry(QtCore.QRect(20, 90, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_cogm.setFont(font)
        self.label_cogm.setObjectName("label_cogm")
        self.label_cogs = QtWidgets.QLabel(self.tab_calc)
        self.label_cogs.setGeometry(QtCore.QRect(20, 160, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_cogs.setFont(font)
        self.label_cogs.setObjectName("label_cogs")
        self.label_price = QtWidgets.QLabel(self.tab_calc)
        self.label_price.setGeometry(QtCore.QRect(20, 300, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")
        self.lineEdit_cogm = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_cogm.setEnabled(False)
        self.lineEdit_cogm.setGeometry(QtCore.QRect(360, 90, 201, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_cogm.setFont(font)
        self.lineEdit_cogm.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_cogm.setObjectName("lineEdit_cogm")
        self.label_vgk_percent = QtWidgets.QLabel(self.tab_calc)
        self.label_vgk_percent.setGeometry(QtCore.QRect(300, 130, 21, 16))
        self.label_vgk_percent.setObjectName("label_vgk_percent")
        self.label_rebates_percent = QtWidgets.QLabel(self.tab_calc)
        self.label_rebates_percent.setGeometry(QtCore.QRect(300, 260, 21, 16))
        self.label_rebates_percent.setObjectName("label_rebates_percent")
        self.lineEdit_price = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_price.setEnabled(False)
        self.lineEdit_price.setGeometry(QtCore.QRect(360, 290, 201, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.spinBox_vgk = QtWidgets.QSpinBox(self.tab_calc)
        self.spinBox_vgk.setEnabled(True)
        self.spinBox_vgk.setGeometry(QtCore.QRect(240, 130, 51, 22))
        self.spinBox_vgk.setMaximum(100)
        self.spinBox_vgk.setProperty("value", 15)
        self.spinBox_vgk.setObjectName("spinBox_vgk")
        self.lineEdit_cogs = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_cogs.setEnabled(False)
        self.lineEdit_cogs.setGeometry(QtCore.QRect(360, 160, 201, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_cogs.setFont(font)
        self.lineEdit_cogs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_cogs.setObjectName("lineEdit_cogs")
        self.lineEdit_rebates = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_rebates.setEnabled(False)
        self.lineEdit_rebates.setGeometry(QtCore.QRect(360, 260, 201, 22))
        self.lineEdit_rebates.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_rebates.setObjectName("lineEdit_rebates")
        self.spinBox_skonto = QtWidgets.QSpinBox(self.tab_calc)
        self.spinBox_skonto.setEnabled(True)
        self.spinBox_skonto.setGeometry(QtCore.QRect(240, 230, 51, 22))
        self.spinBox_skonto.setMaximum(99)
        self.spinBox_skonto.setProperty("value", 3)
        self.spinBox_skonto.setObjectName("spinBox_skonto")
        self.lineEdit_mek = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_mek.setEnabled(False)
        self.lineEdit_mek.setGeometry(QtCore.QRect(360, 10, 201, 22))
        self.lineEdit_mek.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_mek.setObjectName("lineEdit_mek")
        self.label_mgk = QtWidgets.QLabel(self.tab_calc)
        self.label_mgk.setGeometry(QtCore.QRect(20, 30, 211, 16))
        self.label_mgk.setObjectName("label_mgk")
        self.spinBox_profit = QtWidgets.QSpinBox(self.tab_calc)
        self.spinBox_profit.setEnabled(True)
        self.spinBox_profit.setGeometry(QtCore.QRect(240, 200, 51, 22))
        self.spinBox_profit.setMaximum(100)
        self.spinBox_profit.setProperty("value", 20)
        self.spinBox_profit.setObjectName("spinBox_profit")
        self.lineEdit_mgk = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_mgk.setEnabled(False)
        self.lineEdit_mgk.setGeometry(QtCore.QRect(360, 30, 201, 22))
        self.lineEdit_mgk.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_mgk.setObjectName("lineEdit_mgk")
        self.label_vgk = QtWidgets.QLabel(self.tab_calc)
        self.label_vgk.setGeometry(QtCore.QRect(20, 130, 211, 16))
        self.label_vgk.setObjectName("label_vgk")
        self.lineEdit_fgk = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_fgk.setEnabled(False)
        self.lineEdit_fgk.setGeometry(QtCore.QRect(360, 70, 201, 22))
        self.lineEdit_fgk.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_fgk.setObjectName("lineEdit_fgk")
        self.lineEdit_skonto = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_skonto.setEnabled(False)
        self.lineEdit_skonto.setGeometry(QtCore.QRect(360, 230, 201, 22))
        self.lineEdit_skonto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_skonto.setObjectName("lineEdit_skonto")
        self.spinBox_rebates = QtWidgets.QSpinBox(self.tab_calc)
        self.spinBox_rebates.setEnabled(True)
        self.spinBox_rebates.setGeometry(QtCore.QRect(240, 260, 51, 22))
        self.spinBox_rebates.setMaximum(99)
        self.spinBox_rebates.setProperty("value", 5)
        self.spinBox_rebates.setObjectName("spinBox_rebates")
        self.label_fek = QtWidgets.QLabel(self.tab_calc)
        self.label_fek.setGeometry(QtCore.QRect(20, 50, 211, 16))
        self.label_fek.setObjectName("label_fek")
        self.label_mek = QtWidgets.QLabel(self.tab_calc)
        self.label_mek.setGeometry(QtCore.QRect(20, 10, 211, 16))
        self.label_mek.setObjectName("label_mek")
        self.label_fgk = QtWidgets.QLabel(self.tab_calc)
        self.label_fgk.setGeometry(QtCore.QRect(20, 70, 211, 16))
        self.label_fgk.setObjectName("label_fgk")
        self.lineEdit_profit = QtWidgets.QLineEdit(self.tab_calc)
        self.lineEdit_profit.setEnabled(False)
        self.lineEdit_profit.setGeometry(QtCore.QRect(360, 200, 201, 22))
        self.lineEdit_profit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_profit.setObjectName("lineEdit_profit")
        self.label_rebates = QtWidgets.QLabel(self.tab_calc)
        self.label_rebates.setGeometry(QtCore.QRect(20, 260, 211, 16))
        self.label_rebates.setObjectName("label_rebates")
        self.tabWidget.addTab(self.tab_calc, "")
        self.tab_mek = QtWidgets.QWidget()
        self.tab_mek.setObjectName("tab_mek")
        self.label_material = QtWidgets.QLabel(self.tab_mek)
        self.label_material.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.label_material.setObjectName("label_material")
        self.label_material_text = QtWidgets.QLabel(self.tab_mek)
        self.label_material_text.setGeometry(QtCore.QRect(360, 20, 211, 16))
        self.label_material_text.setText("")
        self.label_material_text.setObjectName("label_material_text")
        self.label_mek_detail = QtWidgets.QLabel(self.tab_mek)
        self.label_mek_detail.setGeometry(QtCore.QRect(20, 230, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_mek_detail.setFont(font)
        self.label_mek_detail.setObjectName("label_mek_detail")
        self.lineEdit_mek_detail = QtWidgets.QLineEdit(self.tab_mek)
        self.lineEdit_mek_detail.setEnabled(False)
        self.lineEdit_mek_detail.setGeometry(QtCore.QRect(360, 230, 201, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_mek_detail.setFont(font)
        self.lineEdit_mek_detail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_mek_detail.setObjectName("lineEdit_mek_detail")
        self.lineEdit_sfgA = QtWidgets.QLineEdit(self.tab_mek)
        self.lineEdit_sfgA.setEnabled(False)
        self.lineEdit_sfgA.setGeometry(QtCore.QRect(360, 50, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_sfgA.setFont(font)
        self.lineEdit_sfgA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_sfgA.setObjectName("lineEdit_sfgA")
        self.label_sfgA = QtWidgets.QLabel(self.tab_mek)
        self.label_sfgA.setGeometry(QtCore.QRect(20, 50, 211, 16))
        self.label_sfgA.setObjectName("label_sfgA")
        self.label_sfgB = QtWidgets.QLabel(self.tab_mek)
        self.label_sfgB.setGeometry(QtCore.QRect(20, 70, 211, 16))
        self.label_sfgB.setObjectName("label_sfgB")
        self.lineEdit_sfgB = QtWidgets.QLineEdit(self.tab_mek)
        self.lineEdit_sfgB.setEnabled(False)
        self.lineEdit_sfgB.setGeometry(QtCore.QRect(360, 70, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_sfgB.setFont(font)
        self.lineEdit_sfgB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_sfgB.setObjectName("lineEdit_sfgB")
        self.lineEdit_sfgC = QtWidgets.QLineEdit(self.tab_mek)
        self.lineEdit_sfgC.setEnabled(False)
        self.lineEdit_sfgC.setGeometry(QtCore.QRect(360, 90, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_sfgC.setFont(font)
        self.lineEdit_sfgC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_sfgC.setObjectName("lineEdit_sfgC")
        self.label_sfgC = QtWidgets.QLabel(self.tab_mek)
        self.label_sfgC.setGeometry(QtCore.QRect(20, 90, 211, 16))
        self.label_sfgC.setObjectName("label_sfgC")
        self.label_volume = QtWidgets.QLabel(self.tab_mek)
        self.label_volume.setGeometry(QtCore.QRect(20, 120, 211, 16))
        self.label_volume.setObjectName("label_volume")
        self.lineEdit_volume = QtWidgets.QLineEdit(self.tab_mek)
        self.lineEdit_volume.setEnabled(False)
        self.lineEdit_volume.setGeometry(QtCore.QRect(360, 120, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_volume.setFont(font)
        self.lineEdit_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_volume.setObjectName("lineEdit_volume")
        self.label_density = QtWidgets.QLabel(self.tab_mek)
        self.label_density.setGeometry(QtCore.QRect(20, 140, 211, 16))
        self.label_density.setObjectName("label_density")
        self.lineEdit_density = QtWidgets.QLineEdit(self.tab_mek)
        self.lineEdit_density.setEnabled(False)
        self.lineEdit_density.setGeometry(QtCore.QRect(360, 140, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_density.setFont(font)
        self.lineEdit_density.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_density.setObjectName("lineEdit_density")
        self.lineEdit_weight = QtWidgets.QLineEdit(self.tab_mek)
        self.lineEdit_weight.setEnabled(False)
        self.lineEdit_weight.setGeometry(QtCore.QRect(360, 180, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_weight.setFont(font)
        self.lineEdit_weight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.label_weight = QtWidgets.QLabel(self.tab_mek)
        self.label_weight.setGeometry(QtCore.QRect(20, 180, 211, 16))
        self.label_weight.setObjectName("label_weight")
        self.lineEdit_materialPrice = QtWidgets.QLineEdit(self.tab_mek)
        self.lineEdit_materialPrice.setEnabled(False)
        self.lineEdit_materialPrice.setGeometry(QtCore.QRect(360, 200, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_materialPrice.setFont(font)
        self.lineEdit_materialPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_materialPrice.setObjectName("lineEdit_materialPrice")
        self.label_materialPrice = QtWidgets.QLabel(self.tab_mek)
        self.label_materialPrice.setGeometry(QtCore.QRect(20, 200, 211, 16))
        self.label_materialPrice.setObjectName("label_materialPrice")
        self.label_times_2 = QtWidgets.QLabel(self.tab_mek)
        self.label_times_2.setGeometry(QtCore.QRect(340, 70, 16, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_times_2.setFont(font)
        self.label_times_2.setObjectName("label_times_2")
        self.label_times_3 = QtWidgets.QLabel(self.tab_mek)
        self.label_times_3.setGeometry(QtCore.QRect(340, 90, 16, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_times_3.setFont(font)
        self.label_times_3.setObjectName("label_times_3")
        self.label_times_4 = QtWidgets.QLabel(self.tab_mek)
        self.label_times_4.setGeometry(QtCore.QRect(340, 140, 16, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_times_4.setFont(font)
        self.label_times_4.setObjectName("label_times_4")
        self.label_times_5 = QtWidgets.QLabel(self.tab_mek)
        self.label_times_5.setGeometry(QtCore.QRect(340, 200, 16, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_times_5.setFont(font)
        self.label_times_5.setObjectName("label_times_5")
        self.tabWidget.addTab(self.tab_mek, "")
        self.tab_mgk = QtWidgets.QWidget()
        self.tab_mgk.setObjectName("tab_mgk")
        self.tabWidget.addTab(self.tab_mgk, "")
        self.tab_fek = QtWidgets.QWidget()
        self.tab_fek.setObjectName("tab_fek")
        self.tabWidget.addTab(self.tab_fek, "")
        self.tab_fgk = QtWidgets.QWidget()
        self.tab_fgk.setObjectName("tab_fgk")
        self.lineEdit_fgk_detail = QtWidgets.QLineEdit(self.tab_fgk)
        self.lineEdit_fgk_detail.setEnabled(False)
        self.lineEdit_fgk_detail.setGeometry(QtCore.QRect(360, 110, 201, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_fgk_detail.setFont(font)
        self.lineEdit_fgk_detail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_fgk_detail.setObjectName("lineEdit_fgk_detail")
        self.label_fgk_detail = QtWidgets.QLabel(self.tab_fgk)
        self.label_fgk_detail.setGeometry(QtCore.QRect(20, 110, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_fgk_detail.setFont(font)
        self.label_fgk_detail.setObjectName("label_fgk_detail")
        self.lineEdit_mss = QtWidgets.QLineEdit(self.tab_fgk)
        self.lineEdit_mss.setEnabled(False)
        self.lineEdit_mss.setGeometry(QtCore.QRect(360, 70, 201, 22))
        self.lineEdit_mss.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_mss.setObjectName("lineEdit_mss")
        self.label_mss = QtWidgets.QLabel(self.tab_fgk)
        self.label_mss.setGeometry(QtCore.QRect(20, 70, 211, 16))
        self.label_mss.setObjectName("label_mss")
        self.lineEdit_ruestzeit = QtWidgets.QLineEdit(self.tab_fgk)
        self.lineEdit_ruestzeit.setEnabled(False)
        self.lineEdit_ruestzeit.setGeometry(QtCore.QRect(360, 50, 201, 22))
        self.lineEdit_ruestzeit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_ruestzeit.setObjectName("lineEdit_ruestzeit")
        self.label_ruestzeit = QtWidgets.QLabel(self.tab_fgk)
        self.label_ruestzeit.setGeometry(QtCore.QRect(20, 50, 211, 16))
        self.label_ruestzeit.setObjectName("label_ruestzeit")
        self.label_machine = QtWidgets.QLabel(self.tab_fgk)
        self.label_machine.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.label_machine.setObjectName("label_machine")
        self.label_machine_text = QtWidgets.QLabel(self.tab_fgk)
        self.label_machine_text.setGeometry(QtCore.QRect(360, 20, 211, 16))
        self.label_machine_text.setText("")
        self.label_machine_text.setObjectName("label_machine_text")
        self.label_times = QtWidgets.QLabel(self.tab_fgk)
        self.label_times.setGeometry(QtCore.QRect(340, 70, 16, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_times.setFont(font)
        self.label_times.setObjectName("label_times")
        self.tabWidget.addTab(self.tab_fgk, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kalkulation"))
        self.lineEdit_fek.setText(_translate("Dialog", "0"))
        self.label_skonto.setText(_translate("Dialog", "Skonto:"))
        self.label_skonto_percent.setText(_translate("Dialog", "%"))
        self.lineEdit_vgk.setText(_translate("Dialog", "0"))
        self.label_profit.setText(_translate("Dialog", "Marge:"))
        self.label_profit_percent.setText(_translate("Dialog", "%"))
        self.label_cogm.setText(_translate("Dialog", "Herstellkosten der Erzeugung:"))
        self.label_cogs.setText(_translate("Dialog", "Herstellkosten des Umsatzes:"))
        self.label_price.setText(_translate("Dialog", "Verkaufspreis:"))
        self.lineEdit_cogm.setText(_translate("Dialog", "0"))
        self.label_vgk_percent.setText(_translate("Dialog", "%"))
        self.label_rebates_percent.setText(_translate("Dialog", "%"))
        self.lineEdit_price.setText(_translate("Dialog", "0"))
        self.lineEdit_cogs.setText(_translate("Dialog", "0"))
        self.lineEdit_rebates.setText(_translate("Dialog", "0"))
        self.lineEdit_mek.setText(_translate("Dialog", "0"))
        self.label_mgk.setText(_translate("Dialog", "Materialgemeinkosten:"))
        self.lineEdit_mgk.setText(_translate("Dialog", "0"))
        self.label_vgk.setText(_translate("Dialog", "Vertriebsgemeinkosten:"))
        self.lineEdit_fgk.setText(_translate("Dialog", "0"))
        self.lineEdit_skonto.setText(_translate("Dialog", "0"))
        self.label_fek.setText(_translate("Dialog", "Fertigungseinzelkosten:"))
        self.label_mek.setText(_translate("Dialog", "Materialeinzelkosten:"))
        self.label_fgk.setText(_translate("Dialog", "Fertigungsgemeinkosten:"))
        self.lineEdit_profit.setText(_translate("Dialog", "0"))
        self.label_rebates.setText(_translate("Dialog", "Rabatt:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calc), _translate("Dialog", "Kalkulation"))
        self.label_material.setText(_translate("Dialog", "Material:"))
        self.label_mek_detail.setText(_translate("Dialog", "Materialeinzelkosten:"))
        self.lineEdit_mek_detail.setText(_translate("Dialog", "0"))
        self.lineEdit_sfgA.setText(_translate("Dialog", "0"))
        self.label_sfgA.setText(_translate("Dialog", "Halbzeug a (mm):"))
        self.label_sfgB.setText(_translate("Dialog", "Halbzeug b(mm):"))
        self.lineEdit_sfgB.setText(_translate("Dialog", "0"))
        self.lineEdit_sfgC.setText(_translate("Dialog", "0"))
        self.label_sfgC.setText(_translate("Dialog", "Halbzeug c(mm):"))
        self.label_volume.setText(_translate("Dialog", "Volumen(cm³):"))
        self.lineEdit_volume.setText(_translate("Dialog", "0"))
        self.label_density.setText(_translate("Dialog", "Dichte (kg/cm³):"))
        self.lineEdit_density.setText(_translate("Dialog", "0"))
        self.lineEdit_weight.setText(_translate("Dialog", "0"))
        self.label_weight.setText(_translate("Dialog", "Gewicht (kg):"))
        self.lineEdit_materialPrice.setText(_translate("Dialog", "0"))
        self.label_materialPrice.setText(_translate("Dialog", "Preis (€/kg):"))
        self.label_times_2.setText(_translate("Dialog", "x"))
        self.label_times_3.setText(_translate("Dialog", "x"))
        self.label_times_4.setText(_translate("Dialog", "x"))
        self.label_times_5.setText(_translate("Dialog", "x"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mek), _translate("Dialog", "MEK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mgk), _translate("Dialog", "MGK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fek), _translate("Dialog", "FEK"))
        self.lineEdit_fgk_detail.setText(_translate("Dialog", "0"))
        self.label_fgk_detail.setText(_translate("Dialog", "Fertigungsgemeinkosten:"))
        self.lineEdit_mss.setText(_translate("Dialog", "0"))
        self.label_mss.setText(_translate("Dialog", "Maschinenstundensatz:"))
        self.lineEdit_ruestzeit.setText(_translate("Dialog", "0"))
        self.label_ruestzeit.setText(_translate("Dialog", "Rüstzeit (Stunden):"))
        self.label_machine.setText(_translate("Dialog", "Machine:"))
        self.label_times.setText(_translate("Dialog", "x"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fgk), _translate("Dialog", "FGK"))

