"""
Hexadecimal Colours
"""

COLOURS = {"Banana Yellow": "#ffe135", "Bitter Lime": "#bfff00", "BlanchedAlmond": "#ffebcd",
           "Bleu de France": "#318ce7", "Boysenberry": "#873260", "Brilliant Rose": "#ff55a3",
           "British Racing Green": "#004225", "Bubble Gum": "#ffc1cc", "Carnation Pink": "#ffa6c9",
           "Carrot Orange": "#ed9121"}
print(COLOURS)

colour = input("Please input a colour: ")
while colour != "":
    try:
        print(colour, 'is', COLOURS[colour])
        colour = input("Please input a colour: ")
    except KeyError:
        print("Invalid colour name")
        colour = input("Please input a colour: ")
