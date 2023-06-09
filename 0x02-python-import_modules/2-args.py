#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

arg_Str = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    arg_Str += 's.'
elif argc == 1:
    arg_Str += ':'
else:
    arg_Str += 's:'
print(arg_Str.format(argc))

i = 0
for arg in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, arg))
    i += 1
