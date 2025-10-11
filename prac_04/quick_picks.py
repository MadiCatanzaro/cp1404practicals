"""
Quick Picks
"""

from random import randint

QUICK_PICK = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_picks = int(input("How many quick picks would you like to generate? "))

for line in range(0, number_of_quick_picks):
    quick_pick_numbers = []
    for value in range(0, QUICK_PICK):
        number = randint(MINIMUM, MAXIMUM)
        while number in quick_pick_numbers:
            number = randint(MINIMUM, MAXIMUM)
        quick_pick_numbers.append(number)

    generated_quick_picks = [str(number) for number in quick_pick_numbers]
    print(f"{" ".join(generated_quick_picks):>17}")
