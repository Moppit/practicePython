"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message. (Hint: order of
operations exists in Python)

Print out that many copies of the previous message on separate lines. (Hint: the
string "\n is the same as pressing the ENTER button)
"""

name = input("What's your name?: ")
age = input("How old are you? (in years): ")
year = 2019-int(age)+100
numPrint = int(input("How many times do you want us to print our sagacious advice?: "))
count = 0

while(count < numPrint):
    print(name + ", seeing as it is 2019, you will turn 100 in " + str(year))
    count+=1

# COMPLETE
