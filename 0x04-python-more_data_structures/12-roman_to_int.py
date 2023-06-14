#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        dictionary = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        value = 0
        for p, q in zip(roman_string, roman_string[1:]):
            if dictionary[p] < dictionary[q]:
                value -= dictionary[p]
            else:
                value += dictionary[p]
        value += dictionary[roman_string[-1]]
        return value
    else:
        return 0
