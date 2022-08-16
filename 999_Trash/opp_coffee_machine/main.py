from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

off = False

while not off:
    options = menu.get_items()
    user_choice = input(f"What would you like ({options})?: ").lower()
    if user_choice == "off":
        off = True
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        chosen_drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(chosen_drink):
            if money_machine.make_payment(chosen_drink.cost):
                coffee_maker.make_coffee(chosen_drink)


