# individual menu items: all have name, price, amt of milk, amt of water, amt of coffee
class MenuItem:
    def __init__(self, name, price, milk, water, coffee):
        self.name = name    
        self.price = price
        self.ingredients = [milk, water, coffee]
        
# full menu: list of menu items, also has own functions
class Menu:
    def __init__(self):
        self.menu=[
            MenuItem('Cappucino', 2.50, 50, 200, 30),
            MenuItem('Latte', 1.75, 70, 50, 10),
            MenuItem('Espresso', 2.70, 20, 100, 50)
        ]
        
    def find_item(self, name):
        for item in self.menu:
            if item.name == name:
                return item
      

         
    def display_menu(self):
        for item in self.menu:
            print(item.name)
            print(item.price)
            print(item.ingredients)