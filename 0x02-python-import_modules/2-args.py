#!/usr/bin/python3
import sys

def print_arguments(argv):
    num_arg = len(argv)
    print(f"Number of argument(s): {num_arg}", end='')
    if num_arg == 0:
        print(".", end='\n')
    else:
        if num_arg == 1:
            print(":")
            print(f"1: {argv[0]}")
        else:
            print("s:")
            for i in range(num_arg):
                print(f"{i+1}: {argv[i]}")

if __name__ == "__main__":
    print_arguments(sys.argv[1:])

