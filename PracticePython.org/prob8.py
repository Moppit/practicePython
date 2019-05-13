"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message
of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
"""
import random

def attackMenu():
    print("Choose your attack!")
    print("A. Rock")
    print("B. Paper")
    print("C. Scissors")

def checkWinner(userChoice, compChoice):
    print("You chose " + printType(userChoice))
    print("Computer chose " + printType(compChoice))
    highest = (userChoice + 1)%3 # The highest will always be one more than the previous, unless it hits three
    if(userChoice == compChoice):
        print("Tie!")
    elif(compChoice == highest):
        print("Computer wins!")
    else:
        print("User wins!")

def printType(integer):
    if(integer == 0):
        return "rock"
    if(integer == 1):
        return "paper"
    if(integer == 2):
        return "scissors"

stillPlaying = True

while(stillPlaying):
    choice = input("Would you like to play Rock, Paper, Scissors? (Y/N): ")
    if(choice == "Y" or choice == "y"):
        attackMenu()
        user = input("")
        # Generate the computer's value
        comp = random.randint(0, 2)
        print(comp)
        if(user == "A"):
            checkWinner(0, comp)
        elif(user == "B"):
            checkWinner(1, comp)
        else:
            checkWinner(2, comp)
        print()
    elif(choice == "N" or choice == "n"):
        print("Thanks for playing!")
        stillPlaying = False
    else:
        print("Invalid input, try again.")
