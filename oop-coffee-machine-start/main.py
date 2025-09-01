from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options}): ")
    if choice == "report" or choice == 'r':
        coffee.report()
        money.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                    coffee.make_coffee(drink)