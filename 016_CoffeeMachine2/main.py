from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
from time import sleep

menu = Menu()
menu_latte = menu.find_drink("latte")
menu_espresso = menu.find_drink("espresso")
menu_cappuccino = menu.find_drink("cappuccino")
cof_m = CoffeeMaker()
mon_m = MoneyMachine()

machine_on = True

while machine_on:
    drink = input(f"What would you like? {menu.get_items()}:")
    if drink == "report":
        cof_m.report()
        sleep(4)
        os.system('cls')
        continue
    elif drink == "off":
        os.system('cls')
        print("Good-Bye")
        machine_on = False
        continue
    elif drink == "profit":
        mon_m.report()
        sleep(4)
        os.system('cls')
        continue
    elif not cof_m.is_resource_sufficient(menu.find_drink(drink)):
        sleep(4)
        os.system('cls')
        continue
    if not mon_m.make_payment(menu.find_drink(drink).cost):
        sleep(4)
        os.system('cls')
        continue
    else:
        cof_m.make_coffee(menu.find_drink(drink))
        sleep(4)
        os.system('cls')
        continue

