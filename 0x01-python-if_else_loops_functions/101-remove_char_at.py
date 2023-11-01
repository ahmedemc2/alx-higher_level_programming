#!/usr/bin/python3
def remove_char_at(str, n):
    if str and n >= 0:
        for character in str:
            str1 = str[0:n]
            str2 = str[n + 1: len(str)]
            return str1 + str2
    else:
        return str
