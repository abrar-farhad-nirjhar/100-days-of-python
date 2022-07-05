print("Welcome to the python Love Calculator!")
name_1 = input("Enter the first name: ").lower()
name_2 = input("Enter the second name: ").lower()

true_count = 0
love_count = 0

for i in 'true':
    true_count += name_1.count(i)
    true_count += name_2.count(i)

for i in 'love':
    love_count += name_1.count(i)
    love_count += name_2.count(i)


result = int(str(true_count)+str(love_count))

if result <= 10 or result >= 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
