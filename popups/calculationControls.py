from PyQt5 import QtCore, QtWidgets
import model
from popups import calculation, calculationSharedValues
from decimal import *
import locale

def changeLineEdit(lineEdit, decimal):
    lineEdit.setText(str('{0:n}'.format(decimal)))

def fill_fgk_details(ui, machine, sharedValues):
    ui.label_machine_text.setText(machine['bez'])

    time = Decimal(str(machine['ruest']))
    changeLineEdit(ui.lineEdit_ruestzeit, time)

    hourlyRate = Decimal(str(machine['mss']))
    hourlyRate = hourlyRate.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_mss, hourlyRate)

    changeLineEdit(ui.lineEdit_fgk_detail, sharedValues.getManufacturingOverheads())

def fill_mek_details(mainUi, ui, material, volume, sharedValues):
    ui.label_material_text.setText(mainUi.comboBox_material.currentText())
    ui.lineEdit_sfgA.setText(mainUi.lineEdit_semifinishedSideA.text())
    ui.lineEdit_sfgB.setText(mainUi.lineEdit_semifinishedSideB.text())
    ui.lineEdit_sfgC.setText(mainUi.lineEdit_semifinishedSideC.text())
    ui.lineEdit_volume.setText(str(volume))
    density = Decimal(str(material['dichte']))
    changeLineEdit(ui.lineEdit_density, density)

    weight = volume * density
    changeLineEdit(ui.lineEdit_weight, weight)
    changeLineEdit(ui.lineEdit_mek_detail, sharedValues.getMaterialCosts())

    matPrice = Decimal(str(material['preis']))
    matPrice = matPrice.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_materialPrice, matPrice)

def calc_material_costs(mainUi,ui,material,volume,sharedValues):
    materialCosts = volume * Decimal(str(material['dichte'])) * Decimal(str(material['preis']))

    materialCosts = materialCosts.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setMaterialCosts(materialCosts)
    changeLineEdit(ui.lineEdit_mek, materialCosts)

def calc_material_overheads(ui,sharedValues):
    materialOverheads = Decimal("0.00")
    materialOverheads = materialOverheads.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setMaterialOverheads(materialOverheads)
    changeLineEdit(ui.lineEdit_mgk, materialOverheads)

def calc_manufacturingCosts(ui,sharedValues):
    manufacturingCosts = Decimal("0.00")
    manufacturingCosts = manufacturingCosts.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setManufacturingCosts(manufacturingCosts)
    changeLineEdit(ui.lineEdit_fek, manufacturingCosts)

def calc_manufacturingOverheads(mainUi, ui, machine,sharedValues):
    manufacturingOverheads = Decimal(str(machine['mss'])) * Decimal(str(machine['ruest']))
    manufacturingOverheads = manufacturingOverheads.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setManufacturingOverheads(manufacturingOverheads)
    changeLineEdit(ui.lineEdit_fgk, manufacturingOverheads)

def calculate_cogm(ui,sharedValues):
    cogm = sharedValues.getMaterialCosts() + sharedValues.getMaterialOverheads() + sharedValues.getManufacturingCosts() + sharedValues.getManufacturingOverheads()
    cogm = cogm.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setCogm(cogm)
    changeLineEdit(ui.lineEdit_cogm, cogm)

def calculate_salesOverheads(ui,sharedValues):
    salesOverheads = sharedValues.getCogm() * Decimal(str(ui.spinBox_vgk.value())) / Decimal("100")
    salesOverheads = salesOverheads.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setSalesOverheads(salesOverheads)
    changeLineEdit(ui.lineEdit_vgk, salesOverheads)

def calculate_cogs(ui,sharedValues):
    cogs = sharedValues.getCogm() + sharedValues.getSalesOverheads()
    cogs = cogs.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setCogs(cogs)
    changeLineEdit(ui.lineEdit_cogs, cogs)

def calculate_profit(ui,sharedValues):
    profit = sharedValues.getCogs() * Decimal(str(ui.spinBox_profit.value())) / Decimal("100")
    profit = profit.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setProfit(profit)
    changeLineEdit(ui.lineEdit_profit, profit)

def calculate_skonto(ui,sharedValues):

    valueAfterProfit =  sharedValues.getCogs() + sharedValues.getProfit()
    skontoDivisor = (Decimal("100") - Decimal(str(ui.spinBox_skonto.value()))) / Decimal("100")
    skonto = valueAfterProfit / skontoDivisor - valueAfterProfit
    skonto = skonto.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setSkonto(skonto)
    changeLineEdit(ui.lineEdit_skonto, skonto)

def calculate_rebates(ui,sharedValues):
    valueAfterSkonto = sharedValues.getCogs() + sharedValues.getProfit() + sharedValues.getSkonto()
    rebateDivisor = (Decimal("100") - Decimal(str(ui.spinBox_rebates.value()))) / Decimal("100")
    rebates = valueAfterSkonto / rebateDivisor - valueAfterSkonto
    rebates = rebates.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setRebates(rebates)
    changeLineEdit(ui.lineEdit_rebates, rebates)

def calculate_price(ui,sharedValues):
    price = sharedValues.getCogs() + sharedValues.getProfit() + sharedValues.getSkonto() + sharedValues.getRebates()
    price = price.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_price, price)

def fill_screen(mainUi, ui, sharedValues):
    volume = int(mainUi.lineEdit_semifinishedSideA.text()) * int(mainUi.lineEdit_semifinishedSideB.text()) * int(mainUi.lineEdit_semifinishedSideC.text())
    #educational comment: source for Decimal always has to be a string:
    """This has to be done because a Python float value, like 135.99, is converted from Python’s language (in base 10)
        to the computer’s hardware representation (in base 2) and some precision is lost in the process.
        To avoid the Python language conversion, string literals are used."
        source: http://buildingskills.itmaybeahack.com/book/programming-2.6/html/p13_modules/p13_c03_decimal.html"""
    volume = Decimal(str(volume)) / Decimal("1000")

    material = model.read_material(mainUi.comboBox_material.currentText()[:6])

    calc_material_costs(mainUi, ui, material, volume,sharedValues)
    fill_mek_details(mainUi, ui, material, volume, sharedValues)

    calc_material_overheads(ui,sharedValues)

    calc_manufacturingCosts(ui,sharedValues)

    machine = model.read_machine(mainUi.comboBox_machine.currentText()[:1])
    calc_manufacturingOverheads(mainUi, ui, machine, sharedValues)
    fill_fgk_details(ui, machine, sharedValues)

    calculate_cogm(ui,sharedValues)
    calculate_changables(mainUi,ui,sharedValues)

def calculate_changables(mainUi,ui,sharedValues):
    salesOverheads = calculate_salesOverheads(ui,sharedValues)
    calculate_cogs(ui,sharedValues)
    calculate_profit(ui,sharedValues)
    calculate_skonto(ui,sharedValues)
    calculate_rebates(ui,sharedValues)
    calculate_price(ui,sharedValues)

def connect_spinboxes(mainUi, ui, sharedValues):
    ui.spinBox_vgk.valueChanged.connect(lambda: calculate_changables(mainUi, ui, sharedValues))
    ui.spinBox_rebates.valueChanged.connect(lambda: calculate_changables(mainUi, ui, sharedValues))
    ui.spinBox_skonto.valueChanged.connect(lambda: calculate_changables(mainUi, ui, sharedValues))
    ui.spinBox_profit.valueChanged.connect(lambda: calculate_changables(mainUi, ui, sharedValues))

def close(dialog):
    dialog.done(0)

def connect_buttons(dialog):
    dialog.ui.buttonBox.clicked.connect(lambda: close(dialog))

def show(mainUi):
    dialog = QtWidgets.QDialog()
    dialog.ui = calculation.Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    locale.setlocale(locale.LC_ALL, '')
    globalValues = calculationSharedValues.sharedValues()
    fill_screen(mainUi, dialog.ui, globalValues)
    connect_buttons(dialog)
    connect_spinboxes(mainUi, dialog.ui, globalValues)
    dialog.exec_()
