from turtle import width


def calculation(height=None, width=None, coverage=None):
    number_of_cans_required = (height*width)/coverage
    print(f"The nuber of cans required is {number_of_cans_required}")


width = int(input("What is the width of the wall?\n"))
height = int(input("What is the height of the wall?\n"))

coverage = 5

calculation(width=width, height=height, coverage=coverage)
