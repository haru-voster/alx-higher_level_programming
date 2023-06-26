#!/usr/bin/python3

def safe_print_division(a, b):
    """
    divides two integers and prints the results
    """
    try:
        divide = a / b
    except ZeroDivisionError:
        divide = None
    finally:
        print("Inside result: {}".format(divide))
        return divide
