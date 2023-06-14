#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for d in list(a_dictionary.keys()):
        if a_dictionary[d] is value:
            del a_dictionary[d]
    return a_dictionary
