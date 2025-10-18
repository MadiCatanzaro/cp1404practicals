"""
Word Occurrences
Estimate: 20 minutes
Actual: 1 hour
"""

string = str(input("Text: ")).split(" ")
word_to_count = {}
for word in string:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_word_length = max((len(word)) for word in word_to_count)
for word, count in sorted((word_to_count.items())):
    print(f"{word:<{max_word_length}} : {count}")
