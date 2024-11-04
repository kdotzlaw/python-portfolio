'''
Tic Tac Toe
Rules:
- 2 player game where one player is X and the other is O
- 1 player is the user the other is the computer
- X goes first
- Player wins when they get 3 in a row either horizontally, vertically, or diagonally
- If the board is full, there is a tie
'''
# imports
import random
import sys

game_over = False

board={1:"   ", 2:"   ", 3:"   ", 4:"   ", 5:"   ", 6:"   ", 7:"   ", 8:"   ", 9:"   "}

def check_win(board, player):
    # check for horizontal win
    if board[1] == player and board[2] == player and board[3] == player:
        return True
    elif board[4] == player and board[5] == player and board[6] == player:
        return True
    elif board[7] == player and board[8] == player and board[9] == player:
        return True
    # check for vertical win
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[3] == player and board[6] == player and board[9] == player:
        return True
    # check for diagonal win
    elif board[1] == player and board[5] == player and board[9] == player:
        return True
    elif board[3] == player and board[5] == player and board[7] == player:
        return True
    else:
        return False # no win
# check if the board is full -- False if not
def check_board(board):
    for i in range(1,10):
        if board[i] == "   ":
            return False
    return True

# prints the board 
def print_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("-----------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print()
        

if __name__ == '__main__':
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    turn = ''
    computer = ''
    # randomly choose who starts
    player = 'X' if random.randint(0, 1) == 0 else 'O'
    if player == 'X':
        computer = 'O'
        print("You are X and its your turn first")
        turn = 'player'
        
    else:
        print("You are O and it is the computers turn first")
        computer = 'X'
        turn = 'computer'
    while not game_over:
        if turn == 'player':
            if not check_board(board):
                # get user input
                user_input = input("Enter a number from 1-9: ")
                # place the user input in the board
                board[int(user_input)] = player
                print_board(board)
            # always check for a win after a move
            
            if check_win(board, player):
                print("You win!")
                game_over = True
            elif check_win(board, computer):
                print("You lose!")
                game_over = True
            
        else: #computer turn
            # if the board is empty, ie the computer goes first
            if not check_board(board):
                 # the computer will choose randomly between 1-9  where the choice is weighted 
                sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                computer_choice = random.choices(sample, weights=[20,10,20,10,30,10,20,10,20], k=1)
                while board[computer_choice[0]] != "   ":
                    computer_choice = random.choices(sample, weights=[20,10,20,10,30,10,20,10,20], k=1)
                # place the computer choice in the board
                board[computer_choice[0]] = computer
                print_board(board)
                # always check for a win after a move
            
            if check_win(board, player):
                print("You win!")
                game_over = True
            elif check_win(board, computer):
                print("You lose!")
                game_over = True
             
        turn = 'player' if turn == 'computer' else 'computer'
        
        if check_board(board):  
                # check for a win for the player
            if check_win(board, player):
                print("You win!")
                game_over = True
            elif check_win(board, computer):
                print("You lose!")
                game_over = True
            else:
                print("It's a tie!")
                game_over = True   
                       
                   