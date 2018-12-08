from PyQt5 import QtCore, QtWidgets
import model
from popups import calculation
from decimal import *
import locale

def changeLineEdit(lineEdit, decimal):
    lineEdit.setText(str('{0:n}'.format(decimal)))

def fill_fgk_details(ui, machine, fgk):
    ui.label_machine_text.setText(machine['bez'])

    time = Decimal(str(machine['ruest']))
    changeLineEdit(ui.lineEdit_ruestzeit, time)

    global cent
    hourlyRate = Decimal(str(machine['mss']))
    hourlyRate = hourlyRate.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_mss, hourlyRate)

    changeLineEdit(ui.lineEdit_fgk_detail, fgk)

def fill_mek_details(mainUi, ui, material, volume, mek):
    ui.label_material_text.setText(mainUi.comboBox_material.currentText())
    ui.lineEdit_sfgA.setText(mainUi.lineEdit_semifinishedSideA.text())
    ui.lineEdit_sfgB.setText(mainUi.lineEdit_semifinishedSideB.text())
    ui.lineEdit_sfgC.setText(mainUi.lineEdit_semifinishedSideC.text())
    ui.lineEdit_volume.setText(str(volume))
    density = Decimal(str(material['dichte']))
    changeLineEdit(ui.lineEdit_density, density)

    weight = volume * density
    changeLineEdit(ui.lineEdit_weight, weight)
    changeLineEdit(ui.lineEdit_mek_detail, mek)


    global cent
    matPrice = Decimal(str(material['preis']))
    matPrice = matPrice.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_materialPrice, matPrice)

def fill_screen(mainUi, ui):
    volume = int(mainUi.lineEdit_semifinishedSideA.text()) * int(mainUi.lineEdit_semifinishedSideB.text()) * int(mainUi.lineEdit_semifinishedSideC.text())
    material = model.read_material(mainUi.comboBox_material.currentText()[:6])
    #educational comment: source for Decimal always has to be a string:
    """This has to be done because a Python float value, like 135.99, is converted from Python’s language (in base 10)
        to the computer’s hardware representation (in base 2) and some precision is lost in the process.
        To avoid the Python language conversion, string literals are used."
        source: http://buildingskills.itmaybeahack.com/book/programming-2.6/html/p13_modules/p13_c03_decimal.html"""
    volume = Decimal(str(volume)) / Decimal("1000")
    materialCosts = volume * Decimal(str(material['dichte'])) * Decimal(str(material['preis']))
    fill_mek_details(mainUi, ui, material, volume, materialCosts)

    global cent
    materialCosts = materialCosts.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_mek, materialCosts)

    materialOverheads = Decimal("0.00")
    materialOverheads = materialOverheads.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_mgk, materialOverheads)

    manufacturingCosts = Decimal("0.00")
    manufacturingCosts = manufacturingCosts.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_fek, manufacturingCosts)

    machine = model.read_machine(mainUi.comboBox_machine.currentText()[:1])
    manufacturingOverheads = Decimal(str(machine['mss'])) * Decimal(str(machine['ruest']))
    manufacturingOverheads = manufacturingOverheads.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_fgk, manufacturingOverheads)
    fill_fgk_details(ui, machine, manufacturingOverheads)

    global cogm
    cogm = materialCosts + materialOverheads + manufacturingCosts + manufacturingOverheads
    cogm = cogm.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_cogm, cogm)

    calculate_changables(mainUi, ui)

def calculate_changables(mainUi, ui):
    global cent
    global cogm

    salesOverheads = cogm * Decimal(str(ui.spinBox_vgk.value())) / Decimal("100")
    salesOverheads = salesOverheads.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_vgk, salesOverheads)

    cogs = cogm + salesOverheads
    cogs = cogs.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_cogs, cogs)

    profit = cogs * Decimal(str(ui.spinBox_profit.value())) / Decimal("100")
    profit = profit.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_profit, profit)

    valueAfterProfit = cogs + profit
    skontoDivisor = (Decimal("100") - Decimal(str(ui.spinBox_skonto.value()))) / Decimal("100")
    skonto = valueAfterProfit / skontoDivisor - valueAfterProfit
    skonto = skonto.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_skonto, skonto)

    valueAfterSkonto = valueAfterProfit + skonto
    rebateDivisor = (Decimal("100") - Decimal(str(ui.spinBox_rebates.value()))) / Decimal("100")
    rebates = valueAfterSkonto / rebateDivisor - valueAfterSkonto
    rebates = rebates.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_rebates, rebates)

    price = valueAfterSkonto + rebates
    price = price.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_price, price)

def connect_spinboxes(mainUi, ui):
    ui.spinBox_vgk.valueChanged.connect(lambda: calculate_changables(mainUi, ui))
    ui.spinBox_rebates.valueChanged.connect(lambda: calculate_changables(mainUi, ui))
    ui.spinBox_skonto.valueChanged.connect(lambda: calculate_changables(mainUi, ui))
    ui.spinBox_profit.valueChanged.connect(lambda: calculate_changables(mainUi, ui))

def close(dialog):
    dialog.done(0)

def connect_buttons(dialog):
    dialog.ui.buttonBox.clicked.connect(lambda: close(dialog))

def create_globals():
    locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')

    global cogm
    cogm = Decimal("0.00")

    global cent
    cent = Decimal("0.01")


def show(mainUi):
    dialog = QtWidgets.QDialog()
    dialog.ui = calculation.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    create_globals()
    fill_screen(mainUi, dialog.ui)
    connect_buttons(dialog)
    connect_spinboxes(mainUi, dialog.ui)
    dialog.exec_()
