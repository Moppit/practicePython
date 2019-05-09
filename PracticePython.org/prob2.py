"""
Ask the user for a number. Depending on whether the number is even or odd, print
out an appropriate message to the user. Hint: how does an even / odd number
react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.

Ask the user for two numbers: one number to check (call it num) and one number
to divide by (check). If check divides evenly into num, tell that to the user.
If not, print a different appropriate message.
"""

num = int(input("Enter a number: "))
check = int(input("Enter a second number: "))

if(num%2 == 0):
    if(num%4 == 0):
        print("Oooooh it's a multiple of 4!")
    else:
        print("It's even!")
else:
    print("It's odd!")

# Second extra part
if(num%check == 0):
    print("They divide evenly!")
else:
    print("Your first number is not a multiple of the second :(")

# COMPLETE
