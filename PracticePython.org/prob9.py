"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first
exercise)

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

def isNum(toCheck):
    tis = True
    for i in range(len(toCheck)):
        if toCheck[i] < '0' or toCheck[i] > '9':
            tis = False
    return tis

magicalOne = random.randint(1, 9)

stillPlaying = True
numGuesses = 0

while(stillPlaying):
    guess = input("Guess the number! It's from 1 to 9, inclusive (type 'exit' to quit): ")
    numGuesses+=1
    if(guess == "exit"):
        print("Goodbye!")
        stillPlaying = False
    elif(isNum(guess)):
        if(int(guess) > magicalOne):
            print("Too high")
        elif(int(guess) < magicalOne):
            print("Too low")
        elif(int(guess) == magicalOne):
            print("You got it! It took you " + str(numGuesses) + " guesses to get it right")
            stillPlaying = False
        else:
            print("Number out of range, try again")
    else:
        print("Invalid input, try again")
