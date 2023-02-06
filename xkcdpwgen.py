#!/usr/bin/env python3

import argparse
import random

'''
Using argparse to get command line arguments.
'''
parser = argparse.ArgumentParser(description="Generate a secure, memorable password using the XKCD method.")
parser.add_argument('-w', '--words', type=int, help='include WORDS words in the password (default=4)')
parser.add_argument('-c', '--caps', type=int, help='capitalize the first letter of CAPS random words (default=0)')
parser.add_argument('-n', '--numbers', type=int, help='insert NUMBERS random numbers in the password (default=0)')
parser.add_argument('-s', '--symbols', type=int, help='insert SYMBOLS random symbols in the password (default=0)')
args = parser.parse_args()

'''
General variable setup for the program.
'''
words_string = "" 

if(args.words == None):
    args.words = 4

if(args.caps == None):
    args.caps = 0

if(args.numbers == None):
    args.numbers = 0

if(args.symbols == None):
    args.symbols = 0

with open("words.txt", "r") as file:
	data = file.read()
	words = data.split()

'''
Determines which words to capitalize.
'''
caps_locs = []
try:
    caps_locs = random.sample(range(0, args.words), args.caps)
    caps_locs.sort()
except ValueError:
    print("Cannot capitalize more words than are in the password.")
	
'''
This part takes care of the -w argument. It does so by 
1. creating a string called words_string
2. reading the file words.txt
3. generating a random integer based on the size of words.txt
4. adding the word at that position to the string words_string
This recurrs for as many times as the inputted integer, or 4 if there is no input.
'''
for i in range(args.words):
    word_pos = random.randint(0, len(words)-1)
    add_word = words[word_pos]
    if(len(caps_locs) > 0):
        if(caps_locs[0] == i):
            add_word = add_word.capitalize()
            caps_locs.remove(caps_locs[0])
    words_string = words_string + str(add_word)

'''
Determines where to add numbers in the word_string.
'''
if(args.numbers > 0):
    add_nums = []
    for i in range(args.numbers):
        add_nums.append(random.randint(0, 9))

    if(len(add_nums) > 0):
        num_locs = random.sample(range(0, len(words_string) - 1), len(add_nums))
        for i in range(len(num_locs)):
            words_string = words_string[:num_locs[i] - 1] + str(add_nums[i]) + words_string[num_locs[i] - 1:]

'''
Determines where to add symbols in the word_string.
'''
symbol_list = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]
if(args.symbols > 0):
    add_symbs = []
    for i in range(args.symbols):
        add_symbs.append(symbol_list[random.randint(0, len(symbol_list) - 1)])

    if(len(add_symbs) > 0):
        symb_locs = random.sample(range(0, len(words_string) - 1), len(add_symbs))
        for i in range(len(symb_locs)):
            words_string = words_string[:symb_locs[i] - 1] + str(add_symbs[i]) + words_string[symb_locs[i] - 1:]


print(words_string)
