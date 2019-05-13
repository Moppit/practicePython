"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime
number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this
opportunity to practice using functions, described below.
"""

def isFactor(num, multiple):
    if(multiple%num == 0):
        return True
    return False

def isPrime(number):
    for i in range(2, number):
        if (isFactor(i, number)):
            return False
    return True

toCheck = input("Enter a number: ")
if(isPrime(int(toCheck))):
    print("It's prime")
else:
    print("It is not prime")
