#!/usr/bin/python3


class Square:
    """class defining square"""
    def __init__(self, size=0):
        """data initialized"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
