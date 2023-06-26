#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        divide = fct(*args)
    except BaseException as h:
        divide = None
        print("Exception: {}".format(h), file=sys.stderr)
    finally:
        return divide
