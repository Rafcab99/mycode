#!/usr/bin/env python3
"""Raf's Mad Libs!"""

import os

def main():

    print("Welcome to Raf's Mad Libs!")
    print("Please enter some words to complete the following story:")

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
         "One day, the " + animal + " decided to go " + verb1 + " in the " + noun2 + ".",
         "As the " + animal + " was " + verb2 + ", it suddenly saw a " + fruit + " flying through the air!",
         "The " + animal + " caught the " + fruit + " and felt like a " + superhero + " from " + country + ".",
         "The " + animal + " celebrated by eating some " + food + " and " + dessert + ", and lived happily ever after.",
         "The End, " + year + "."]

#Print to the command line and save to hme directory
    filename = os.path.join(os.path.expanduser("~"), "madlibs.txt")
    with open(filename, "w") as f:
        for line in story:
            f.write(line + "\n")
            print(line)
            input("Press Enter to continue...")

    print("Your Mad Libs story has been saved to:", filename)

if __name__ == "__main__":
    main()
