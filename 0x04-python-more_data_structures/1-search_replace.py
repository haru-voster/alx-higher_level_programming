#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if elmt == search else elmt for elmt in my_list]
