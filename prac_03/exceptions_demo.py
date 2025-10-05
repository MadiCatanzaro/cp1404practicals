"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator must not be zero, please try again.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# Question 1
# A ValueError will occur if a string is entered for the numerator or denominator,
# or if the value has a large number of decimal places.

# Question 2
# A ZeroDivisionError will occur if the denominator is 0.

# Question 3
# The code could be changed to include an if statement, if the denominator is inputted as zero,
# the program will ask the user for another value, thus removing the possibility of a ZeroDivisionError.
