"""
Wikipedia
"""

import wikipedia
from wikipedia import PageError, DisambiguationError

user_search = input("Enter page title: ")
while user_search != "":
    try:
        us = wikipedia.page(user_search, auto_suggest=False)
        print(us.title)
        print(us.summary)
        print(us.url)
    except PageError:
        print(f"Page id '{user_search}' does not match any pages. Try another id!")
    except DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print("['Pythonidae', 'Python (genus)', 'Python (mythology)', 'Python (programming language)', "
              "'CMU Common Lisp'...")
    print('\n')
    user_search = input("Enter page title: ")
print("Thank you.")
