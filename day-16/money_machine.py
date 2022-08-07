class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: {self.profit}")

    def make_payment(self, cost):
        pennies = int(input("Number of Pennies: "))*0.01
        nickels = int(input("Number of Nickels: "))*0.05
        dimes = int(input("Number of Dimes: "))*0.1
        quarters = int(input("Number of Quarters: "))*0.25
        total = pennies + nickels + dimes + quarters
        if cost > total:
            print("Sorry that's not enough money. Money Refunded")
            return False
        print(f"Here is your change ${total-cost}")

        self.profit += cost
        return True
