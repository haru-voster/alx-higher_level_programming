#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
    A peak is an Element in An array if its NOT smaller
    than its neighbours.
"""


def find_peak(list_of_integers):
    """ returns the a peak in a an unsored list"""

    if list_of_integers == []:
        return None

    siz = len(list_of_integers)
    if siz == 1:
        return list_of_integers[0]
    elif siz == 2:
        return max(list_of_integers)

    hlf = int(siz / 2)
    peak = list_of_integers[hlf]
    if peak > list_of_integers[hlf - 1] and peak > list_of_integers[hlf + 1]:
        return peak
    elif peak < list_of_integers[hlf - 1]:
        return find_peak(list_of_integers[:hlf])
    else:
        return find_peak(list_of_integers[hlf + 1:])
