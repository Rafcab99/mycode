#!/usr/bin/env python3
import random

def main():
    
    names = ['Lexi', 'Trey', 'Zack', 'Wade', 'Kevin', 'Aidi', 'Clark', 'Darrin', 'James', 'Matt', 'Rhett', 'Chris', 'Rafael', 'Hutch', 'Steph']

    chosen_name = random.choice(names)

    tries = 5

    while tries > 0:
        print(f'You have {tries} tries left.')
        guess = input('Guess the classmate I\'m thinking of: ').title()
        while guess not in names:
            guess = input('Invalid input. Guess the name: ')
        if guess == chosen_name:
            print('Congratulations, you guessed the name!')
            break
        else:
            print('Incorrect guess.')
            tries -= 1

    if tries == 0:
        print(f'You ran out of tries. The name was {chosen_name}.')

if __name__ == "__main__":
    main()
