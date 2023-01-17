#!/usr/bin/python3
"""creates class Square with private instance attribute size"""


class Square:
    """defines class and
instantiates private instance attribute size with validation."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security

