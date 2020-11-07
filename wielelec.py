from questions import *

import random

CHANCES = 9

def print_question(question, found):
    for letter in question:
        if letter.lower() in found:
            print(letter, end='')
        else:
            print('*', end='')
    print()


question = random.choice(questions)
left = CHANCES
found = set()
tried = set()
while True:
    print_question(question, found)

    # TODO check if is a letter
    letter = input(f"Szans: {left}. Wybierz literę > ").lower()
    if len(letter) > 1:  # if more than 1 letter
        letter = letter[0]  # take the first one
        
    elif len(letter) < 1:  # if empty string provided
        continue  # repeat the input
    tried.add(letter)  # collecting tried
    if letter in question.lower():
        found.add(letter)
    else:
        left -= 1
    
    if found == set(question.lower()):
        print('Wygrałeś!')
        print_question(question, found)
        exit()
    elif left == 0:
        print('Przegrałeś!')
        print_question(question, found)
        exit()
