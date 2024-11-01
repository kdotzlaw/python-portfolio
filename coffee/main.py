import numpy as np
# Global variables
moneyMade = 0
customersServed = 0
coffees = {'Cappucino': 2.50, 'Latte': 1.75, 'Espresso': 2.70}
resources = {'milk': 200, 'water': 300, 'coffee': 100}
needed = {'Cappucino': {'milk':50, 'water': 200 , 'coffee': 14}, 'Latte': {'milk': 70, 'water': 50, 'coffee': 10}, 'Espresso': {'milk': 20, 'water': 100, 'coffee': 30}}
coins = {'toonies': 2.00, 'loonies': 1.00, 'quarters': 0.25,'dimes': 0.10, 'nickels': 0.05, 'pennies': 0.01}


def report():
    print('Coffees made: ' + str(moneyMade))
    print('Customers served: ' + str(customersServed))
    print('Resources remaining: ' + str(resources))
    return

def payment(amount):
    global moneyMade
    print('Here are your coins: ' + str(coins))
    sum = 0
    for key in coins:
        num = input('How many  ' + key + ' do you want to use? ')
        sum += coins[key]*int(num)
    #sum = np.sum(use.values()*coins.values())
    
    if sum < amount:
        print('You dont have enough money')
        return False
    elif sum > amount:
        print('Here is your change : '+ str(sum - amount))
        moneyMade += sum - amount
        return True
    else:
        # if payment is successful, add to money made
        moneyMade += amount
        return True
    
    
def coffeeShop(coffeeType):
    global customersServed
    print('You chose ' + coffeeType+' which costs $' + str(coffees[coffeeType]))
    # check if resources are available
    if resources['milk'] >= needed[coffeeType]['milk'] and resources['water'] >= needed[coffeeType]['water'] and resources['coffee'] >= needed[coffeeType]['coffee']:
       # check if user has enough money
       if payment(coffees[coffeeType]):
          # deduct resources
          print('Here is your '+ coffeeType)
          resources['milk'] -= needed[coffeeType]['milk']
          resources['water'] -= needed[coffeeType]['water']
          resources['coffee'] -= needed[coffeeType]['coffee']
          customersServed += 1
          print('Resources remaining: ' + str(resources))
    else:
        print('Sorry, there are not enough resources to make that coffee')
    return        
     
       
    
    

if __name__ == '__main__':
   print('Welcome to Coffee')
   while True:
      print('What type of coffee do you want?')
      print('Coffee types: Cappucino, Latte, Espresso' + '\n' + 'Or type "Off" to end')
      coffeeType = input()
      if coffeeType == 'Off':
         report()
         break
      else:
         coffeeShop(coffeeType)
   exit()