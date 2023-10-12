from vendingMachine import VendingMachine
from beverage import Beverage

vendingMachine = VendingMachine()
vendingMachine.addBeverage(Beverage("Coca Cola", 3200))
vendingMachine.addBeverage(Beverage("Suv", 1000))
vendingMachine.addBeverage(Beverage("Pepsi", 2500))

cocaColaPrice = vendingMachine.getPrice("Coca Cola")
print(cocaColaPrice)

vendingMachine.addBeverage(Beverage("Limanat", 2000))
limanatPrice = vendingMachine.getPrice("Limanat")
print(limanatPrice)