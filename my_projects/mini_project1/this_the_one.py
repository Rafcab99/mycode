#!/usr/bin/env python3

import  random

number = random.randint(1, 100)

tries = 5

while tries > 0:
    print(f'You have {tries} tries left.')
    guess = input('Guess the number (1-100): ')
    while not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
        guess = input('Invalid input. Guess the number (1-100): ')
    guess = int(guess)
    if guess == number:
        print('Congratulations, you guessed the number!')
        break
    elif guess < number:
        print('The number is higher.')
    else:
        print('The number is lower.')
    tries -= 1

if tries == 0:
    print(f'You ran out of tries. The number was {number}.')
