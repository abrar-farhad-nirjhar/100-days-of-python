from menu_item import MenuItem
from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

espresso = MenuItem('Espresso', 1.5, {
    "water": 50,
    "coffee": 18,
})
latte = MenuItem("Latte", 2.5, {
    "water": 200,
    "milk": 150,
    "coffee": 24,
})
cappuccino = MenuItem("Cappuccino", 3.0, {
    "water": 250,
    "milk": 100,
    "coffee": 24,
})

menu_obj = Menu()
menu_obj.add_item(espresso)
menu_obj.add_item(latte)
menu_obj.add_item(cappuccino)

money_machine_obj = MoneyMachine()

coffee_maker_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_maker_obj = CoffeeMaker(coffee_maker_resources)

while True:
    choice = input(f"What do you want to order? {menu_obj.get_items()}: ")
    if choice == 'report':
        coffee_maker_obj.report()
        money_machine_obj.report()
    elif choice == 'off':
        print("Thank you! Have a nice day.")
        break
    else:
        item = menu_obj.find_drink(choice)

        if not item:
            print("The drink is not available.")
            continue

        if not coffee_maker_obj.is_resource_sufficient(item):
            continue

        if not money_machine_obj.make_payment(item.cost):
            continue

        coffee_maker_obj.make_coffee(item)
