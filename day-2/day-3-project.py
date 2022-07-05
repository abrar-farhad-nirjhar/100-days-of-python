print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
tip_percentage = float(
    input("What is the tip percentage you would like to give?"))
people_present = float(input("How many people are splitting the bill?"))


total_bill = total_bill + (total_bill*(tip_percentage/100))
each_person_owes = total_bill/people_present

print(f'Each person should pay: {each_person_owes:.2f}')
