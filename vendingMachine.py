from beverage import Beverage

class VendingMachine:
    def __init__(self):
        self.beverages = {}

    def addBeverage(self, beverage):
        self.beverages[beverage.getName()] = beverage

    def getPrice(self, beverageName):
        if beverageName not in self.beverages:
            return -1.0
        return self.beverages[beverageName].getPrice()