"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.

Write this in one line of Python. # Frick this one, not useful

Ask the user for a number and return a list that contains only elements from the
original list a that are smaller than that number given by the user.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in range(len(a)):
    if(a[i] < 5):
        b.append(a[i])

print("Proof stuff doesn't print beforehand!")

for j in range(len(b)):
    print(b[j])

# More extra stuff
num = int(input("Enter in the upper bound: "))
for element in a:
    if(element < num):
        print(element)
