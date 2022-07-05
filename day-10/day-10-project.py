def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2


def calculate(n1=None, n2=None):
    if not n1:
        n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    operation = input("Enter + for addition, - for subtration, * for multication and  / for division: ")
    result = None
    if operation == '+':
        result = add(n1, n2)
    elif operation == '-':
        result = sub(n1, n2)
    elif operation == '*':
        result = multiply(n1, n2)
    else:
        result = divide(n1, n2)
    
    print(f"{n1} {operation} {n2} = {result}")

    choice = input("If you want to perform another calculation with the result enter y, else enter n: ")
    if choice == 'y':
        calculate(n1=result)
    else:
        calculate()

calculate()