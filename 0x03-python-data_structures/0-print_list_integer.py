#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))


my_list = [1, 2, 3, 4, 5, 8, 123, 1998]
print_list_integer(my_list)
