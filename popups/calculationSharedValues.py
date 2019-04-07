from decimal import *

class sharedValues():
    def __init__(self):
        self._cent = Decimal("0.01")
        self._materialCosts = Decimal("0.00")
        self._materialOverheads = Decimal("0.00")
        self._manufacturingCosts = Decimal("0.00")
        self._manufacturingOverheads = Decimal("0.00")
        self._cogm = Decimal("0.00")
        self._salesOverheads = Decimal("0.00")
        self._cogs = Decimal("0.00")
        self._profit = Decimal("0.00")
        self._skonto= Decimal("0.00")
        self._rebates = Decimal("0.00")

    def getCent(self):
        return self._cent

    def getMaterialCosts(self):
        return self._materialCosts

    def getMaterialOverheads(self):
        return self._materialOverheads

    def getManufacturingCosts(self):
        return self._manufacturingCosts

    def getManufacturingOverheads(self):
        return self._manufacturingOverheads

    def getCogm(self):
        return self._cogm

    def getSalesOverheads(self):
        return self._salesOverheads

    def getCogs(self):
        return self._cogs

    def getProfit(self):
        return self._profit

    def getSkonto(self):
        return self._skonto

    def getRebates(self):
        return self._rebates

    def setMaterialCosts(self,materialCosts):
        self._materialCosts = materialCosts

    def setMaterialOverheads(self,materialOverheads):
        self._materialOverheads = materialOverheads

    def setManufacturingCosts(self,manufacturingCosts):
        self._manufacturingCosts = manufacturingCosts

    def setManufacturingOverheads(self,manufacturingOverheads):
        self._manufacturingOverheads = manufacturingOverheads

    def setCogm(self,cogm):
        self._cogm = cogm

    def setSalesOverheads(self,salesOverheads):
        self._salesOverheads = salesOverheads

    def setCogs(self,cogs):
        self._cogs = cogs

    def setProfit(self,profit):
        self._profit = profit

    def setSkonto(self,skonto):
        self._skonto = skonto

    def setRebates(self,rebates):
        self._rebates = rebates
