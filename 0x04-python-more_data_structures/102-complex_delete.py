#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        keys = list(a_dictionary.keys())
        val = list(a_dictionary.values())

        time = val.count("C")

        for i in range(0, time):
            pos = val.index("C")
            value = keys[pos]
            del a_dictionary[value]
            del keys[pos]
            del val[pos]
    return a_dictionary
