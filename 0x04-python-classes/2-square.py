#!/usr/bin/python3
"""
Square Class: Define a Square with private instance
"""


class Square:
    """ class Square that defines a square """
    def __init__(self, size=0):
        """ initialize variables """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
