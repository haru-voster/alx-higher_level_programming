#!/usr/bin/python3


class Square:
    """defineing  a square object"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """calculates and returns the current area"""
        return self.__size * self.__size
