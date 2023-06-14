#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for digit in sorted(a_dictionary.keys()):
        print("{}: {}".format(digit, a_dictionary[digit]))
