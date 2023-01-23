#!/usr/bin/python3
"""
Module documentation goes here
"""


class Rectangle:
    """
    This class represents a rectangle with private instance attributes
    width and height. It has methods to set and get their values,
    and raise exceptions if their values are not integers or less than 0.
    """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    """
    Initialize the width and height attributes with the provided values.
    """

    @property
    def width(self):
        return self._width

    """
        Set the value of width attribute, if the value is an integer
        and greater than 0
        """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    """
        Get the value of width attribute
        """
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
