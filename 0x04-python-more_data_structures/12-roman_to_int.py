#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    ro_d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_list = list(roman_string)
    som = 0
    for i in range(len(roman_list)):
        if i > 0 and ro_d[roman_list[i]] > ro_d[roman_list[i - 1]]:
            som += (ro_d[roman_list[i]] - 2 * ro_d[roman_list[i - 1]])
        else:
            som += ro_d[roman_list[i]]
    return som
