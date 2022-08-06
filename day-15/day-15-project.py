MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

coin_values = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25

}


def is_possible(choice):
    for key in MENU[choice]['ingredients']:
        if MENU[choice]['ingredients'][key] > resources[key]:
            return False
    return True


def adjust_resources(choice):
    resources['money'] += MENU[choice]['cost']
    resources['water'] -= MENU[choice]['ingredients']['water'] if 'water' in MENU[choice]['ingredients'] else 0
    resources['coffee'] -= MENU[choice]['ingredients']['coffee'] if 'coffee' in MENU[choice]['ingredients'] else 0
    resources['milk'] -= MENU[choice]['ingredients']['milk'] if 'milk' in MENU[choice]['ingredients'] else 0


def generate_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    if 'money' in resources:
        print(f"Money: {resources['money']}")


def calculate_money(penny, nickel, dime, quarter):
    total = coin_values['penny']*penny + coin_values['nickel'] * \
        nickel + coin_values['dime']*dime + coin_values['quarter']*quarter
    return total


def get_payment(choice):
    pennies = int(input("Number of Pennies: "))
    nickels = int(input("Number of Nickels: "))
    dimes = int(input("Number of Dimes: "))
    quarters = int(input("Number of Quarters: "))

    total = calculate_money(pennies, nickels, dimes, quarters)

    if MENU[choice]['cost'] > total:
        print("Sorry that's not enough money. Money Refunded")
        return
    return total


def get_change(choice, total):
    return total - MENU[choice]['cost']


resources['money'] = 0
while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'report':
        generate_report()
    elif choice == 'off':
        print("Thank you have a great day.")
        break
    else:
        if not is_possible(choice):
            print("Not enough ingredients")
            continue

        payment = get_payment(choice)

        if not payment:
            continue
        change = get_change(choice, payment)
        adjust_resources(choice)
        print(f"Here is your change: ${change}")
        print(f"Enjoy your {choice} and have a nice day")
