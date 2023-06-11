#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    replace = my_list[:]
    if idx >= 0 and idx < len(replace):
        replace[idx] = element

    return replace
