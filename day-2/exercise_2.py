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
print(math.floor(result))
