#!/usr/bin/python3
for characters in range(122, 96, -1):
    if characters % 2 != 0:
        characters -= 32
    str = chr(characters)
    print("{}".format(str), end="")
