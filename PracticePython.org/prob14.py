"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

def removeDuplicates(a = [], *args):
    newList = []
    for element in a:
        if element not in newList:
            newList.append(element)
    return newList

a = [1, 2, 3, 4, 5, 6, 3, 5, 2, 6, 3, 5, 3, 1]

b = removeDuplicates(a)
for element in b:
    print(element)
