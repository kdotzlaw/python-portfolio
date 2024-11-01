from src import money
from src import menu    
from src import coffee


if __name__ == '__main__':
    # initialize
    menu = menu.Menu()
    coffeeMachine = coffee.CoffeeMachine()
    moneyMachine = money.MoneyMachine()
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
            if not moneyMachine.check_resources(ingredient):
                print('Sorry, you do not have enough ' + ingredient)
                break
        else:
            # if resources are available, prompt user for payment
            moneyMachine.payment(item, item.price)
            # if payment is successful, make the coffee
            if moneyMachine.total_money >= item.price:
                coffeeMachine.make_coffee(item.ingredients)
                # remove resources from inventory
                for ingredient in item.ingredients:
                    moneyMachine.add_money(moneyMachine.coins[ingredient])
                # display a message
                print('Here is your coffee')
                print('Enjoy!')
        
        choice = input('What type of coffee do you want? ')
        
    coffeeMachine.report()
    print('Customers served: ' + str(customers))
    print('Total money made: $' + str(moneyMachine.total_money))
    exit()