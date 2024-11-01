class MoneyMachine:
    def __init__(self):
        self.coins = {'toonies':2.00, 'loonies':1.00, 'quarters':0.25, 'dimes':0.10, 'nickels':0.05, 'pennies':0.01}
        self.total_money=0
    
    # add money paid to total money
    def add_money(self, amount):
        self.total_money += amount
        return self.total_money
    
    
    def payment(self, num_coins, amount):
        print('Here are your coins'+str(self.coins))
        sum = 0
        for coin in self.coins:
            num = int(input('How many '+coin+' do you want? '))
            sum += num * self.coins[coin]
        # check if payment is successful
        if sum == num_coins:
            print('Payment successful')
            self.add_money(sum)
            return True
        elif sum > num_coins:
            print('Here is your change: $'+str(sum-amount))
            self.add_money(sum-amount)
            return True
        else:
            print('Sorry, you do not have enough money')
            return False