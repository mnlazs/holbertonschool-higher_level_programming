#!/usr/bin/python3
"""
    This class represents a rectangle with private instance attributes
    width and height. It has methods to set and get their values,
    and raise exceptions if their values are not integers or less than 0.
    """


class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    """
    Initialize the width and height attributes with the provided values.
    """

    @property
    def width(self):
        return self._width

    @width.setter
    """
        Set the value of width attribute, if the value is an integer
        and greater than 0
        """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    """
        Get the value of width attribute
        """
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value