#!/usr/bin/env python3
"""Raf's Mad Libs!"""

import os
import time

def main():

# Start menu

    print("\t\tWelcome to Raf's Mad Lib!\n\n\
\t\tLet's write a story.\n\n\
Follow the prompt and watch as the story of your dreams appears before your eyes! Remember, adjectives are descriptive. Nouns are a naming word. And verbs are actions!\n\
\tHave fun and good luck!!\n")

    input("Press any key to continue...")


#Ask the user to enter words for story
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    verb1 = input("Enter a verb ending in -ing: ")
    verb2 = input("Enter another verb ending in -ing: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    fruit = input("Enter a type of fruit: ")
    superhero = input("Enter a superhero name: ")
    country = input("Enter a country name: ")
    dessert = input("Enter a type of dessert: ")
    year = input("Enter a year: ")

#Create the story with the user's words filled in
    story = ["Once upon a time, there was a " + adjective1 + " " + animal + " who lived in a " + adjective2 + " " + noun1 + ".",
         "\nOne day, the " + animal + " decided to go " + verb1 + " in the " + noun2 + ".",
         "\nAs the " + animal + " was " + verb2 + ", it suddenly saw a " + fruit + " flying through the air!",
         "\nThe " + animal + " caught the " + fruit + " and felt like a " + superhero + " from " + country + ".",
         "\nThe " + animal + " celebrated by eating some " + food + " and " + dessert + ", and lived happily ever after.",
         "\nThe End, " + year + "."]

#Print to the command line and save to hme directory/pdf  
    with open("madlib.pdf", "w") as madlib:
        for line in story:
            print(line, file = madlib)    

    madlib = "madlib.pdf" 
    print("Your Mad Libs story has been saved to: madlib.pdf")
    answer = input("Do you want to print your story? (y/n): ")
    if answer.lower() == "y":
        with open(madlib, "r") as f:
            content = f.read()
            for letter in content:
                print(letter, end='', flush=True)
                time.sleep(0.05)
    

if __name__ == "__main__":
    main()
