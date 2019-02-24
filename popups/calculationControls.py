from PyQt5 import QtCore, QtWidgets
import model
from popups import calculation
from decimal import *
import locale

class sharedValues():
    def __init__(self):
        self._cent = Decimal("0.01")
        self._cogm = Decimal("0.00")
        self._cogs = Decimal("0.00")
        self._profit = Decimal("0.00")
        self._skonto= Decimal("0.00")
        self._rebates = Decimal("0.00")

    def getCent(self):
        return self._cent

    def getCogm(self):
        return self._cogm

    def getCogs(self):
        return self._cogs

    def getProfit(self):
        return self._profit

    def getSkonto(self):
        return self._skonto

    def getRebates(self):
        return self._rebates

    def setCogm(self,cogm):
        self._cogm = cogm

    def setCogs(self,cogs):
        self._cogs = cogs

    def setProfit(self,profit):
        self._profit = profit

    def setSkonto(self,skonto):
        self._skonto = skonto

    def setRebates(self,rebates):
        self._rebates = rebates

def changeLineEdit(lineEdit, decimal):
    lineEdit.setText(str('{0:n}'.format(decimal)))

def fill_fgk_details(ui, machine, fgk, sharedValues):
    ui.label_machine_text.setText(machine['bez'])

    time = Decimal(str(machine['ruest']))
    changeLineEdit(ui.lineEdit_ruestzeit, time)

    hourlyRate = Decimal(str(machine['mss']))
    hourlyRate = hourlyRate.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_mss, hourlyRate)

    changeLineEdit(ui.lineEdit_fgk_detail, fgk)

def fill_mek_details(mainUi, ui, material, volume, mek,sharedValues):
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


    matPrice = Decimal(str(material['preis']))
    matPrice = matPrice.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_materialPrice, matPrice)

def calc_material_costs(mainUi,ui,material,volume,sharedValues):
    materialCosts = volume * Decimal(str(material['dichte'])) * Decimal(str(material['preis']))

    materialCosts = materialCosts.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_mek, materialCosts)

    return materialCosts

def calc_material_overheads(ui,sharedValues):
    materialOverheads = Decimal("0.00")
    materialOverheads = materialOverheads.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_mgk, materialOverheads)
    return materialOverheads

def calc_manufacturingCosts(ui,sharedValues):
    manufacturingCosts = Decimal("0.00")
    manufacturingCosts = manufacturingCosts.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_fek, manufacturingCosts)
    return manufacturingCosts

def calc_manufacturingOverheads(mainUi, ui, machine,sharedValues):
    manufacturingOverheads = Decimal(str(machine['mss'])) * Decimal(str(machine['ruest']))
    manufacturingOverheads = manufacturingOverheads.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_fgk, manufacturingOverheads)
    return manufacturingOverheads

def calculate_cogm(ui,materialCosts,materialOverheads,manufacturingCosts,manufacturingOverheads,sharedValues):
    cogm = materialCosts + materialOverheads + manufacturingCosts + manufacturingOverheads
    cogm = cogm.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    sharedValues.setCogm(cogm)
    changeLineEdit(ui.lineEdit_cogm, cogm)

def calculate_salesOverheads(ui,sharedValues):
    salesOverheads = sharedValues.getCogm() * Decimal(str(ui.spinBox_vgk.value())) / Decimal("100")
    salesOverheads = salesOverheads.quantize(sharedValues.getCent(), ROUND_HALF_UP)
    changeLineEdit(ui.lineEdit_vgk, salesOverheads)
    return salesOverheads

def calculate_cogs(ui, salesOverheads,sharedValues):
    cogs = sharedValues.getCogm() + salesOverheads
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

    materialCosts = calc_material_costs(mainUi, ui, material, volume,sharedValues)
    fill_mek_details(mainUi, ui, material, volume, materialCosts,sharedValues)

    materialOverheads = calc_material_overheads(ui,sharedValues)

    manufacturingCosts = calc_manufacturingCosts(ui,sharedValues)

    machine = model.read_machine(mainUi.comboBox_machine.currentText()[:1])
    manufacturingOverheads = calc_manufacturingOverheads(mainUi, ui, machine,sharedValues)
    fill_fgk_details(ui, machine, manufacturingOverheads,sharedValues)

    calculate_cogm(ui,materialCosts,materialOverheads,manufacturingCosts,manufacturingOverheads,sharedValues)
    calculate_changables(mainUi, ui,sharedValues)

def calculate_changables(mainUi, ui,sharedValues):
    salesOverheads = calculate_salesOverheads(ui,sharedValues)
    calculate_cogs(ui, salesOverheads,sharedValues)
    calculate_profit(ui,sharedValues)
    calculate_skonto(ui,sharedValues)
    calculate_rebates(ui,sharedValues)
    calculate_price(ui,sharedValues)

def connect_spinboxes(mainUi, ui):
    ui.spinBox_vgk.valueChanged.connect(lambda: calculate_changables(mainUi, ui))
    ui.spinBox_rebates.valueChanged.connect(lambda: calculate_changables(mainUi, ui))
    ui.spinBox_skonto.valueChanged.connect(lambda: calculate_changables(mainUi, ui))
    ui.spinBox_profit.valueChanged.connect(lambda: calculate_changables(mainUi, ui))

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
    fill_screen(mainUi, dialog.ui, sharedValues())
    connect_buttons(dialog)
    connect_spinboxes(mainUi, dialog.ui)
    dialog.exec_()
