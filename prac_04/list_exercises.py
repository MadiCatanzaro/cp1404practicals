"""
List Exercises
"""

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
