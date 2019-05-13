"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
user the same string, except with the words in backwards order. For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
"""

def reverse(toReverse):
    # Split the string
    originalOrder = toReverse.split(" ")

    # Add all the elements starting at the front to the new list
    newList = []
    for element in originalOrder:
        newList = [element] + newList
    # Join the list with a space and return
    return " ".join(newList)

print(reverse("I certainly hope this works!"))
print(reverse("This one too?"))
