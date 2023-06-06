#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 4 and digit2 == 6:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
