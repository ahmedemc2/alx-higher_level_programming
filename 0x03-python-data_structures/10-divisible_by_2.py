#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in range(len(my_list)):
        new_list[i] = True if my_list[i] % 2 == 0 else False
    return new_list
