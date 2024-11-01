class CoffeeMaker:
    def __init__(self):
        self.resources = {'milk':200, 'water':300, 'coffee':100}
        print('Resources available: '+str(self.resources))
    
    
    def report(self):
        print('Resources available: ')
        for resource in self.resources:
            print(resource)
            print(self.resources[resource])
            
    # ingredient is int of a single ingredient amt
    def check_resources(self, ingredient, amount):
        return self.resources[ingredient]>=amount
            
    
    def make_coffee(self, ingredients, amount):
        print('Making coffee')
        orig = self.resources
        for ingredient in ingredients:
            if self.check_resources(ingredient, amount):
                self.resources[ingredient] -= ingredients[ingredient]
                print('You have ' + str(self.resources[ingredient]) + ' of ' + ingredient)
            else:
                print('Sorry, you do not have enough ' + ingredient)
                # add back all the ingredients
                for ingredient in ingredients:
                    if self.resources[ingredient] != orig[ingredient]:
                        self.resources[ingredient] += ingredients[ingredient]
                return False
        return True
        