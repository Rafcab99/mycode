#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
import random 
def main():
    number = random.randint(1, 100)

    tries = 5
    guess = 0
    while tries > 0 and guess != number:
        print(f'You have {tries} tries left. ')
        guess= input("Guess a number between 1 and 100\n>")
        while not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
        # COOL CODE ALERT: what is the purpose of the next four lines?
            if guess.isdigit():
               guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            tries - 1

        elif guess < num:
            print("Too low!")
            tries - 1

        else:
            print("Correct!")
if __name__ == "__main__" :
    main()
main()
