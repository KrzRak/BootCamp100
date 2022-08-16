MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0.0,
}


def check_resources(chosen_drink):
    enough_resources = True
    if resources['water'] < MENU[chosen_drink]["ingredients"]["water"]:
        enough_resources = False
        print(f"Sorry there is not enough water")
    if resources['milk'] < MENU[chosen_drink]["ingredients"]["milk"]:
        enough_resources = False
        print(f"Sorry there is not enough milk")
    if resources['coffee'] < MENU[chosen_drink]["ingredients"]["coffee"]:
        enough_resources = False
        print(f"Sorry there is not enough coffee")
    return enough_resources == True


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['Money']}")


def calculate_coins():
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_amount(amount, chosen_drink):
    if amount >= MENU[chosen_drink]["cost"]:
        resources["Money"] += MENU[chosen_drink]["cost"]
        if amount > MENU[chosen_drink]["cost"]:
            change = round(amount - MENU[chosen_drink]["cost"], 2)
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def reduce_resources(chosen_drink):
    resources['water'] -= MENU[chosen_drink]["ingredients"]["water"]
    resources['milk'] -= MENU[chosen_drink]["ingredients"]["milk"]
    resources['coffee'] -= MENU[chosen_drink]["ingredients"]["coffee"]


def coffee_machine():
    off = False
    while not off:
        user_choice = input(f"What do you like? (espresso/latte/cappuccino): ").lower()

        if user_choice == "off":
            off = True
        elif user_choice == "report":
            print_resources()
        elif check_resources(user_choice):
            user_sum_coins = calculate_coins()
            if check_amount(user_sum_coins, user_choice):
                reduce_resources(user_choice)
                print(f"Here is your {user_choice}☕. Enjoy!")


coffee_machine()
