"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads
the same forwards and backwards.)
"""

def palindrome(toCheck):
    for i in range (len(toCheck)):
        if(toCheck[i] != toCheck[len(toCheck)-i-1]):
            return "False"

    return "True"

print(palindrome("this is not a palindrome"))
print(palindrome("sittis"))
