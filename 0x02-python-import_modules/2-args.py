#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv) - 1

    print(arg, end=" ")

    if arg == 1:
        print("argument", end="")
    else:
        print("arguments", end="")

    if arg == 0:
        print(".")
    else:
        print(":")

    for i in range(1, arg + 1):
        print("{:d}: {}".format(i, argv[i]))
