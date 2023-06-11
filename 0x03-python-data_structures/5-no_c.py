#!/usr/bin/python3
"""n_string : new string """
def no_c(my_string):
    n_string = ""
    for char in range(len(my_string)):
        if my_string[char] != 'c' and my_string[char] != 'C':
            new_string += my_string[char]
    return n_string
