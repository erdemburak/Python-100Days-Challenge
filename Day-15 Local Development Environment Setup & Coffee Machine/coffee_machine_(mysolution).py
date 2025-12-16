from menu import MENU
from menu import resources
import time


def check_resources(drink):
    good_to_go = False
    if resources["water"] >= MENU[drink]["ingredients"]["water"] and resources["milk"] >= MENU[drink]["ingredients"]["milk"] and resources["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
        return True
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry There is not enough water")
    if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry There is not enough milk")
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry There is not enough coffee")
    return good_to_go

def coin_count():
    print("Please insert your coins\n")
    quarters = int(input("Quarters: ")) * 0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickles = int(input("Nickles: ")) * 0.05
    pennies = int(input("Pennies: ")) * 0.01
    total_money = quarters + dimes + nickles + pennies
    return total_money

def prepare_drink(drink):
    print(f"Preparing {drink} please wait!!!")
    time.sleep(2)
    print(f"{drink} is ready you can take it!!!")
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    print(resources)
    time.sleep(5)

def count_change(money):
    change = money - MENU["espresso"]["cost"]
    print(f"Don't forget your {change}$ change")

def order(order):
    money_from_sale = 0
    if check_resources(order):
        print(resources)
        money = coin_count()
        if money >= MENU[order]["cost"]:
            count_change(money)
            prepare_drink(order)
            money_from_sale += MENU[order]["cost"]
        else:
            needed_money_to_order = MENU[order]["cost"] - money 
            print(f"You need {needed_money_to_order}$ more to order {order} Please try again")
            time.sleep(5)
    else:
        time.sleep(5)
    return money_from_sale

profit = 0
there_is_resources = True
coffee_machine_on = True

while there_is_resources and coffee_machine_on:
    print("\n" * 20)
    users_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if users_order == "espresso":
        profit += order(users_order)
    elif users_order == "latte":
        profit += order(users_order)
    elif users_order == "cappuccino":
        profit += order(users_order)
    elif users_order == "report":
        print(f"Current resource values: \nWater: {resources["water"]} \nMilk: {resources["milk"]} \nCoffee: {resources["coffee"]} \nMoney: {profit}")
        time.sleep(5)    
    elif users_order == "off":
        coffee_machine_on = False
        print("Makine kapatılıyor")
