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

def calc_material_costs(mainUi,ui,material,volume):
    materialCosts = volume * Decimal(str(material['dichte'])) * Decimal(str(material['preis']))

    global cent
    materialCosts = materialCosts.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_mek, materialCosts)

    return materialCosts

def calc_material_overheads(ui):
    global cent
    materialOverheads = Decimal("0.00")
    materialOverheads = materialOverheads.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_mgk, materialOverheads)
    return materialOverheads

def calc_manufacturingCosts(ui):
    global cent
    manufacturingCosts = Decimal("0.00")
    manufacturingCosts = manufacturingCosts.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_fek, manufacturingCosts)
    return manufacturingCosts

def calc_manufacturingOverheads(mainUi, ui, machine):
    global cent
    manufacturingOverheads = Decimal(str(machine['mss'])) * Decimal(str(machine['ruest']))
    manufacturingOverheads = manufacturingOverheads.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_fgk, manufacturingOverheads)
    return manufacturingOverheads

def calculate_cogm(ui,materialCosts,materialOverheads,manufacturingCosts,manufacturingOverheads):
    global cent
    global cogm
    cogm = materialCosts + materialOverheads + manufacturingCosts + manufacturingOverheads
    cogm = cogm.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_cogm, cogm)

def calculate_salesOverheads(ui):
    global cent
    global cogm
    salesOverheads = cogm * Decimal(str(ui.spinBox_vgk.value())) / Decimal("100")
    salesOverheads = salesOverheads.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_vgk, salesOverheads)
    return salesOverheads

def calculate_cogs(ui, salesOverheads):
    global cent
    global cogm
    global cogs
    cogs = cogm + salesOverheads
    cogs = cogs.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_cogs, cogs)

def calculate_profit(ui):
    global cent
    global cogs
    global profit
    profit = cogs * Decimal(str(ui.spinBox_profit.value())) / Decimal("100")
    profit = profit.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_profit, profit)

def calculate_skonto(ui):
    global cent
    global cogs
    global profit
    global skonto
    valueAfterProfit = cogs + profit
    skontoDivisor = (Decimal("100") - Decimal(str(ui.spinBox_skonto.value()))) / Decimal("100")
    skonto = valueAfterProfit / skontoDivisor - valueAfterProfit
    skonto = skonto.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_skonto, skonto)

def calculate_rebates(ui):
    global cent
    global cogs
    global profit
    global skonto
    global rebates
    valueAfterSkonto = cogs + profit + skonto
    rebateDivisor = (Decimal("100") - Decimal(str(ui.spinBox_rebates.value()))) / Decimal("100")
    rebates = valueAfterSkonto / rebateDivisor - valueAfterSkonto
    rebates = rebates.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_rebates, rebates)

def calculate_price(ui):
    global cent
    global cogs
    global profit
    global skonto
    global rebates

    price = cogs + profit + skonto + rebates
    price = price.quantize(cent, ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_price, price)

def fill_screen(mainUi, ui):
    volume = int(mainUi.lineEdit_semifinishedSideA.text()) * int(mainUi.lineEdit_semifinishedSideB.text()) * int(mainUi.lineEdit_semifinishedSideC.text())
    #educational comment: source for Decimal always has to be a string:
    """This has to be done because a Python float value, like 135.99, is converted from Python’s language (in base 10)
        to the computer’s hardware representation (in base 2) and some precision is lost in the process.
        To avoid the Python language conversion, string literals are used."
        source: http://buildingskills.itmaybeahack.com/book/programming-2.6/html/p13_modules/p13_c03_decimal.html"""
    volume = Decimal(str(volume)) / Decimal("1000")

    material = model.read_material(mainUi.comboBox_material.currentText()[:6])

    materialCosts = calc_material_costs(mainUi, ui, material, volume)
    fill_mek_details(mainUi, ui, material, volume, materialCosts)

    materialOverheads = calc_material_overheads(ui)

    manufacturingCosts = calc_manufacturingCosts(ui)

    machine = model.read_machine(mainUi.comboBox_machine.currentText()[:1])
    manufacturingOverheads = calc_manufacturingOverheads(mainUi, ui, machine)
    fill_fgk_details(ui, machine, manufacturingOverheads)

    calculate_cogm(ui,materialCosts,materialOverheads,manufacturingCosts,manufacturingOverheads)
    calculate_changables(mainUi, ui)

def calculate_changables(mainUi, ui):
    salesOverheads = calculate_salesOverheads(ui)
    calculate_cogs(ui, salesOverheads)
    calculate_profit(ui)
    calculate_skonto(ui)
    calculate_rebates(ui)
    calculate_price(ui)

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
    locale.setlocale(locale.LC_ALL, '')

    global cent
    cent = Decimal("0.01")

    global cogm
    cogm = Decimal("0.00")

    global cogs
    cogs = Decimal("0.00")

    global profit
    profit = Decimal("0.00")

    global skonto
    skonto= Decimal("0.00")

    global rebates
    rebates = Decimal("0.00")



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
