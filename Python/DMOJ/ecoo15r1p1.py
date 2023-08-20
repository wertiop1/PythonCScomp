from math import ceil
for cases in range(10):
    red = 0
    violet = 0
    blue = 0
    pink = 0
    brown = 0
    green = 0
    yellow = 0
    orange = 0
    while 1:
        color = input()
        if color == "end of box":
            break
        elif color == "red":
            red = red + 1
        elif color == "brown":
            brown = brown + 1
        elif color == "violet":
            violet = violet + 1
        elif color ==  "blue":
            blue = blue + 1
        elif color == "pink":
            pink = pink + 1
        elif color == "green":
            green = green + 1
        elif color == "yellow":
            yellow = yellow + 1
        elif color == "orange":
            orange = orange + 1
    hand = (ceil(brown/7)+ceil(violet/7)+ceil(blue/7)+ceil(pink/7)+ceil(green/7)+ceil(yellow/7)+ceil(orange/7))
    print(hand * 13 + red * 16)