def check_prime(n):
    if n == 1 or n==2:
        print("PRIME")
    elif n%2==0:
        print("NOT PRIME")
    else:
        is_prime = True
        for i in range(3, n, 1):
            if n % i ==0:
                is_prime = False
                break
        
        if is_prime:
            print("PRIME")
        else:
            print("NOT PRIME")

    
number = int(input("Enter the number you want to check:\n"))

check_prime(number)
