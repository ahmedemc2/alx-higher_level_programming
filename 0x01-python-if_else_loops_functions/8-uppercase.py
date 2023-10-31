#!/usr/bin/python3
def uppercase(str):
    output = ""
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            output += chr(ord(character) - 32)
        else:
            output += chr(ord(character))
    print("{}".format(output))
