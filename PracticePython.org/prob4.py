"""
Create a program that asks the user for a number and then prints out a list of
all the divisors of that number. (If you don’t know what a divisor is, it is a
number that divides evenly into another number. For example, 13 is a divisor of
26 because 26 / 13 has no remainder.)
"""

# Your original, brute force/ugly method
num = int(input("Enter a number: "))
for i in range(num):
    if(num%(i+1) == 0):
        print(i+1)
