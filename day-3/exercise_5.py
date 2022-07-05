print("Welcome to the rollercoaster!!")
height = int(input("WHat is your height in cm?"))
price = None

if height < 120:
    print("Sorry you're not tall enough to ride the rollercoaster.")
else:
    age = int(input("What is your age?"))
    if age < 12:
        price = 5
    elif age <= 18:
        price = 7
    else:
        price = 12

    wants_photo = input("Do you want a photo taken? y/n")

    if wants_photo == 'y':
        price += 3

    print(f"That will be ${price}.")
