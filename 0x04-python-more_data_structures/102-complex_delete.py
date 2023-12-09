#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        keys = list(a_dictionary.keys())
        val = list(a_dictionary.values())

        time = val.count(value)

        for i in range(0, time):
            pos = val.index(value)
            valeur = keys[pos]
            del a_dictionary[valeur]
            del keys[pos]
            del val[pos]
    return a_dictionary
