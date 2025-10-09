"""
List Exercises
"""

"""Basis List Operations """
number_of_numbers = 5
numbers = []

for value in range(0, number_of_numbers):
    number = input("Number: ")
    numbers.append(float(number))

print(f'The first number is {numbers[0]}')
print(f'The last number is {numbers[-1]}')
print(f'The smallest number is {min(numbers)}')
print(f'The largest number is {max(numbers)}')
print(f'The average of the numbers is {(sum(numbers)) / number_of_numbers}')

"""Woefully inadequate security checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
