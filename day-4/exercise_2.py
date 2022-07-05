import random
names = input(
    "Enter the names of the participants in a comma and space separated format:\n")
names = names.split(', ')

who_is_gonna_pay = names[random.randint(0, len(names)-1)]

print(f"{who_is_gonna_pay} is gonna buy the meal today.")
