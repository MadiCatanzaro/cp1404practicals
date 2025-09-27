"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint


def main():
    user_score = float(input("Enter score: "))
    user_result = determine_result(user_score)
    print(f"Result: {user_result}")
    random_score = randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score of {random_score} with result: {random_result}")


def determine_result(user_score):
    if user_score < 0 or user_score > 100:
        return "Invalid score"
    elif user_score >= 90:
        return "Excellent"
    elif user_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
