#!/usr/bin/python3
def remove_char_at(str, n):
    for character in str:
        str1 = str[0:n]
        str2 = str[n + 1 : len(str)]
        return str1 + str2
