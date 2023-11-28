#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for alpha in str:
        if ord(alpha) >= 97 and ord(alpha) <= 122:
            alpha = chr(ord(alpha) - 32)
        str1 = str1 + alpha
    print(str1)
