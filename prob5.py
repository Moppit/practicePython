"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on
two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at
this point - we’ll get to it soon)
"""
import random

def randomList():
    # Generate length
    length = random.randint(0, 20)
    # Make empty list
    d = []
    # For each element, generate a random number and append to list
    for i in range(length):
        d.append(random.randint(0, 20))
    # Return yo list
    return d

# Find the list of longer length
def listSimilarity(a = [], b = [], *args):
    # Print initial lists
    print("First list: ", end = " ")
    for z in a:
        print(z, end = " ")
    print("")
    print("Second list: ", end = " ")
    for y in b:
        print(y, end = " ")
    print("")

    c = []
    # Actual list similarity
    if(len(a) >= len(b)):
        longBoi = a
        shortBoi = b
    else:
        longBoi = b
        shortBoi = a

    # Iterate through each element of that boi
    for element in longBoi:
        # For each element check if it is in the shorter list
        if element in shortBoi:
            # If it is, check if it exists in list c
                if element not in c:
                    # If it doesn't, add to c
                    c.append(element)

    # Print dat boi
    print("Overlapping Elements: ", end = " ")
    for i in c:
        print(i, end = " ")
    print("")

# Test
list1 = randomList()
list2 = randomList()
listSimilarity(list1, list2)

# COMPLETE
