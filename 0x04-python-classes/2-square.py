#!/usr/bin/python3
"""Class Square"""


class Square:
    """defines class and
instantiates private."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
