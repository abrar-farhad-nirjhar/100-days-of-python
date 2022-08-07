class CoffeeMaker:
    def __init__(self, resources):
        self.resources = resources

    def report(self):
        for k, v in self.resources.items():
            print(f"{k.capitalize()}: {v}")

    def is_resource_sufficient(self, item):
        for k in item.ingredients:
            if item.ingredients[k] > self.resources[k]:
                print(f"Not enough {k} to make this drink. Sorry.")
                return False
        return True

    def make_coffee(self, item):
        for k in item.ingredients:
            if k in self.resources:
                self.resources[k] -= item.ingredients[k]
        print(f"Here is your {item.name}. Have a nice day")
