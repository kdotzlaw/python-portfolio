import random
import numpy as np
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
stillPlaying = True
dPts = 0
pPts = 0
result = []

def reset():
   player_hand = []
   dealer_hand = []
   stillPlaying = True
   dPts = 0
   pPts = 0
   # win status, point total
   result = []
   return

def play():
    
    # choose a random card from the deck for the dealer
    dealer_hand.append(random.choice(cards))
    print('Dealer has ' + str(np.sum(dealer_hand)) + ' points')
    # choose a random card from the deck for the player
    player_hand.append(random.choice(cards))
    print('You have ' + str(np.sum(player_hand)) + ' points')
    # dont need to compare yet
    # dealer always gets a second card
    print('Dealer gets a card')
    dealer_hand.append(random.choice(cards))
    print('Dealer has ' + str(np.sum(dealer_hand)) + ' points')
    # check dealer score
    dPts = np.sum(dealer_hand)
    if dPts > 21:
        result = ['Bust', dPts]
        return result
    elif dPts == 21:
        result = ['Blackjack', dPts]
        return result
    else:
        while np.sum(player_hand) < 21:
           print('Dealer has ' + str(dPts) + ' points')
           print('You have ' + str(np.sum(player_hand)) + ' points')
           # ask player if they want to hit
           resp = input('Hit? (y/n)')
           if resp == 'y':
             # player gets a card
             print('Player gets a card')
             player_hand.append(random.choice(cards))
             print('You have ' + str(np.sum(player_hand)) + ' points')
             # check player score
             pPts = np.sum(player_hand)
             if pPts > 21:
                result = ['Lose', pPts]
                return result
             elif pPts == 21:
                result = ['Blackjack', pPts]
                return result
             else:
                # check if dealer gets another card
                if dPts < 17:
                    dealer_hand.append(random.choice(cards))
                    dPts = np.sum(dealer_hand)  
                    if dPts > 21: 
                        result = ['Win', pPts]
                        return result
                    elif dPts == 21:
                        result = ['Blackjack', dPts]
                        return result  
          
           else:
                # player doesnt hit
                # compare the two hands
                if np.sum(player_hand) > np.sum(dealer_hand):
                    result = ['Win', np.sum(player_hand)]
                    return result
                elif np.sum(player_hand) < np.sum(dealer_hand):
                    result = ['Lose', np.sum(dealer_hand)]
                    return result
                else:
                    result = ['Draw', np.sum(player_hand)]
                    return result
    return result


if __name__ == '__main__':
  print('Welcome to Blackjack')
  while stillPlaying:
     reset()
     result = play()
     if result[0] == 'Lose':
        if result[1] > 21:
            print('Bust')
        else:
            print('You lose')
     elif result[0] == 'Win':
        print('You win with a score of ' + str(result[1]))
     elif result[0] == 'Blackjack':
        print('You win with a blackjack')
     else:
        print('Draw')
     print('Do you want to play again?')
     resp = input('(y/n)')
     if resp == 'y':
        continue
     else:
        stillPlaying = False
  print('Thanks for playing')
  exit()
     

  
