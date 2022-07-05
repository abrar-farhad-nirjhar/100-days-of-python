import random


print("Welcome to the PyPassword Generator!")


alphabets_upper = [chr(i) for i in range(65, 91, 1)]

alphabets_lower = [chr(i) for i in range(97, 123, 1)]

alphabets = alphabets_upper+alphabets_lower

special_characters = [chr(i) for i in range(32, 47, 1)] + [chr(i) for i in range(
    91, 97, 1)] + [chr(i) for i in range(58, 65, 1)] + [chr(i) for i in range(123, 127, 1)]

numbers = [str(i) for i in range(10)]

number_of_letters = int(
    input("How many letters do you want in the password: \n"))

password = [' ']*number_of_letters
number_of_numbers = 0
number_of_special_characters = 0
while True:
    number_of_numbers = int(
        input("How many numbers would you like in your password?\n"))
    if number_of_numbers > number_of_letters:
        print("Sorry the number of numbers cannot be greater than the number of letters. Please try again.")
    else:
        break

while True:
    number_of_special_characters = int(
        input("How many special characters would you like in your password? \n"))
    if number_of_special_characters > number_of_letters:
        print(
            f"Sorry the number of special characters cannot be greater than the number of letters. Please try again. Max you can select is {number_of_letters-number_of_numbers}")
    else:
        break


count = 0

while count != number_of_special_characters:
    idx = random.randint(0, number_of_letters-1)
    special_characters_index = random.randint(0, len(special_characters)-1)

    if password[idx] == ' ':
        password[idx] = special_characters[special_characters_index]
        count += 1


count = 0

while count != number_of_numbers:
    idx = random.randint(0, number_of_letters-1)
    numbers_index = random.randint(0, len(numbers)-1)

    if password[idx] == ' ':
        password[idx] = numbers[numbers_index]
        count += 1

count = 0

while count != (number_of_letters-number_of_numbers-number_of_special_characters):
    idx = random.randint(0, number_of_letters-1)
    alphabets_idx = random.randint(0, len(alphabets)-1)

    if password[idx] == ' ':
        password[idx] = alphabets[alphabets_idx]
        count += 1

password = ''.join(password)

print(f"Your super secure password is : {password}")

# SHUFFLE FUNCTION KEEP IN MIND
