from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_switch = "on"

machine_coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

while machine_switch == "on":
    user_input = input("What would you like? (" + menu.get_items() + "): ")
    if user_input == "off":
        machine_switch = "off"
        break
    elif user_input == "report":
        machine_coffee.report()
        money.report()
    drink = menu.find_drink(user_input)
    if drink != None:
        if machine_coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine_coffee.make_coffee(drink)
