#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    repeat = my_list.count(search)
    for i in range(repeat):
        idx = new_list.index(search)
        new_list[idx] = replace
    return new_list
