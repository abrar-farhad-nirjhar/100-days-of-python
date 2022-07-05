print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? s/m/l: ")
add_extra_meat = input("Do you want extra mean? y/n: ")
extra_cheese = input("Do you want extra cheese? y/n: ")
total_price = 0

if size == 's':
    total_price += 15
    if add_extra_meat == 'y':
        total_price += 2
elif size == 'm':
    total_price += 20
    if add_extra_meat == 'y':
        total_price += 3
else:
    total_price += 25
    if add_extra_meat == 'y':
        total_price += 3

if extra_cheese == 'y':
    total_price += 1

print(f"Your final bill is: ${total_price}.")
