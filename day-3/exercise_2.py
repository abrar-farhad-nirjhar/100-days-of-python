print("Welcome to the rollercoaster!!")
height = int(input("WHat is your height in cm?"))


if height < 120:
    print("Sorry you're not tall enough to ride the rollercoaster.")
else:
    age = int(input("What is your age?"))
    if age < 12:
        print("That will be $5 please.")
    elif age <= 18:
        print("That will be $7 please.")
    else:
        print("That will be $12 please.")
