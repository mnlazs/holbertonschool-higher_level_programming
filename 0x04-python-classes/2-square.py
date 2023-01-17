#!/usr/bin/python3
"""Square Class:defines a square by: (based on 1-square.py)
"""


class Square:
"""defines class and instantiates private instance attribute size with validation.
"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size