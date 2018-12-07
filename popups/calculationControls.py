import model
from decimal import *
import locale

def showResultLine(text, decimal):
    print(text + '{0:n}'.format(decimal))

def show(ui):
    cent = Decimal("0.01")
    locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')

    volume = int(ui.lineEdit_semifinishedSideA.text()) * int(ui.lineEdit_semifinishedSideB.text()) * int(ui.lineEdit_semifinishedSideC.text())
    material = model.read_material(ui.comboBox_material.currentText()[:6])
    #educational comment: source for Decimal always has to be a string:
    """This has to be done because a Python float value, like 135.99, is converted from Python’s language (in base 10)
        to the computer’s hardware representation (in base 2) and some precision is lost in the process.
        To avoid the Python language conversion, string literals are used."
        source: http://buildingskills.itmaybeahack.com/book/programming-2.6/html/p13_modules/p13_c03_decimal.html"""
    materialCosts = Decimal(str(volume)) / Decimal("1000") * Decimal(str(material['dichte'])) * Decimal(str(material['preis']))

    materialCosts = materialCosts.quantize(cent, ROUND_HALF_UP)
    showResultLine("MEK: ", materialCosts)

    materialOverheads = Decimal("0.00")
    materialOverheads = materialOverheads.quantize(cent, ROUND_HALF_UP)
    showResultLine("MGK: ", materialOverheads)

    manufacturingCosts = Decimal("0.00")
    manufacturingCosts = manufacturingCosts.quantize(cent, ROUND_HALF_UP)
    showResultLine("FEK: ", manufacturingCosts)

    machine = model.read_machine(ui.comboBox_machine.currentText()[:1])
    manufacturingOverheads = Decimal(str(machine['mss'])) * Decimal(str(machine['ruest']))
    manufacturingOverheads = manufacturingOverheads.quantize(cent, ROUND_HALF_UP)
    showResultLine("FGK: ", manufacturingOverheads)

    cogm = materialCosts + materialOverheads + manufacturingCosts + manufacturingOverheads
    cogm = cogm.quantize(cent, ROUND_HALF_UP)
    showResultLine("HK d. Erz.:", cogm)

    salesOverheads = cogm * Decimal("0.15")
    salesOverheads = salesOverheads.quantize(cent, ROUND_HALF_UP)
    showResultLine("VGK: ", salesOverheads)

    cogs = cogm + salesOverheads
    cogs = cogs.quantize(cent, ROUND_HALF_UP)
    showResultLine("HK d. Ums.:", cogs)

    rebates = cogs * Decimal("0.05")
    rebates = rebates.quantize(cent, ROUND_HALF_UP)
    showResultLine("Rabatt: ", rebates)

    skonto = (cogs + rebates) * Decimal("0.03")
    skonto = skonto.quantize(cent, ROUND_HALF_UP)
    showResultLine("Skonto ", skonto)

    profit = (cogs + skonto + rebates) * Decimal("0.20")
    profit = profit.quantize(cent, ROUND_HALF_UP)
    showResultLine("Gewinn: ", profit)

    price = cogs + rebates + skonto + profit
    price = price.quantize(cent, ROUND_HALF_UP)
    showResultLine("VK-Preis: ", price)
