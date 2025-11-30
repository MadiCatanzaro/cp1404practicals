"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    empty_car = Car()
    assert car.fuel == 10
    assert empty_car.fuel == 0


run_tests()

doctest.testmod()


def format_phrase_to_sentence(phrase):
    """
    Format a phrase to have a starting capital letter and end with a full stop.
    >>> format_phrase_to_sentence('hello')
    'Hello.'
    >>> format_phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_to_sentence('the flowers outside are lovely')
    'The flowers outside are lovely.'
    """

    if phrase[-1] == '.':
        return f"{phrase[0].upper()}{phrase[1:]}"
    else:
        return f"{phrase[0].upper()}{phrase[1:]}."
