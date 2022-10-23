from database import MENU, resources
import os
import time


def resource_check(drink):
    if MENU[drink]["ingredients"]["water"]<=resources["water"] and MENU[drink]["ingredients"]["milk"]<=resources["milk"] and MENU[drink]["ingredients"]["coffee"]<=resources["coffee"]:
        return True
    else:
        return False


def drink_prep(drink, amount_paid):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    resources["money"] += MENU[drink]["cost"]
    change = amount_paid - MENU[drink]["cost"]
    print(f"Change: {change}")
    print(f"Here is your {drink}. Enjoy☕!")


machine_on = True
while machine_on:
    drink = input(" What would you like? (espresso/latte/cappuccino):")
    if drink == "report" :
        for item in resources:
            print(f"{item}: {resources[item]}")
        time.sleep(3)
        os.system('cls')
        continue
    elif drink == 'shutdown':
        os.system('cls')
        print("XXX POWER OFF XXX")
        machine_on = False
        continue
    elif not resource_check(drink):
        print("Not enough ingredients. Sorry")
        time.sleep(3)
        os.system('cls')
        continue

    print("Please enter coins.")
    q = int(input("How many quarters?:"))
    d = int(input("How many dimes?:"))
    n = int(input("How many nickels?:"))
    p = int(input("How many pennies?:"))
    amount_paid = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01

    if amount_paid < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        time.sleep(3)
        os.system('cls')
        continue
    else:
        drink_prep(drink, amount_paid)
        continue


