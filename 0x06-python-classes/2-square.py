#!/usr/bin/python3
"""defines a square """


class Square:
    """A Class That Defines a Square"""
    def __init__(self, size=0):
        """initializes the size"""
        self.__size = size
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
