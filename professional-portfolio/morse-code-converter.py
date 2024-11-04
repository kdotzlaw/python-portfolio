import sys

# create dictionary of international morse code
imc_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def morse_code(string):
    global imc_dict
    res = ''
    # ignore string cases
    string = string.upper()
    
    for char in string:
        res += imc_dict[char] + ' '
    return res

if __name__ == '__main__':
    print('Enter a string to convert to Morse Code:')
    string = input()
    print("Your original string is: " + string)
    print("Your string in Morse Code is: " + morse_code(string))
