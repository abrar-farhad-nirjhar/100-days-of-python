class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        result = ''
        for item in self.items:
            result += item.name+'/'

        return result[0:len(result)-1]

    def find_drink(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return
