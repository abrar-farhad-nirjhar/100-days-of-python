import math
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# print((int(weight)/(float(height)**2)))
height = float(height)
weight = int(weight)
result = weight/(height**2)

print(f"Your BMI is {result}")

if result < 18.5:
    print("You are underweight")
elif result >= 18.5 and result < 25:
    print("Your weight is normal.")
elif result >= 25 and result < 30:
    print("You are overweight.")
elif result >= 30 and result < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
