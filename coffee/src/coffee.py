class CoffeeMaker:
    def __init__(self):
        self.resources = {'milk':200, 'water':300, 'coffee':100}
    
    
    def report(self):
        print('Resources available: ')
        for resource in self.resources:
            print(resource)
            print(self.resources[resource])
            
    def check_resources(self, ingredient):
        return self.resources[ingredient] > ingredient
    
    def make_coffee(self, ingredients):
        print('Making coffee')
        for ingredient in ingredients:
            if self.check_resources(ingredient):
                self.resources[ingredient] -= ingredient
                print('You have ' + str(self.resources[ingredient]) + ' of ' + ingredient)
            else:
                print('Sorry, you do not have enough ' + ingredient)
                return False