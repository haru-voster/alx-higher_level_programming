#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_number = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            printed_number += 1
        except Error:
            continue
    print("")
    return printed_number
