# add to path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.money import MoneyMachine
from src.menu import Menu
from src.coffee import CoffeeMaker


if __name__ == '__main__':
    # initialize
    menu = Menu()
    coffeeMachine = CoffeeMaker()
    moneyMachine = MoneyMachine()
    customers=0
    # display menu
    menu.display_menu()
    # prompt user for coffee choice
    choice = input('What type of coffee do you want? ')
    while choice != 'off':
        customers+=1
        # get item
        item = menu.find_item(choice)
        # check if resources are available
        for ingredient in item.ingredients:
            #print(ingredient)
            if not coffeeMachine.check_resources(ingredient, item.ingredients[ingredient]):
                print('Sorry, you do not have enough ' + ingredient.name)
                break
        else:
            # if resources are available, prompt user for payment
            # if payment is successful, make the coffee
            if moneyMachine.payment(item.price):
            #if moneyMachine.total_money >= item.price:
                coffeeMachine.make_coffee(item.ingredients,item.price)
                # display a message
                print('Here is your coffee')
                print('Enjoy!')
            
        
        choice = input('What type of coffee do you want? ')
        
    coffeeMachine.report()
    print('Customers served: ' + str(customers))
    print('Total money made: $' + str(moneyMachine.total_money))
    exit()