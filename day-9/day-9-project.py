import os

clear = lambda: os.system('clear')

bids = []


def add_bid_to_dictionary(name, amount):
    bids.append({
        "name":name,
        "amount": amount
    })

while True:
    name = input("What is your name?\n")
    amount =  int(input("What is the amount you want to bid?\n$"))

    add_bid_to_dictionary(name, amount)

    choice = input("Are there any other bidders? y/n: ")

    if choice == "y":
        clear()
        continue
    else:
        clear()
        current_max = -1
        max_name = None
        for bid in bids:
            if bid['amount']>current_max:
                current_max = bid['amount']
                max_name = bid['name']
        
        print(f"The winner of the silent auction is {max_name} who bid ${current_max}")
        break