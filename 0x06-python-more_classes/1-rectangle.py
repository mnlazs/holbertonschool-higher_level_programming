#!/usr/bin/python3
"""
Module documentation goes here
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with optional width and height
        :param width: Width of the rectangle
        :param height: Height of the rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle
        :return: Width of the rectangle
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle
        :param value: Width of the rectangle
        :raise TypeError: If width is not an integer
        :raise ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

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

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
