#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    result = len(sys.argv) - 1
    if result == 0:
        print("0 arguments.")
    elif result == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(result))
    for i in range(result):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
