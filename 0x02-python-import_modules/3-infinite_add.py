#!/usr/bin/python3
# 3-ininite loop
from sys import argv
if __name__ == "__main__":
    results = 0
    if len(argv) == 1:
        print("0")
    else:
        for i in range(1, len(argv)):
            results += int(argv[i])
        print(results)
