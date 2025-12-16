from menu import MENU
from menu import resources

profit = 0

def is_resource_sufficent(order_ingredients):
    """Retursn true when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated coins inserted."""
    print("Please insert your coins\n")
    quarters = int(input("Quarters: ")) * 0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickles = int(input("Nickles: ")) * 0.05
    pennies = int(input("Pennies: ")) * 0.01
    total_money = quarters + dimes + nickles + pennies
    return total_money

def is_transaction_successful(money_recieved, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Current resource values: \nWater: {resources["water"]} \nMilk: {resources["milk"]} \nCoffee: {resources["coffee"]} \nMoney: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
