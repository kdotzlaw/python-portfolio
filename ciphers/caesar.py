'''
ENCRYPTION: take text and shift it by a certain amount
- keep symbols the same 
- keep spaces the same
- keep punctuation the same
- keep numbers the same
DECRYPTION: take the encrypted text and shift it back by the same amount
- keep symbols the same 
- keep spaces the same
- keep punctuation the same
- keep numbers the same
RESTART: ask if user wants to start again then reset cipher
'''
import sys

def caesar(text, shift, direction):
    cipher = ''
    # ord() gives int representation of character
    # set shift direction
    if direction == 'd':
        shift = -shift
    elif direction == 'e':
        shift = +shift
    for char in text:
        # check if character is a letter -- dont encrypt/decrypt if not
        if char.isalpha():
           cipher+= chr((ord(char) + shift))
        else: # if not a letter, keep the same
            cipher += char
    return cipher

if __name__ == '__main__':
    play = True
    while play:
        print("Welcome to the Caesar Cipher!")
        direction = input("Enter 'e' for encryption or 'd' for decryption: ")
        print("Enter the text you want to encrypt or decrypt:")
        text = input()
        print("Enter the amount of shift you want to apply:")
        shift = int(input())
        if direction == 'e':
            print("Your encrypted text is: " + caesar(text, shift, 'e'))
        elif direction == 'd':
            print("Your decrypted text is: " + caesar(text, shift, 'd'))
        inp = input("Would you like to play again? (y/n): ")
        if inp == 'y':
            play = True
        else:
            play = False
    
